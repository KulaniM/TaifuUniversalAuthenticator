# TaifuUniversalAuthenticator
This project can be used to automate the authentication or login to a web client. It takes the username, password and login page of the web client as inputs. This project was developed as part of the implementation of Taifu-Fuzzer (https://sites.google.com/view/taifu-demo/home) Project which was published at the ISSTA 2021 Conference. Our paper title "Identifying privacy weaknesses from multi-party trigger-action integration platforms" can be find at https://dl.acm.org/doi/abs/10.1145/3460319.3464838. 

Dependencies:

tested with Python 3.9

**UniversalWebClientAuthenticator.py**
1) Selenium (tested with 3.141.0)
2) beautifulsoup4 (tested with 4.9.3)

**samplelogin.py**

3) chromedriver-py	92.0.4515.43	

Known weaknesses or isssues of the authenticator:
- When 2-factor authentication or additional verifications are used, those steps cannot be automated. The user has to manually click or provide additional info to complete the login.
- This project is based on a common set of keywords to identify the form elements. Hence, if the web client uses uncommon names or ids for HTML element attributes the authenticator will be failed to login.
