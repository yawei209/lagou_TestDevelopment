# -*- coding: utf-8 -*-
# @Time : 2021/3/11 19:19
# @Author : zhangyawei
# @Email : zhangyawei209@163.com
# @File : index_page.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from Pageobject_实战课程.page.addmember_page import AddMemberPage


class IndexPage:

    def __init__(self):
        option = Options()
        option.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=option)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    def click_add_member(self):
        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1)').click()
        return AddMemberPage(self.driver)