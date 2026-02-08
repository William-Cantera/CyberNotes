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

## Network Traffic Analysis with Wireshark

### Introduction
Wireshark is a powerful, open-source network protocol analyzer used for network troubleshooting, analysis, and security auditing. It allows cybersecurity professionals to capture and interactively browse the traffic running on a computer network.

### Key Concepts

1. **Packet Capture**: Wireshark can capture live network traffic or read from previously saved capture files.

2. **Protocol Dissection**: It understands and can decode hundreds of network protocols, presenting data in a human-readable format.

3. **Filtering**: Users can apply complex display filters to focus on specific traffic of interest.

4. **Colorization**: Packets are color-coded based on their type, making it easier to identify different protocols or potential issues.

### Best Practices

- Always ensure you have proper authorization before capturing network traffic.
- Use capture filters to reduce the amount of data collected, especially on busy networks.
- Regularly update Wireshark to benefit from the latest protocol decoders and security patches.
- Save capture files for later analysis or as evidence in security investigations.

### Real-World Example: Detecting a Port Scan

To detect a potential port scan using Wireshark:

1. Capture traffic on the suspected target network.
2. Apply a display filter to show only TCP SYN packets:
   ```
   tcp.flags.syn == 1 and tcp.flags.ack == 0
   ```
3. Look for a single source IP sending SYN packets to multiple ports on your system.
4. Use the "Conversations" feature to visualize the scan pattern.

### Tip: Using Display Filters

Wireshark's display filters are powerful but can be complex. Start with simple filters and build up:

- `http`: Shows only HTTP traffic
- `ip.addr == 192.168.1.1`: Displays packets to/from a specific IP
- `tcp.port == 80 or udp.port == 53`: Shows web and DNS traffic

Combine filters with logical operators (`and`, `or`, `not`) for more precise analysis.

### Conclusion

Wireshark is an essential tool for network analysis and security. By mastering its features, cybersecurity professionals can gain deep insights into network behavior, detect anomalies, and investigate security incidents effectively.

---

## Network Traffic Analysis with Wireshark

### Overview
Wireshark is a powerful open-source network protocol analyzer used for network troubleshooting, analysis, and security auditing. It allows cybersecurity professionals to capture and interactively browse network traffic in real-time.

### Key Concepts

1. **Packet Capture**: Wireshark can capture packets from a live network or read from a saved capture file.

2. **Protocol Dissection**: It understands and can decode hundreds of protocols, presenting data in a human-readable format.

3. **Filtering**: Users can apply complex display filters to focus on specific traffic of interest.

4. **Color Coding**: Packets are color-coded based on their type, making it easier to identify different protocols or potential issues.

### Best Practices

- Always ensure you have proper authorization before capturing network traffic.
- Use capture filters to reduce the amount of data collected, especially on busy networks.
- Regularly update Wireshark to benefit from the latest protocol decoders and security patches.
- Save capture files for later analysis or as evidence in security incidents.

### Real-World Example: Detecting a Port Scan

To detect a potential port scan using Wireshark:

1. Start a packet capture on the suspected target interface.
2. Apply a display filter to show only TCP SYN packets:
   ```
   tcp.flags.syn == 1 and tcp.flags.ack == 0
   ```
3. Look for a high number of SYN packets from a single source IP to multiple destination ports.

### Tip: Using Display Filters

Wireshark's display filters are powerful tools for focusing on specific traffic. Here are some useful examples:

- Show only HTTP traffic: `http`
- Display packets with a specific IP: `ip.addr == 192.168.1.100`
- Find all DNS queries: `dns.qry.name contains "example.com"`

Remember, mastering Wireshark takes practice. Regularly analyzing both normal and abnormal traffic will improve your skills in identifying potential security threats and network issues.

---

