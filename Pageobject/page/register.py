# -*- coding: utf-8 -*-
# @Time : 2021/2/25 19:02
# @Author : zhangyawei
# @Email : zhangyawei209@163.com
# @File : register.py
# @Software: PyCharm
from selenium.webdriver.common.by import By

from Pageobject.page.base_page import BasePage


class Register(BasePage):
    def register(self):
        self.find(By.ID, "corp_name").send_keys("hello")
        self.find(By.ID, "manager_name").send_keys("world")
        return True