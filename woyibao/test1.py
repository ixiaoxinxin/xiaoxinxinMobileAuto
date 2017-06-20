# coding=utf-8

# appium 微信h5自动化示例
import os
from appium import webdriver
import unittest
import HTMLTestRunner
import time

from selenium.webdriver.common.by import By

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class elementA(unittest.TestCase):
    def test_(self):
        desired_caps = {}
        desired_caps['deviceName'] = 'ec01b232'  # adb devices查到的设备名
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['appPackage'] = 'com.tencent.mm'  # 被测App的包名
        desired_caps['appActivity'] = '.ui.LauncherUI'  # 启动时的Activity
        desired_caps['chromeOptions'] = {'androidProcess': 'com.tencent.mm:tools'}
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

        driver.implicitly_wait(30)
        # -------------------------------------------------------------------------------------
        driver.find_element_by_name("1").click()
        time.sleep(1)
        wyb = driver.find_element_by_id("com.tencent.mm:id/a4i")
        wyb.click()
        time.sleep(1)
        shulaibao = driver.find_element_by_name(u"术来保")
        shulaibao.click()
        driver.implicitly_wait(30)
        #-------------------------------------------------------------------------------------
        #用dev tools来定位H5页面具体信息
        driver.find_element_by_name("operationName").send_keys("凯勒乐keller手术拇囊肿切除术")
        time.sleep(1)
        driver.find_element_by_name("hosName").send_keys("凯勒乐keller手术拇囊肿切除术")
        driver.quit()

if __name__ == '__main__':
    testunit=unittest.TestSuite()        #定义一个单元测试容器
    testunit.addTest(elementA("test_"))  #将测试用例加入到测试容器中
    filename="./toubaoLog.html"        #定义个报告存放路径，支持相对路径。
    fp=file(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'我医保',description='Report_description')  #使用HTMLTestRunner配置参数，输出报告路径、报告标题、描述
    runner.run(testunit)



