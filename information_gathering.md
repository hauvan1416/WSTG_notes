1. Conduction search engine discovery reconnaissance for information leakage.
2. Fingerprint web server.
3. Review Webserver metafile for information leakage.
4. Enumerate Applications on Webserver.
5. Review webpage Content for information leakage.
6. Identify Applications Entry points.
7. Map Execution paths through Applications.
8. Fingerprint Web Application Framework.
9. Fingerprint Web Application.
10. Map Application Archtecture.

## Use google hacking database 

https://www.exploit-db.com/google-hacking-database

## Whatweb
	
https://github.com/urbanadventurer/WhatWeb) 
usage(kali) : whatweb url

## Review robots.txt,HTML tags (<META>),...

## sub domain 

subdomain enumeration (subfinder: subfinder -d url)
		
## Directory 
	
use dirbuster in kali to enumeration dir 
		
## F12 > review comments for interesting information 
	
SQL code, usernames and passwords, internal IP addresses, or debugging information.
		
## Use JSfinder to list all URLs and subdomains from JS files on a website.
			
## Request : parameters used in POST request pay special attention to any hidden parameters.

GET: 
GET /shoppingApp/buyme.asp?CUSTOMERID=100&ITEM=z101a&PRICE=62.50&IP=x.x.x.x HTTP/1.1
Host: x.x.x.x
Cookie: SESSIONID=Z29vZCBqb2IgcGFkYXdhIG15IHVzZXJuYW1lIGlzIGZvbyBhbmQgcGFzc3dvcmQgaXMgYmFy
					
-> injection locations : CUSTOMERID,ITEM,PRICE,IP,SESSIONID
				
POST: Same with GET
	
## Response 
Identify where new cookies are set (Set-Cookie header), modified, or added to.
## Identify where there are any redirects (3xx HTTP status code), 400 status codes, in particular 403 Forbidden, and 500 internal server errors during normal responses (i.e., unmodified requests).
## Define the current framework :

HTTP headers
Cookies (search cookies on Cookiepedia)
HTML source code
Specific files and folders
File Extensions
Error Message

## 
		
