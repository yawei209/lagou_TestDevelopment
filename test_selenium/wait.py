# -*- coding: utf-8 -*-
# @Time : 2021/2/10 11:30
# @Author : zhangyawei
# @Email : zhangyawei209@163.com
# @File : second.py
# @Software: PyCharm
from time import sleep

from selenium import webdriver
# from selenium.webdriver.common.by import By


class TestWait:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_wait(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_xpath('//*[@id="kw"]').send_keys("selenium")
        # self.driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys("selenium")
        self.driver.find_element_by_xpath('//*[@id="su"]').click()
        sleep(2)