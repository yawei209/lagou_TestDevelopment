# -*- coding: utf-8 -*-
# @Time : 2021/2/10 11:30
# @Author : zhangyawei
# @Email : zhangyawei209@163.com
# @File : second.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver import TouchActions
from time import sleep

class TestTouchAction:
    def setup(self):
        #TouchActions(driver).scroll_from_element()需要配置
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option('w3c', False)

        self.driver = webdriver.Chrome(chrome_options= opt)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_touchaction_scrollbottom(self):
        self.driver.get("https://www.baidu.com")
        element_input = self.driver.find_element_by_xpath('//input[@id="kw"]')
        element_submit = self.driver.find_element_by_xpath('//input[@id="su"]')

        element_input.send_keys('selenium')
        actions = TouchActions(self.driver)
        actions.tap(element_submit)  #TouchAction.tap() 是点击功能
        actions.perform()
        #actions.scrool_from_element()方法
        actions.scroll_from_element(element_input,0,5000).perform()
        sleep(2)