from collections import defaultdict

ip_activity = defaultdict(int)
failed_logins = defaultdict(int)

def analyze_log(log):
    alerts = []

    ip = log["ip"]
    ip_activity[ip] += 1

    # 🔥 DoS Detection (LOW threshold for testing)
    if ip_activity[ip] > 5:
        alerts.append(("DoS", ip))

    # 🔥 Brute Force
    if log.get("event") == "failed_login":
        failed_logins[ip] += 1
        if failed_logins[ip] > 3:
            alerts.append(("Brute Force", ip))

    # 🔥 Scanning
    if log.get("status") == 404:
        alerts.append(("Scanning", ip))

    return alerts