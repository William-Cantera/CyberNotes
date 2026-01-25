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

