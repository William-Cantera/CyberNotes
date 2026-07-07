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

```python
import re
import urllib.parse

def sql_injection_checker(input_string):
    """
    Checks a given input string for potential SQL injection attempts.
    
    Args:
    input_string (str): The string to check for SQL injection patterns
    
    Returns:
    tuple: (is_suspect, reasons)
        is_suspect (bool): True if potential SQL injection detected, False otherwise
        reasons (list): List of reasons why the input is suspect
    
    Usage:
    result, reasons = sql_injection_checker("user' OR '1'='1")
    if result:
        print("Potential SQL injection detected!")
        for reason in reasons:
            print(f"- {reason}")
    
    This function is useful in pentesting to identify potential vulnerabilities
    in input handling, and in defense to validate and sanitize user inputs.
    """
    
    is_suspect = False
    reasons = []
    
    # List of SQL injection patterns to check
    patterns = [
        (r"'\s*OR\s*'?\d+'?='?\d+'?", "OR condition"),
        (r"'\s*;\s*", "Multiple SQL statements"),
        (r"--", "SQL comment"),
        (r"UNION\s+SELECT", "UNION SELECT statement"),
        (r"DROP\s+TABLE", "DROP TABLE statement"),
        (r"INSERT\s+INTO", "INSERT INTO statement"),
        (r"DELETE\s+FROM", "DELETE FROM statement"),
        (r"UPDATE\s+\w+\s+SET", "UPDATE statement"),
        (r"\bEXEC\b", "EXEC statement"),
        (r"xp_cmdshell", "xp_cmdshell procedure"),
    ]
    
    # URL decode the input string to catch encoded injection attempts
    decoded_input = urllib.parse.unquote(input_string)
    
    for pattern, reason in patterns:
        if re.search(pattern, decoded_input, re.IGNORECASE):
            is_suspect = True
            reasons.append(f"Detected potential {reason}")
    
    # Check for suspicious number of single quotes
    if decoded_input.count("'") > 2:
        is_suspect = True
        reasons.append("Suspicious number of single quotes")
    
    # Check for SQL keywords
    sql_keywords = ['SELECT', 'FROM', 'WHERE', 'AND', 'OR', 'UNION', 'JOIN', 'HAVING', 'GROUP BY']
    found_keywords = [keyword for keyword in sql_keywords if keyword in decoded_input.upper()]
    if found_keywords:
        is_suspect = True
        reasons.append(f"SQL keywords detected: {', '.join(found_keywords)}")
    
    return is_suspect, reasons

# Example usage
test_inputs = [
    "normal input",
    "user' OR '1'='1",
    "admin'--",
    "SELECT%20*%20FROM%20users",
    "1'; DROP TABLE users; --",
    "' UNION SELECT username, password FROM users --",
]

for test_input in test_inputs:
    result, reasons = sql_injection_checker(test_input)
    print(f"\nChecking: {test_input}")
    if result:
        print("Potential SQL injection detected!")
        for reason in reasons:
            print(f"- {reason}")
    else:
        print("No SQL injection detected.")
```

```python
import re
import urllib.parse

def sql_injection_scanner(url, params):
    """
    Scans a URL and its parameters for potential SQL injection vulnerabilities.
    
    Args:
    url (str): The base URL to scan
    params (dict): A dictionary of parameter names and values
    
    Returns:
    list: A list of potentially vulnerable parameters
    
    This function is useful for identifying potential SQL injection points
    during penetration testing or security audits. It helps defenders 
    understand how attackers might probe for vulnerabilities.
    
    Usage example:
    url = "http://example.com/search"
    params = {"q": "user input", "sort": "date"}
    vulnerable_params = sql_injection_scanner(url, params)
    """
    
    vulnerable_params = []
    payloads = [
        "' OR '1'='1",
        "1 OR 1=1",
        "' UNION SELECT NULL--",
        '" OR ""="',
        "1' ORDER BY 1--",
        "1 AND 1=1",
        "' AND '1'='1",
        "1; DROP TABLE users--",
    ]
    
    for param, value in params.items():
        for payload in payloads:
            # Construct the test URL
            test_params = params.copy()
            test_params[param] = payload
            test_url = url + "?" + urllib.parse.urlencode(test_params)
            
            # Simulate sending a request (in a real scenario, you'd use requests library)
            print(f"Testing: {test_url}")
            
            # Check for common SQL error patterns in the response
            # (In a real scenario, you'd analyze the actual HTTP response)
            error_patterns = [
                r"SQL syntax.*MySQL",
                r"Warning.*mysql_.*",
                r"valid MySQL result",
                r"MySqlClient\.",
                r"ORA-[0-9][0-9][0-9][0-9]",
                r"Oracle error",
                r"Microsoft SQL Server",
                r"ODBC Driver.*SQL Server",
                r"SQLite/JDBCDriver",
                r"SQLite.Exception",
                r"System.Data.SQLite.SQLiteException",
                r"PostgreSQL.*ERROR",
                r"Warning.*\Wpg_.*",
                r"valid PostgreSQL result",
            ]
            
            # Simulate checking response for SQL errors
            # (In a real scenario, you'd check the actual HTTP response content)
            mock_response = "Some content... valid MySQL result ... More content"
            
            for pattern in error_patterns:
                if re.search(pattern, mock_response, re.IGNORECASE):
                    if param not in vulnerable_params:
                        vulnerable_params.append(param)
                    break
    
    return vulnerable_params

# Example usage
if __name__ == "__main__":
    test_url = "http://example.com/search"
    test_params = {
        "q": "user input",
        "sort": "date",
        "page": "1"
    }
    
    results = sql_injection_scanner(test_url, test_params)
    
    if results:
        print("Potentially vulnerable parameters:", results)
    else:
        print("No obvious vulnerabilities detected.")
```

# Fallback content for SQL Injection Deep Dive
Error 1

# Fallback content for SQL Injection Deep Dive
Error 1

# Fallback content for SQL Injection Deep Dive
Error 1

# Fallback content for SQL Injection Deep Dive
Error 1

# Fallback content for SQL Injection Deep Dive
Error 1

# Fallback content for SQL Injection Deep Dive
Error 1

# Fallback content for SQL Injection Deep Dive
Error 1

