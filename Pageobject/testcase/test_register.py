# -*- coding: utf-8 -*-
# @Time : 2021/2/25 19:12
# @Author : zhangyawei
# @Email : zhangyawei209@163.com
# @File : test_register.py
# @Software: PyCharm
from Pageobject.page.main import Main


class TestRegister:

    def setup(self):
        self.main = Main()

    def test_register(self):
        assert self.main.goto_register().register()