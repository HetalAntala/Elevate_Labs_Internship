def check_security_headers(resp):
    h = resp.headers
    return {
        "CSP": h.get("Content-Security-Policy"),
        "X-Frame-Options": h.get("X-Frame-Options"),
        "HSTS": h.get("Strict-Transport-Security"),
    }