# -*- coding: utf-8 -*-
# @Time : 2021/2/20 18:19
# @Author : zhangyawei
# @Email : zhangyawei209@163.com
# @File : base.py
# @Software: PyCharm

from selenium import webdriver
class Base():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()