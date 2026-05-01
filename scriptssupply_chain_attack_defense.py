# Cybersecurity educational code example
# Safe for learning only

```python
import hashlib
import os
import json
import urllib.request
from typing import Dict, List

def verify_software_integrity(software_dir: str, manifest_url: str) -> Dict[str, List[str]]:
    """
    Verifies the integrity of software packages in a given directory against a remote manifest.

    This function is useful for detecting potential supply chain attacks where software
    packages or their dependencies might have been tampered with before reaching the end user.

    Args:
    software_dir (str): Path to the directory containing software packages to verify
    manifest_url (str): URL of the JSON manifest containing expected file hashes

    Returns:
    Dict[str, List[str]]: A dictionary with two keys: 'verified' and 'failed', each containing
                          a list of filenames that passed or failed the integrity check.

    Usage:
    result = verify_software_integrity("/path/to/software", "https://example.com/manifest.json")
    print(f"Verified files: {result['verified']}")
    print(f"Failed verification: {result['failed']}")

    Note: This is a simplified example. In a real-world scenario, you'd want to use HTTPS,
    implement proper error handling, and possibly use digital signatures for the manifest.
    """

    # Fetch and load the remote manifest
    with urllib.request.urlopen(manifest_url) as response:
        manifest = json.loads(response.read().decode())

    results = {"verified": [], "failed": []}

    # Iterate through all files in the software directory
    for filename in os.listdir(software_dir):
        filepath = os.path.join(software_dir, filename)
        if os.path.isfile(filepath):
            # Calculate SHA256 hash of the file
            with open(filepath, "rb") as f:
                file_hash = hashlib.sha256(f.read()).hexdigest()

            # Check if the file's hash matches the one in the manifest
            if filename in manifest and manifest[filename] == file_hash:
                results["verified"].append(filename)
            else:
                results["failed"].append(filename)

    return results

# Example usage:
# result = verify_software_integrity("/path/to/software", "https://example.com/manifest.json")
# print(f"Verified files: {result['verified']}")
# print(f"Failed verification: {result['failed']}")
```

```python
import os
import hashlib
import json
from datetime import datetime

def supply_chain_integrity_check(directory_path, manifest_file):
    """
    Perform a supply chain integrity check on software components.
    
    This function scans a directory for files, calculates their hashes,
    and compares them against a known-good manifest file. It helps detect
    potential supply chain attacks where files might have been tampered with.
    
    Args:
    directory_path (str): Path to the directory containing files to check
    manifest_file (str): Path to the JSON manifest file with known-good hashes
    
    Returns:
    dict: Results of the integrity check
    
    Usage:
    results = supply_chain_integrity_check("/path/to/software", "/path/to/manifest.json")
    """
    
    results = {
        "timestamp": datetime.now().isoformat(),
        "checked_files": 0,
        "mismatched_files": [],
        "missing_files": [],
        "extra_files": []
    }
    
    # Load the manifest file
    try:
        with open(manifest_file, 'r') as f:
            manifest = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"error": "Invalid or missing manifest file"}
    
    # Get list of files in the directory
    actual_files = set()
    for root, _, files in os.walk(directory_path):
        for file in files:
            actual_files.add(os.path.relpath(os.path.join(root, file), directory_path))
    
    # Check each file in the manifest
    for file_path, expected_hash in manifest.items():
        results["checked_files"] += 1
        full_path = os.path.join(directory_path, file_path)
        
        if os.path.exists(full_path):
            with open(full_path, 'rb') as f:
                file_hash = hashlib.sha256(f.read()).hexdigest()
            
            if file_hash != expected_hash:
                results["mismatched_files"].append(file_path)
            
            actual_files.remove(file_path)
        else:
            results["missing_files"].append(file_path)
    
    # Any remaining files in actual_files are extra
    results["extra_files"] = list(actual_files)
    
    return results

# Example usage:
if __name__ == "__main__":
    results = supply_chain_integrity_check("./software_package", "./manifest.json")
    print(json.dumps(results, indent=2))

"""
This script is useful in cybersecurity for:
1. Verifying the integrity of software packages before deployment
2. Detecting potential supply chain attacks where files might have been modified
3. Ensuring that all expected components are present and no extra files exist
4. Creating an audit trail of integrity checks for compliance purposes

To use:
1. Create a manifest.json file with expected file paths and their SHA256 hashes
2. Run the script, pointing it to your software directory and manifest file
3. Review the results to identify any discrepancies

Note: This is a basic implementation. In a real-world scenario, you might want to:
- Use more sophisticated hash algorithms or signing mechanisms
- Implement secure storage and transmission of the manifest file
- Add logging and alerting capabilities
- Integrate with CI/CD pipelines for automated checks
"""
```

