MALICIOUS_IPS = ["192.168.1.100"]

def check_ip_reputation(ip):
    if ip in MALICIOUS_IPS:
        return {"malicious": True, "confidence": 90}
    return {"malicious": False, "confidence": 10}