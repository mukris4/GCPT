from selenium import  webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class common_browser:
    def __init__(self,driver):
        self.driver=driver
    def login(self, username, password):
        self.driver.find_element_by_id("username").clear()
        self.driver.find_element_by_id("username").send_keys(username)
        # 改用双击事件
        password1 = self.driver.find_element_by_id("password")
        ActionChains(self.driver).double_click(password1).perform()
        # 输入内容
        # password.clear()
        password1.send_keys(password)
        self.driver.find_element_by_id("ImageBtLogin").click()


        #js去掉readonly属性
        # js='document.getElementById("conCon_txtBillNo").removeAttribute("readonly");'
        # self.driver.execute_script(js)

