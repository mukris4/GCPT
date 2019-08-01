import time
import unittest
import random,os
from selenium import  webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from operate.Common_Operations import common_browser
from selenium.webdriver.support.select import Select
from BeautifulReport import BeautifulReport
# 登录
class OrderM(unittest.TestCase):
    def save_img(self, img_name):
        """
            传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
        """
        #pycharm执行
        self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(r"H:\GCPT\img"), img_name))
        #Jenkins构建脚本  未启动浏览器截图出错
        # self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(r"H:\Jenkins\workspace\gcpt_test\img"), img_name))
    @classmethod
    def setUpClass(cls) :
        cls.driver = webdriver.Ie()
        cls.driver.get('http://192.168.1.24:8031/(S(q0bjadi3zomcgh3afy4snowk))/Login.aspx')
        cls.driver.maximize_window()


    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        cls.driver.quit()

    # @unittest.skip('暂不执行')
    def test_a1_login(self):
        '''管理员登录'''
        common_browser.login(self,"admin","abc123")
        self.driver.switch_to.frame("topFrame")
        result=self.driver.find_element_by_id("userName1").text
        assert "管理员" in result

#订单管理
    # @unittest.skip('暂不执行')
    def test_a2_enterorderF(self):
        '''进入订单通知复核页面'''
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.frame('leftFrame')
        self.driver.find_element_by_link_text("订单通知复核").click()
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.frame('main')
        # 显式等待
        element = WebDriverWait(self.driver, 10,3).until(EC.presence_of_element_located((By.CLASS_NAME, 'titlebt'))).text
        self.assertEqual(element, "订单通知复核")



    @unittest.skip('暂不执行')
    def test_a3_ordercheck_seach(self):
        '''订单复核通知查询'''
        WebDriverWait(self.driver, 10, 3).until(
                 EC.presence_of_element_located((By.ID, 'WebTool_btQuery'))).click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        element1 = WebDriverWait(self.driver, 10, 3).until(
            EC.presence_of_element_located((By.ID, 'btQuery'))).get_attribute('value')
        self.assertEqual(element1, "查 询")

    @unittest.skip('暂不执行')
    def test_a4_closesearch(self):
        '''关闭订单复核查询'''
        WebDriverWait(self.driver, 10,3).until(
            EC.presence_of_element_located((By.ID, 'btCance'))).click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[0]) #切换至原来窗口
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.frame('main')#切换至main frame
        element = WebDriverWait(self.driver, 10, 3).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'titlebt'))).text
        self.assertEqual(element, "订单通知复核")

    #@unittest.skip('暂不执行')
    @BeautifulReport.add_test_img('test_a5_orderSave')
    def test_a5_orderSave(self):
        '''点击选择第一条数据保存'''

        WebDriverWait(self.driver, 10, 3).until(
            EC.presence_of_element_located((By.ID, 'conCon_gridListHdr_selected_1'))).click()
        global orderNO  # 订单号
        orderNO = self.driver.find_element_by_xpath('//*[@id="conCon_gridListHdr"]/tbody/tr[2]/td[4]').text
        # print(orderNO)

        global gys  # 供应商账号
        gys = self.driver.find_element_by_xpath(' // *[ @ id = "conCon_gridListHdr_txtLinker1_0"]').text
        WebDriverWait(self.driver, 10, 3).until(
            EC.presence_of_element_located((By.ID, 'WebTool_btSave'))).click()
        time.sleep(1)
        # 获取alert对话框
        dig_alert = self.driver.switch_to.alert

        self.assertIn("保存成功！", dig_alert.text)
        time.sleep(3)
        dig_alert.accept()

    #@unittest.skip('暂不执行')
    # @unittest.expectedFailure
    @BeautifulReport.add_test_img('test_a6_orderSubmit')
    def test_a6_orderSubmit(self):
        '''点击选择第一条数据提交'''
        # 将返回该匹配行的第一列（暂未实现）
        #  By.xpath("//td[./span[text()=orderNO]]/../td[1]")
        self.driver.switch_to.alert.accept()
        #层级定位
        # table_div = self.driver.find_element_by_id('conCon_UPgridList')
        # table=table_div.find_element_by_tag_name("table")
        # row = table.find_elements_by_tag_name('td')
        #
        # for item in row:
        #     item1=item.text
        #     list.append(item1)
        #     print(list)
        #     trOrder= list.index(orderNO)
        #     trNO=trOrder//13
        #     print(trNO)

        WebDriverWait(self.driver, 10, 3).until(
            EC.presence_of_element_located((By.ID, 'conCon_gridListHdr_selected_0'))).click()
        # WebDriverWait(self.driver, 10,3).until(
        #      EC.presence_of_element_located((By.ID, '"conCon_gridListHdr_selected_"+trNO'))).click()
        WebDriverWait(self.driver, 10, 3).until(
            EC.presence_of_element_located((By.ID, 'WebTool_btTj'))).click()
        time.sleep(1)
        # 获取alert对话框
        dig_alert = self.driver.switch_to.alert
        time.sleep(1)
        print(dig_alert.text)
        # 获取文本值为空
        self.assertIn("提交成功！", dig_alert.text,"IE浏览器当弹窗出现不允许此页创建更多的消息时获取不到弹窗的文本值")
        time.sleep(3)
        self.driver.switch_to.alert.accept()

        '''后期优化未保存，就提交的case'''

        #切换供应商账号

    @unittest.skip('暂不执行')
    def test_a7_switch_Supplier(self):
        '''注销'''
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.frame("topFrame")
        self.driver.find_element_by_link_text("注销").click()
        username=self.driver.find_element_by_xpath('//*[@id="loginBg"]/table/tbody/tr[1]/td[1]/span').text
        self.assertIn(username,"账 号：")

    @unittest.skip('暂不执行')
    @BeautifulReport.add_test_img('test_a8_supplier_login')
    def test_a8_supplier_login(self):
        '''供应商登录'''
        common_browser.login(self, gys, "abc123")
        # common_browser.login(self,gys,"abc123")
        self.driver.switch_to.frame("topFrame")
        result = self.driver.find_element_by_id("userName1").text
        assert gys in result
        # assert "gkzy" in result

    @unittest.skip('暂不执行')
    def test_a9_order_receive_confirm(self):
        '''进入订单接收确认页面'''
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.frame('leftFrame')
        self.driver.find_element_by_link_text("订单接收确认").click()
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.frame('main')
        # 显式等待
        element = WebDriverWait(self.driver, 10, 3).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'titlebt'))).text
        self.assertEqual(element, "订单接收确认")

    @unittest.skip('暂不执行')
    def test_b1_order_receive_save(self):
        '''订单接收确认—点击确认按钮'''

        global orderNO1 #配送单订单号
        orderNO1=self.driver.find_element_by_id("conCon_txtBillNo").get_attribute('value')
        self.driver.find_element_by_id("WebTool_btSave").click()
        time.sleep(1)
        dig_alert = self.driver.switch_to.alert
        time.sleep(1)
        self.assertIn("确认成功！", dig_alert.text)
        self.driver.switch_to.alert.accept()

    @unittest.skip('暂不执行')
    def test_b2_Distribution_list_submit(self):
        '''进入配送单提交页面'''
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.frame('leftFrame')
        self.driver.find_element_by_link_text("配送单提交").click()
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.frame('main')
        element = WebDriverWait(self.driver, 10, 3).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'titlebt'))).text
        self.assertEqual(element, "配送单提交")

    @unittest.skip('暂不执行')
    def test_b3_Distribution_add(self):
        '''配送单提交-新增订单明细数据-获取订单号后，循环获取仓库，查询订单是否在该仓库中'''
        self.driver.find_element_by_id("WebTool_btAdd").click()
        # 选择仓库
        select = self.driver.find_element_by_id("conCon_ddlCKName")
        # 获取select里面的option标签，注意使用find_elements
        options_list = select.find_elements_by_tag_name('option')
        # 遍历option
        Warehouse = []
        for option in options_list:
           Warehouse.append(option.get_attribute("value"))
        for selectWarehouse in Warehouse:
            Select(self.driver.find_element_by_id("conCon_ddlCKName")).select_by_value(selectWarehouse)
            time.sleep(3)
            self.driver.find_element_by_id("conCon_btnAddDtl").click()
            windows = self.driver.window_handles
            self.driver.switch_to.window(windows[1])
            WebDriverWait(self.driver, 15, 5).until(
                EC.presence_of_element_located((By.ID, 'txtBillNo'))).send_keys(orderNO1)
            # time.sleep(3)
            # self.driver.find_element_by_id("txtBillNo").send_keys(orderNO1)
            self.driver.find_element_by_id("btQuery").click()
            billNo=self.driver.find_element_by_xpath('//*[@id="gridLogList"]/tbody/tr[2]/td[2]').text
            if billNo=="1":
                self.driver.find_element_by_id("gridLogList_selected_0").click()
                self.driver.find_element_by_id("btOK").click()
                break
            else:
                self.driver.find_element_by_id("btCance").click()
                # 判断当前窗口
                all_handles = self.driver.window_handles
                self.driver.switch_to.window(all_handles[0])
                self.driver.switch_to.parent_frame()
                self.driver.switch_to.frame('main')
        self.assertEqual(billNo, "1")

    @unittest.skip('暂不执行')
    def test_b4_Distribution_save(self):
        '''配送单保存'''
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[0])  # 切换至原来窗口
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.frame('main')  # 切换至main frame
        #销售清单号
        WebDriverWait(self.driver, 10, 3).until(
            EC.presence_of_element_located((By.ID, 'conCon_txtSplOutBillNo'))).send_keys(orderNO1+"10086")

        #批号
        WebDriverWait(self.driver, 10, 3).until(
            EC.presence_of_element_located((By.ID, 'conCon_gridList_txtLotNo_0'))).send_keys(random.randint(1,10))
        #生产日期   有效期
        time.sleep(2)

        prodate=self.driver.find_element_by_id("conCon_gridList_txtProDate_0")
        # ActionChains(self.driver).double_click(prodate).perform()
        prodate.click()
        self.driver.find_element_by_id("conCon_gridList_txtProDate_0").send_keys("20140101")
        self.driver.find_element_by_id("conCon_gridList_txtEndDate_0").send_keys("21000101")

        self.driver.find_element_by_id("WebTool_btSave").click()
        time.sleep(1)
        dig_alert = self.driver.switch_to.alert
        time.sleep(1)
        self.assertIn("保存成功！", dig_alert.text)
        self.driver.switch_to.alert.accept()

    @unittest.skip('暂不执行')
    def test_b5_Distribution_submit(self):
        '''配送单提交'''
        self.driver.find_element_by_id("WebTool_btTj").click()
        time.sleep(1)

        time.sleep(1)
        self.assertEqual("", self.driver.switch_to.alert.text,"IE浏览器当弹窗出现不允许此页创建更多的消息时获取不到弹窗的文本值，如果提交不成功则报错")
        self.driver.switch_to.alert.accept()