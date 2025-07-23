# 🔍 Log Anomaly Detection System

This project is a simple Python-based log anomaly detection system. It reads system logs from a file, detects anomalies, and classifies them into **SECURITY** or **SYSTEM** alerts with severity levels like `CRITICAL` or `MEDIUM`.

## 📁 Project Structure

📦 Log Anomaly Detection \n
├── anamoly_detection.py # Python script for anomaly detection \n
├── server.log # Input log file \n
├── anomaly.log # Output file with detected anomalies \n
└── instruction.txt # Setup instructions \n


## ✅ Features

- Automatically scans logs and extracts only critical or suspicious activity.
- Classifies anomalies into:
  - 🔐 **Security Alerts** (e.g., failed login, ransomware, port scan)
  - 🖥️ **System Alerts** (e.g., disk usage, kernel panic, deadlocks)
- Tags alerts with severity: `CRITICAL` or `MEDIUM`.

## 🔧 Installation & Execution
```bash
**### Step 1: Install required packages (optional for extended functionality)**

pip install pandas matplotlib seaborn scikit-learn nltk

**Step 2: Run the anomaly detection script**
python anamoly_detection.py

**Step 3: Output**
* Detected anomalies will be saved in anomaly.log

* Check the terminal for the confirmation message:
✅ Anomaly detection complete. Check 'anomaly.log'

**Output Format (anomaly.log)**
[SECURITY ALERT] [MEDIUM] 2025-07-23 09:14:10 : Authentication failed for user 'admin' from IP 172.16.5.21

**Detection Logic**
The script scans only logs with the level WARNING, ERROR, or CRITICAL. It uses keyword-based classification:

**🔐 Security Keywords:**
* unauthorized access

* failed login

* brute-force

* ransomware

* port scan

* suspicious

* authentication failed

**🖥️ System Keywords:**

* disk usage

* kernel panic

* cpu usage

* deadlock

* timeout

* application crashed

* ssl

* latency

🧠 **How It Works**

* Reads logs line by line from server.log

* Matches format using regular expressions

* Filters logs by level

* Checks if the message contains anomaly keywords

* Classifies and writes formatted result to anomaly.log
---

