from element_config.login import loginpage
import time
import unittest
from ddt import ddt,data,unpack
from selenium import  webdriver
'''
PO模式对代码重构
'''
# 登录
@ddt
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

    @data(('', 'abc123','不能为空'),
          ('admin', 'abc123',''))
    @unpack
    def test_login(self,username,password,assert_text):
        # username="admin"
        # password="abc123"
        loginpage.login(self,username,password)
        if username=="admin":
            self.driver.switch_to.frame("topFrame")
            result = self.driver.find_element_by_id("userName1").text
            self.assertIn("管理员" , result)
        else:
            # 获取alert对话框
            dig_alert = self.driver.switch_to.alert
            self.assertIn(assert_text, dig_alert.text)
            dig_alert.accept()


if __name__ == '__main__':
    unittest.main()






