import unittest
import random
import time
from Case1.CRM.Public import Mysql2
from Case1.CRM.Public.EmpInit import Employee
from Case1.CRM.Page.Base import PageBase
from selenium.webdriver.common.by import By
from Case1.CRM.Image.ScreenShot import createP


class MytestCaseAddEmp(unittest.TestCase, PageBase):
    '''登录初始化'''
    def setUp(self) -> None:
        PageBase()
        self.add1 = Employee()
        self.sendkey(By.NAME, 'userNum', value='Admin')
        self.sendkey(By.NAME, 'userPw', value='123456')
        self.click(By.ID, 'in1')
        # 验证是否成功登录
        self.frame('topFrame')
        self.message = self.find(By.XPATH,'/html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td[1]/table/tbody/tr/td[2]/div').text
        self.addperson = self.message[5:]
        # 切回主页
        self.driver.switch_to.default_content()
        assert (self.message[0:5] == '当前用户：'), '未登录成功'
        self.frame(1)
        self.click(By.XPATH,'/html/body/table/tbody/tr[2]/td/table/tbody/tr[4]/td/table/tbody/tr[1]/td/table/tbody/tr/td[2]')
        self.click(By.LINK_TEXT,'添加员工')
        self.driver.switch_to.default_content()

    def tearDown(self) -> None:
        time.sleep(3)
        self.driver.quit()

    def testAddeEmp1(self):

        # self.frame('mainFrame')
        # 新增前数据库的数量
        sql2 = "select count(*) from user_info"
        SQLnum1 = Mysql2.getAllNum(sql2)

        # 切换frame
        # self.driver.switch_to.frame('mainFrame')
        self.frame('mainFrame')

        # 添加员工姓名
        name1 = self.add1.getName()
        self.driver.find_element_by_name('userName').send_keys(self.add1.getName())

        # 添加员工年龄
        self.driver.find_element_by_name('userAge').send_keys(self.add1.getAge())

        # 随机获取员工性别
        s = self.driver.find_element_by_name('userSex')
        c = s.find_elements_by_tag_name('option')
        i = random.randint(0, len(c) - 1)
        c[i].click()

        # 随机获取学历
        s2 = self.driver.find_element_by_name('userDiploma')
        c2 = s2.find_elements_by_tag_name('option')
        i2 = random.randint(0, len(c2) - 1)
        c2[i2].click()

        # 随机获取部门
        s3 = self.driver.find_element_by_name('departmentId')
        c3 = s3.find_elements_by_tag_name('option')
        i3 = random.randint(0, len(c3) - 1)
        c3[i3].click()

        # 添加座机号
        self.driver.find_element_by_css_selector('[valid=isPhone]').send_keys(self.add1.getTelNum())

        # 添加工资卡
        self.driver.find_element_by_css_selector('[valid="isNumber"]').send_keys(self.add1.getBankCard())

        # 添加身份证
        self.driver.find_element_by_css_selector('[valid="isIdCard"]').send_keys(self.add1.getID())

        # 获取添加人
        self.driver.find_element_by_name('userAddman').send_keys(self.addperson)

        # 随机添加账号
        self.driver.find_element_by_name('userNum').send_keys(self.add1.getUserNum())

        # 添加密码
        self.driver.find_element_by_name('userPw').send_keys(self.add1.getPwd())

        # 添加民族
        self.driver.find_element_by_name('userNation').send_keys(self.add1.getNation())

        # 随机选择婚姻
        s4 = self.driver.find_element_by_name('isMarried')
        c4 = s4.find_elements_by_tag_name('option')
        i4 = random.randint(0, len(c4) - 1)
        c4[i4].click()

        # 随机选择角色
        s5 = self.driver.find_element_by_name('roleId')
        c5 = s5.find_elements_by_tag_name('option')
        i5 = random.randint(0, len(c5) - 1)
        c5[i5].click()

        # 随机生成爱好
        self.driver.find_element_by_name('userIntest').send_keys(self.add1.getFea())

        # 随机生成移动手机号
        self.driver.find_element_by_name('userMobile').send_keys(self.add1.getPhoneNum())

        # 随机生成地址
        self.driver.find_element_by_name('userAddress').send_keys(self.add1.getAddress())

        # 随机生成邮箱
        self.driver.find_element_by_name('userEmail').send_keys(self.add1.getEmail())

        #截图
        # Pic_path1 = r'./' + name1 + ".png"
        time.sleep(1)
        self.driver.save_screenshot(createP())
        time.sleep(2)

        # 点击添加按钮
        self.driver.find_element_by_name('submit').click()
        time.sleep(2)

        self.driver.switch_to.alert.accept()
        Mysql2.db.commit()

        # driver.quit()

        # 新增员工后人数
        SQLnum2 = Mysql2.getAllNum(sql2)
        assert (SQLnum1+1 == SQLnum2),'数据未添加成功'



if __name__ == '__main__':
    unittest.main()
