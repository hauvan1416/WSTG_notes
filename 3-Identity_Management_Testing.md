# Identity Management Testing
 
## 1. [Test Role Definitions](https://github.com/OWASP/wstg/blob/master/document/4-Web_Application_Security_Testing/03-Identity_Management_Testing/01-Test_Role_Definitions.md)

## 2. [Test User Registration Process](https://github.com/OWASP/wstg/blob/master/document/4-Web_Application_Security_Testing/03-Identity_Management_Testing/02-Test_User_Registration_Process.md)

## 3. [Test Account Provisioning Process](https://github.com/OWASP/wstg/blob/master/document/4-Web_Application_Security_Testing/03-Identity_Management_Testing/03-Test_Account_Provisioning_Process.md)

## 4. [Testing for Account Enumeration and Guessable User Account](https://github.com/OWASP/wstg/blob/master/document/4-Web_Application_Security_Testing/03-Identity_Management_Testing/04-Testing_for_Account_Enumeration_and_Guessable_User_Account.md)

## 5. [Testing for Weak or Unenforced Username Policy](https://github.com/OWASP/wstg/blob/master/document/4-Web_Application_Security_Testing/03-Identity_Management_Testing/05-Testing_for_Weak_or_Unenforced_Username_Policy.md)

## Need to Check

### IDOR check 

* Cookie variable (e.g. role=admin, isAdmin=True)
* Account variable (e.g. Role: manager)
* Hidden directories or files (e.g. /admin, /mod, /backups)
* Switching to well known users (e.g. admin, backups, etc.)
 
`Use Auth Analyze Extension in BurpSuite`

![Auth_Analyze](./img/Auth_analyze.png)
### User Registration Process

Verify that the identity requirements for user registration are aligned with business and security requirements:

1. Can anyone register for access?
2. Are registrations vetted by a human prior to provisioning, or are they automatically granted if the criteria are met?
3. Can the same person or identity register multiple times?
4. Can users register for different roles or permissions?
5. What proof of identity is required for a registration to be successful?
6. Are registered identities verified?

Validate the registration process:

1. Can identity information be easily forged or faked?
2. Can the exchange of identity information be manipulated during registration ?

### Account Enumeration and Guessable User Account

#### Analyzing 
1. Valid credentials
2. Valid user with wrong password
3. Non exist username 
4. Error code recived on login page
5. URLs and URL Redirections
Example:
```
http://www.foo.com/err.jsp?User=baduser&Error=0
http://www.foo.com/err.jsp?User=gooduser&Error=2
```
** => In the first case they have provided a bad user ID and bad password. In the second, a good user ID and a bad password, so they can identify a valid user ID. **
6. URI Probing ( Thăm dò)
Example:
```
http://www.foo.com/account1 - we receive from web server: 403 Forbidden  ---------- ** the user exists, but the tester cannot view the web page **
http://www.foo.com/account2 - we receive from web server: 404 file Not Found ---------- ** the user "account2" does not exist **
```
7. Web Page Titles
```
Invalid user
Invalid authentication
```
8.  Message Received from a Recovery Facility ( Forgotten password function,... )
```
Invalid username: email address is not valid or the specified user was not found.
Valid username: Your password has been successfully sent to the email address you registered with.
```
9.  404 Error Message
10. Response Times 

### Username Policy
1. Determine the structure of account names.
2. Evaluate the application's response to valid and invalid account names.
3. Use different responses to valid and invalid account names to enumerate valid account names.
4. Use account name dictionaries to enumerate valid account names.
