import re
from datetime import datetime

# Input and output files in current directory
LOG_FILE = 'server.log'
ANOMALY_FILE = 'anomaly.log'

def classify_log(message):
    """
    Classifies log entries as SYSTEM or SECURITY alerts with severity.
    """
    message_lower = message.lower()

    # SECURITY-related messages
    if any(keyword in message_lower for keyword in ['unauthorized access', 'failed login', 'hijacking', 'brute-force', 'ransomware', 'port scan', 'suspicious','authentication failed']):
        if 'critical' in message_lower or 'ransomware' in message_lower or 'port scan' in message_lower:
            severity = "CRITICAL"
        else:
            severity = "MEDIUM"
        return "SECURITY ALERT", severity

    # SYSTEM-related messages
    if any(keyword in message_lower for keyword in ['disk usage', 'kernel panic', 'application crashed', 'cpu usage', 'deadlock', 'timeout', 'ssl', 'latency']):
        if 'critical' in message_lower or 'kernel panic' in message_lower:
            severity = "CRITICAL"
        else:
            severity = "MEDIUM"
        return "SYSTEM ALERT", severity

    return None, None

def detect_anomalies():
    with open(LOG_FILE, 'r') as infile, open(ANOMALY_FILE, 'w') as outfile:
        for line in infile:
            # Match log format like: 2025-07-23 09:14:30 [ERROR] message
            match = re.match(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \[(.*?)\] (.*)", line)
            if match:
                timestamp_str, log_level, message = match.groups()

                # Check only WARNING, ERROR, CRITICAL logs for anomalies
                if log_level.upper() in ['WARNING', 'ERROR', 'CRITICAL']:
                    category, severity = classify_log(message)
                    if category:
                        formatted = f"[{category}] [{severity}] {timestamp_str} : {message.strip()}\n"
                        outfile.write(formatted)

if __name__ == "__main__":
    detect_anomalies()
    print("✅ Anomaly detection complete. Check 'anomaly.log'")
