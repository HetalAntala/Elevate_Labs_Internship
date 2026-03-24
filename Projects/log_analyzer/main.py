from monitor import monitor_files
from parser import parse_line
from detector import analyze_log
from threat_intel import check_ip_reputation
from risk_engine import calculate_risk
from alert_engine import generate_alert
from reporter import save_report

all_alerts = []

def process_line(line):
    print("Processing:", line.strip())   # DEBUG LINE

    log = parse_line(line)
    if not log:
        return

    alerts = analyze_log(log)

    for alert_type, ip in alerts:
        reputation = check_ip_reputation(ip)
        risk = calculate_risk(alert_type, reputation)

        generate_alert(alert_type, ip, risk)

        all_alerts.append({
            "type": alert_type,
            "ip": ip,
            "risk": risk
        })

if __name__ == "__main__":
    try:
        monitor_files(["logs/apache.log", "logs/ssh.log"], process_line)
    except KeyboardInterrupt:
        save_report(all_alerts)