SEVERITY_SCORE = {
    "Critical": 10,
    "High": 7,
    "Medium": 3,
    "Low": 1,
    "Info": 0
}


def severity_counts(vulns):
    counts = {
        "Critical": 0,
        "High": 0,
        "Medium": 0,
        "Low": 0,
        "Info": 0
    }

    for v in vulns:
        sev = v.get("severity", "Info")
        counts[sev] += 1

    return counts


def calculate_score(vulns):
    score = 0
    for v in vulns:
        score += SEVERITY_SCORE.get(v["severity"], 0)
    return score


def overall_rating(score):
    if score >= 20:
        return "Critical"
    elif score >= 10:
        return "High"
    elif score >= 5:
        return "Medium"
    elif score > 0:
        return "Low"
    else:
        return "Secure"