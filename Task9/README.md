# Network Vulnerability Scanning – Cyber Security Internship Task 9

## 🎯 Objective
Perform network reconnaissance and vulnerability scanning using Nmap.

---

## 🛠 Tools Used
- Nmap
- Linux / Windows

---

## 📌 Steps Performed

### 1️⃣ Host Discovery
Command:
nmap -sn 192.168.56.0/24

Discovered active devices on the local network.

---

### 2️⃣ Port Scanning
Command:
nmap 192.168.56.102

Identified open ports.

---

### 3️⃣ Service Enumeration
Command:
nmap -sV 192.168.56.102

Detected services and versions.

---

### 4️⃣ OS Detection
Command:
sudo nmap -O 192.168.56.102

Identified target OS.

---

### 5️⃣ Vulnerability Scan
Command:
sudo nmap --script vuln 192.168.56.102

Checked known vulnerabilities.

---

## 🔎 Findings

| Port | Service |
|------|---------|
|  21  |   FTP   |              
|  22  |   SSH   | 
|  53  |  Domain | 

---

## 📂 Files Included
- Scan results (.txt)
- Screenshots
- Report

---

## 🎯 Outcome
- Learned network scanning
- Identified services
- Understood vulnerabilities
- Gained reconnaissance skills

---

