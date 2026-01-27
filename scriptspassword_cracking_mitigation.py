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

```python
import hashlib
import random
import string
import time

def password_strength_checker(password):
    """
    Check the strength of a given password and suggest improvements.
    
    Args:
    password (str): The password to check
    
    Returns:
    dict: A dictionary containing the strength score and improvement suggestions
    
    This function is useful for both defensive security (helping users create strong passwords)
    and offensive security (understanding common password weaknesses).
    """
    score = 0
    suggestions = []
    
    # Check password length
    if len(password) < 8:
        suggestions.append("Increase password length to at least 8 characters")
    elif len(password) >= 12:
        score += 2
    else:
        score += 1
    
    # Check for uppercase letters
    if not any(c.isupper() for c in password):
        suggestions.append("Add uppercase letters")
    else:
        score += 1
    
    # Check for lowercase letters
    if not any(c.islower() for c in password):
        suggestions.append("Add lowercase letters")
    else:
        score += 1
    
    # Check for numbers
    if not any(c.isdigit() for c in password):
        suggestions.append("Add numbers")
    else:
        score += 1
    
    # Check for special characters
    special_chars = string.punctuation
    if not any(c in special_chars for c in password):
        suggestions.append("Add special characters")
    else:
        score += 1
    
    # Check for common patterns
    common_patterns = ['123', 'abc', 'qwerty', 'password', 'admin']
    if any(pattern in password.lower() for pattern in common_patterns):
        suggestions.append("Avoid common patterns and words")
        score -= 1
    
    # Calculate final strength score
    strength = (score / 6) * 100
    
    return {
        "strength": strength,
        "score": score,
        "suggestions": suggestions
    }

def simulate_brute_force(password, max_attempts=1000000):
    """
    Simulate a brute force attack on a given password.
    
    Args:
    password (str): The password to attack
    max_attempts (int): Maximum number of attempts before giving up
    
    Returns:
    tuple: (success, attempts, time_taken)
    
    This function demonstrates the importance of password complexity and
    the time required for brute force attacks, useful for both attackers and defenders.
    """
    start_time = time.time()
    charset = string.ascii_letters + string.digits + string.punctuation
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    
    for attempts in range(1, max_attempts + 1):
        guess = ''.join(random.choice(charset) for _ in range(len(password)))
        if hashlib.sha256(guess.encode()).hexdigest() == password_hash:
            end_time = time.time()
            return True, attempts, end_time - start_time
    
    end_time = time.time()
    return False, max_attempts, end_time - start_time

# Example usage
if __name__ == "__main__":
    test_password = "P@ssw0rd123"
    
    # Check password strength
    result = password_strength_checker(test_password)
    print(f"Password strength: {result['strength']}%")
    print(f"Suggestions: {', '.join(result['suggestions'])}")
    
    # Simulate brute force attack
    success, attempts, time_taken = simulate_brute_force(test_password)
    if success:
        print(f"Password cracked in {attempts} attempts and {time_taken:.2f} seconds")
    else:
        print(f"Failed to crack password after {attempts} attempts and {time_taken:.2f} seconds")
```

