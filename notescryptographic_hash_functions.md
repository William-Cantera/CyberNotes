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

## Cryptographic Hash Functions

Cryptographic hash functions are fundamental tools in information security, providing a way to generate fixed-size outputs (called hashes) from arbitrary-sized inputs. These functions play a crucial role in various security applications, including:

- Data integrity verification
- Password storage
- Digital signatures
- Blockchain technology

### Key Properties

1. **One-way function**: It should be computationally infeasible to reverse the hash and obtain the original input.
2. **Deterministic**: The same input always produces the same hash output.
3. **Avalanche effect**: A small change in the input should result in a significantly different hash output.
4. **Collision resistance**: It should be extremely difficult to find two different inputs that produce the same hash.

### Common Hash Functions

- MD5 (deprecated due to vulnerabilities)
- SHA-1 (deprecated for most uses)
- SHA-256, SHA-384, SHA-512 (part of the SHA-2 family)
- SHA-3 family

### Best Practices

- Always use cryptographically secure hash functions (e.g., SHA-256 or better).
- Regularly update hash algorithms as older ones become vulnerable.
- For password hashing, use specialized algorithms like bcrypt, Argon2, or PBKDF2.
- Implement salting when storing password hashes to prevent rainbow table attacks.

### Real-world Example: File Integrity Check

To verify the integrity of a downloaded file:

1. The provider publishes the file's hash.
2. After downloading, the user generates the file's hash locally.
3. The user compares the two hashes to ensure they match.

```bash
# Generate SHA-256 hash of a file
shasum -a 256 filename.zip

# Compare with the published hash
echo "published_hash filename.zip" | shasum -a 256 -c
```

### Security Tip

Never transmit passwords in plain text. Instead, hash them client-side before sending them over the network. This practice helps protect the user's original password even if the transmission is intercepted.

---

## Cryptographic Hash Functions

Cryptographic hash functions are fundamental tools in cybersecurity, providing a way to create fixed-size outputs (hashes) from input data of any size. These functions play a crucial role in various security applications, including:

- Data integrity verification
- Password storage
- Digital signatures
- Blockchain technology

### Key Characteristics

1. **Deterministic**: The same input always produces the same hash output.
2. **Quick computation**: Generating a hash is fast for any given input.
3. **Pre-image resistance**: It's computationally infeasible to reverse a hash to find its input.
4. **Small changes, big impact**: A slight change in input results in a significantly different hash.
5. **Collision resistance**: It's extremely difficult to find two different inputs that produce the same hash.

### Common Hash Functions

- MD5 (128-bit) - No longer considered secure
- SHA-1 (160-bit) - Deprecated due to vulnerabilities
- SHA-256 (256-bit) - Widely used, part of the SHA-2 family
- SHA-3 (224, 256, 384, or 512-bit) - Newest standard, high security

### Best Practices

1. Use cryptographically secure hash functions (e.g., SHA-256 or higher).
2. Regularly update hash algorithms as older ones become vulnerable.
3. When storing passwords, always use salting in conjunction with hashing.
4. Verify file integrity using hash checksums before installation or execution.

### Real-World Example: File Integrity

To verify a downloaded file's integrity:

1. The provider publishes the file's hash.
2. After downloading, generate the file's hash locally.
3. Compare the two hashes; they should match exactly.

```bash
# Generate SHA-256 hash of a file
sha256sum filename.zip

# Output
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  filename.zip
```

By understanding and correctly implementing cryptographic hash functions, cybersecurity professionals can significantly enhance data security and integrity in various applications and systems.

---

## Cryptographic Hash Functions

Cryptographic hash functions are fundamental tools in information security, serving as the backbone for various cryptographic applications. These functions take an input (or 'message') of any length and produce a fixed-size output, typically called a 'hash' or 'digest'.

### Key Characteristics:

- **One-way function**: It should be computationally infeasible to reverse the hash to obtain the original input.
- **Deterministic**: The same input always produces the same hash.
- **Fast computation**: Generating the hash should be quick for any given input.
- **Avalanche effect**: A small change in the input should result in a significantly different hash.
- **Collision resistance**: It should be extremely difficult to find two different inputs that produce the same hash.

### Common Hash Functions:

- MD5 (128-bit) - *Note: No longer considered cryptographically secure*
- SHA-1 (160-bit) - *Note: Weaknesses have been found; avoid for new applications*
- SHA-2 family (SHA-256, SHA-512)
- SHA-3 family

### Best Practices:

1. Use cryptographically secure hash functions (e.g., SHA-256 or better).
2. Regularly update hash functions as new vulnerabilities are discovered.
3. For password storage, use specialized password hashing functions like bcrypt, scrypt, or Argon2.
4. Implement salt when hashing passwords to prevent rainbow table attacks.

### Real-world Example:

Digital signatures often use hash functions. Instead of signing an entire document, which would be computationally expensive, the document is first hashed, and then the hash is signed.

```python
import hashlib

document = "This is a confidential message."
hash_object = hashlib.sha256(document.encode())
document_hash = hash_object.hexdigest()

print(f"Document hash: {document_hash}")
# Output: Document hash: a7630e8b56a0d6018a0f72d3f6c363b3dcb74961343d27e88e66e75fd9c51a65
```

In this example, SHA-256 is used to create a unique fingerprint of the document. This hash can then be signed with the sender's private key to create a digital signature, ensuring both integrity and authenticity of the document.

---

## Cryptographic Hash Functions

Cryptographic hash functions are fundamental tools in information security, serving as the backbone for various cryptographic applications. These functions take an input (or 'message') of any length and produce a fixed-size output, typically called a 'hash' or 'digest'.

### Key Characteristics:

- **One-way function**: It's computationally infeasible to reverse the hash to obtain the original input.
- **Deterministic**: The same input always produces the same hash.
- **Fixed output size**: Regardless of input size, the output length is constant.
- **Avalanche effect**: A small change in input results in a significantly different hash.
- **Collision resistance**: It's extremely difficult to find two different inputs that produce the same hash.

### Common Hash Functions:

- MD5 (deprecated due to vulnerabilities)
- SHA-1 (also considered weak)
- SHA-256, SHA-384, SHA-512 (part of the SHA-2 family)
- SHA-3 (newest standard)

### Best Practices:

1. Always use cryptographically secure hash functions (e.g., SHA-256 or higher).
2. Keep hash functions updated as older ones become vulnerable.
3. Use salting when hashing passwords to prevent rainbow table attacks.
4. Implement key stretching techniques like PBKDF2 for password hashing.

### Real-world Example:

Password storage is a common application of cryptographic hash functions. Instead of storing plaintext passwords, systems store their hashes:

```python
import hashlib

def hash_password(password):
    # Using SHA-256
    return hashlib.sha256(password.encode()).hexdigest()

# Store this hash instead of the actual password
stored_hash = hash_password("mySecurePassword123")
```

When a user attempts to log in, their input is hashed and compared to the stored hash.

### Security Tip:

Never try to implement your own cryptographic hash function. Always use well-established, thoroughly tested libraries and functions provided by reputable sources. Cryptography is complex, and even small mistakes can lead to significant vulnerabilities.

---

