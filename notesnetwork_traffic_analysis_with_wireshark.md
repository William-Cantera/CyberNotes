# Cybersecurity Study Notes

## Network Traffic Analysis with Wireshark

### Introduction
Wireshark is a powerful, open-source network protocol analyzer used for network troubleshooting, analysis, and security auditing. It allows cybersecurity professionals to capture and inspect network traffic in real-time, providing deep insights into network communications.

### Key Concepts

1. **Packet Capture**: Wireshark can capture live network traffic or read from saved capture files.
2. **Protocol Dissection**: It understands and can decode hundreds of network protocols.
3. **Filtering**: Allows users to focus on specific traffic types or patterns.
4. **Colorization**: Uses color coding to quickly identify different protocols or traffic types.

### Best Practices

- **Capture Filters**: Use capture filters to reduce the amount of data collected, focusing only on relevant traffic.
- **Display Filters**: Utilize display filters to analyze specific aspects of captured traffic.
- **Save Session Data**: Regularly save capture files for future analysis or comparison.
- **Use in Controlled Environments**: Be cautious when using Wireshark on production networks to avoid performance impacts.

### Example: Analyzing HTTP Traffic

To analyze HTTP traffic:

1. Start a capture on the appropriate network interface.
2. Apply a display filter: `http`
3. Look for HTTP requests and responses.
4. Examine headers, content, and status codes.

### Practical Tip

To quickly identify potential security issues, use the following display filter:

```
http.request.method == "POST" or http.authbasic
```

This filter shows POST requests (which may contain sensitive data) and Basic Authentication headers (which contain credentials in base64 encoding).

### Conclusion

Wireshark is an essential tool for network analysis and security auditing. By understanding its features and applying best practices, cybersecurity professionals can gain valuable insights into network traffic, identify potential security threats, and troubleshoot network issues effectively.

---