```python
import hashlib
import json
import os
import sys
from datetime import datetime

def verify_software_supply_chain(software_dir):
    """
    Verifies the integrity of software components in a given directory.
    
    This function scans a directory containing software components (e.g., libraries, 
    executables) and compares their current hash values against a known good state.
    It helps detect potential supply chain attacks where components might have been 
    tampered with or replaced with malicious versions.

    Args:
    software_dir (str): Path to the directory containing software components

    Returns:
    dict: A report of the verification results

    Usage:
    python supply_chain_verifier.py /path/to/software/directory

    Why it's useful:
    - Helps detect unauthorized changes in software components
    - Can be integrated into CI/CD pipelines for automated checks
    - Provides an audit trail of software integrity over time
    """

    def calculate_file_hash(file_path):
        """Calculate SHA256 hash of a file."""
        sha256_hash = hashlib.sha256()
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()

    def load_known_hashes(json_file):
        """Load known good hashes from a JSON file."""
        if os.path.exists(json_file):
            with open(json_file, 'r') as f:
                return json.load(f)
        return {}

    def save_known_hashes(known_hashes, json_file):
        """Save current hashes to a JSON file."""
        with open(json_file, 'w') as f:
            json.dump(known_hashes, f, indent=2)

    known_hashes_file = os.path.join(software_dir, 'known_hashes.json')
    known_hashes = load_known_hashes(known_hashes_file)
    current_hashes = {}
    verification_results = {
        'timestamp': datetime.now().isoformat(),
        'verified': [],
        'new': [],
        'modified': [],
        'missing': []
    }

    # Scan and verify files
    for root, _, files in os.walk(software_dir):
        for file in files:
            if file == 'known_hashes.json':
                continue
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, software_dir)
            current_hash = calculate_file_hash(file_path)
            current_hashes[relative_path] = current_hash

            if relative_path in known_hashes:
                if current_hash == known_hashes[relative_path]:
                    verification_results['verified'].append(relative_path)
                else:
                    verification_results['modified'].append(relative_path)
            else:
                verification_results['new'].append(relative_path)

    # Check for missing files
    for known_file in known_hashes:
        if known_file not in current_hashes:
            verification_results['missing'].append(known_file)

    # Update known hashes
    save_known_hashes(current_hashes, known_hashes_file)

    return verification_results

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python supply_chain_verifier.py /path/to/software/directory")
        sys.exit(1)
    
    software_dir = sys.argv[1]
    results = verify_software_supply_chain(software_dir)
    print(json.dumps(results, indent=2))
```

```python
import hashlib
import os
import json
import time

def verify_software_supply_chain(software_path, manifest_path):
    """
    Verifies the integrity of a software package against a trusted manifest.
    
    This function helps defend against supply chain attacks by ensuring
    downloaded software matches expected cryptographic hashes.
    
    Args:
    software_path (str): Path to the software package to verify
    manifest_path (str): Path to the JSON manifest file with expected hashes
    
    Returns:
    bool: True if verification succeeds, False otherwise
    
    Usage:
    result = verify_software_supply_chain("/path/to/software.zip", "/path/to/manifest.json")
    if result:
        print("Software package verified successfully")
    else:
        print("Verification failed - potential supply chain attack!")
    """
    
    # Load the manifest file
    try:
        with open(manifest_path, 'r') as f:
            manifest = json.load(f)
    except (IOError, json.JSONDecodeError):
        print("Error: Unable to read or parse manifest file")
        return False
    
    # Verify the software package exists
    if not os.path.exists(software_path):
        print("Error: Software package not found")
        return False
    
    # Calculate SHA256 hash of the software package
    sha256_hash = hashlib.sha256()
    with open(software_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    calculated_hash = sha256_hash.hexdigest()
    
    # Compare calculated hash with expected hash from manifest
    expected_hash = manifest.get('sha256_hash')
    if not expected_hash:
        print("Error: Manifest does not contain expected SHA256 hash")
        return False
    
    if calculated_hash != expected_hash:
        print("Error: Hash mismatch")
        print(f"Calculated: {calculated_hash}")
        print(f"Expected:   {expected_hash}")
        return False
    
    # Verify timestamp (optional, assumes 'timestamp' key in manifest)
    if 'timestamp' in manifest:
        manifest_time = manifest['timestamp']
        current_time = int(time.time())
        if current_time - manifest_time > 86400:  # 24 hours
            print("Warning: Manifest is more than 24 hours old")
    
    print("Software package verified successfully")
    return True

# Example usage:
# verify_software_supply_chain("./downloaded_software.zip", "./trusted_manifest.json")
```

