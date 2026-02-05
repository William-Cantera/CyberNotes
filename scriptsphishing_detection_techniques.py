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

```python
import re
import urllib.parse
from urllib.request import urlopen
from html.parser import HTMLParser

class PhishingDetector:
    """A basic phishing detection class to analyze URLs and webpage content."""

    def __init__(self):
        self.suspicious_words = [
            'login', 'account', 'bank', 'verify', 'secure', 'webscr', 'update'
        ]
        self.safe_domains = ['paypal.com', 'google.com', 'gmail.com', 'github.com']

    def check_url(self, url):
        """
        Check if a URL has characteristics commonly associated with phishing.
        
        :param url: The URL to check
        :return: A tuple (is_suspicious, reasons)
        """
        parsed = urllib.parse.urlparse(url)
        reasons = []

        # Check for IP address in hostname
        if re.match(r'\d+\.\d+\.\d+\.\d+', parsed.netloc):
            reasons.append("IP address used instead of domain name")

        # Check for suspicious words in URL
        if any(word in url.lower() for word in self.suspicious_words):
            reasons.append("Suspicious words found in URL")

        # Check for URL shortening services
        if len(parsed.netloc) < 7:  # Most short URL services use short domain names
            reasons.append("Possibly a shortened URL")

        # Check if the domain is not in our list of known safe domains
        if parsed.netloc not in self.safe_domains:
            reasons.append("Domain not in list of known safe domains")

        return bool(reasons), reasons

    def analyze_webpage(self, url):
        """
        Fetch and analyze the content of a webpage for potential phishing indicators.
        
        :param url: The URL of the webpage to analyze
        :return: A list of suspicious elements found
        """
        class PhishingHTMLParser(HTMLParser):
            def __init__(self):
                super().__init__()
                self.forms = []
                self.external_links = []
            
            def handle_starttag(self, tag, attrs):
                if tag == 'form':
                    self.forms.append(dict(attrs))
                elif tag == 'a':
                    href = dict(attrs).get('href', '')
                    if href.startswith('http'):
                        self.external_links.append(href)

        try:
            with urlopen(url) as response:
                html_content = response.read().decode('utf-8')
            
            parser = PhishingHTMLParser()
            parser.feed(html_content)

            suspicious_elements = []

            # Check for password fields in forms
            for form in parser.forms:
                if any('password' in str(attr).lower() for attr in form.values()):
                    suspicious_elements.append("Form with password field detected")
                    break

            # Check for links to external domains
            parsed_url = urllib.parse.urlparse(url)
            base_domain = parsed_url.netloc
            for link in parser.external_links:
                if urllib.parse.urlparse(link).netloc != base_domain:
                    suspicious_elements.append(f"Link to external domain: {link}")

            return suspicious_elements

        except Exception as e:
            return [f"Error analyzing webpage: {str(e)}"]

# Usage example:
if __name__ == "__main__":
    detector = PhishingDetector()
    test_url = "http://suspicious-login.example.com/verify.php"
    
    url_check, reasons = detector.check_url(test_url)
    print(f"URL check results for {test_url}:")
    print(f"Suspicious: {url_check}")
    for reason in reasons:
        print(f"- {reason}")
    
    print("\nWebpage analysis:")
    webpage_analysis = detector.analyze_webpage(test_url)
    for element in webpage_analysis:
        print(f"- {element}")

# This script provides a basic framework for phishing detection.
#

