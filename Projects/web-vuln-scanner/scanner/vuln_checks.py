def check_xss(text, payload):
    return payload in text

def check_sqli(text):
    errors = ["sql syntax", "mysql_fetch", "ORA-", "SQLite error"]
    return any(e.lower() in text.lower() for e in errors)

def check_csrf(form):
    for inp in form.find_all("input"):
        name = inp.get("name", "").lower()
        if "csrf" in name or "token" in name:
            return False
    return True