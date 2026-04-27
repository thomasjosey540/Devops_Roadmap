# Networking Basics

## OSI Model

The OSI model defines how network communication works in layers.

1. Physical  
2. Data Link  
3. Network  
4. Transport  
5. Session  
6. Presentation  
7. Application  

---

## IP Address

An IP address uniquely identifies a device on a network.

Example:
192.168.1.1

---

## Private IP Ranges

Private IPs are used within internal networks and are not routable on the internet.

Ranges:
- 10.0.0.0 – 10.255.255.255
- 172.16.0.0 – 172.31.255.255
- 192.168.0.0 – 192.168.255.255

---

## Protocols

Protocols define rules for communication.

Examples:
- HTTP → Web communication
- HTTPS → Secure web communication
- FTP → File transfer
- SSH → Remote login

---

## Ports

Ports identify services on a system.

Examples:
- 80 → HTTP
- 443 → HTTPS
- 22 → SSH
- 3306 → MySQL

---

## Networking Commands

### Check IP Address
ifconfig  
ip addr  

---

### Test Connectivity
ping google.com  

---

### Trace Route
traceroute google.com  
tracert google.com  

---

### Active Connections
netstat -antp  

---

### Network Scanning
nmap localhost  

---

### DNS Lookup
dig google.com  

---

### Routing Table
route -n  

---

### ARP Table
arp -a  

---

### Network Diagnostics
mtr google.com  

---

### Test Port Connectivity
telnet google.com 80  

---

## Real-World Use

- Used to connect services in DevOps environments  
- Helps debug network issues  
- Required for cloud and container networking  

---

## Key Learning

- Understanding how systems communicate  
- Identifying services using ports  
- Troubleshooting using networking commands  