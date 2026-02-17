def analyze_headers(headers, target_url):
    findings = []

    def add(name, severity, evidence):
        findings.append({
            "type": name,
            "severity": severity,
            "payload": "",
            "url": target_url,   # ✅ FIX HERE
            "evidence": evidence
        })

    if not headers.get("Content-Security-Policy"):
        add("Missing CSP", "Medium", "Content-Security-Policy not set")

    if not headers.get("X-Frame-Options"):
        add("Clickjacking Risk", "Medium", "X-Frame-Options missing")

    if not headers.get("Strict-Transport-Security"):
        add("HSTS Missing", "Low", "Strict-Transport-Security not set")

    return findings