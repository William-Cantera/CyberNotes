# Cybersecurity educational code example
# Safe for learning only

```python
import hashlib
import os

def hash_file(file_path, algorithms=['md5', 'sha1', 'sha256']):
    """
    Calculate cryptographic hashes of a file using specified algorithms.
    
    Args:
    file_path (str): Path to the file to be hashed
    algorithms (list): List of hash algorithms to use (default: ['md5', 'sha1', 'sha256'])
    
    Returns:
    dict: A dictionary with algorithm names as keys and corresponding hash values as values
    
    Usage:
    result = hash_file('/path/to/file.txt')
    print(result)
    
    This function is useful in cybersecurity for:
    1. File integrity checking
    2. Malware identification (by comparing hashes with known malware databases)
    3. Digital forensics and data verification
    """
    
    result = {}
    
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    for algorithm in algorithms:
        if algorithm not in hashlib.algorithms_available:
            raise ValueError(f"Unsupported hash algorithm: {algorithm}")
        
        hash_obj = hashlib.new(algorithm)
        
        with open(file_path, 'rb') as file:
            for chunk in iter(lambda: file.read(4096), b''):
                hash_obj.update(chunk)
        
        result[algorithm] = hash_obj.hexdigest()
    
    return result

def compare_hashes(file_path, expected_hashes):
    """
    Compare the hashes of a file with expected hash values.
    
    Args:
    file_path (str): Path to the file to be checked
    expected_hashes (dict): Dictionary of expected hashes {algorithm: hash_value}
    
    Returns:
    dict: A dictionary with algorithm names as keys and boolean match results as values
    
    Usage:
    expected = {'md5': '098f6bcd4621d373cade4e832627b4f6', 'sha256': '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08'}
    result = compare_hashes('/path/to/file.txt', expected)
    print(result)
    
    This function is useful in cybersecurity for:
    1. Verifying file integrity during software updates
    2. Checking for unauthorized modifications to critical system files
    3. Validating downloaded files from untrusted sources
    """
    
    actual_hashes = hash_file(file_path, algorithms=list(expected_hashes.keys()))
    result = {}
    
    for algorithm, expected_hash in expected_hashes.items():
        result[algorithm] = actual_hashes[algorithm] == expected_hash
    
    return result

# Example usage
if __name__ == "__main__":
    try:
        file_path = "example.txt"
        
        # Create a sample file
        with open(file_path, "w") as f:
            f.write("Hello, World!")
        
        # Calculate hashes
        hashes = hash_file(file_path)
        print("Calculated hashes:", hashes)
        
        # Compare hashes
        expected_hashes = {
            'md5': '65a8e27d8879283831b664bd8b7f0ad4',
            'sha256': 'dffd6021bb2bd5b0af676290809ec3a53191dd81c7f70a4b28688a362182986f'
        }
        comparison = compare_hashes(file_path, expected_hashes)
        print("Hash comparison results:", comparison)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        # Clean up
        if os.path.exists(file_path):
            os.remove(file_path)
```

