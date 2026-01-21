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

