# 🔐 Log Monitoring & Analysis – Cyber Security Internship Task 12

## 📌 Objective
The objective of this task is to monitor and analyze system logs to detect suspicious activities such as failed login attempts, authentication abuse, and anomalies. This helps in understanding incident detection and basic SIEM concepts used in Security Operations Centers (SOC).

---

## 🛠 Tools Used
- WSL (Ubuntu Linux)
- Linux auth logs (/var/log/auth.log)
- grep, awk, tail commands
- Splunk Free (optional SIEM)

---

## 📂 Log Types Analyzed
- Authentication logs
- Failed login attempts
- Successful login attempts
- SSH access logs
- Sudo activity logs

---

## ⚙️ Steps Performed

### 1. Started logging services
sudo service rsyslog start
sudo service ssh start


### 2. Generated security events
- Wrong passwords
- Invalid SSH users
- Multiple login attempts

### 3. Monitored logs
tail -f /var/log/auth.log

---

## 🔍 Findings
- Multiple failed login attempts detected
- Repeated authentication failures observed
- Possible brute-force attack behavior
- Suspicious login patterns identified

---

## 🚨 Skills Learned
✅ Linux log monitoring  
✅ Security event analysis  
✅ Incident detection  
✅ Basic SIEM usage  
✅ Threat hunting basics  

---

