import yagmail
from os.path import dirname,abspath

def sendemail(report):

    # yag = yagmail.SMTP(user='18895308764@163.com', password='abc123', host='smtp.163.com', port='465')
    yag = yagmail.SMTP(user='549502773@qq.com', password='niflyywsucambdih', host='smtp.qq.com', port='465')
    yag.send('1402697976@qq.com', subject="自动化测试报告", contents='自动化测试报告请看附件', attachments=report)
    print("邮件已发送")
# report = 'H:/GCPT/report/test_report.html'
# sendemail(report)
#添加模块至sys
#rootPath = dirname(abspath(__file__))
#sys.path.append(rootPath)
#sys.path.append(rootPath+"\\venv\\Lib\\site-packages")