```python
import hashlib
import os
import json
import time

def verify_software_supply_chain(software_dir, manifest_file):
    """
    Verifies the integrity of software in a directory against a supplied manifest.
    
    This function helps defend against supply chain attacks by ensuring that
    the software files haven't been tampered with since the manifest was created.
    
    Args:
    software_dir (str): Path to the directory containing software files
    manifest_file (str): Path to the JSON manifest file with expected hashes
    
    Returns:
    tuple: (bool, list) - (True if all files match, list of mismatched files)
    
    Usage:
    result, mismatches = verify_software_supply_chain("./software", "manifest.json")
    if result:
        print("All files verified successfully!")
    else:
        print("Mismatched files:", mismatches)
    
    Why it's useful:
    - Detects unauthorized modifications in software supply chain
    - Can be integrated into CI/CD pipelines for automated checks
    - Helps maintain integrity of software before deployment
    """
    
    with open(manifest_file, 'r') as f:
        expected_hashes = json.load(f)
    
    mismatched_files = []
    
    for root, _, files in os.walk(software_dir):
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, software_dir)
            
            if relative_path in expected_hashes:
                with open(file_path, 'rb') as f:
                    file_hash = hashlib.sha256(f.read()).hexdigest()
                
                if file_hash != expected_hashes[relative_path]:
                    mismatched_files.append(relative_path)
            else:
                print(f"Warning: {relative_path} not found in manifest")
    
    return len(mismatched_files) == 0, mismatched_files

def create_software_manifest(software_dir, output_file):
    """
    Creates a manifest file with SHA256 hashes of all files in a directory.
    
    This function helps in creating a baseline for software integrity checks.
    
    Args:
    software_dir (str): Path to the directory containing software files
    output_file (str): Path where the manifest JSON file will be saved
    
    Usage:
    create_software_manifest("./software", "manifest.json")
    
    Why it's useful:
    - Establishes a trusted baseline for software integrity
    - Can be used in conjunction with verify_software_supply_chain()
    - Helps in tracking changes in software over time
    """
    
    manifest = {}
    
    for root, _, files in os.walk(software_dir):
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, software_dir)
            
            with open(file_path, 'rb') as f:
                file_hash = hashlib.sha256(f.read()).hexdigest()
            
            manifest[relative_path] = file_hash
    
    with open(output_file, 'w') as f:
        json.dump(manifest, f, indent=4)

    print(f"Manifest created: {output_file}")

# Example usage
if __name__ == "__main__":
    software_dir = "./example_software"
    manifest_file = "manifest.json"
    
    # Create a manifest
    create_software_manifest(software_dir, manifest_file)
    
    # Simulate some time passing
    time.sleep(2)
    
    # Verify the software against the manifest
    result, mismatches = verify_software_supply_chain(software_dir, manifest_file)
    
    if result:
        print("All files verified successfully!")
    else:
        print("Mismatched files:", mismatches)
```

