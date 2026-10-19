# 🌐 Website IP Resolver

A lightweight Python script offering multiple ways to resolve a website's domain name into its corresponding IP address(es).

---

## 🛠️ Prerequisites

* **Python 3.x**

---

## 📦 Dependency Installation

The core functionality uses Python's built-in `socket` library. However, if you plan to use the advanced DNS resolver script, install the third-party package:

```bash
pip install dnspython
```

---

## 💻 Usage

1. Open `ip_resolver.py` and choose one of the available implementations based on your needs:

   **Option 1: Single IP Resolution (Built-in)**
   ```python
   import socket
   website = input("Enter your url here: ")
   ip = socket.gethostbyname(website)
   print(f"IP address of {website} is : {ip}")
   ```

   **Option 2: Multiple IP & Alias Resolution (Built-in)**
   ```python
   import socket
   website = input("Enter your url here: ")
   hostname, aliases, ip_list = socket.gethostbyname_ex(website)
   print(f"IP address of {website} is : {ip_list}")
   ```

   **Option 3: Advanced DNS Resolver (Third-Party)**
   ```python
   import dns.resolver
   website = input("Enter your url here: ")
   result = dns.resolver.resolve(website, 'A')
   for ipval in result:
       print(f"IP Address: {ipval.to_text()}")
   ```

2. Run your preferred script directly from your terminal:
   ```bash
   python ip_resolver.py
   ```

### ℹ️ How it Works
The script takes a user-supplied URL/domain string and queries DNS infrastructure. Options 1 and 2 wrap native OS networking APIs via the `socket` module to fetch basic IP mapping details. Option 3 utilizes `dnspython` to perform explicit direct queries against 'A' records for granular DNS information.

---

## ⚡ Alternative One-Command CLI Solutions

If you want to quickly find a website's IP address directly from your terminal without running a Python script, you can use any of these built-in system tools:

| Command | How to Use It | What It Does |
| :--- | :--- | :--- |
| **`ping`** | `ping google.com` | Sends test packets to the website and displays its IP address in the response. |
| **`nslookup`** | `nslookup google.com` | The standard built-in terminal command specifically for querying DNS servers. |
| **`dig`** | `dig google.com +short` | *(Mac/Linux)* A powerful, concise tool preferred by network administrators. |
| **`host`** | `host google.com` | *(Mac/Linux)* A simple utility that prints a quick summary of the domain's IP mapping. |

---

## 📚 Resources & Documentation

* [Python socket Module Documentation](https://python.org)
* [dnspython Official Documentation](https://dnspython.org)
