## 1 Testing for Credentials Transported over an Encrypted Channel

### Check SSL Certificate
-  Use SSLscan or burpsuite extension
** sslscan 'url' **
```
slscan thisislegal.com
Version: 2.0.15-static
OpenSSL 1.1.1q-dev  xx XXX xxxx

Connected to 178.79.182.67

Testing SSL server thisislegal.com on port 443 using SNI name thisislegal.com

  SSL/TLS Protocols:
SSLv2     disabled
SSLv3     disabled
TLSv1.0   disabled
TLSv1.1   disabled
TLSv1.2   enabled
TLSv1.3   enabled

  TLS Fallback SCSV:
Server supports TLS Fallback SCSV

  TLS renegotiation:
Session renegotiation not supported

  TLS Compression:
Compression disabled

  Heartbleed:
TLSv1.3 not vulnerable to heartbleed
TLSv1.2 not vulnerable to heartbleed
......................................
```


## 2 Testing for Default Credentials

1. Searching for "[SOFTWARE] default password".
2. Reviewing the manual or vendor documentation.
3. Checking common default password databases, such as CIRT.net, SecLists Default Passwords or DefaultCreds-cheat-sheet.
4. Inspecting the application source code (if available).
5. Installing the application on a virtual machine and inspecting it. 
6. "admin", "password", "12345", or other common default passwords.
7. An empty or blank password.
8. The serial number or MAC address of the device

** Tool : burp intruder **

## 3 Testing for Weak Lock Out Mechanism

Use Burp Intruder.

1. Attempt to log in with an incorrect password 3 times.
2. Successfully log in with the correct password, thereby showing that the lockout mechanism doesn't trigger after 3 incorrect authentication attempts.
3. Attempt to log in with an incorrect password 4 times.
4. Successfully log in with the correct password, thereby showing that the lockout mechanism doesn't trigger after 4 incorrect authentication attempts.
5. Attempt to log in with an incorrect password 5 times.
6. Attempt to log in with the correct password. The application returns "Your account is locked out.", thereby confirming that the account is locked out after 5 incorrect authentication attempts.
7. Attempt to log in with the correct password 5 minutes later. The application returns "Your account is locked out.", thereby showing that the lockout mechanism does not automatically unlock after 5 minutes.
8. Attempt to log in with the correct password 10 minutes later. The application returns "Your account is locked out.", thereby showing that the lockout mechanism does not automatically unlock after 10 minutes.
9. Successfully log in with the correct password 15 minutes later, thereby showing that the lockout mechanism automatically unlocks after a 10 to 15 minute period.

## 4 Testing for Bypassing Authentication Schema
1. Try to access a page directly with the URL (page that is normally shown when authenticated)
2.. Try changing parameter values, like
` http://www.site.com/page.asp?authenticated=no `
 to
` http://www.site.com/page.asp?authenticated=yes `
3. If the session cookie value is predictable (linear), try guessing the next value.
4. Try a [SQL Injection](./SQL_Injection.md) in the login form.

## 5 Testing for Vulnerable Remember Password
1. Check for attribute autocomplete=”off”.
2. Look for passwords being stored in a cookie. Examine the cookies stored by the application. Verify that the credentials are not stored in clear text, must be hashed.
3. Examine the hashing mechanism: if it is a common, well-known algorithm, check for its strength; in homegrown hash functions, attempt several usernames to check whether the hash function is easily guessable.
4. Verify that the credentials are only sent during the log in phase, and not sent together with every request to the application.
5. Consider other sensitive form fields (e.g. an answer to a secret question that must be entered in a password recovery or account unlock form).

## 6 Testing for Browser Cache Weaknesses
1. Entering information into the application  and logging out. Click on ** Back ** button of the browser to check whether previous displayed sensitive information can be access while unauthenticated. 
2. check that the application does not leak any sensitive data into the browser cache ( Use burp )
```
Cache-Control: no-cache, no-store
Expires: 0
Pragma: no-cache
```

## 7 Testing for Weak Password Policy

## 8 Testing for Weak Security Question Answer

## 9 Testing for Weak Password Change or Reset Functionalities

## 10 Testing for Weaker Authentication in Alternative Channel

## 11 Testing Multi-Factor Authentication