```python
import hashlib
import os
import json
import time

def check_software_integrity(software_dir, manifest_file):
    """
    Checks the integrity of software files against a known-good manifest.
    
    This function helps detect potential supply chain attacks by verifying
    that installed software files match their expected cryptographic hashes.
    
    Args:
    software_dir (str): Directory containing the software files to check
    manifest_file (str): Path to JSON manifest file with expected file hashes
    
    Returns:
    list: List of any files that failed the integrity check
    
    Usage:
    failed_files = check_software_integrity("/path/to/software", "manifest.json")
    if failed_files:
        print("Warning: Possible supply chain attack detected!")
        for file in failed_files:
            print(f"Integrity check failed for: {file}")
    else:
        print("All files passed integrity check.")
    """
    
    # Load the manifest file
    with open(manifest_file, 'r') as f:
        manifest = json.load(f)
    
    failed_files = []
    
    # Iterate through all files in the software directory
    for root, _, files in os.walk(software_dir):
        for filename in files:
            filepath = os.path.join(root, filename)
            rel_path = os.path.relpath(filepath, software_dir)
            
            # Skip files not in the manifest
            if rel_path not in manifest:
                continue
            
            # Calculate the SHA256 hash of the file
            with open(filepath, 'rb') as f:
                file_hash = hashlib.sha256(f.read()).hexdigest()
            
            # Compare the calculated hash with the expected hash
            if file_hash != manifest[rel_path]:
                failed_files.append(rel_path)
    
    return failed_files

def generate_manifest(software_dir, output_file):
    """
    Generates a manifest file with SHA256 hashes of all files in a directory.
    
    This function can be used to create a "known-good" manifest for later
    integrity checking. It should be run in a secure environment before
    deploying software.
    
    Args:
    software_dir (str): Directory containing the software files
    output_file (str): Path to save the generated manifest JSON file
    
    Usage:
    generate_manifest("/path/to/clean/software", "manifest.json")
    """
    
    manifest = {}
    
    for root, _, files in os.walk(software_dir):
        for filename in files:
            filepath = os.path.join(root, filename)
            rel_path = os.path.relpath(filepath, software_dir)
            
            with open(filepath, 'rb') as f:
                file_hash = hashlib.sha256(f.read()).hexdigest()
            
            manifest[rel_path] = file_hash
    
    with open(output_file, 'w') as f:
        json.dump(manifest, f, indent=2)

# Example usage
if __name__ == "__main__":
    # Generate a manifest for a "known-good" software directory
    generate_manifest("./clean_software", "manifest.json")
    
    # Simulate some time passing
    time.sleep(2)
    
    # Check the integrity of the software directory
    failed = check_software_integrity("./clean_software", "manifest.json")
    
    if failed:
        print("Warning: Possible supply chain attack detected!")
        for file in failed:
            print(f"Integrity check failed for: {file}")
    else:
        print("All files passed integrity check.")
```

```python
import hashlib
import os
import json
import time

def verify_package_integrity(package_dir, manifest_file):
    """
    Verifies the integrity of files in a software package against a manifest.
    
    This function helps defend against supply chain attacks by ensuring
    that the files in a software package haven't been tampered with.
    
    Args:
    package_dir (str): Path to the directory containing package files
    manifest_file (str): Path to the manifest JSON file
    
    Returns:
    tuple: (bool, list) - (integrity_check_passed, list_of_mismatched_files)
    
    Usage:
    passed, mismatches = verify_package_integrity('./my_package', './manifest.json')
    if passed:
        print("Package integrity verified.")
    else:
        print(f"Integrity check failed. Mismatched files: {mismatches}")
    
    Note: This is a simplified example. In practice, you'd want to use
    more sophisticated methods like digital signatures for verification.
    """
    
    def calculate_file_hash(filepath):
        """Calculate SHA256 hash of a file."""
        sha256_hash = hashlib.sha256()
        with open(filepath, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    
    # Load the manifest
    with open(manifest_file, 'r') as f:
        manifest = json.load(f)
    
    mismatched_files = []
    
    # Verify each file in the manifest
    for filename, expected_hash in manifest.items():
        filepath = os.path.join(package_dir, filename)
        
        if not os.path.exists(filepath):
            mismatched_files.append(f"{filename} (missing)")
            continue
        
        actual_hash = calculate_file_hash(filepath)
        
        if actual_hash != expected_hash:
            mismatched_files.append(filename)
    
    return len(mismatched_files) == 0, mismatched_files

# Example usage and demonstration
if __name__ == "__main__":
    # Create a mock package and manifest for demonstration
    os.makedirs("./mock_package", exist_ok=True)
    
    with open("./mock_package/file1.txt", "w") as f:
        f.write("This is file 1")
    with open("./mock_package/file2.txt", "w") as f:
        f.write("This is file 2")
    
    manifest = {
        "file1.txt": calculate_file_hash("./mock_package/file1.txt"),
        "file2.txt": calculate_file_hash("./mock_package/file2.txt")
    }
    
    with open("./manifest.json", "w") as f:
        json.dump(manifest, f)
    
    # Verify the package
    passed, mismatches = verify_package_integrity("./mock_package", "./manifest.json")
    print(f"Initial check passed: {passed}")
    
    # Simulate a supply chain attack by modifying a file
    time.sleep(1)  # Wait to ensure file modification time changes
    with open("./mock_package/file1.txt", "a") as f:
        f.write("\nThis file has been tampered with!")
    
    # Verify again
    passed, mismatches = verify_package_integrity("./mock_package", "./manifest.json")
    print(f"Check after tampering passed: {passed}")
    print(f"Mismatched files: {mismatches}")
    
    # Clean up
    os.remove("./mock_package/file1.txt")
    os.remove("./mock_package/file2.txt")
    os.rmdir("./mock_package")
    os.remove("./manifest.json")
```

# Fallback content for Supply Chain Attack Defense
Error 1

