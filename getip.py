#Finding the ip address of any website using socket.gethostbyname (for getting single ip)
import socket
website = input("Enter your url here :")
ip = socket.gethostbyname(website)
print(f"IP address of {website} is : {ip}")



# Finding the ip address of any website using socket.gethostbyname_ex (for getting multiple ips)
import socket
website = input("Enter your url here :")
hostname, aliases, ip_list = socket.gethostbyname_ex(website)
print(f"IP address of {website} is : {ip_list}")



#using third party python library
# pip install dnspython
import dns.resolver
website = input("Enter your url here : ")
result = dns.resolver.resolve(website, 'A')
for ipval in result:
    print(f"IP Address: {ipval.to_text()}")


"""
### Alternative One-Command CLI Solutions

If you want to quickly find a website's IP address directly from your terminal 
without running a Python script, you can use any of these built-in commands:

| Command | How to Use It | What It Does |
| :--- | :--- | :--- |
| **`ping`** | `ping google.com` | Sends test packets to the website and displays its IP address in the response. |
| **`nslookup`** | `nslookup google.com` | The standard built-in terminal command specifically for querying DNS servers. |
| **`dig`** | `dig google.com +short` | *(Mac/Linux)* A powerful, concise tool preferred by network administrators. |
| **`host`** | `host google.com` | *(Mac/Linux)* A simple utility that prints a quick summary of the domain's IP mapping. |
"""
