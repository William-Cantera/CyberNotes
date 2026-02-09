# Cybersecurity educational code example
# Safe for learning only

```python
import re
import datetime
import os

def analyze_log(log_file_path):
    """
    Analyzes a log file for potential security events.
    
    Usage:
    analyze_log('/path/to/logfile.log')
    
    This function is useful in forensic analysis and penetration testing to:
    - Identify potential security incidents
    - Track user activities
    - Detect unauthorized access attempts
    - Analyze system behavior
    """
    
    # Patterns to search for in logs
    patterns = {
        'failed_login': r'Failed login.*from (\d+\.\d+\.\d+\.\d+)',
        'successful_login': r'Successful login.*user (\w+)',
        'file_access': r'File accessed: (.*) by user (\w+)',
        'sudo_command': r'sudo: (\w+) : TTY=.* ; PWD=(.*) ; USER=root ; COMMAND=(.*)',
        'firewall_block': r'Firewall blocked connection from (\d+\.\d+\.\d+\.\d+)'
    }

    # Initialize counters and storage
    event_counts = {event: 0 for event in patterns}
    ip_attempts = {}
    suspicious_activities = []

    # Read and analyze the log file
    try:
        with open(log_file_path, 'r') as log_file:
            for line in log_file:
                for event, pattern in patterns.items():
                    match = re.search(pattern, line)
                    if match:
                        event_counts[event] += 1
                        
                        # Track failed login attempts by IP
                        if event == 'failed_login':
                            ip = match.group(1)
                            ip_attempts[ip] = ip_attempts.get(ip, 0) + 1
                            if ip_attempts[ip] > 5:
                                suspicious_activities.append(f"Multiple failed logins from {ip}")
                        
                        # Track suspicious sudo usage
                        if event == 'sudo_command':
                            user, directory, command = match.groups()
                            if any(keyword in command for keyword in ['chmod', 'chown', 'rm -rf']):
                                suspicious_activities.append(f"Suspicious sudo command by {user}: {command}")

        # Generate report
        print(f"Log Analysis Report for {log_file_path}")
        print(f"Generated on: {datetime.datetime.now()}\n")
        
        print("Event Counts:")
        for event, count in event_counts.items():
            print(f"- {event}: {count}")
        
        print("\nTop IPs with failed login attempts:")
        for ip, attempts in sorted(ip_attempts.items(), key=lambda x: x[1], reverse=True)[:5]:
            print(f"- {ip}: {attempts} attempts")
        
        print("\nSuspicious Activities:")
        for activity in suspicious_activities:
            print(f"- {activity}")

    except FileNotFoundError:
        print(f"Error: Log file not found at {log_file_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    log_path = "/var/log/auth.log"  # Replace with actual log file path
    if os.path.exists(log_path):
        analyze_log(log_path)
    else:
        print(f"Log file not found at {log_path}. Please provide a valid log file path.")
```

