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

