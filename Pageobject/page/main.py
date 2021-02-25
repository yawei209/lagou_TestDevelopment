# -*- coding: utf-8 -*-
# @Time : 2021/2/25 18:19
# @Author : zhangyawei
# @Email : zhangyawei209@163.com
# @File : main.py
# @Software: PyCharm
from selenium.webdriver.common.by import By

from Pageobject.page.base_page import BasePage
from Pageobject.page.login import Login
from Pageobject.page.register import Register


class Main(BasePage):
    _base_url = 'https://work.weixin.qq.com/'
    def goto_register(self):
        self.find(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
        return Register(self._driver)

    def goto_login(self):
        self.find(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()
        return Login(self._driver)