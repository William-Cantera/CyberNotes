# Cybersecurity educational code example
# Safe for learning only

```python
import re
import hashlib
import secrets

def secure_password_policy_checker(password):
    """
    Check if a given password meets secure policy requirements.
    
    This function is useful in secure SDLC practices to ensure that 
    user-created passwords meet minimum security standards before 
    being accepted into the system.
    
    Usage:
    result = secure_password_policy_checker("MyP@ssw0rd123")
    if result['valid']:
        print("Password is secure!")
    else:
        print("Password is not secure. Issues:", result['issues'])
    
    Args:
    password (str): The password to check
    
    Returns:
    dict: A dictionary with 'valid' (bool) and 'issues' (list) keys
    """
    issues = []
    
    # Check length
    if len(password) < 12:
        issues.append("Password should be at least 12 characters long")
    
    # Check for uppercase
    if not re.search(r'[A-Z]', password):
        issues.append("Password should contain at least one uppercase letter")
    
    # Check for lowercase
    if not re.search(r'[a-z]', password):
        issues.append("Password should contain at least one lowercase letter")
    
    # Check for digits
    if not re.search(r'\d', password):
        issues.append("Password should contain at least one digit")
    
    # Check for special characters
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        issues.append("Password should contain at least one special character")
    
    # Check for common passwords (example list, should be more comprehensive in practice)
    common_passwords = ['password', '123456', 'qwerty', 'admin']
    if password.lower() in common_passwords:
        issues.append("Password is too common")
    
    # Calculate password entropy
    entropy = len(password) * log2(len(set(password)))
    if entropy < 60:
        issues.append("Password entropy is too low")
    
    return {
        'valid': len(issues) == 0,
        'issues': issues
    }

def generate_secure_password():
    """
    Generate a secure password that meets the policy requirements.
    
    This function is useful in secure SDLC practices to provide users 
    with a secure password option if they struggle to create one themselves.
    
    Usage:
    new_password = generate_secure_password()
    print("Your new secure password is:", new_password)
    
    Returns:
    str: A secure password meeting all policy requirements
    """
    while True:
        # Generate a 16-character password
        password = ''.join(secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*(),.?":{}|<>') for _ in range(16))
        
        # Check if it meets all requirements
        if secure_password_policy_checker(password)['valid']:
            return password

def hash_password(password):
    """
    Securely hash a password using SHA-256.
    
    This function demonstrates proper password hashing, which is crucial 
    in secure SDLC to protect stored passwords from breach exposure.
    
    Usage:
    hashed_password = hash_password("MySecurePassword123!")
    print("Hashed password:", hashed_password)
    
    Args:
    password (str): The password to hash
    
    Returns:
    str: The hashed password
    """
    return hashlib.sha256(password.encode()).hexdigest()

# Example usage
if __name__ == "__main__":
    test_password = "Weak"
    result = secure_password_policy_checker(test_password)
    print(f"Password '{test_password}' check result:")
    print("Valid:", result['valid'])
    print("Issues:", result['issues'])
    
    secure_passwor

```python
import re
import sys

def analyze_secure_sdlc_practices(code_file):
    """
    Analyzes a Python code file for basic secure SDLC practices.
    
    Usage: analyze_secure_sdlc_practices('path/to/code.py')
    
    This function checks for:
    1. Use of input() without validation
    2. Hardcoded credentials
    3. Use of deprecated/insecure functions
    4. Potential SQL injection vulnerabilities
    5. Lack of input sanitization

    Useful for:
    - Quick security checks during code reviews
    - Educating developers on common security pitfalls
    - Integrating basic security checks into CI/CD pipelines
    """

    with open(code_file, 'r') as file:
        code = file.read()

    issues = []

    # Check for use of input() without validation
    if 'input(' in code and not re.search(r'input\([^)]+\)\s*\.strip\(\)', code):
        issues.append("WARNING: Use of input() without validation detected.")

    # Check for hardcoded credentials
    if re.search(r'password\s*=\s*["\'][^"\']+["\']', code, re.IGNORECASE):
        issues.append("CRITICAL: Hardcoded password detected.")

    # Check for deprecated/insecure functions
    insecure_functions = ['eval(', 'exec(', 'os.system(', 'subprocess.call(']
    for func in insecure_functions:
        if func in code:
            issues.append(f"WARNING: Use of potentially insecure function {func} detected.")

    # Check for potential SQL injection vulnerabilities
    if re.search(r'cursor\.execute\([^)]*\+', code):
        issues.append("CRITICAL: Potential SQL injection vulnerability detected.")

    # Check for lack of input sanitization
    if 'sanitize' not in code and 'escape' not in code:
        issues.append("INFO: No obvious input sanitization detected. Verify manually.")

    return issues

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_code_file>")
        sys.exit(1)

    code_file = sys.argv[1]
    results = analyze_secure_sdlc_practices(code_file)

    if results:
        print("Potential security issues found:")
        for issue in results:
            print(f"- {issue}")
    else:
        print("No obvious security issues detected. Always perform thorough manual review.")

    print("\nRemember: This is a basic check and does not replace comprehensive security testing.")
```

```python
import re
import sys

def analyze_secure_sdlc_practices(code):
    """
    Analyzes Python code for basic secure SDLC practices.
    
    Usage: 
    analyze_secure_sdlc_practices(code_string)
    
    This function checks for common security issues in code and can be used
    as part of a secure code review process or developer education.
    It's a basic example and should be expanded for real-world use.
    """

    issues = []

    # Check for hardcoded secrets
    secret_pattern = r'(password|secret|api_key)\s*=\s*[\'\"][^\'\"\s]+[\'\"]'
    secrets = re.findall(secret_pattern, code, re.IGNORECASE)
    if secrets:
        issues.append(f"Potential hardcoded secrets found: {', '.join(secrets)}")

    # Check for use of dangerous functions
    dangerous_funcs = ['eval', 'exec', 'os.system', 'subprocess.call']
    for func in dangerous_funcs:
        if func in code:
            issues.append(f"Use of potentially dangerous function: {func}")

    # Check for SQL injection vulnerability
    sql_injection_pattern = r'execute\([\'"]SELECT.*?\%s.*?[\'"]'
    if re.search(sql_injection_pattern, code):
        issues.append("Potential SQL injection vulnerability detected")

    # Check for proper exception handling
    if 'except:' in code and 'except Exception:' not in code:
        issues.append("Broad exception handling detected. Consider catching specific exceptions.")

    # Check for use of assert statements (can be disabled at runtime)
    if 'assert' in code:
        issues.append("Use of assert statements found. These can be disabled at runtime.")

    # Check for use of print statements (might leak sensitive info in production)
    if 'print(' in code:
        issues.append("Use of print statements found. Ensure these are removed in production code.")

    return issues

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    try:
        with open(filename, 'r') as file:
            code = file.read()
            issues = analyze_secure_sdlc_practices(code)
            if issues:
                print("Potential security issues found:")
                for issue in issues:
                    print(f"- {issue}")
            else:
                print("No obvious security issues detected. Remember, this is a basic check and doesn't guarantee security.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except IOError:
        print(f"Error: Unable to read file '{filename}'.")
```

# Fallback content for Secure SDLC Practices
Error 1

