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



#CLI alternatives :
# ping url
# nslookup url
# dig url +short
# host url
