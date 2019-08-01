import time
import unittest
from selenium import  webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os
from BeautifulReport import BeautifulReport as bf
# 登录
class TestSwitchUser(unittest.TestCase):
    # 定义一个保存截图函数
    # def save_img(self, img_name):
    #     self.browser.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath("H:/GCPT/error/img"), img_name))
    @classmethod
    def setUpClass(cls) :
        cls.driver = webdriver.Ie()
        # cls.driver = webdriver.Chrome()
        cls.driver.get('http://192.168.1.24:8031/(S(q0bjadi3zomcgh3afy4snowk))/Login.aspx')
        cls.driver.maximize_window()


    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        cls.driver.quit()


    def test_1_login(self):


        self.driver.find_element_by_id("username").clear()
        self.driver.find_element_by_id("username").send_keys("admin")
        # self.driver.find_element_by_id("password").clear()
        password=self.driver.find_element_by_id("password")
        # IE浏览器clear失效 改用双击事件

        ActionChains(self.driver).double_click(password).perform()
        # 输入内容
        # password.clear()
        password.send_keys("abc123")
        self.driver.find_element_by_id("ImageBtLogin").click()

        '''IE浏览器click()失效   js'''
        # js = 'document.getElementById("ImageBtLogin").click();'
        # self.driver.execute_script(js)
        '''模拟键盘点击enter'''
        # self.driver.find_element_by_id("ImageBtLogin").send_keys(Keys.ENTER)  # 键盘输入enter
        time.sleep(2)
        self.driver.switch_to.frame("topFrame")
        result=self.driver.find_element_by_class_name("userName").text
        assert "当前用户" in result


#基础资料
#用户
    def test_2_usermanage(self):
        #self.driver.switch_to.default_content()
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.frame('leftFrame')
        #self.driver.find_element_by_link_text("用户管理").click()
        # js = "documentElement.scrollTop=1000"#针对Firefox有效
        js = "document.body.scrollTop=1000"#针对Chrome有效
        self.driver.execute_script(js)
        userm = self.driver.find_element_by_link_text("用户管理")
        ActionChains(self.driver).double_click(userm).perform()
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.frame('main')
        nowuser=self.driver.find_element_by_class_name('titlebt').text
        self.assertEqual(nowuser, "用户管理")

    def test_3_openadduser(self):
        self.driver.find_element_by_id('WebTool_btnAdd').click()
        result=self.driver.find_element_by_class_name("left_bt2").text
        assert "操作说明" in result





