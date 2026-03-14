# Cybersecurity educational code example
# Safe for learning only

```python
import re
import urllib.parse
import http.client
from typing import List, Tuple

def check_xss_vulnerabilities(url: str, params: List[Tuple[str, str]]) -> List[str]:
    """
    Checks for potential XSS vulnerabilities in a given URL and its parameters.
    
    This function is useful for identifying basic XSS vulnerabilities during
    penetration testing or security audits. It helps defend against OWASP Top 10
    risks, specifically A03:2021-Injection.

    Args:
    url (str): The base URL to check
    params (List[Tuple[str, str]]): List of (parameter_name, parameter_value) tuples

    Returns:
    List[str]: List of potentially vulnerable parameters

    Usage:
    url = "http://example.com/page"
    params = [("search", "query"), ("id", "123")]
    vulnerabilities = check_xss_vulnerabilities(url, params)
    """

    vulnerable_params = []
    xss_payloads = [
        "<script>alert('XSS')</script>",
        "javascript:alert('XSS')",
        "<img src=x onerror=alert('XSS')>",
        "<svg/onload=alert('XSS')>"
    ]

    for param_name, param_value in params:
        for payload in xss_payloads:
            test_url = construct_url(url, param_name, payload)
            
            try:
                response = send_request(test_url)
                if payload in response:
                    vulnerable_params.append(param_name)
                    break
            except Exception as e:
                print(f"Error testing {param_name}: {str(e)}")

    return list(set(vulnerable_params))

def construct_url(base_url: str, param_name: str, param_value: str) -> str:
    """Constructs a URL with the given parameter and value"""
    encoded_value = urllib.parse.quote(param_value)
    return f"{base_url}?{param_name}={encoded_value}"

def send_request(url: str) -> str:
    """Sends a GET request to the given URL and returns the response body"""
    parsed_url = urllib.parse.urlparse(url)
    conn = http.client.HTTPSConnection(parsed_url.netloc)
    conn.request("GET", parsed_url.path + "?" + parsed_url.query)
    response = conn.getresponse()
    return response.read().decode('utf-8')

def sanitize_input(input_string: str) -> str:
    """
    Sanitizes user input to prevent XSS attacks.
    
    This function helps in defending against OWASP Top 10 risk A03:2021-Injection
    by removing potentially malicious content from user input.

    Args:
    input_string (str): The input string to sanitize

    Returns:
    str: Sanitized string

    Usage:
    user_input = "<script>alert('XSS')</script>Hello"
    safe_input = sanitize_input(user_input)
    """
    
    # Remove <script> tags
    input_string = re.sub(r'<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>', '', input_string, flags=re.IGNORECASE)
    
    # Remove JavaScript events
    input_string = re.sub(r'on\w+\s*=\s*".*?"', '', input_string, flags=re.IGNORECASE)
    
    # Remove data: and javascript: protocols
    input_string = re.sub(r'(data|javascript):', '', input_string, flags=re.IGNORECASE)
    
    # Encode special characters
    input_string = input_string.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace("'", '&#x27;')
    
    return input_

