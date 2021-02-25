# -*- coding: utf-8 -*-
# @Time : 2021/2/25 18:21
# @Author : zhangyawei
# @Email : zhangyawei209@163.com
# @File : base_page.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _base_url = ""

    def __init__(self, driver:WebDriver=None):
        self._driver = ""
        if driver is None:
            self._driver = webdriver.Chrome()
        else:
            self._driver = driver
        if self._base_url != "":
            self._driver.get(self._base_url)
    def find(self, by, locator):
        return self._driver.find_element(by, locator)
