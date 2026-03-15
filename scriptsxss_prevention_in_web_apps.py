# Cybersecurity educational code example
# Safe for learning only

```python
import html
import re

def xss_sanitize_input(input_string):
    """
    Sanitizes user input to prevent XSS attacks.
    
    Args:
    input_string (str): The user input to sanitize
    
    Returns:
    str: Sanitized string safe for rendering in HTML
    
    Usage:
    sanitized = xss_sanitize_input(user_input)
    
    This function is useful for pentesting/defense because:
    1. It demonstrates proper input sanitization techniques
    2. It can be used to test if a web app is vulnerable to XSS
    3. It provides a baseline for implementing XSS prevention in web apps
    """
    
    # Step 1: HTML encode special characters
    sanitized = html.escape(input_string)
    
    # Step 2: Remove potential JavaScript events
    sanitized = re.sub(r'on\w+\s*=', '', sanitized, flags=re.IGNORECASE)
    
    # Step 3: Remove potential JavaScript functions
    sanitized = re.sub(r'javascript:', '', sanitized, flags=re.IGNORECASE)
    
    # Step 4: Remove potential script tags
    sanitized = re.sub(r'<script.*?>.*?</script>', '', sanitized, flags=re.IGNORECASE|re.DOTALL)
    
    # Step 5: Remove potential inline styles (which can contain JavaScript)
    sanitized = re.sub(r'style\s*=\s*".*?"', '', sanitized, flags=re.IGNORECASE)
    
    return sanitized

def xss_check(input_string):
    """
    Checks if a given input string potentially contains XSS payloads.
    
    Args:
    input_string (str): The string to check for XSS payloads
    
    Returns:
    bool: True if potential XSS payload detected, False otherwise
    
    Usage:
    is_xss = xss_check(user_input)
    
    This function is useful for pentesting/defense because:
    1. It can be used to quickly scan user inputs for potential XSS
    2. It helps identify common XSS patterns in penetration testing
    3. It can be integrated into web apps as a first-line defense
    """
    
    # List of common XSS patterns to check
    xss_patterns = [
        r'<script.*?>',
        r'javascript:',
        r'onerror\s*=',
        r'onload\s*=',
        r'onclick\s*=',
        r'alert\s*\(',
        r'String.fromCharCode\(',
        r'eval\s*\(',
        r'document\.cookie',
        r'document\.write'
    ]
    
    # Check if any XSS pattern is present in the input
    for pattern in xss_patterns:
        if re.search(pattern, input_string, re.IGNORECASE):
            return True
    
    return False

# Example usage
if __name__ == "__main__":
    test_inputs = [
        "Hello, world!",
        "<script>alert('XSS')</script>",
        "onclick='alert(\"XSS\")'",
        "javascript:alert('XSS')",
        "Normal text with <b>bold</b> HTML",
    ]
    
    for input_str in test_inputs:
        print(f"Original: {input_str}")
        print(f"Sanitized: {xss_sanitize_input(input_str)}")
        print(f"XSS Detected: {xss_check(input_str)}")
        print("---")
```

