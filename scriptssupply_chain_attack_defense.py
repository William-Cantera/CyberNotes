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

