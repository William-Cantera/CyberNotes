# Cybersecurity educational code example
# Safe for learning only

```python
import socket
import ssl
import json
from urllib.parse import urlparse

def analyze_zero_trust_config(config_file):
    """
    Analyzes a Zero Trust configuration file and checks for common security issues.
    
    Args:
    config_file (str): Path to the JSON configuration file
    
    Returns:
    dict: Analysis results with warnings and recommendations
    
    This function is useful for both defenders and pentesters to quickly assess
    the security posture of a Zero Trust implementation based on its configuration.
    It checks for issues like:
    - Missing or weak authentication methods
    - Overly permissive network access
    - Lack of encryption for sensitive data
    - Inadequate logging and monitoring
    """
    
    with open(config_file, 'r') as f:
        config = json.load(f)
    
    results = {
        "warnings": [],
        "recommendations": []
    }
    
    # Check authentication methods
    auth_methods = config.get("authentication", {}).get("methods", [])
    if not auth_methods:
        results["warnings"].append("No authentication methods specified")
    elif "password" in auth_methods and "mfa" not in auth_methods:
        results["warnings"].append("Password authentication without MFA")
        results["recommendations"].append("Implement Multi-Factor Authentication")
    
    # Check network access policies
    network_policies = config.get("network_policies", [])
    for policy in network_policies:
        if policy.get("allow_all", False):
            results["warnings"].append(f"Overly permissive network policy: {policy.get('name', 'Unnamed')}")
    
    # Check encryption settings
    encryption = config.get("encryption", {})
    if not encryption.get("data_in_transit", False):
        results["warnings"].append("Data in transit encryption not enabled")
        results["recommendations"].append("Enable TLS for all data in transit")
    
    # Check logging and monitoring
    logging = config.get("logging", {})
    if not logging.get("enabled", False):
        results["warnings"].append("Logging is not enabled")
        results["recommendations"].append("Enable comprehensive logging for all system activities")
    
    return results

def test_zero_trust_endpoint(url):
    """
    Tests a given endpoint for basic Zero Trust principles.
    
    Args:
    url (str): The URL of the endpoint to test
    
    Returns:
    dict: Test results including TLS version, certificate info, and headers
    
    This function is useful for quickly assessing whether an endpoint adheres to
    basic Zero Trust principles like using strong TLS, proper certificate configuration,
    and security headers. It's a starting point for more comprehensive Zero Trust testing.
    """
    
    parsed_url = urlparse(url)
    hostname = parsed_url.hostname
    port = parsed_url.port or (443 if parsed_url.scheme == "https" else 80)
    
    results = {
        "url": url,
        "tls_version": None,
        "cert_info": None,
        "security_headers": {}
    }
    
    try:
        # Create SSL context and wrap socket
        context = ssl.create_default_context()
        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as secure_sock:
                results["tls_version"] = secure_sock.version()
                cert = secure_sock.getpeercert()
                results["cert_info"] = {
                    "subject": dict(x[0] for x in cert['subject']),
                    "issuer": dict(x[0] for x in cert['issuer']),
                    "version": cert['version'],
                    "serialNumber": cert['serialNumber'],
                    "notBefore": cert['notBefore'],
                    "notAfter": cert['notAfter']
                }
                
                # Send HTTP request and check headers
                secure_sock.send(f"GET / HTTP/1.1\r\nHost: {hostname}\r\n\r\n".encode())

