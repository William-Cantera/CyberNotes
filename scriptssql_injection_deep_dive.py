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

```python
import re
import urllib.parse

def sql_injection_checker(input_string):
    """
    Checks a given input string for potential SQL injection attempts.
    
    This function examines the input for common SQL injection patterns
    and returns a list of potential risks found.
    
    Args:
    input_string (str): The string to be checked for SQL injection attempts
    
    Returns:
    list: A list of potential SQL injection risks found in the input
    
    Usage:
    risks = sql_injection_checker("admin' OR '1'='1")
    for risk in risks:
        print(risk)
    
    This tool is useful for:
    - Developers to test their input validation
    - Security teams to scan for potential vulnerabilities
    - Educational purposes to understand SQL injection patterns
    """
    
    risks = []
    
    # Decode URL-encoded input
    decoded_input = urllib.parse.unquote(input_string)
    
    # Check for basic SQL injection attempts
    if re.search(r"(\s|^)(UNION|SELECT|FROM|WHERE)(\s|$)", decoded_input, re.IGNORECASE):
        risks.append("Potential SQL keywords detected")
    
    # Check for comment-based SQL injection
    if re.search(r"(--|#|/\*)", decoded_input):
        risks.append("SQL comment markers detected")
    
    # Check for equality-based SQL injection
    if re.search(r"('|\")\s*(=|LIKE)\s*('|\")", decoded_input, re.IGNORECASE):
        risks.append("Potential equality-based SQL injection detected")
    
    # Check for UNION-based SQL injection
    if re.search(r"UNION\s+(ALL\s+)?SELECT", decoded_input, re.IGNORECASE):
        risks.append("Potential UNION-based SQL injection detected")
    
    # Check for time-based blind SQL injection
    if re.search(r"(SLEEP|WAITFOR\s+DELAY|BENCHMARK)", decoded_input, re.IGNORECASE):
        risks.append("Potential time-based blind SQL injection detected")
    
    # Check for boolean-based blind SQL injection
    if re.search(r"(AND|OR)\s+(\d+|'[^']+'|\"[^\"]+\")\s*=\s*(\d+|'[^']+'|\"[^\"]+\")", decoded_input, re.IGNORECASE):
        risks.append("Potential boolean-based blind SQL injection detected")
    
    # Check for batched (stacked) queries
    if re.search(r";.*(\s|^)(INSERT|UPDATE|DELETE|DROP|TRUNCATE)(\s|$)", decoded_input, re.IGNORECASE):
        risks.append("Potential batched query detected")
    
    return risks

# Example usage
if __name__ == "__main__":
    test_inputs = [
        "admin' OR '1'='1",
        "1 UNION SELECT username, password FROM users",
        "1; DROP TABLE users--",
        "1 AND 1=1",
        "1' AND SLEEP(5)--",
        "Safe input here"
    ]
    
    for input_string in test_inputs:
        print(f"Checking: {input_string}")
        results = sql_injection_checker(input_string)
        if results:
            print("Potential SQL injection risks found:")
            for risk in results:
                print(f"- {risk}")
        else:
            print("No SQL injection risks detected.")
        print()
```

