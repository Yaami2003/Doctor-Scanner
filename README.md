# 🩺 Doctor Scanner

**Doctor Scanner** is a lightweight, Python-based web vulnerability scanner built using Flask.
It helps identify common web application vulnerabilities such as:

- ✅ Cross-Site Scripting (XSS)
- ✅ SQL Injection (SQLi)

With a clean Flask-powered web interface, it’s easy to use for both students and cybersecurity enthusiasts to scan and test target websites in a legal and ethical way.

---

## 🚀 Demo Screenshot

> ![Doctor Scanner UI](https://github.com/Yaami2003/Doctor-Scanner/blob/77396783066437f45737466f67dc03e08c6a7f50/docscanf.png)
> ![Doctor Scanner result]

---

## 🔧 Features

- 🕷️ **Crawler** – Automatically explores web pages from a given target URL
- ⚙️ **Payload Injector** – Sends known XSS & SQLi payloads to forms and URLs
- 📊 **Result Viewer** – Scan results are shown in a clean web browser interface
- 🌐 **Flask Web UI** – User-friendly web interface to interact with the tool
- 🩺 **Branding** – Fully customizable logo and theme

---

## 📁 Project Structure
web_vuln_scanner/

├── app.py                  # Flask web server

├── scanner.py              # Scanning logic

├── run.py                  # CLI version (optional)

├── payloads.py             # Predefined XSS and SQLi payloads

├── templates/

│   ├── index.html          # Web form input

│   └── result.html         # Results display

├── static/

│   └── logo.png            # Custom logo

├── requirements.txt        # Dependencies

└── README.md               # Documentation

---

## ⚙️ How to Install & Run the Scanner

Follow these steps to set up and run the Doctor Scanner on your system:

### 🔹 1. Clone the Repository

git clone https://github.com/yaami2003/doctor-scanner.git
cd doctor-scanner

### 🔹 2. Install All Required Dependencies

pip install -r requirements.txt

This will install:

- Flask

- Requests

- BeautifulSoup4


### 🔹 3. Start the Flask Web App

python app.py

Then open your browser and go to:

http://127.0.0.1:5000
Enter a target website URL in the input field and click Start Scan ✅
---

## 🌐 Safe Test URLs (For Practice)

Use only **legally approved and intentionally vulnerable** testing sites:

| Test URL | Vulnerabilities |
|----------------------------------|------------------------|
| http://testphp.vulnweb.com | ✅ XSS, ✅ SQLi |
| http://zero.webappsecurity.com | ✅ XSS |
| http://demo.testfire.net | ✅ Auth, ✅ SQLi |

⚠️ **IMPORTANT:**
Doctor Scanner is intended **only for ethical testing and learning.**
Never scan websites without permission.

---

## 💡 Future Improvements

- 🔐 Add login bypass and CSRF testing
- 📝 Export results to PDF or CSV
- 🎨 Dark mode / theme toggle
- 🛡️ Add more payload categories
- 📤 Deploy online using Render or PythonAnywhere

---

## 👩‍💻 Author

**Yaami Raj**
💻 Student | Cybersecurity Enthusiast | Python Developer
📍 Kerala, India
🌐 [GitHub Profile](https://github.com/yaami2003)

---

## 🧾 License

This project is intended for educational and ethical testing purposes only.
Use it responsibly.





