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

