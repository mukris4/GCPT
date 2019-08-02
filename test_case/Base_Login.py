from element_config.login import loginpage
import time
import unittest
from selenium import  webdriver
'''
PO模式对代码重构
'''
# 登录
class LoginCase(unittest.TestCase,loginpage):

    @classmethod
    def setUpClass(cls) :
        cls.driver = webdriver.Ie()
        cls.driver.get('http://192.168.1.24:8031/(S(q0bjadi3zomcgh3afy4snowk))/Login.aspx')
        cls.driver.maximize_window()


    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        cls.driver.quit()
    def test_login(self):
        username="admin"
        password="abc123"
        loginpage.login(self,username,password)

if __name__ == '__main__':
    unittest.main()






