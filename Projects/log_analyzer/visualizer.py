import matplotlib.pyplot as plt
from collections import Counter

def plot_dashboard(logs):
    ips = [log["ip"] for log in logs]
    counts = Counter(ips)

    plt.figure()
    plt.bar(counts.keys(), counts.values())
    plt.xticks(rotation=90)
    plt.title("SOC Dashboard - Traffic Analysis")
    plt.tight_layout()
    plt.show()