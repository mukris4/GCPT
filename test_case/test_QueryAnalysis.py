import time
import unittest
from selenium import  webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
# 登录
class QueryA(unittest.TestCase):

    @classmethod
    def setUpClass(cls) :
        cls.driver = webdriver.Ie()
        cls.driver.get('http://192.168.1.24:8031/(S(q0bjadi3zomcgh3afy4snowk))/Login.aspx')
        cls.driver.maximize_window()


    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        cls.driver.quit()


    def test_a1_login(self):
        '''用户登录'''

        self.driver.find_element_by_id("username").clear()
        self.driver.find_element_by_id("username").send_keys("gkzy")
        # self.driver.find_element_by_id("password").clear()

        # 改用双击事件
        password = self.driver.find_element_by_id("password")
        ActionChains(self.driver).double_click(password).perform()
        # 输入内容
        # password.clear()
        password.send_keys("abc123")
        self.driver.find_element_by_id("ImageBtLogin").click()
        self.driver.switch_to.frame("topFrame")
        result=self.driver.find_element_by_class_name("userName").text
        assert "当前用户" in result


#查询分析

    def test_a2_orderStatu(self):
        '''订单状态跟踪'''
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.frame('leftFrame')
        self.driver.find_element_by_link_text("订单状态跟踪").click()
        time.sleep(2)
        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        self.driver.maximize_window()

        # 显式等待
        element = WebDriverWait(self.driver, 10,0.5).until(EC.presence_of_element_located((By.CLASS_NAME, 'titlebt'))).text
        self.assertEqual(element, "订单状态跟踪")




    def test_a3_order_timecheck(self):
        '''订单跟踪状态-查询2018-01-01至今订单列表'''
        #修改订单复核时间
        timecheck = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'conCon_txtFHStartDate')))
        timecheck.clear()
        timecheck.send_keys("2018-01-01")
        #点击查询按钮
        self.driver.find_element_by_id("conCon_btnQuery").click()

        order_list=self.driver.find_element_by_id('conCon_gridListHdr_lbtnDtlQuery_0').text
        self.assertEqual(order_list,"查看")


    def test_a4_orderinfo(self):
        '''查看订单列表第一个订单的明细详情'''
        self.driver.find_element_by_id('conCon_gridListHdr_lbtnDtlQuery_0').click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="gridListDtl"]/tbody/tr[2]/td[2]')))
        Orderinfo=element.text
        self.assertEqual(Orderinfo,"1")

    def test_a5_close_orderinfo(self):
        '''关闭订单状态明细页面'''
        self.driver.find_element_by_id("btCance").click()
        #判断当前窗口
        all_handles = self.driver.window_handles
        # print(all_handles)
        self.driver.switch_to.window(all_handles[1])
        element=self.driver.find_element_by_class_name("titlebt").text
        self.assertEqual(element, "订单状态跟踪")

   # @unittest.skip('暂不执行')
    def test_a6_orderdistribution(self):
        '''第一条订单配送详情'''
        self.driver.find_element_by_id("conCon_gridListHdr_lbtnPSQuery_0").click()
        windows = self.driver.window_handles
        print(windows)
        self.driver.switch_to.window(windows[-1])

        element1 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="gridListHdr"]/tbody/tr[2]/td[1]')))
        self.assertEqual(element1.text, "1")

    @unittest.expectedFailure  #第四个窗口定位不到
    def test_a7_orderdistributioninfo(self):
        '''查看配送单据的第一条数据的详情'''
        self.driver.find_element_by_id('gridListHdr_lbtnDtlQuery_0').click()
        # self.driver.maximize_window()
        windows = self.driver.window_handles
        print(windows)
        try:
            self.driver.switch_to.window(windows[3])
        except IndexError:
            print
            "Error:未定位到配送单明细查询窗口"

        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="gridListDtl"]/tbody/tr[2]/td[1]')))
        self.assertEqual(element.text, "1")


    def test_a8_close_orderdistributioninfo(self):
        '''关闭配送单明详情页面'''
        self.driver.close()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        element=self.driver.find_element_by_class_name("titlebt").text
        self.assertEqual(element, "订单状态跟踪")


    def test_a9_orderstatus_list_skip_page(self):
        '''订单列表相关跳转-下一页'''
        target = self.driver.find_element_by_id("conCon_gridListHdr_LinkButtonNextPage")
        self.driver.execute_script("arguments[0].scrollIntoView();", target)  # 拖动到可见的元素去
        target.click()
        time.sleep(3)
        #显式等待无效，使用强制等待
        #firstpage = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'conCon_gridListHdr_LinkButtonFirstPage')))
        firstpage=self.driver.find_element_by_id("conCon_gridListHdr_LinkButtonFirstPage")
        self.assertEqual(firstpage.text,"首页")

    @unittest.expectedFailure
    def test_b1_orderstatus_list_skip_numpage(self):
        '''订单列表相关跳转-指定页数'''
        page=self.driver.find_element_by_id("conCon_gridListHdr_txtNewPageIndex")
        page.clear()
        key=random.randint(1, 10)
        page.send_keys(key)
        self.driver.find_element_by_id("conCon_gridListHdr_btnGo").click()
        #当前页
        page1 = self.driver.find_element_by_id("conCon_gridListHdr_LabelCurrentPage")
        self.assertEqual(page1.text,key,msg="实际已跳转，定位当前页出错，原因未知")
