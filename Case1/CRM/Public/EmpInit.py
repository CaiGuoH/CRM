import random
import time

class Employee():
    '''初始化定义员工所有信息'''
    SURNAME = '王李张刘陈杨黄赵吴周徐孙马朱胡郭何高林罗郑梁谢宋唐位许韩冯邓曹彭曾萧田董潘袁于蒋蔡余杜叶程苏魏吕丁任沈姚卢姜崔钟谭陆汪范金石廖贾夏韦傅方白邹孟熊秦邱江尹薛阎段雷侯龙史陶黎贺顾毛郝龚邵万钱严覃武戴莫孔向汤'
    NAME = '丹举义之乐书乾云亦从代以伟佑俊修健傲儿元光兰冬冰冷凌凝凡凯初力勤千卉半华南博又友同向君听和哲嘉国坚城夏夜天奇奥如妙子存季孤宇安宛宸寒寻尔尧山岚峻巧平幼康建开弘强彤彦彬彭心忆志念怀怜恨惜慕成擎敏文新旋旭昊明易' \
           '昕映春昱晋晓晗晟景晴智曼朋朗杰松枫柏柔柳格桃梦楷槐正水沛波泽洁洋济浦浩海涛润涵渊源溥濮瀚灵灿炎烟烨然煊煜熙熠玉珊珍理琪琴瑜瑞瑶瑾璞痴皓盼真睿碧磊祥祺秉程立竹笑紫绍经绿群翠翰致航良芙芷苍苑若茂荣莲菡菱萱蓉蓝蕊' \
           '蕾薇蝶觅访诚语谷豪赋超越轩辉达远邃醉金鑫锦问雁雅雨雪霖霜露青靖静风 飞香驰骞高鸿鹏鹤黎'
    # TelF = '0750'
    TelF = ''
    BankF ='632'
    IDF = '510'
    UserF = '1000'
    Nat = ['汉','回','藏','黎','壮']
    FF = ['画画','唱歌','跳舞','看书','看电视']
    PhoneF = '136'
    Addres = ['成都','北京','上海']
    EmailEnd = ['@qq.com','@126.com','@163.com']

    def getName(self):
        '''定义员工姓名'''
        NameF = random.sample(Employee.SURNAME,1)
        NameL = random.sample(Employee.NAME,2)
        name = NameF+NameL
        name1 = ''
        for i in name:
            name1 += i
        name2 = name1.split()
        self.name = name2[0]
        return self.name

    def getAge(self):
        '''定义员工年龄'''
        self.age = random.randint(20,50)
        return self.age

    # def getSex(self):
    #     '''通过页面随机选择员工性别'''
    #     driver.switch_to.frame('mainFrame')
    #     s = driver.find_element_by_css_selector('[name = userSex]')
    #     c = s.find_elements_by_tag_name('option')
    #     i = random.randint(0,len(c))
    #     self.sex = c[i]
    #     return self.sex

    # def getDip(self):
    #     '''从页面自动获取'''

    # def getDpt(self):
    #     '''从页面获取'''

    def getTelNum(self):
        '''随机生成电话号码'''
        list1 = list((random.randint(0, 9) for i in range(7)))
        for j in list1:
            self.TelF += str(j)
        return self.TelF

    def getBankCard(self):
        '''随机生成工资卡号'''
        list2 = list((random.randint(0,9) for i in range(16)))
        for j in list2:
            self.BankF += str(j)
        return self.BankF
    def getID(self):
        '''随机生成身份证号码'''
        yd = '20001114'
        sid1 = list((random.randint(0, 9) for i in range(3)))
        self.sid1 = ''
        for i in sid1:
            self.sid1 += str(i)
        sid2 = list((random.randint(0, 9) for i in range(4)))
        self.sid2 = ''
        for j in sid2:
            self.sid2 += str(j)
        self.id = self.IDF + self.sid1 + yd + self.sid2
        return self.id

    # def AddPerson(self):
    #     '''添加人自动获取'''
    #     return self.name

    def getUserNum(self):
        '''随机生成员工账号'''
        i = random.randint(0,1000)
        self.UserF += str(i)
        return self.UserF

    def getPwd(self):
        self.pwd = '123456'
        return self.pwd

    def getNation(self):
        '''随机获取民族'''
        i = random.randint(0,len(self.Nat)-1)
        self.Nation = self.Nat[i]
        return self.Nation

    # def getMarried(self):
    #     '''从网页获取婚姻状况'''

    # def getRole(self):
    #     '''从网页随机获取角色'''

    def getFea(self):
        i = random.randint(0,len(self.FF)-1)
        self.Fea = self.FF[i]
        return self.Fea

    def getPhoneNum(self):
        '''随机生成手机号码'''
        self.ydnumm = list((random.randint(0, 9) for i in range(8)))
        for k in self.ydnumm:
            self.PhoneF += str(k)
        return self.PhoneF

    def getAddress(self):
        i = random.randint(0,len(self.Addres)-1)
        self.Addre = self.Addres[i]
        return self.Addre

    def getEmail(self):
        self.EmailStart = ''
        list4 = list((random.randint(1,9) for i in range(10)))
        for j in list4:
            self.EmailStart += str(j)
        k = random.randint(0,len(self.EmailEnd)-1)
        self.Email = self.EmailStart+self.EmailEnd[k]
        return self.Email







if __name__ == '__main__':

    n = Employee()
    print(n.getName())
    print(n.getAge())
    # print(n.getSex())
    print(n.getTelNum())
    print(n.getBankCard())
    print(n.getID())
    print(n.getUserNum())
    print(n.getPwd())
    print(n.getNation())
    print(n.getFea())
    print(n.getPhoneNum())
    print(n.getEmail())