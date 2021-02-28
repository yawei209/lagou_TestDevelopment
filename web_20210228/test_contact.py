# -*- coding: utf-8 -*-
# @Time : 2021/2/10 11:30
# @Author : zhangyawei
# @Email : zhangyawei209@163.com
# @File : second.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestWx:
    def setup(self):
        option = Options()
        option.debugger_address = "127.0.0.1:9222" #需要提前在命令行中运行Chrome --remote-debugging-port=9222
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def test_case1(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        self.driver.find_element_by_xpath('//*[@id="menu_contacts"]').click()