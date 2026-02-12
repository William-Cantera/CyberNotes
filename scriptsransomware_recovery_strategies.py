# Cybersecurity educational code example
# Safe for learning only

```python
import os
import hashlib
import datetime
import json

def ransomware_recovery_scanner(directory):
    """
    Scans a directory for potentially encrypted files and generates a report.
    This can help identify affected files after a ransomware attack.

    Args:
    directory (str): The path to the directory to scan

    Returns:
    dict: A report containing scan results and statistics
    """

    # Initialize counters and lists
    total_files = 0
    suspicious_files = 0
    file_types = {}
    suspicious_extensions = ['.encrypted', '.locked', '.crypted', '.crypt']

    report = {
        'scan_time': datetime.datetime.now().isoformat(),
        'scanned_directory': directory,
        'suspicious_files': [],
        'statistics': {}
    }

    # Walk through the directory
    for root, _, files in os.walk(directory):
        for filename in files:
            total_files += 1
            filepath = os.path.join(root, filename)
            
            # Check file extension
            _, ext = os.path.splitext(filename)
            file_types[ext] = file_types.get(ext, 0) + 1

            # Flag suspicious extensions
            if ext.lower() in suspicious_extensions:
                suspicious_files += 1
                report['suspicious_files'].append(filepath)
                continue

            # Check for entropy (randomness) in file content
            try:
                with open(filepath, 'rb') as f:
                    data = f.read(4096)  # Read first 4KB
                    entropy = calculate_entropy(data)
                    if entropy > 7.9:  # High entropy threshold
                        suspicious_files += 1
                        report['suspicious_files'].append(filepath)
            except Exception as e:
                print(f"Error reading file {filepath}: {str(e)}")

    # Generate statistics
    report['statistics'] = {
        'total_files': total_files,
        'suspicious_files': suspicious_files,
        'file_types': file_types
    }

    return report

def calculate_entropy(data):
    """Calculate the Shannon entropy of a byte string."""
    if not data:
        return 0
    entropy = 0
    for x in range(256):
        p_x = float(data.count(x))/len(data)
        if p_x > 0:
            entropy += - p_x * math.log(p_x, 2)
    return entropy

def save_report(report, output_file):
    """Save the scan report to a JSON file."""
    with open(output_file, 'w') as f:
        json.dump(report, f, indent=4)

if __name__ == "__main__":
    target_dir = input("Enter the directory to scan: ")
    output_file = input("Enter the output file name (e.g., report.json): ")

    if os.path.isdir(target_dir):
        print(f"Scanning directory: {target_dir}")
        report = ransomware_recovery_scanner(target_dir)
        save_report(report, output_file)
        print(f"Scan complete. Report saved to {output_file}")
    else:
        print("Invalid directory. Please provide a valid path.")

# How to use:
# 1. Run the script
# 2. Enter the directory you want to scan when prompted
# 3. Enter a filename for the output report
# 
# This script is useful for:
# - Quick assessment of potential ransomware damage
# - Identifying suspicious files for further investigation
# - Generating statistics about affected file types
# - Creating a baseline for normal file entropy in your system
#
# Note: This is a basic scanner and may produce false positives.
# Always verify results and consult with security professionals
# for thorough ransomware recovery strategies.
```

