XSS_PAYLOADS = [
    "<script>alert(1)</script>",
    "\"><img src=x onerror=alert(1)>"
]

SQLI_PAYLOADS = [
    "' OR 1=1--",
    "' UNION SELECT NULL--"
]

CSRF_INDICATORS = ["csrf", "token", "authenticity_token"]