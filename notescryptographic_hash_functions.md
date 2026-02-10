# Cybersecurity Study Notes

## Cryptographic Hash Functions

Cryptographic hash functions are fundamental tools in cybersecurity, serving as the backbone for various security applications. These functions take an input (or 'message') of any length and produce a fixed-size output, typically called a 'hash' or 'digest'.

### Key Characteristics:

- **One-way function**: It should be computationally infeasible to reverse the hash to obtain the original input.
- **Deterministic**: The same input always produces the same hash.
- **Avalanche effect**: A small change in the input results in a significantly different hash.
- **Collision resistance**: It should be extremely difficult to find two different inputs that produce the same hash.

### Common Hash Functions:

- MD5 (deprecated due to vulnerabilities)
- SHA-1 (also deprecated)
- SHA-256, SHA-384, SHA-512 (part of the SHA-2 family)
- SHA-3 (newest standard)

### Applications:

1. Password storage
2. Digital signatures
3. File integrity verification
4. Blockchain technology

### Best Practices:

- Always use cryptographically secure hash functions (e.g., SHA-256 or better).
- Never use deprecated hash functions like MD5 or SHA-1 for security-critical applications.
- Implement additional security measures like salting when hashing passwords.
- Regularly update hash functions as new standards and recommendations emerge.

### Real-world Example:

In password storage, instead of storing plaintext passwords, systems store hashed versions. When a user attempts to log in, the entered password is hashed and compared to the stored hash.

```python
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Store this hash instead of the actual password
stored_hash = hash_password("mySecurePassword123")

# Later, to verify:
entered_password = "mySecurePassword123"
if hash_password(entered_password) == stored_hash:
    print("Password is correct!")
else:
    print("Password is incorrect.")
```

By using cryptographic hash functions, even if the database is compromised, the actual passwords remain protected, as long as a strong, modern hash function is used along with proper salting techniques.

---

