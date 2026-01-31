# Cybersecurity educational code example
# Safe for learning only

```python
import socket
import random
import time

def iot_device_simulator(port=12345, vulnerability_level=0):
    """
    Simulates an IoT device with configurable vulnerability levels.
    
    Args:
    port (int): Port number to run the simulator on
    vulnerability_level (int): 0 (Secure) to 5 (Highly Vulnerable)
    
    Usage:
    Run this script and connect to it using a tool like netcat.
    Test different vulnerability levels to see how device behavior changes.
    
    Useful for:
    - Testing IoT device communication
    - Practicing IoT device hardening techniques
    - Demonstrating the importance of secure configurations
    """

    def generate_response(request):
        if vulnerability_level == 0:
            return "Secure IoT Device: Access Denied"
        elif vulnerability_level == 1:
            return f"IoT Device: Received command '{request}'. Access Restricted."
        elif vulnerability_level == 2:
            return f"IoT Device: Executing command '{request}'. Caution: Limited Access."
        elif vulnerability_level == 3:
            return f"IoT Device: Executed '{request}'. Warning: Device Unsecured."
        elif vulnerability_level == 4:
            return f"IoT Device: '{request}' executed. Critical: No Security Measures."
        else:
            return f"Vulnerable IoT Device: Full access granted. Executed: {request}"

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', port))
    sock.listen(1)

    print(f"IoT Device Simulator running on port {port}")
    print(f"Vulnerability Level: {vulnerability_level}")

    while True:
        connection, client_address = sock.accept()
        try:
            print(f"Connection from {client_address}")
            while True:
                data = connection.recv(1024).decode('utf-8').strip()
                if data:
                    print(f"Received: {data}")
                    response = generate_response(data)
                    connection.sendall(response.encode('utf-8'))
                    
                    # Simulate potential vulnerabilities
                    if vulnerability_level >= 3:
                        time.sleep(random.uniform(0.1, 1.0))  # Inconsistent response times
                    if vulnerability_level >= 4 and random.random() < 0.1:
                        connection.sendall(b"Error: Memory corruption detected\n")
                else:
                    break
        finally:
            connection.close()

if __name__ == "__main__":
    iot_device_simulator(vulnerability_level=3)
```

