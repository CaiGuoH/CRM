import time
import unittest
from Case1.CRM.Report.CreateReport import createRep
from Case1.CRM.SendEmail.SendEmail import send_mail
from Case1.CRM.Image.ScreenShot import createP

dir = './Case1/CRM/Case'
dis = unittest.defaultTestLoader.discover(dir,pattern='Crm*.py')

rep = createRep("crm添加员工测试",'正确添加员工用例详情',dis)
pa = createP()

time.sleep(5)
send_mail(rep,pa)
