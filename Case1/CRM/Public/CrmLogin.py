from Case1.CRM.Page.Base import PageBase
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class CrmLogin(PageBase):
    '''登录初始化'''
    def Login(self,name,pwd):
        self.sendkey(By.NAME,'userNum',value=name)
        self.sendkey(By.NAME,'userPw',value=pwd)
        self.click(By.ID,'in1')

        # 验证是否成功登录
        self.frame('topFrame')
        self.message = self.find(By.XPATH,'/html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td[1]/table/tbody/tr/td[2]/div').text

        # 切回主页
        self.driver.switch_to.default_content()
        assert (self.message[0:5] == '当前用户：'), '未登录成功'
        # if self.message[0:5] == '当前用户：':
        #     print('登录成功')
        # else:
        #     print('未登录成功')







