# -*- coding: utf-8 -*-
# @Time : 2021/2/18 14:11
# @Author : zhangyawei
# @Email : zhangyawei209@163.com
# @File : test_ActionChains.py
# @Software: PyCharm
import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains


class TestActionChains():

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_case_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        #定义元素变量
        element_click = self.driver.find_element_by_xpath('//input[@value="click me"]')
        element_doubleclick= self.driver.find_element_by_xpath('//input[@value="dbl click me"]')
        element_rightclick = self.driver.find_element_by_xpath('//input[@value="right click me"]')

        actions =ActionChains(self.driver)

        #点击
        actions.click(element_click)
        #右击
        actions.context_click(element_rightclick)
        #双击
        actions.double_click(element_doubleclick)

        sleep(1)
        actions.perform()
        sleep(1)

if __name__ == '__main__':
    # pytest.main(['-v','-s','test_ActionChains.py'])
    pytest.main()