```python
import hashlib
import os

def hash_file(filename, algorithm='sha256'):
    """
    Calculate the hash of a file using the specified algorithm.
    
    Args:
    filename (str): Path to the file to be hashed
    algorithm (str): Hash algorithm to use (default: sha256)
    
    Returns:
    str: Hexadecimal representation of the file's hash
    
    This function is useful in cybersecurity for:
    - Verifying file integrity
    - Detecting changes in critical system files
    - Creating file signatures for malware analysis
    """
    
    # Dictionary of supported hash algorithms
    hash_functions = {
        'md5': hashlib.md5,
        'sha1': hashlib.sha1,
        'sha256': hashlib.sha256,
        'sha512': hashlib.sha512
    }
    
    if algorithm not in hash_functions:
        raise ValueError(f"Unsupported algorithm: {algorithm}")
    
    hash_obj = hash_functions[algorithm]()
    
    try:
        with open(filename, 'rb') as file:
            # Read and update hash in chunks for memory efficiency
            for chunk in iter(lambda: file.read(4096), b''):
                hash_obj.update(chunk)
        return hash_obj.hexdigest()
    except IOError:
        print(f"Error: File '{filename}' not found or inaccessible.")
        return None

def compare_file_hashes(file1, file2, algorithm='sha256'):
    """
    Compare the hashes of two files.
    
    Args:
    file1 (str): Path to the first file
    file2 (str): Path to the second file
    algorithm (str): Hash algorithm to use (default: sha256)
    
    Returns:
    bool: True if hashes match, False otherwise
    
    This function is useful for:
    - Verifying if two files are identical
    - Checking if a file has been modified
    - Validating downloaded files against known good hashes
    """
    
    hash1 = hash_file(file1, algorithm)
    hash2 = hash_file(file2, algorithm)
    
    if hash1 and hash2:
        return hash1 == hash2
    return False

def verify_file_integrity(filename, expected_hash, algorithm='sha256'):
    """
    Verify the integrity of a file by comparing its hash to an expected value.
    
    Args:
    filename (str): Path to the file to verify
    expected_hash (str): Expected hash value
    algorithm (str): Hash algorithm to use (default: sha256)
    
    Returns:
    bool: True if the file's hash matches the expected hash, False otherwise
    
    This function is crucial for:
    - Ensuring critical system files haven't been tampered with
    - Verifying the authenticity of downloaded software or updates
    - Detecting potential malware infections or unauthorized modifications
    """
    
    file_hash = hash_file(filename, algorithm)
    if file_hash:
        return file_hash.lower() == expected_hash.lower()
    return False

# Example usage
if __name__ == "__main__":
    # Calculate and print the SHA256 hash of this script
    print(f"SHA256 hash of this script: {hash_file(__file__)}")
    
    # Compare this script with itself (should be True)
    print(f"Self-comparison result: {compare_file_hashes(__file__, __file__)}")
    
    # Verify the integrity of this script (replace with actual hash)
    expected_hash = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    print(f"Integrity check result: {verify_file_integrity(__file__, expected_hash)}")
```

```python
import hashlib
import os

def hash_file(file_path, algorithms=['md5', 'sha1', 'sha256']):
    """
    Calculate cryptographic hashes for a given file.
    
    Args:
    file_path (str): Path to the file to be hashed
    algorithms (list): List of hash algorithms to use (default: md5, sha1, sha256)
    
    Returns:
    dict: A dictionary with algorithm names as keys and corresponding hash values
    
    This function is useful in cybersecurity for:
    - File integrity checking
    - Malware identification (comparing file hashes with known malware hashes)
    - Digital forensics (creating file fingerprints)
    """
    
    hash_dict = {}
    
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    for algorithm in algorithms:
        if algorithm not in hashlib.algorithms_available:
            raise ValueError(f"Unsupported hash algorithm: {algorithm}")
        
        hasher = hashlib.new(algorithm)
        
        with open(file_path, 'rb') as file:
            buffer = file.read(65536)  # Read in 64k chunks
            while len(buffer) > 0:
                hasher.update(buffer)
                buffer = file.read(65536)
        
        hash_dict[algorithm] = hasher.hexdigest()
    
    return hash_dict

def compare_hashes(file_path, known_hashes):
    """
    Compare file hashes with known hashes.
    
    Args:
    file_path (str): Path to the file to be checked
    known_hashes (dict): Dictionary of known hashes {algorithm: hash_value}
    
    Returns:
    dict: A dictionary with comparison results
    
    This function is useful for:
    - Verifying file integrity
    - Detecting file tampering
    - Identifying known malicious files
    """
    
    file_hashes = hash_file(file_path, algorithms=list(known_hashes.keys()))
    comparison = {}
    
    for algorithm, known_hash in known_hashes.items():
        if algorithm in file_hashes:
            comparison[algorithm] = file_hashes[algorithm] == known_hash
        else:
            comparison[algorithm] = False
    
    return comparison

# Example usage
if __name__ == "__main__":
    try:
        # Calculate hashes for a file
        file_path = "example.txt"
        hashes = hash_file(file_path)
        print(f"Hashes for {file_path}:")
        for algorithm, hash_value in hashes.items():
            print(f"{algorithm}: {hash_value}")
        
        # Compare with known hashes
        known_hashes = {
            "md5": "098f6bcd4621d373cade4e832627b4f6",
            "sha256": "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08"
        }
        results = compare_hashes(file_path, known_hashes)
        print("\nHash comparison results:")
        for algorithm, match in results.items():
            print(f"{algorithm}: {'Match' if match else 'Mismatch'}")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```

