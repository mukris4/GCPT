import unittest
import  datetime
from BeautifulReport import BeautifulReport
from util.send_email import sendemail
# 用例存放位置
test_case_path="H:/GCPT/test_case"
# 测试报告存放位置
log_path='H:/GCPT/report'
# 测试报告名称
now = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S-')
# filename = '测试报告'
# filename="test_report"
filename=str(now)+'test_report'
#用例名称
description='枣阳供采平台'
# 需要执行哪些用例，如果目录下的全部，可以改为"*.py"，如果是部分带test后缀的，可以改为"*test.py"
pattern="test_orderManage.py"

if __name__ == '__main__':
    test_suite = unittest .defaultTestLoader.discover(test_case_path, pattern=pattern)
    result = BeautifulReport(test_suite)
    result.report(filename=filename,description=description,report_dir=log_path)
    # report='H:/GCPT/report/'+filename+'.html'
    # sendemail(report)
