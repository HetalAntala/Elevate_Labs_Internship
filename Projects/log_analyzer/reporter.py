import json
import time
import os

def save_report(alerts):
    # Create reports folder if not exists
    os.makedirs("reports", exist_ok=True)

    # File path inside folder
    file_path = f"reports/soc_report_{int(time.time())}.json"

    report = {
        "time": time.ctime(),
        "alerts": alerts
    }

    with open(file_path, "w") as f:
        json.dump(report, f, indent=4)

    print(f"\n[+] Report saved at: {file_path}")