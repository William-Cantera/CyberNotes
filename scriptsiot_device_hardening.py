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

```python
import socket
import ssl
import random
import string

def iot_device_hardening_checker(ip, port):
    """
    Simulates an IoT device and checks for basic security hardening measures.
    
    Args:
    ip (str): IP address of the simulated IoT device
    port (int): Port number to check

    Returns:
    dict: Results of security checks

    Usage:
    results = iot_device_hardening_checker('192.168.1.100', 8080)
    print(results)

    This function is useful for:
    - Simulating basic IoT device behavior
    - Checking for common security misconfigurations
    - Identifying potential vulnerabilities in IoT setups
    """

    results = {
        'default_credentials': False,
        'weak_encryption': False,
        'open_ports': [],
        'insecure_protocols': []
    }

    # Simulate checking for default credentials
    default_users = ['admin', 'root', 'user']
    default_passwords = ['password', '123456', 'admin']
    for user in default_users:
        for password in default_passwords:
            if user == 'admin' and password == 'password':
                results['default_credentials'] = True

    # Simulate checking for weak encryption
    try:
        context = ssl.create_default_context()
        with socket.create_connection((ip, port)) as sock:
            with context.wrap_socket(sock, server_hostname=ip) as secure_sock:
                cipher = secure_sock.cipher()
                if cipher[0] in ['TLS_RSA_WITH_RC4_128_SHA', 'TLS_RSA_WITH_RC4_128_MD5']:
                    results['weak_encryption'] = True
    except:
        pass

    # Simulate port scanning
    common_ports = [21, 22, 23, 80, 443, 8080]
    for p in common_ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, p))
        if result == 0:
            results['open_ports'].append(p)
        sock.close()

    # Simulate checking for insecure protocols
    if 21 in results['open_ports']:
        results['insecure_protocols'].append('FTP')
    if 23 in results['open_ports']:
        results['insecure_protocols'].append('Telnet')

    return results

def generate_random_ip():
    """Generate a random IP address for simulation purposes."""
    return f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}"

# Example usage
if __name__ == "__main__":
    simulated_ip = generate_random_ip()
    simulated_port = 8080
    print(f"Checking simulated IoT device at {simulated_ip}:{simulated_port}")
    results = iot_device_hardening_checker(simulated_ip, simulated_port)
    print("Security check results:")
    for key, value in results.items():
        print(f"{key}: {value}")
```

# Fallback content for IoT Device Hardening
Error 1

# Fallback content for IoT Device Hardening
Error 1

# Fallback content for IoT Device Hardening
Error 1

# Fallback content for IoT Device Hardening
Error 1

# Fallback content for IoT Device Hardening
Error 1

# Fallback content for IoT Device Hardening
Error 1

# Fallback content for IoT Device Hardening
Error 1

# Fallback content for IoT Device Hardening
Error 1

# Fallback content for IoT Device Hardening
Error 1

