# -*- coding: utf-8 -*-
# @Time : 2021/2/10 11:30
# @Author : zhangyawei
# @Email : zhangyawei209@163.com
# @File : second.py
# @Software: PyCharm

import selenium
from selenium import webdriver

def test_selenium():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com/")