# Cybersecurity educational code example
# Safe for learning only

```python
import socket
import ipaddress
import concurrent.futures
import time

def port_scan(target_ip, port, timeout=1):
    """
    Attempt to connect to a specific port on the target IP.
    
    Args:
    target_ip (str): The IP address to scan
    port (int): The port number to check
    timeout (float): Connection timeout in seconds
    
    Returns:
    tuple: (port, True) if open, (port, False) if closed
    """
    try:
        with socket.create_connection((target_ip, port), timeout=timeout):
            return (port, True)
    except (socket.timeout, ConnectionRefusedError):
        return (port, False)

def scan_network(network, ports, num_threads=50):
    """
    Scan a network range for open ports.
    
    Args:
    network (str): Network in CIDR notation (e.g., '192.168.1.0/24')
    ports (list): List of ports to scan
    num_threads (int): Number of concurrent threads to use
    
    Returns:
    dict: IP addresses with open ports {ip: [open_ports]}
    """
    ip_network = ipaddress.ip_network(network)
    results = {}
    
    def scan_host(ip):
        open_ports = []
        for port, is_open in executor.map(lambda p: port_scan(str(ip), p), ports):
            if is_open:
                open_ports.append(port)
        if open_ports:
            results[str(ip)] = open_ports
    
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        executor.map(scan_host, ip_network.hosts())
    
    duration = time.time() - start_time
    print(f"Scan completed in {duration:.2f} seconds")
    return results

# Example usage
if __name__ == "__main__":
    network_to_scan = "192.168.1.0/24"  # Replace with your target network
    ports_to_scan = [21, 22, 80, 443, 3306, 8080]  # Common ports to check
    
    print(f"Scanning network: {network_to_scan}")
    print(f"Ports to scan: {ports_to_scan}")
    
    results = scan_network(network_to_scan, ports_to_scan)
    
    for ip, open_ports in results.items():
        print(f"Open ports on {ip}: {open_ports}")

"""
This script demonstrates a basic network port scanner, a common tool in penetration testing.
It's useful for:
1. Discovering live hosts on a network
2. Identifying open ports on those hosts
3. Inferring potential services running on the network

In pentesting, this helps map out the attack surface of a network.
For defense, it helps identify potentially vulnerable or unnecessary open ports.

Usage:
1. Set the 'network_to_scan' variable to your target network in CIDR notation
2. Adjust 'ports_to_scan' list to include ports of interest
3. Run the script

Note: Only use on networks you have permission to scan. Unauthorized scanning may be illegal.
"""
```

```python
import socket
import ipaddress
import concurrent.futures
import time

def port_scanner(target, ports, timeout=1):
    """
    A simple multi-threaded port scanner.

    Args:
    target (str): IP address or hostname to scan
    ports (list): List of ports to scan
    timeout (float): Timeout for each connection attempt

    Returns:
    list: List of open ports
    """
    open_ports = []

    def check_port(port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((target, port))
        sock.close()
        if result == 0:
            return port
        return None

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        future_to_port = {executor.submit(check_port, port): port for port in ports}
        for future in concurrent.futures.as_completed(future_to_port):
            port = future.result()
            if port:
                open_ports.append(port)

    return open_ports

def main():
    # Example usage
    target = input("Enter target IP or hostname: ")
    port_range = input("Enter port range (e.g., 1-1000): ")
    
    try:
        start_port, end_port = map(int, port_range.split('-'))
        ports = range(start_port, end_port + 1)
    except ValueError:
        print("Invalid port range. Using default range 1-1000.")
        ports = range(1, 1001)

    try:
        ip = ipaddress.ip_address(target)
    except ValueError:
        try:
            ip = socket.gethostbyname(target)
        except socket.gaierror:
            print("Invalid IP or hostname.")
            return

    print(f"Scanning {ip} for open ports...")
    start_time = time.time()
    open_ports = port_scanner(str(ip), ports)
    end_time = time.time()

    if open_ports:
        print("Open ports:")
        for port in open_ports:
            print(f"- Port {port}")
    else:
        print("No open ports found.")

    print(f"Scan completed in {end_time - start_time:.2f} seconds.")

if __name__ == "__main__":
    main()

# This script demonstrates a basic port scanner, which is a common tool in penetration testing.
# It helps identify open ports on a target system, which can reveal potential vulnerabilities or entry points.
# 
# Key features and benefits for pentesting/defense:
# 1. Reconnaissance: Helps in the initial phase of penetration testing by identifying active services.
# 2. Vulnerability assessment: Open ports may indicate services that could be exploited.
# 3. Network mapping: Assists in understanding the target's network structure.
# 4. Security auditing: Helps identify unnecessarily open ports that should be closed.
# 5. Performance: Uses multi-threading for faster scanning of multiple ports.
# 
# Usage:
# 1. Run the script
# 2. Enter the target IP or hostname when prompted
# 3. Enter the desired port range (e.g., 1-1000)
# 
# Note: This tool should only be used on systems you own or have explicit permission to test.
# Unauthorized port scanning may be illegal or against acceptable use policies.
```

# Fallback content for Penetration Testing Methodology
Error 1

