## 1 Testing for Credentials Transported over an Encrypted Channel

### Check SSL Certificate
-  Use SSLscan or burpsuite extension
** sslscan 'url' **
``` sslscan
slscan thisislegal.com
Version: 2.0.15-static
OpenSSL 1.1.1q-dev  xx XXX xxxx

Connected to 178.79.182.67

Testing SSL server thisislegal.com on port 443 using SNI name thisislegal.com
s
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
1. What character  are permitted and forbidden for use  within a password (Lower, uppercase letters, digits and special symbols; ...)
2. How often user can change their password ? how quickly user can change their password after a previous change ? user may bypass  hisstory requirements b y changing  their password 5 times in a row after the lát password change  the have configured their intial passsword again.
3. When must user change their password ?
4. How ofteb user can reuse a password ? Does the application maintain a history of the user’s previous used 8 passwords
5. How differrnt must the next password be from the last password?
6. Is the user prevented from using his username or orther account  information ( first name, lastname..) in the password ?
7. Min, max of password lenght ?
8. Possible to set common password (123456,Password ......)?

## 8 Testing for Weak Security Question Answer
1. Try to obtain a list of security questions by creating a new account or forgot password .If any question fall in the (guessed, brute forced, avaiable in social media,etc .) it is vulnerable to attacked.
2. If the system allows the user to generate their own security questions, it is vulnerable to having insecure questions created. 
3. If the system uses the self-generated security questions during the forgotten password functionality and if usernames can be enumerated
### step to bruce-forcible answers
* The application allow the end user chose the question to answer :
	+ A "public answer" ,search in gg.
	+ A factual answer ,Ex: first school, your maiden name
	....
*Determine how many guesses you have if possible.
	+ Function allow unlimited attempts?
	+ Lockout after many time incorrect answer ?
	+ Pick the appropriate question based on analysis from the above points, and do research to determine the most likely answers.

## 9 Testing for Weak Password Change or Reset Functionalities
### Genaral concern
+ Password reset process weaker than the authentication process ?
+ Have rate limit or orther protect against automated attack ?
+ It is vulnerable to common attacks?
+ Does the reset process allow user enumeration ?

### Email - New password sent
+ is the user forced to change the password on initial login?
+ Is the password securely generated?
+ Is the user's existing password sent to them?
+ the emails sent from a domain with anti-spoofing protection?

### email- Link sent
+ link use HTTPS?
+ link be used multiple times?
+ link expire if it remains unused?
+ token sufficiently long and random? (At least 128 bits (or 32 hex characters))
+ Does the link contain a user ID?
+ Can you inject a different host header?
+ the link exposed to third parties?
+ the emails sent from a domain with anti-spoofing protection?

### Tokens Sent Over SMS or Phone Call
+ token sufficiently long and random?
+ the token be used multiple times?
+ Are appropriate rate limiting and restrictions in place?

### Authenticated Password Changes
+ When setting the password, can you specify the user ID?
+ Is the user required to re-authenticate?
+ Is the password change form vulnerable to CSRF?
+ Is a strong and effective password policy applied?

## 10 Testing for Weaker Authentication in Alternative Channel
+ Understand the Primary Mechanism
+ Identify Other Channels
+ Enumerate Authentication Functionality
+ Review and Test

## 11 Testing Multi-Factor Authentication
### Types of MFA

| Factor | Examples |
|--------|----------|
| Something You Know | Passwords, PINs and security questions. |
| Something You Have | Hardware or software tokens, certificates, email*, SMS, and phone calls. |
| Something You Are | Fingerprints, facial recognition, iris scans, handprint scans and behavioural factors. |
| Location | Source IP ranges, and geolocation. |

### Check for MFA Bypasses
*  first step
	+ The main login page .
	+ Security critcal functionality(such as disabling MFA or changing a password).
	+ Federated login providers.
	+ API endpoints
	+ Alternative (non-HTTP) protocols
	+ Test or debug functionality.