```python
import hashlib
import os
import time

def hash_file_checker(file_path, expected_hash, hash_type='sha256'):
    """
    Check if a file's hash matches an expected value.
    
    Args:
    file_path (str): Path to the file to be checked
    expected_hash (str): The expected hash value
    hash_type (str): The hash algorithm to use (default: sha256)
    
    Returns:
    tuple: (bool, str) - (Whether hash matches, Actual calculated hash)
    
    Usage:
    result, actual_hash = hash_file_checker('/path/to/file', 'expected_hash_value')
    
    This function is useful in cybersecurity for:
    1. Verifying file integrity
    2. Detecting unauthorized modifications
    3. Validating downloaded files
    4. Identifying known malicious files
    """
    
    # Dictionary of supported hash algorithms
    hash_functions = {
        'md5': hashlib.md5,
        'sha1': hashlib.sha1,
        'sha256': hashlib.sha256,
        'sha512': hashlib.sha512
    }
    
    # Check if the specified hash type is supported
    if hash_type not in hash_functions:
        raise ValueError(f"Unsupported hash type: {hash_type}")
    
    # Get the appropriate hash function
    hash_func = hash_functions[hash_type]
    
    # Check if file exists
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Calculate the file's hash
    start_time = time.time()
    with open(file_path, 'rb') as file:
        file_hash = hash_func()
        chunk = file.read(8192)
        while chunk:
            file_hash.update(chunk)
            chunk = file.read(8192)
    
    calculated_hash = file_hash.hexdigest()
    end_time = time.time()
    
    # Compare calculated hash with expected hash
    hash_matches = calculated_hash.lower() == expected_hash.lower()
    
    # Print results
    print(f"File: {file_path}")
    print(f"Hash type: {hash_type}")
    print(f"Calculated hash: {calculated_hash}")
    print(f"Expected hash: {expected_hash}")
    print(f"Hash match: {'Yes' if hash_matches else 'No'}")
    print(f"Time taken: {end_time - start_time:.4f} seconds")
    
    return hash_matches, calculated_hash

# Example usage:
# result, actual_hash = hash_file_checker('example.txt', '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824')
```

```python
import hashlib
import os
import time

def hash_file(file_path, algorithms=['md5', 'sha1', 'sha256']):
    """
    Calculate cryptographic hashes for a given file.
    
    Args:
    file_path (str): Path to the file to be hashed
    algorithms (list): List of hash algorithms to use (default: md5, sha1, sha256)
    
    Returns:
    dict: A dictionary with algorithm names as keys and corresponding hash values
    
    This function is useful in cybersecurity for:
    - File integrity checking
    - Malware identification (comparing hashes with known malware databases)
    - Digital forensics (creating file fingerprints)
    """
    
    hash_dict = {}
    
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    for algorithm in algorithms:
        if algorithm not in hashlib.algorithms_available:
            raise ValueError(f"Unsupported hash algorithm: {algorithm}")
        
        hash_obj = hashlib.new(algorithm)
        
        with open(file_path, 'rb') as file:
            for chunk in iter(lambda: file.read(4096), b''):
                hash_obj.update(chunk)
        
        hash_dict[algorithm] = hash_obj.hexdigest()
    
    return hash_dict

def benchmark_hash_speed(data_size=1024*1024, algorithms=['md5', 'sha1', 'sha256', 'sha512']):
    """
    Benchmark the speed of different hash algorithms.
    
    Args:
    data_size (int): Size of random data to hash, in bytes (default: 1 MB)
    algorithms (list): List of hash algorithms to benchmark
    
    Returns:
    dict: A dictionary with algorithm names as keys and speed in MB/s as values
    
    This function is useful in cybersecurity for:
    - Selecting appropriate hash algorithms based on performance requirements
    - Understanding the trade-offs between security and speed for different algorithms
    """
    
    speed_dict = {}
    data = os.urandom(data_size)
    
    for algorithm in algorithms:
        if algorithm not in hashlib.algorithms_available:
            raise ValueError(f"Unsupported hash algorithm: {algorithm}")
        
        hash_obj = hashlib.new(algorithm)
        
        start_time = time.time()
        hash_obj.update(data)
        hash_obj.hexdigest()
        end_time = time.time()
        
        speed = data_size / (end_time - start_time) / (1024 * 1024)  # MB/s
        speed_dict[algorithm] = round(speed, 2)
    
    return speed_dict

# Example usage:
if __name__ == "__main__":
    # File hashing example
    try:
        file_hashes = hash_file("example.txt")
        print("File Hashes:")
        for algo, hash_value in file_hashes.items():
            print(f"{algo}: {hash_value}")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    
    # Hash speed benchmark example
    print("\nHash Speed Benchmark:")
    speeds = benchmark_hash_speed()
    for algo, speed in speeds.items():
        print(f"{algo}: {speed} MB/s")
```

