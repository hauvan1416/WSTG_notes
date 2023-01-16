# Information gathering

## 1. Conduction search engine discovery reconnaissance for information leakage. 
## 2. Fingerprint web server.
## 3. Review Webserver metafile for information leakage.
## 4. Enumerate Applications on Webserver.
## 5. Review webpage Content for information leakage.
## 6. Identify Applications Entry points.
## 7. Map Execution paths through Applications.
## 8. Fingerprint Web Application Framework.
## 9. Fingerprint Web Application.
## 10. Map Application Archtecture.

### Use [google hacking database](https://www.exploit-db.com/google-hacking-database)

### Website
intitle: This dork will tell Google to show only those pages that have the term in their HTML title
```
intitle:”login page”
```
inurl: It searches for the specified term in the URL
```
inurl:”login.php”
```
define: Google will define this message and will look for what had this error. 
```
define:”sql syntax error”
```
### Files
filetype: Searches for specific file types.
```
filetype:txt
```
intitle: You can look into file directories of websites directly and download specified file
```
intitle: “index of ” intext: “movie name” .
```
### Finding username and passwords
```
intext: passwords filetype: txt
mysql history files
intext: account details filetype: txt
intitle:index.of intext:”secring .skr”|&q…
people.lst
passwd
master.passwd
pwd.db
htpasswd / htpasswd.bak
htpasswd / htgroup
spwd.db / passwd
passwd / etc (reliable)
config.php
passlist
```
## [Whatweb](https://github.com/urbanadventurer/WhatWeb)
usage(kali)
```
Whatweb 'url'
Help : whatweb -h
	
```

## Review robots.txt,HTML tags (<META>)...

## Sub domain 
Subdomain enumeration
``` 
subfinder: subfinder -d url
```

### Directory
``` 
Use dirbuster in kali to enumeration dir 
```
### View page source 
review comments for interesting information 
* SQL code 
* Usernames and passwords 
* internal IP addresses 
* debugging information

### Use JSfinder to list all URLs and subdomains from JS files on a website.

Request : parameters used in POST request pay special attention to any hidden parameters.

```GET: 
GET /shoppingApp/buyme.asp?CUSTOMERID=100&ITEM=z101a&PRICE=62.50&IP=x.x.x.x HTTP/1.1
Host: x.x.x.x
Cookie: SESSIONID=Z29vZCBqb2IgcGFkYXdhIG15IHVzZXJuYW1lIGlzIGZvbyBhbmQgcGFzc3dvcmQgaXMgYmFy

>> injection locations : CUSTOMERID,ITEM,PRICE,IP,SESSIONID

POST: Same with GET
```
Response 

Identify where new cookies are set (Set-Cookie header), modified, or added to.
Identify where there are any redirects (3xx HTTP status code), 400 statuscodes, in particular 403 Forbidden, and 500 internal server errors during normal responses (i.e., unmodified requests).
	
### Define the current framework :
* HTTP headers
* Cookies (search cookies on Cookiepedia)
* HTML source code  
* Specific files and folders
* File Extensions
* Error Message

### Port Scan
use Nmap or nabuu
```Nmap
nmap [Scan Type(s)] [Options] {target specification}
```
Open Ports
```
nmap -p port url
```
Identify Operating Systems
```
nmap -sV url
```
Stealth Scanning
```
Stealth scans are executed to avoid detection by firewalls and security systems. This is achieved by avoiding a 3-way handshake between the systems
nmap -sS url
```
Scan Commonly Used Ports
```
nmap –top-ports n url
n is the number of ports you’d like to scan

Vulnerability scan nmap
[Link](https://github.com/scipag/vulscan)







