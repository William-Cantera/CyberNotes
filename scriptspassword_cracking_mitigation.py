# Cybersecurity educational code example
# Safe for learning only

```python
import hashlib
import random
import string
import time

def password_strength_checker(password):
    """
    Check the strength of a given password and provide feedback.
    
    Args:
    password (str): The password to check
    
    Returns:
    tuple: (score, feedback)
    
    This function is useful for both defenders and pentesters:
    - Defenders can use it to enforce strong password policies
    - Pentesters can use it to demonstrate password vulnerabilities
    """
    
    score = 0
    feedback = []
    
    # Check length
    if len(password) < 8:
        feedback.append("Password is too short. Use at least 8 characters.")
    elif len(password) >= 12:
        score += 1
        feedback.append("Good password length.")
    
    # Check for uppercase
    if not any(c.isupper() for c in password):
        feedback.append("Add uppercase letters.")
    else:
        score += 1
    
    # Check for lowercase
    if not any(c.islower() for c in password):
        feedback.append("Add lowercase letters.")
    else:
        score += 1
    
    # Check for digits
    if not any(c.isdigit() for c in password):
        feedback.append("Add numbers.")
    else:
        score += 1
    
    # Check for special characters
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    if not any(c in special_chars for c in password):
        feedback.append("Add special characters.")
    else:
        score += 1
    
    # Check for common passwords
    common_passwords = ["password", "123456", "qwerty", "admin"]
    if password.lower() in common_passwords:
        score = 0
        feedback = ["This is a very common password. Please choose a unique one."]
    
    return score, feedback

def simulate_brute_force(password):
    """
    Simulate a brute force attack on a given password.
    
    Args:
    password (str): The password to attack
    
    Returns:
    float: Time taken to crack the password
    
    This simulation helps demonstrate the importance of password complexity:
    - Shows how quickly simple passwords can be cracked
    - Illustrates the exponential increase in cracking time for complex passwords
    """
    
    start_time = time.time()
    charset = string.ascii_letters + string.digits + string.punctuation
    
    attempt = ""
    while attempt != password:
        attempt = ''.join(random.choice(charset) for _ in range(len(password)))
    
    end_time = time.time()
    return end_time - start_time

def main():
    password = input("Enter a password to check: ")
    
    score, feedback = password_strength_checker(password)
    print(f"Password strength score: {score}/5")
    for item in feedback:
        print(f"- {item}")
    
    if score < 3:
        print("\nThis password is weak. Here's why it matters:")
        crack_time = simulate_brute_force(password)
        print(f"Simulated brute force cracking time: {crack_time:.2f} seconds")
        print("A real attack could be much faster with optimized hardware and techniques.")
    else:
        print("\nGood job! This password is relatively strong.")
        print("Remember to use unique passwords for each account and consider a password manager.")

if __name__ == "__main__":
    main()
```

