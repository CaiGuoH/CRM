from HTMLTestRunner import HTMLTestRunner
import time
import unittest

def createRep(title1,title2,dis):
    # 我们要新建一个用于保存我们测试结果的文件，html
    now = time.strftime("%Y-%m-%d-%H-%M-%S")
    # 定义文件的名字
    # filename = './' + now + "_result.html"
    filename = now + "_result.html"
    file = open(filename, "wb")
    # 执行我们的报告写入
    runner = HTMLTestRunner(stream=file, title=title1, description=title2)
    # stream：是指定测试报告文件
    # title：指定报告的标题
    # description:指定报告的副标题
    # 执行我们测试用例
    runner.run(dis)
    time.sleep(3)
    # 要进行关闭
    file.close()
    return filename
    # 执行测试用例
    # runner=unittest.TextTestRunner()
    # runner.run(suite)
