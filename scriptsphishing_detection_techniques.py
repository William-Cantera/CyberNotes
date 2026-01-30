# Cybersecurity educational code example
# Safe for learning only

```python
import re
import urllib.parse
from urllib.request import urlopen
from html.parser import HTMLParser

class LinkExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    self.links.append(attr[1])

def analyze_url_for_phishing(url):
    """
    Analyzes a given URL for potential phishing indicators.
    
    Args:
    url (str): The URL to analyze
    
    Returns:
    dict: A dictionary containing analysis results and risk score
    
    Usage:
    result = analyze_url_for_phishing("http://example.com")
    print(result)
    
    This function is useful in cybersecurity for:
    1. Quickly assessing potential phishing URLs
    2. Automated scanning of links in emails or messages
    3. Educational purposes to understand phishing techniques
    """
    
    risk_score = 0
    analysis = {}
    
    # Check for HTTP vs HTTPS
    if url.startswith('http://'):
        risk_score += 1
        analysis['uses_http'] = True
    else:
        analysis['uses_http'] = False
    
    # Check for IP address in hostname
    parsed_url = urllib.parse.urlparse(url)
    if re.match(r'\d+\.\d+\.\d+\.\d+', parsed_url.hostname):
        risk_score += 1
        analysis['ip_in_domain'] = True
    else:
        analysis['ip_in_domain'] = False
    
    # Check for suspicious TLDs
    suspicious_tlds = ['.tk', '.ml', '.ga', '.cf', '.gq']
    if any(parsed_url.hostname.endswith(tld) for tld in suspicious_tlds):
        risk_score += 1
        analysis['suspicious_tld'] = True
    else:
        analysis['suspicious_tld'] = False
    
    # Check for suspicious keywords in URL
    suspicious_keywords = ['login', 'signin', 'verify', 'secure', 'account']
    if any(keyword in url.lower() for keyword in suspicious_keywords):
        risk_score += 1
        analysis['suspicious_keywords'] = True
    else:
        analysis['suspicious_keywords'] = False
    
    # Analyze page content
    try:
        with urlopen(url, timeout=5) as response:
            html_content = response.read().decode('utf-8')
            
            # Check for form actions
            if '<form' in html_content.lower() and 'action=' in html_content.lower():
                risk_score += 1
                analysis['has_form_with_action'] = True
            else:
                analysis['has_form_with_action'] = False
            
            # Extract and analyze links
            link_extractor = LinkExtractor()
            link_extractor.feed(html_content)
            external_links = [link for link in link_extractor.links if not link.startswith(url)]
            if len(external_links) > 5:
                risk_score += 1
                analysis['many_external_links'] = True
            else:
                analysis['many_external_links'] = False
                
    except Exception as e:
        analysis['error'] = str(e)
    
    analysis['risk_score'] = risk_score
    return analysis

# Example usage
if __name__ == "__main__":
    test_url = "http://example.com"
    result = analyze_url_for_phishing(test_url)
    print(f"Analysis results for {test_url}:")
    print(result)
```

