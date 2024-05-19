import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def browser():
    # Set up Chrome options
    driver = webdriver.Chrome()
    yield driver 


"""
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
"""

def test_jwllonline(browser):
    # Launch Chrome and navigate to www.jwll.online
    browser.get("https://www.jwll.online")

    # Locate tag_name, h1, and its content
    hd = browser.find_element(By.TAG_NAME, 'h1')
    #print(hd.text)
    #print(hd.tag_name)

    #Note: text() selects all text node children of the context node

    # Example assertion (you can modify this according to your requirements)
    assert "Welcome" in hd.text  # Adjust the expected title

    # Additional interactions or assertions can be added here
    # For example, finding an element and interacting with it:
    # element = browser.find_element(By.NAME, "q")
    # element.send_keys("pytest" + Keys.RETURN)
    time.sleep(3)  # Wait for the results before close it
    
    browser.close()    

    # Add any other interactions or checks you'd like here
