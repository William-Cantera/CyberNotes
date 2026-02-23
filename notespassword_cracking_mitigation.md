# Cybersecurity Study Notes

## Password Cracking Mitigation

Password cracking is a significant threat to cybersecurity. Implementing effective mitigation strategies is crucial to protect systems and user accounts. Here are key concepts and best practices for mitigating password cracking attempts:

### Key Concepts

1. **Password Complexity**: Enforcing strong password policies that require a mix of uppercase and lowercase letters, numbers, and special characters.

2. **Password Length**: Encouraging longer passwords or passphrases, as they are more resistant to brute-force attacks.

3. **Password Hashing**: Using strong, slow hashing algorithms like bcrypt or Argon2 to store passwords securely.

4. **Salt and Pepper**: Implementing salting and peppering techniques to make rainbow table attacks ineffective.

### Best Practices

- **Multi-Factor Authentication (MFA)**: Implement MFA to add an extra layer of security beyond passwords.
- **Account Lockout Policies**: Set up policies to lock accounts after a certain number of failed login attempts.
- **Regular Password Changes**: Encourage or enforce periodic password changes, but balance this with user convenience.
- **Password Blacklists**: Maintain a list of commonly used or previously breached passwords and prevent their use.
- **Monitoring and Logging**: Implement robust logging and monitoring systems to detect and alert on potential password cracking attempts.

### Real-World Example

Many organizations use password managers to generate and store complex, unique passwords for each account. For instance, a company might use a password policy like this:

```
Minimum length: 14 characters
Require: Uppercase, lowercase, numbers, and special characters
Prohibit: Common words, sequential characters, and personal information
Implement: Multi-factor authentication for all accounts
```

### Tip

When implementing password policies, consider the NIST Special Publication 800-63B guidelines. These recommend focusing on password length rather than complexity and suggest against mandatory periodic password changes unless there's evidence of compromise.

By applying these mitigation strategies, organizations can significantly reduce the risk of successful password cracking attempts and enhance overall security posture.

---

## Password Cracking Mitigation

Password cracking remains a significant threat to cybersecurity. Implementing effective mitigation strategies is crucial for protecting user accounts and sensitive information.

### Key Concepts

1. **Password Complexity**: Enforcing strong password policies
2. **Salting and Hashing**: Secure storage of passwords
3. **Rate Limiting**: Preventing brute-force attacks
4. **Multi-Factor Authentication (MFA)**: Adding an extra layer of security

### Best Practices

- **Implement Strong Password Policies**
  - Require minimum length (e.g., 12 characters)
  - Mix uppercase, lowercase, numbers, and special characters
  - Prohibit common words and patterns

- **Use Modern Hashing Algorithms**
  - Employ bcrypt, Argon2, or PBKDF2
  - Avoid outdated algorithms like MD5 or SHA-1

- **Salt Passwords Before Hashing**
  - Generate unique salt for each password
  - Combine salt with password before hashing

- **Enforce Account Lockouts**
  - Temporarily lock accounts after multiple failed attempts
  - Implement exponential backoff for retry attempts

- **Enable Multi-Factor Authentication**
  - Combine something the user knows (password) with something they have (e.g., smartphone) or are (biometrics)

### Real-World Example

A company experienced a data breach where hashed passwords were stolen. Passwords hashed with MD5 were quickly cracked, while those using bcrypt with a high work factor remained secure.

### Implementation Tip

To implement salting and hashing using bcrypt in Python:

```python
import bcrypt

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

# Usage
hashed_password = hash_password("user_password")
is_correct = verify_password("user_password", hashed_password)
```

By implementing these mitigation strategies, organizations can significantly reduce the risk of successful password cracking attempts and enhance overall account security.

---