```python
import re
import html

def xss_sanitizer(input_string):
    """
    Sanitizes input to prevent XSS attacks in web applications.
    
    Args:
    input_string (str): The user input to be sanitized.
    
    Returns:
    str: Sanitized string safe for rendering in HTML.
    
    Usage:
    sanitized_input = xss_sanitizer(user_input)
    
    This function is useful in cybersecurity for:
    1. Demonstrating proper input sanitization techniques
    2. Testing web application security
    3. Educating developers about XSS prevention
    """
    
    # Step 1: HTML Encoding
    # Convert special characters to HTML entities
    encoded_string = html.escape(input_string)
    
    # Step 2: JavaScript Encoding
    # Escape any JavaScript-specific characters
    js_escape_chars = {
        '\\': '\\\\',
        "'": "\\'",
        '"': '\\"',
        '\n': '\\n',
        '\r': '\\r',
        '\t': '\\t',
        '\f': '\\f',
        '\b': '\\b'
    }
    for char, escaped in js_escape_chars.items():
        encoded_string = encoded_string.replace(char, escaped)
    
    # Step 3: URL Encoding
    # Encode characters that have special meaning in URLs
    encoded_string = re.sub(r'[^\w\-\.\~]', lambda m: f'%{ord(m.group(0)):02X}', encoded_string)
    
    # Step 4: Remove potential script tags
    encoded_string = re.sub(r'<script.*?>.*?</script>', '', encoded_string, flags=re.IGNORECASE | re.DOTALL)
    
    # Step 5: Remove potential event handlers
    encoded_string = re.sub(r'on\w+\s*=', '', encoded_string, flags=re.IGNORECASE)
    
    return encoded_string

def xss_vulnerability_checker(input_string):
    """
    Checks if a given input string potentially contains XSS vulnerabilities.
    
    Args:
    input_string (str): The string to be checked for XSS vulnerabilities.
    
    Returns:
    bool: True if potential XSS vulnerability is detected, False otherwise.
    
    Usage:
    is_vulnerable = xss_vulnerability_checker(user_input)
    
    This function is useful in cybersecurity for:
    1. Quick assessment of user inputs
    2. Automated scanning of web application inputs
    3. Educating about common XSS patterns
    """
    
    # List of common XSS patterns to check
    xss_patterns = [
        r'<script.*?>',
        r'javascript:',
        r'onerror=',
        r'onload=',
        r'onclick=',
        r'alert\(',
        r'eval\(',
        r'document\.cookie',
        r'document\.write',
        r'\.innerhtml',
    ]
    
    # Check if any of the patterns are in the input string
    for pattern in xss_patterns:
        if re.search(pattern, input_string, re.IGNORECASE):
            return True
    
    return False

# Example usage
if __name__ == "__main__":
    test_input = "<script>alert('XSS');</script>"
    print(f"Original input: {test_input}")
    print(f"Sanitized input: {xss_sanitizer(test_input)}")
    print(f"Is vulnerable: {xss_vulnerability_checker(test_input)}")
```

```python
import html
import re

def xss_sanitize(input_string):
    """
    Sanitize input to prevent XSS attacks.
    
    Args:
    input_string (str): The string to sanitize
    
    Returns:
    str: Sanitized string
    
    This function helps prevent XSS attacks by:
    1. HTML encoding special characters
    2. Removing potentially dangerous HTML tags
    3. Removing JavaScript event handlers
    
    Usage:
    sanitized = xss_sanitize(user_input)
    
    Useful in pentesting/defense to:
    - Test input sanitization in web applications
    - Implement basic XSS protection in simple web apps
    - Demonstrate XSS prevention techniques
    """
    
    # Step 1: HTML encode special characters
    sanitized = html.escape(input_string)
    
    # Step 2: Remove potentially dangerous HTML tags
    dangerous_tags = ['script', 'iframe', 'embed', 'object', 'meta']
    for tag in dangerous_tags:
        sanitized = re.sub(f'<{tag}.*?>.*?</{tag}>', '', sanitized, flags=re.IGNORECASE | re.DOTALL)
        sanitized = re.sub(f'<{tag}.*?/?>', '', sanitized, flags=re.IGNORECASE)
    
    # Step 3: Remove JavaScript event handlers
    event_handlers = ['onload', 'onclick', 'onmouseover', 'onerror', 'onsubmit']
    for handler in event_handlers:
        sanitized = re.sub(f'{handler}=.*?["\'](.*?)["\']', '', sanitized, flags=re.IGNORECASE)
    
    return sanitized

def xss_check(input_string):
    """
    Check if a string potentially contains XSS payload.
    
    Args:
    input_string (str): The string to check
    
    Returns:
    bool: True if potential XSS detected, False otherwise
    
    This function checks for common XSS indicators:
    1. Presence of <script> tags
    2. Presence of JavaScript event handlers
    3. Presence of data: or javascript: URI schemes
    
    Usage:
    is_xss = xss_check(user_input)
    
    Useful in pentesting/defense to:
    - Quickly scan inputs for potential XSS payloads
    - Implement basic XSS detection in web applications
    - Educate about common XSS patterns
    """
    
    # Check for <script> tags
    if re.search('<script.*?>.*?</script>', input_string, re.IGNORECASE | re.DOTALL):
        return True
    
    # Check for event handlers
    event_handlers = ['onload', 'onclick', 'onmouseover', 'onerror', 'onsubmit']
    for handler in event_handlers:
        if re.search(f'{handler}=', input_string, re.IGNORECASE):
            return True
    
    # Check for dangerous URI schemes
    if re.search('(data|javascript):' , input_string, re.IGNORECASE):
        return True
    
    return False

# Example usage
if __name__ == "__main__":
    test_inputs = [
        "Hello, world!",
        "<script>alert('XSS')</script>",
        "Click <a href='javascript:alert(\"XSS\")'>here</a>",
        "<img src='x' onerror='alert(\"XSS\")'>",
        "<iframe src='data:text/html,<script>alert(\"XSS\")</script>'>",
    ]
    
    for input_str in test_inputs:
        print(f"Original: {input_str}")
        print(f"Sanitized: {xss_sanitize(input_str)}")
        print(f"XSS Detected: {xss_check(input_str)}")
        print()
```

