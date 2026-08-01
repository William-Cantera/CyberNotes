# Cybersecurity educational code example
# Safe for learning only

```python
import json
import re
from datetime import datetime, timedelta

def analyze_iam_policies(policy_file):
    """
    Analyzes IAM policies for potential security issues and best practice violations.
    
    Args:
    policy_file (str): Path to a JSON file containing IAM policies
    
    Returns:
    dict: Analysis results with potential issues and recommendations
    
    Usage:
    results = analyze_iam_policies('iam_policies.json')
    print(json.dumps(results, indent=2))
    
    This function is useful for both defensive security audits and penetration
    testing to identify overly permissive or outdated IAM configurations.
    """
    
    with open(policy_file, 'r') as f:
        policies = json.load(f)
    
    results = {
        "overly_permissive": [],
        "outdated": [],
        "unused": [],
        "recommendations": []
    }
    
    current_date = datetime.now()
    
    for policy in policies:
        # Check for overly permissive policies
        if "*" in policy.get("Action", []) and "*" in policy.get("Resource", []):
            results["overly_permissive"].append(policy["PolicyName"])
            results["recommendations"].append(f"Restrict broad permissions in {policy['PolicyName']}")
        
        # Check for outdated policies (assuming LastUpdated field exists)
        if "LastUpdated" in policy:
            last_updated = datetime.strptime(policy["LastUpdated"], "%Y-%m-%d")
            if (current_date - last_updated) > timedelta(days=180):
                results["outdated"].append(policy["PolicyName"])
                results["recommendations"].append(f"Review and update {policy['PolicyName']}")
        
        # Check for potentially unused policies (assuming LastUsed field exists)
        if "LastUsed" in policy:
            last_used = datetime.strptime(policy["LastUsed"], "%Y-%m-%d")
            if (current_date - last_used) > timedelta(days=90):
                results["unused"].append(policy["PolicyName"])
                results["recommendations"].append(f"Consider removing unused policy {policy['PolicyName']}")
        
        # Check for use of deprecated services or API versions
        for action in policy.get("Action", []):
            if re.search(r":2016|:2017|:2018", action):
                results["recommendations"].append(f"Update to latest API version in {policy['PolicyName']} for {action}")
    
    return results

# Example usage:
# results = analyze_iam_policies('iam_policies.json')
# print(json.dumps(results, indent=2))
```

# Fallback content for Cloud IAM Best Practices
Error 1

# Fallback content for Cloud IAM Best Practices
Error 1

# Fallback content for Cloud IAM Best Practices
Error 1

# Fallback content for Cloud IAM Best Practices
Error 1

