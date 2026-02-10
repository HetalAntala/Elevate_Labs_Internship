# Linux Server Hardening & Secure Configuration

## 📌 Objective
The goal of this project is to harden a Linux server to reduce vulnerabilities and protect it against common cyber attacks such as unauthorized access, brute force attacks, and privilege escalation.

---

## 🛠 Tools Used
- Ubuntu / Kali Linux
- UFW Firewall
- SSH
- Lynis Security Scanner
- Linux System Logs

---

## 🔍 Methodology

### 1. System Update
Updated all packages to latest versions.

### 2. User Management
- Reviewed users
- Removed unused accounts
- Restricted sudo access

### 3. SSH Security
- Disabled root login
- Disabled password authentication
- Enabled key-based authentication

### 4. Firewall Configuration
- Enabled UFW
- Allowed only SSH port
- Blocked other traffic

### 5. Service Hardening
- Disabled unused services

### 6. File Permissions
- Secured sensitive files
- Restricted root access

### 7. Automatic Updates
- Enabled unattended upgrades

### 8. Security Audit
- Performed audit using Lynis

### 9. Log Monitoring
- Checked authentication logs

---

## 📋 Hardening Checklist
(Include checklist table here)

---

## 📸 Screenshots
(Add all screenshots here)

---

## 🔐 Security Configuration Summary
The server was hardened by limiting access, disabling unnecessary services, configuring a firewall, and enforcing secure authentication methods. This significantly reduces the attack surface.

---