```python
import hashlib
import time

def hash_strength_checker(password):
    """
    Check the strength of different hash algorithms for a given password.
    
    This function demonstrates the time and output differences between
    various cryptographic hash functions. It's useful in cybersecurity
    to understand the trade-offs between speed and security for different
    hashing algorithms.
    
    Args:
    password (str): The password to hash and test.
    
    Returns:
    None. Prints results to console.
    
    Usage:
    hash_strength_checker("mypassword123")
    """
    
    algorithms = ['md5', 'sha1', 'sha256', 'sha3_256', 'blake2s', 'blake2b']
    
    print(f"Testing hash strength for password: {password}")
    print("-" * 50)
    
    for algo in algorithms:
        start_time = time.time()
        
        # Create a new hash object
        hasher = hashlib.new(algo)
        
        # Update the hash object with the password bytes
        hasher.update(password.encode('utf-8'))
        
        # Get the hexadecimal representation of the hash
        hashed = hasher.hexdigest()
        
        end_time = time.time()
        
        print(f"Algorithm: {algo}")
        print(f"Hash: {hashed}")
        print(f"Length: {len(hashed)} characters")
        print(f"Time taken: {(end_time - start_time):.6f} seconds")
        print("-" * 50)

    print("Note: Slower hashing algorithms and longer hash lengths generally")
    print("provide better security against brute-force and rainbow table attacks.")
    print("However, they also require more computational resources.")
    print("\nIn pentesting, understanding these differences helps in:")
    print("1. Identifying weak hashing algorithms in target systems")
    print("2. Estimating time required for potential brute-force attacks")
    print("3. Recommending stronger hashing algorithms for better security")

# Example usage
if __name__ == "__main__":
    hash_strength_checker("MySecurePassword123!")
```

```python
import hashlib
import os
import time

def hash_file(file_path, algorithms=None):
    """
    Calculate cryptographic hashes of a file using specified algorithms.
    
    Args:
    file_path (str): Path to the file to be hashed
    algorithms (list): List of hash algorithms to use. If None, uses default set.
    
    Returns:
    dict: A dictionary with algorithm names as keys and hex digests as values
    
    This function is useful in cybersecurity for:
    - Verifying file integrity
    - Detecting file modifications
    - Creating unique file identifiers
    - Comparing files without revealing their contents
    """
    
    if algorithms is None:
        algorithms = ['md5', 'sha1', 'sha256', 'sha512']
    
    results = {}
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    for algo in algorithms:
        if algo not in hashlib.algorithms_available:
            print(f"Warning: {algo} is not available. Skipping.")
            continue
        
        hash_obj = hashlib.new(algo)
        
        start_time = time.time()
        
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                hash_obj.update(chunk)
        
        end_time = time.time()
        
        results[algo] = {
            'digest': hash_obj.hexdigest(),
            'time': end_time - start_time
        }
    
    return results

def print_results(results):
    """
    Print the hash results in a formatted manner.
    """
    print("\nHash Results:")
    print("-" * 50)
    for algo, data in results.items():
        print(f"{algo.upper()}:")
        print(f"  Digest: {data['digest']}")
        print(f"  Time: {data['time']:.4f} seconds")
        print("-" * 50)

if __name__ == "__main__":
    file_path = input("Enter the path of the file to hash: ")
    try:
        results = hash_file(file_path)
        print_results(results)
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Usage example:
# python hash_file.py
# Then enter the path to the file when prompted
#
# This script demonstrates the use of cryptographic hash functions,
# which are essential in cybersecurity for ensuring data integrity,
# creating digital signatures, and securely storing passwords.
# It can be used to:
# 1. Verify downloaded files haven't been tampered with
# 2. Create checksums for malware samples
# 3. Benchmark different hash algorithms
# 4. Understand how file hashing works in practice
```

