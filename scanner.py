import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from payloads import XSS_PAYLOADS, SQLI_PAYLOADS

visited = set()

def get_forms(url):
    try:
        soup = BeautifulSoup(requests.get(url).text, 'html.parser')
        return soup.find_all("form")
    except Exception as e:
        print(f"Error reading forms: {e}")
        return []

def form_details(form):
    details = {}
    action = form.attrs.get("action", "").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        name = input_tag.attrs.get("name")
        if name:
            inputs.append({"type": input_type, "name": name})
    details['action'] = action
    details['method'] = method
    details['inputs'] = inputs
    return details

def submit_form(form_details, url, payload):
    target_url = urljoin(url, form_details['action'])
    data = {}
    for input in form_details['inputs']:
        if input['type'] in ['text', 'search']:
            data[input['name']] = payload
    if form_details['method'] == 'post':
        return requests.post(target_url, data=data)
    return requests.get(target_url, params=data)

def scan_xss(url):
    print(f"[+] Scanning {url} for XSS...")
    forms = get_forms(url)
    for form in forms:
        details = form_details(form)
        for payload in XSS_PAYLOADS:
            response = submit_form(details, url, payload)
            if payload in response.text:
                print(f"[!] XSS Vulnerability Detected!")
                print(f"Payload: {payload}")
                print(f"URL: {url}\n")

def scan_sqli(url):
    print(f"[+] Scanning {url} for SQL Injection...")
    for payload in SQLI_PAYLOADS:
        try:
            r = requests.get(url + "?" + payload)
            errors = ["you have an error in your sql syntax",
                      "warning: mysql", "unclosed quotation mark", "quoted string not properly terminated"]
            for error in errors:
                if error in r.text.lower():
                    print(f"[!] SQLi Vulnerability Detected!")
                    print(f"Payload: {payload}")
                    print(f"URL: {url}")
                    break
        except Exception as e:
            print(f"Error during SQLi test: {e}")

def crawl(url, depth=1):
    output = []
    if depth == 0 or url in visited:
        return output
    visited.add(url)
    output.append(f"[~] Crawling: {url}")
    try:
        soup = BeautifulSoup(requests.get(url).text, "html.parser")

# XSS
        output.append(f"[+] Scanning {url} for XSS...")
        forms = get_forms(url)
        for form in forms:
            details = form_details(form)
            for payload in XSS_PAYLOADS:
                response = submit_form(details, url, payload)
                if payload in response.text:
                    output.append(f"[!] XSS Detected at {url} using payload: {payload}")

# SQLi
        output.append(f"[+] Scanning {url} for SQL Injection...")
        for payload in SQLI_PAYLOADS:
            r = requests.get(url + "?" + payload)
            errors = ["you have an error in your sql syntax", "warning: mysql", "unclosed quotation mark"]
            for error in errors:
                if error in r.text.lower():
                    output.append(f"[!] SQL Injection Detected at {url} using payload: {payload}")
                    break

        for link in soup.find_all("a"):
            href = link.attrs.get("href")
            if href and href.startswith("http"):
                output.extend(crawl(href, depth - 1))
    except Exception as e:
        output.append(f"Error: {e}")
    return output