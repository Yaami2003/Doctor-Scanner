from scanner import crawl

if __name__ == "__main__":
    target = input("Enter target URL to scan: ")
    crawl(target, depth=1)