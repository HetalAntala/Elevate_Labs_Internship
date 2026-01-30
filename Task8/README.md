# Task 8: SQL Injection Practical Exploitation

## 📌 Objective
The objective of this task is to understand and practically exploit SQL Injection vulnerabilities using manual testing and automated tools, analyze their impact, and suggest effective mitigation techniques.

---

## 🛠 Tools Used
- SQLMap
- Web Browser (Firefox)
- Kali Linux
- Target: http://testphp.vulnweb.com (Intentionally Vulnerable Web Application)

---

## 🎯 Target Description
The target application `testphp.vulnweb.com` is a legally permitted and intentionally vulnerable web application designed for practicing web security testing techniques such as SQL Injection.

---

## 🔍 Step-by-Step Attack Flow

### Step 1: Identifying Vulnerable Parameter (Manual Testing)

Target URL:
http://testphp.vulnweb.com/listproducts.php?cat=1


Manual payloads tested:
- `cat=1'`
- `cat=1 OR 1=1`
- `cat=1 AND 1=2`

Observation:
- Different responses were observed for true and false conditions.
- SQL error messages and abnormal page behavior confirmed SQL Injection vulnerability.

---

### Step 2: Automated Exploitation using SQLMap

SQLMap was used to automate the exploitation of the SQL Injection vulnerability.

#### Extract Database Names
SQLMap successfully identified available databases.

#### Extract Tables
Tables inside the vulnerable database were enumerated.

#### Extract Columns
Sensitive columns such as usernames and passwords were discovered.

#### Dump User Data
User credentials were successfully extracted, demonstrating the severity of the vulnerability.

---

## 💥 Impact Analysis

- Attackers can extract sensitive user credentials.
- Authentication mechanisms can be bypassed.
- Confidential and critical data can be exposed.
- Data integrity can be compromised.
- Severe legal, financial, and reputational damage may occur.

---

## 🛡 Mitigation & Prevention Techniques

- Use Prepared Statements (Parameterized Queries)
- Validate and sanitize all user inputs
- Implement Least Privilege for database users
- Deploy Web Application Firewall (WAF)
- Disable verbose SQL error messages
- Regular security testing and code reviews

---

##  Learning Outcome
This task enhanced my understanding of SQL Injection vulnerabilities, real-world exploitation techniques, and defensive measures required to secure web applications.
