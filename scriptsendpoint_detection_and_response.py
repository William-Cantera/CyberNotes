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

