# Authorization Testing
## Directory traversal File Include

### Techniques

1. Input Vector Enumeration 
* Are there request parameters which could be used for file-related operations?
* Are there unusual file extensions?
* Are there interesting variable names?
	+ http://example.com/getUserProfile.jsp?``item``=``ikki``.html

