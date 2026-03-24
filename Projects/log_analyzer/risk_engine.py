def calculate_risk(alert_type, reputation):
    score = 0

    if alert_type == "DoS":
        score += 70
    elif alert_type == "Brute Force":
        score += 60
    elif alert_type == "Scanning":
        score += 40

    if reputation["malicious"]:
        score += reputation["confidence"]

    return min(score, 100)