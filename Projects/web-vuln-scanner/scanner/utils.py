from urllib.parse import urlparse
import json
from pathlib import Path

def normalize_url(url):
    if not url.startswith(("http://", "https://")):
        url = "http://" + url
    return url

def host_from_url(url):
    return urlparse(url).hostname

def save_report(report, host):
    Path("reports").mkdir(exist_ok=True)
    filename = f"reports/report-{host}.json"
    with open(filename, "w") as f:
        json.dump(report, f, indent=2)
    return filename