```python
import hashlib
import os
import time

def hash_file(filename, algorithm='sha256'):
    """
    Calculate the hash of a file using the specified algorithm.
    
    Args:
    filename (str): Path to the file to be hashed
    algorithm (str): Hash algorithm to use (default: sha256)
    
    Returns:
    str: Hexadecimal representation of the file's hash
    
    Raises:
    ValueError: If an unsupported hash algorithm is specified
    FileNotFoundError: If the specified file does not exist
    """
    
    # Dictionary of supported hash algorithms
    hash_funcs = {
        'md5': hashlib.md5,
        'sha1': hashlib.sha1,
        'sha256': hashlib.sha256,
        'sha512': hashlib.sha512
    }
    
    # Check if the specified algorithm is supported
    if algorithm not in hash_funcs:
        raise ValueError(f"Unsupported hash algorithm: {algorithm}")
    
    # Create a hash object
    hasher = hash_funcs[algorithm]()
    
    # Open the file in binary mode and update the hash object
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    
    # Return the hexadecimal representation of the hash
    return hasher.hexdigest()

def verify_file_integrity(filename, expected_hash, algorithm='sha256'):
    """
    Verify the integrity of a file by comparing its hash to an expected value.
    
    Args:
    filename (str): Path to the file to be verified
    expected_hash (str): Expected hash value
    algorithm (str): Hash algorithm to use (default: sha256)
    
    Returns:
    bool: True if the file's hash matches the expected hash, False otherwise
    """
    
    actual_hash = hash_file(filename, algorithm)
    return actual_hash.lower() == expected_hash.lower()

def monitor_file_changes(filename, interval=5, algorithm='sha256'):
    """
    Monitor a file for changes by periodically calculating its hash.
    
    Args:
    filename (str): Path to the file to be monitored
    interval (int): Time interval between checks in seconds (default: 5)
    algorithm (str): Hash algorithm to use (default: sha256)
    """
    
    initial_hash = hash_file(filename, algorithm)
    print(f"Initial {algorithm} hash: {initial_hash}")
    
    try:
        while True:
            time.sleep(interval)
            current_hash = hash_file(filename, algorithm)
            
            if current_hash != initial_hash:
                print(f"File changed! New {algorithm} hash: {current_hash}")
                initial_hash = current_hash
            else:
                print(f"File unchanged. {algorithm} hash: {current_hash}")
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

# Example usage:
if __name__ == "__main__":
    test_file = "example.txt"
    
    # Create a test file
    with open(test_file, "w") as f:
        f.write("This is a test file for hashing.")
    
    # Calculate and print the file's hash
    file_hash = hash_file(test_file)
    print(f"SHA256 hash of {test_file}: {file_hash}")
    
    # Verify file integrity
    is_valid = verify_file_integrity(test_file, file_hash)
    print(f"File integrity verified: {is_valid}")
    
    # Monitor file for changes
    print(f"Monitoring {test_file} for changes (Ctrl+C to stop):")
    monitor_file_changes(test_file)

# This script demonstrates the use of cryptographic hash functions for file integrity verification
# and change monitoring. These techniques are crucial in cybersecurity for:
# 1. Ensuring the integrity of critical system files
# 2. Detecting unauthorized modifications to sensitive data
# 3. Identifying potential

