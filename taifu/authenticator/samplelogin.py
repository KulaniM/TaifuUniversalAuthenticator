# Dependencies
# Tested on Python 3.9
# https://pypi.org/project/chromedriver-py/ (use command pip install chromedriver-py)
# other libraries: selenium

from selenium import webdriver
from UniversalWebClientAuthenticator import authentication
from chromedriver_py import binary_path

# inputs: username, password, and login url
data_list_values = ['username','password']
LOGIN_URL = "https://exampl.com/login/index.php"

# Chrome Webdriver Options
browser = webdriver.Chrome(executable_path=binary_path)

# load the login page to the browser
browser.get(LOGIN_URL)

# call the authentication function by giving the webdriver,
login_type, browser = authentication(browser,  data_list_values, 1)

# set request cookies from the browser cookies (use if necessary only)
cookies= {}
for key, value in browser.get_cookies()[0].items():
    cookies = dict(key= value)

