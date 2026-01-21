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

