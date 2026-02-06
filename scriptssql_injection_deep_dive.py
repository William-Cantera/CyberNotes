# Cybersecurity educational code example
# Safe for learning only

```python
import re
import urllib.parse

def sql_injection_checker(user_input, context="login"):
    """
    Checks user input for potential SQL injection attempts.
    
    Args:
    user_input (str): The string to check for SQL injection patterns
    context (str): The context of the input (e.g., "login", "search")
    
    Returns:
    tuple: (is_suspicious, risk_level, reasons)
    
    Usage:
    result = sql_injection_checker("admin' --", "login")
    print(result)
    
    This function is useful for:
    1. Education: Understanding common SQL injection patterns
    2. Defense: Basic input validation and risk assessment
    3. Testing: Simulating potential attacks in a safe environment
    """
    
    is_suspicious = False
    risk_level = "Low"
    reasons = []
    
    # List of SQL injection patterns to check
    patterns = [
        (r"'\s*--", "Comment operator"),
        (r";\s*--", "Query stacking"),
        (r"UNION\s+SELECT", "UNION-based injection"),
        (r"OR\s+1\s*=\s*1", "OR 1=1 tautology"),
        (r"admin'\s*OR\s*'1'='1", "Login bypass attempt"),
        (r"DROP\s+TABLE", "Table dropping attempt"),
        (r"EXEC(\s|\+)+(xp|sp)_", "Stored procedure execution attempt"),
        (r"SELECT\s+.*\s+FROM", "SELECT statement"),
        (r"INSERT\s+INTO", "INSERT statement"),
        (r"UPDATE\s+.*\s+SET", "UPDATE statement"),
        (r"DELETE\s+FROM", "DELETE statement")
    ]
    
    # Decode URL-encoded input
    decoded_input = urllib.parse.unquote(user_input)
    
    # Check for each pattern
    for pattern, description in patterns:
        if re.search(pattern, decoded_input, re.IGNORECASE):
            is_suspicious = True
            reasons.append(description)
    
    # Assess risk level
    if len(reasons) > 2:
        risk_level = "High"
    elif len(reasons) > 0:
        risk_level = "Medium"
    
    # Context-specific checks
    if context == "login":
        if "Login bypass attempt" in reasons:
            risk_level = "High"
    elif context == "search":
        if "UNION-based injection" in reasons:
            risk_level = "High"
    
    return (is_suspicious, risk_level, reasons)

# Example usage
test_inputs = [
    "normal username",
    "admin' --",
    "1 UNION SELECT username, password FROM users",
    "search term' OR '1'='1",
    "Robert'); DROP TABLE Students;--"
]

for inp in test_inputs:
    result = sql_injection_checker(inp)
    print(f"Input: {inp}")
    print(f"Suspicious: {result[0]}")
    print(f"Risk Level: {result[1]}")
    print(f"Reasons: {', '.join(result[2])}")
    print("---")
```

