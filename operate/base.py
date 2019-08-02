class basepage:

    '''基础page层 封装一些常用的方法'''

    def __init__(self,driver):
        self.driver=driver
    def by_id(self,id):
        return self.driver.find_element_by_id(id)
    def by_name(self,name):
        return self.driver.find_element_by_name(name)
    def by_xpath(self,xpath):
        return self.driver.find_element_by_xpath(xpath)
    def by_tag_name(self,tag_name):
        return self.driver.find_element_by_tag_name(tag_name)
    def by_link_text(self,link_text):
        return self.driver.find_element_by_link_text(link_text)
    def by_tag_className(self, className):
        return self.driver.find_element_by_className(className)


    '''定位登录元素'''
    # 定位账号输入框
    def sendusername(self):
        return self.by_id("username")
    # 定位密码输入框
    def sendpassword(self):
        return self.by_id("password")
    # 定位登录按钮
    def clicksubmit(self):
        return self.by_id("ImageBtLogin")