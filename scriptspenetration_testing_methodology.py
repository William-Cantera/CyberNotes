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

