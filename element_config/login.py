from operate.base import basepage
from selenium.webdriver.common.action_chains import ActionChains
class loginpage(basepage):

    '''登录操作'''
    def login(self,username,password):
        self.sendusername().clear()
        self.sendusername().send_keys(username)
        ActionChains(self.driver).double_click(self.sendpassword()).perform()
        self.sendpassword().send_keys(password)
        self.clicksubmit().click()