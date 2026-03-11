# Cybersecurity educational code example
# Safe for learning only

```python
import os
import psutil
import hashlib
import time

def edr_sim():
    """
    Simulates basic Endpoint Detection and Response (EDR) functionality.
    This function monitors system processes, file changes, and network connections.
    It's useful for understanding EDR concepts and testing detection capabilities.
    
    Usage: Simply run the function. Press Ctrl+C to stop.
    """
    
    print("Starting EDR simulation...")
    
    # Initialize baseline of running processes
    baseline_processes = set(psutil.process_iter(['pid', 'name']))
    
    # Initialize baseline of files in current directory
    baseline_files = {}
    for file in os.listdir():
        if os.path.isfile(file):
            with open(file, 'rb') as f:
                baseline_files[file] = hashlib.md5(f.read()).hexdigest()
    
    try:
        while True:
            # Check for new processes
            current_processes = set(psutil.process_iter(['pid', 'name']))
            new_processes = current_processes - baseline_processes
            for process in new_processes:
                print(f"[ALERT] New process detected: {process.info['name']} (PID: {process.info['pid']})")
            baseline_processes = current_processes
            
            # Check for file changes
            for file in os.listdir():
                if os.path.isfile(file):
                    with open(file, 'rb') as f:
                        current_hash = hashlib.md5(f.read()).hexdigest()
                    if file in baseline_files:
                        if current_hash != baseline_files[file]:
                            print(f"[ALERT] File modified: {file}")
                            baseline_files[file] = current_hash
                    else:
                        print(f"[ALERT] New file detected: {file}")
                        baseline_files[file] = current_hash
            
            # Check network connections
            for conn in psutil.net_connections():
                if conn.status == 'ESTABLISHED':
                    print(f"[INFO] Active connection: {conn.laddr} -> {conn.raddr}")
            
            time.sleep(5)  # Wait for 5 seconds before next check
            
    except KeyboardInterrupt:
        print("\nEDR simulation stopped.")

if __name__ == "__main__":
    edr_sim()
```

```python
import os
import hashlib
import time
import logging

# Set up logging
logging.basicConfig(filename='edr_sim.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def simulate_edr():
    """
    Simulates basic Endpoint Detection and Response (EDR) functionality.
    This function monitors a specified directory for file changes and logs suspicious activity.
    
    Usage:
    Call this function and let it run in the background to monitor a directory.
    
    Why it's useful:
    - Demonstrates basic file system monitoring concepts used in EDR solutions
    - Helps understand how EDR tools detect and log potential threats
    - Can be used to test and verify security monitoring setups
    """
    
    MONITORED_DIR = "C:\\Users\\Public"  # Directory to monitor
    SCAN_INTERVAL = 5  # Seconds between scans
    file_hashes = {}  # Store file hashes
    
    print(f"Starting EDR simulation. Monitoring: {MONITORED_DIR}")
    logging.info("EDR simulation started")
    
    try:
        while True:
            for root, _, files in os.walk(MONITORED_DIR):
                for file in files:
                    file_path = os.path.join(root, file)
                    try:
                        # Calculate file hash
                        with open(file_path, "rb") as f:
                            file_hash = hashlib.md5(f.read()).hexdigest()
                        
                        # Check if file is new or modified
                        if file_path not in file_hashes:
                            logging.info(f"New file detected: {file_path}")
                            file_hashes[file_path] = file_hash
                        elif file_hashes[file_path] != file_hash:
                            logging.warning(f"File modified: {file_path}")
                            file_hashes[file_path] = file_hash
                        
                        # Example: Flag executable files as suspicious
                        if file.endswith(('.exe', '.dll', '.bat')):
                            logging.warning(f"Suspicious file detected: {file_path}")
                    
                    except Exception as e:
                        logging.error(f"Error processing file {file_path}: {str(e)}")
            
            # Check for deleted files
            for file_path in list(file_hashes.keys()):
                if not os.path.exists(file_path):
                    logging.info(f"File deleted: {file_path}")
                    del file_hashes[file_path]
            
            time.sleep(SCAN_INTERVAL)
    
    except KeyboardInterrupt:
        print("EDR simulation stopped.")
        logging.info("EDR simulation stopped")

if __name__ == "__main__":
    simulate_edr()
```

```python
import os
import psutil
import datetime
import logging

# Set up logging
logging.basicConfig(filename='edr_simulator.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def simulate_edr():
    """
    Simulates basic Endpoint Detection and Response (EDR) functionality.
    
    This function monitors system processes, checks for suspicious activities,
    and logs potential security events. It's useful for understanding EDR concepts
    and testing defense mechanisms.

    Usage:
    Simply call the function to start the simulation. Press Ctrl+C to stop.

    Note: This is a simplified simulation for educational purposes only and
    should not be used as a real security tool.
    """
    
    print("Starting EDR simulation. Press Ctrl+C to stop.")
    logging.info("EDR simulation started")

    try:
        while True:
            # Monitor running processes
            for proc in psutil.process_iter(['pid', 'name', 'username', 'cmdline']):
                try:
                    # Check for suspicious process names
                    if any(susp in proc.info['name'].lower() for susp in ['hack', 'exploit', 'mal']):
                        logging.warning(f"Suspicious process detected: {proc.info}")
                    
                    # Check for unusual system binaries location
                    if proc.info['name'] in ['cmd.exe', 'powershell.exe'] and \
                       not proc.info['exe'].startswith(r'C:\Windows\System32'):
                        logging.warning(f"System binary in unusual location: {proc.info}")
                    
                    # Check for processes running as SYSTEM
                    if proc.info['username'] == 'NT AUTHORITY\\SYSTEM' and \
                       proc.info['name'] not in ['svchost.exe', 'services.exe']:
                        logging.warning(f"Unusual process running as SYSTEM: {proc.info}")

                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass

            # Monitor file system for suspicious activities
            suspicious_extensions = ['.exe', '.dll', '.bat', '.ps1']
            for root, dirs, files in os.walk(r'C:\Users'):
                for file in files:
                    if any(file.endswith(ext) for ext in suspicious_extensions):
                        full_path = os.path.join(root, file)
                        creation_time = datetime.datetime.fromtimestamp(os.path.getctime(full_path))
                        if (datetime.datetime.now() - creation_time).seconds < 60:
                            logging.warning(f"Suspicious file created: {full_path}")

    except KeyboardInterrupt:
        print("\nEDR simulation stopped.")
        logging.info("EDR simulation stopped")

if __name__ == "__main__":
    simulate_edr()
```

