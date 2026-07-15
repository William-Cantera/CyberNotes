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

```python
import hashlib
import re
import time

def password_strength_checker(password):
    """
    Check the strength of a given password and provide feedback.
    
    This function analyzes a password for common weaknesses and provides
    a score along with suggestions for improvement. It's useful for:
    - Educating users on password security
    - Implementing password policies
    - Demonstrating password cracking mitigation techniques
    
    Usage:
    score, feedback = password_strength_checker("your_password_here")
    print(f"Password strength: {score}/5")
    print("Feedback:", feedback)
    
    :param password: The password to check
    :return: Tuple containing score (0-5) and feedback string
    """
    score = 5
    feedback = []
    
    # Check length
    if len(password) < 12:
        score -= 1
        feedback.append("Password should be at least 12 characters long.")
    
    # Check for uppercase, lowercase, numbers, and special characters
    if not re.search(r'[A-Z]', password):
        score -= 1
        feedback.append("Include at least one uppercase letter.")
    if not re.search(r'[a-z]', password):
        score -= 1
        feedback.append("Include at least one lowercase letter.")
    if not re.search(r'\d', password):
        score -= 1
        feedback.append("Include at least one number.")
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score -= 1
        feedback.append("Include at least one special character.")
    
    # Check for common patterns
    common_patterns = ['123', 'abc', 'qwerty', 'password', 'admin']
    if any(pattern in password.lower() for pattern in common_patterns):
        score -= 1
        feedback.append("Avoid common words or patterns.")
    
    # Simulate basic brute-force attempt
    start_time = time.time()
    iterations = 100000
    for _ in range(iterations):
        hashlib.sha256(password.encode()).hexdigest()
    time_taken = time.time() - start_time
    
    crack_time_estimate = (time_taken / iterations) * (36 ** len(password))
    if crack_time_estimate < 1e6:  # Less than 11.5 days
        feedback.append(f"Estimated brute-force time: {crack_time_estimate:.2f} seconds. Consider a stronger password.")
    
    score = max(0, score)  # Ensure score doesn't go below 0
    feedback_str = " ".join(feedback) if feedback else "Good password!"
    
    return score, feedback_str

# Example usage
if __name__ == "__main__":
    test_passwords = [
        "password123",
        "P@ssw0rd!",
        "thisisaverylongpasswordbutnotsecure",
        "Tr0ub4dor&3",
        "correcthorsebatterystaple"
    ]
    
    for pwd in test_passwords:
        score, feedback = password_strength_checker(pwd)
        print(f"Password: {pwd}")
        print(f"Strength: {score}/5")
        print(f"Feedback: {feedback}")
        print("-" * 50)
```

```python
import hashlib
import string
import random
import time

def password_strength_checker(password):
    """
    Check the strength of a given password and provide feedback.
    
    Args:
    password (str): The password to check
    
    Returns:
    tuple: (score, feedback)
    
    This function is useful for both defensive purposes (helping users create strong passwords)
    and for understanding common password weaknesses during penetration testing.
    """
    score = 0
    feedback = []
    
    # Check length
    if len(password) < 8:
        feedback.append("Password is too short. Aim for at least 8 characters.")
    elif len(password) >= 12:
        score += 2
        feedback.append("Good length!")
    else:
        score += 1
    
    # Check for uppercase
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add uppercase letters for complexity.")
    
    # Check for lowercase
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Add lowercase letters for complexity.")
    
    # Check for digits
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Add numbers for complexity.")
    
    # Check for special characters
    if any(c in string.punctuation for c in password):
        score += 1
    else:
        feedback.append("Add special characters for complexity.")
    
    # Simulate basic dictionary attack
    common_passwords = ['password', '123456', 'qwerty', 'admin']
    if password.lower() in common_passwords:
        score = 0
        feedback.append("This is a very common password. Highly insecure!")
    
    # Provide overall assessment
    if score < 3:
        feedback.insert(0, "Weak password. Please improve.")
    elif score < 5:
        feedback.insert(0, "Moderate password. Could be stronger.")
    else:
        feedback.insert(0, "Strong password!")
    
    return (score, feedback)

def simulate_brute_force(password, max_attempts=1000000):
    """
    Simulate a simple brute force attack to demonstrate the importance of password complexity.
    
    Args:
    password (str): The password to crack
    max_attempts (int): Maximum number of attempts before giving up
    
    Returns:
    tuple: (success, attempts, time_taken)
    
    This simulation helps in understanding the relationship between password complexity
    and the time required to crack it, emphasizing the importance of strong passwords.
    """
    charset = string.ascii_letters + string.digits + string.punctuation
    attempts = 0
    start_time = time.time()
    
    while attempts < max_attempts:
        guess = ''.join(random.choice(charset) for _ in range(len(password)))
        attempts += 1
        
        if guess == password:
            end_time = time.time()
            return (True, attempts, end_time - start_time)
    
    end_time = time.time()
    return (False, attempts, end_time - start_time)

# Example usage
if __name__ == "__main__":
    test_password = "P@ssw0rd123"
    
    # Check password strength
    strength_score, feedback = password_strength_checker(test_password)
    print(f"Password strength score: {strength_score}/6")
    for item in feedback:
        print(f"- {item}")
    
    # Simulate brute force attack
    success, attempts, time_taken = simulate_brute_force(test_password)
    if success:
        print(f"\nPassword cracked in {attempts} attempts and {time_taken:.2f} seconds")
    else:
        print(f"\nFailed to crack password after {attempts} attempts and {time_taken:.2f} seconds")
```

# Fallback content for Password Cracking Mitigation
Error 1

# Fallback content for Password Cracking Mitigation
Error 1

# Fallback content for Password Cracking Mitigation
Error 1

# Fallback content for Password Cracking Mitigation
Error 1

