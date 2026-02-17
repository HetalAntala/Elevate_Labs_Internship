import requests
import time
from .crawler import crawl
from .payloads import XSS_PAYLOADS, SQLI_PAYLOADS
from .vuln_checks import check_xss, check_sqli, check_csrf
from .headers_check import analyze_headers
from .risk import calculate_score, overall_rating
from .reporter import save_json, save_pdf
from .risk import calculate_score, overall_rating, severity_counts


class Scanner:

    def __init__(self, targets):
        self.targets = targets
        self.session = requests.Session()

    def scan_target(self, url):
        vulns = []
        seen = set()

        r = self.session.get(url)
        headers = r.headers

        # Header findings
        vulns.extend(analyze_headers(headers, url))

        pages, forms = crawl(url, self.session)

        for page, form in forms:
            action = form.get("action") or page
            method = form.get("method", "get").lower()

            inputs = {i.get("name"): "" for i in form.find_all("input") if i.get("name")}

            # CSRF only POST
            if check_csrf(form):
                key = ("csrf", action)
                if key not in seen:
                    seen.add(key)
                    vulns.append({
                        "type": "CSRF",
                        "severity": "Medium",
                        "url": action,
                        "payload": "",
                        "evidence": "No CSRF token"
                    })

            # XSS
            for payload in XSS_PAYLOADS:
                data = {k: payload for k in inputs}
                res = self.session.post(action, data=data)

                if check_xss(res.text, payload):
                    vulns.append({
                        "type": "XSS",
                        "severity": "High",
                        "url": action,
                        "payload": payload,
                        "evidence": "Payload reflected"
                    })

            # SQLi
            for payload in SQLI_PAYLOADS:
                data = {k: payload for k in inputs}
                res = self.session.post(action, data=data)

                if check_sqli(res.text):
                    vulns.append({
                        "type": "SQL Injection",
                        "severity": "Critical",
                        "url": action,
                        "payload": payload,
                        "evidence": "SQL error detected"
                    })

       
        score = calculate_score(vulns)
        rating = overall_rating(score)
        counts = severity_counts(vulns)

        report = {
            "target": url,
            "risk_score": score,
            "rating": rating,
            "counts": counts,
            "total_findings": len(vulns),
            "vulnerabilities": vulns
        }

        ts = int(time.time())

        json_file = f"reports/report_{ts}.json"
        pdf_file = f"reports/report_{ts}.pdf"

        save_json(report, json_file)
        save_pdf(report, pdf_file)

        report["report_file"] = json_file
        report["pdf_file"] = pdf_file

        return report

    def run(self):
        return [self.scan_target(t) for t in self.targets]