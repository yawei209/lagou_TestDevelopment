# -*- coding: utf-8 -*-
# @Time : 2021/3/11 19:41
# @Author : zhangyawei
# @Email : zhangyawei209@163.com
# @File : test_contact.py
# @Software: PyCharm
from time import sleep

from Pageobject_实战课程.page.index_page import IndexPage


class TestContact:
    def setup(self):
        self.index = IndexPage()    #记得添加(),完成实例化

    def test_addcontact(self):
        # self.index.click_add_member().add_member()
        result = self.index.click_add_member().add_member()
        assert result
