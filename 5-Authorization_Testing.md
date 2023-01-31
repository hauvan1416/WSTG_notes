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