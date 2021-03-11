# -*- coding: utf-8 -*-
# @Time : 2021/3/11 19:29
# @Author : zhangyawei
# @Email : zhangyawei209@163.com
# @File : addmember_page.py
# @Software: PyCharm
from time import sleep

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class AddMemberPage:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def add_member(self):
        name = "aa_0"
        account = "aa_0_zyw"
        phonenum = "13500000001"
        sleep(2)
        #input mane
        self.driver.find_element(By.ID, 'username').send_keys(name)
        #input account
        self.driver.find_element(By.ID, 'memberAdd_acctid').send_keys(account)
        #input phonenum
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys(phonenum)
        #click save
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()

        return True