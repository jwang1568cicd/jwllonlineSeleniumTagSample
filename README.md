# jwllonlineSeleniumTagSample
This is a simple Pytest selenium project to verify the the jwll.online web site hosted via Github

1. If you need information regarding the web hosting, jwll.online, please check the repository, jwll.online.
2. In order to run this project, use 'pip install pytest, selenium' to install the required python libraries.
3. Use 'curl www.jwll.online' to verify the sample web page
C:\Users\CICD-Student\cicdclass\python>curl www.jwll.online
<!DOCTYPE html>
<html>
<head>
        <style>
                h1{
                        padding:5%;
                        color:lightblue;
                        text-align:center;
                }
        </style>
</head>
<body>
<h1 >Welcome to jwll.online</h1>
    <img src="jwllonline.png" alt="jwll.online logo Image" width="200" style="display:block; margin-left:auto; margin-right:auto;">

</body>
</html>

4. Use 'pytest jwllpytest.py' to launch; here is sample of execution output log      
C:\Users\CICD-Student\cicdclass\python>pytest jwllpytest.py
================================================= test session starts =================================================
platform win32 -- Python 3.12.2, pytest-8.2.0, pluggy-1.5.0
rootdir: C:\Users\CICD-Student\cicdclass\python
plugins: anyio-3.7.1
collected 1 item

jwllpytest.py
DevTools listening on ws://127.0.0.1:2863/devtools/browser/fcc91c1e-37f1-402d-9f0d-bffb6fbe1621
.                                                                                                  [100%]

================================================== 1 passed in 7.21s ==================================================

C:\Users\CICD-Student\cicdclass\python>
