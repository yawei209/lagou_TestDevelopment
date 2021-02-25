# -*- coding: utf-8 -*-
# @Time : 2021/2/25 19:08
# @Author : zhangyawei
# @Email : zhangyawei209@163.com
# @File : login.py
# @Software: PyCharm
from selenium.webdriver.common.by import By

from Pageobject.page.base_page import BasePage
from Pageobject.page.register import Register


class Login(BasePage):
    def scan(self):
        pass
    def goto_register(self):
        self.find(By.CSS_SELECTOR, "login_registerBar_link").click()
        return Register(self._driver)