```python
import html
import re

def xss_sanitize(input_string):
    """
    Sanitizes input to help prevent XSS attacks in web applications.
    
    Args:
    input_string (str): The user input to be sanitized
    
    Returns:
    str: Sanitized string safe for rendering in HTML
    
    Usage:
    sanitized = xss_sanitize(user_input)
    
    This function is useful in pentesting/defense to:
    1. Demonstrate proper input sanitization
    2. Test if a web app is vulnerable to XSS
    3. Implement a basic XSS prevention measure
    """
    
    # Step 1: HTML Escape
    escaped = html.escape(input_string)
    
    # Step 2: Remove potential JavaScript events
    escaped = re.sub(r'on\w+', '', escaped)
    
    # Step 3: Remove potential JavaScript functions
    escaped = re.sub(r'javascript:', '', escaped, flags=re.IGNORECASE)
    
    # Step 4: Remove potential DOM manipulation
    escaped = re.sub(r'document\.', '', escaped, flags=re.IGNORECASE)
    
    return escaped

def xss_vulnerability_check(input_string):
    """
    Checks if a string might be vulnerable to XSS attacks.
    
    Args:
    input_string (str): The string to check for potential XSS vulnerabilities
    
    Returns:
    bool: True if potentially vulnerable, False otherwise
    
    Usage:
    is_vulnerable = xss_vulnerability_check(user_input)
    
    This function is useful in pentesting/defense to:
    1. Quickly assess if user input might contain XSS payloads
    2. Test web app input fields for potential vulnerabilities
    3. Demonstrate common XSS attack patterns
    """
    
    # List of common XSS attack patterns
    xss_patterns = [
        r'<script.*?>',
        r'javascript:',
        r'onerror=',
        r'onload=',
        r'onclick=',
        r'alert\(',
        r'document\.cookie',
        r'document\.write',
        r'<img.*?src=',
        r'<iframe.*?src='
    ]
    
    # Check if any pattern matches the input string
    for pattern in xss_patterns:
        if re.search(pattern, input_string, re.IGNORECASE):
            return True
    
    return False

# Example usage
if __name__ == "__main__":
    test_inputs = [
        "Hello, World!",
        "<script>alert('XSS')</script>",
        "onclick=alert('XSS')",
        "<img src='x' onerror='alert(\"XSS\")'>",
        "JavaScript:alert('XSS')",
        "document.cookie",
        "<iframe src='javascript:alert(`XSS`)'></iframe>"
    ]
    
    print("XSS Vulnerability Check:")
    for input_str in test_inputs:
        print(f"Input: {input_str}")
        print(f"Vulnerable: {xss_vulnerability_check(input_str)}")
        print(f"Sanitized: {xss_sanitize(input_str)}")
        print()
```

