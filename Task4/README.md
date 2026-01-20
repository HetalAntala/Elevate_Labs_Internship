# Task 4 – Password Security & Authentication Analysis

## 📌 Internship Task Overview
This task focuses on understanding password security, authentication mechanisms, and 
demonstrating how weak passwords can be compromised using common attack techniques.
The objective is to gain practical and theoretical knowledge of password hashing,
password cracking methods, and modern authentication defenses.

---

## 🎯 Objectives
- Understand how passwords are stored using hashing
- Identify common hash types such as MD5 and SHA-1
- Perform a dictionary-based password cracking attack
- Analyze why weak passwords fail
- Study the importance of Multi-Factor Authentication (MFA)
- Provide recommendations for strong authentication practices

---

## 🛠 Tools Used
- **John the Ripper (Jumbo version)** – for password cracking
- **Online Hash Generators** – for generating test hashes
- **Linux / WSL Environment** – for executing commands
- **GitHub** – for version control and submission

---

## 📂 Project Structure
Task-4/
├── README.md
├── Password_Security_Analysis_Report.md
├── passwords.txt
├── hashes.txt
├── cracked_results.txt
└── screenshots/
└── john_output.png


---

## 🧪 Practical Work Summary

### 1. Password Hash Generation
Weak passwords were selected and converted into cryptographic hashes
using MD5 and SHA-1 algorithms.

### 2. Dictionary Attack
A dictionary attack was performed using John the Ripper with a custom
wordlist to crack weak password hashes.

### 3. Results
Weak passwords such as `admin123` and `password` were successfully cracked,
demonstrating the risks of poor password practices.

---

## 🔐 Key Concepts Learned
- Difference between hashing and encryption
- How dictionary and brute force attacks work
- Why MD5 and SHA-1 are insecure
- Importance of bcrypt for secure password storage
- Role of Multi-Factor Authentication in security

---

## 📘 Deliverables
- Password Security Analysis Report
- Generated password hashes
- Dictionary attack results
- Screenshots of tool execution
- GitHub repository documentation

---

## ✅ Outcome
This task provided hands-on experience with password attacks and defenses,
highlighting the importance of strong password policies and secure
authentication mechanisms in cybersecurity.

---

## 👤 Author
**Name:** Hetal Antala  
**Internship:** Cyber Security Internship  
**Task:** Password Security & Authentication Analysis  
