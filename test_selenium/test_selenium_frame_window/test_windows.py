# -*- coding: utf-8 -*-
# @Time : 2021/2/20 18:22
# @Author : zhangyawei
# @Email : zhangyawei209@163.com
# @File : test_windows.py
# @Software: PyCharm
from time import sleep
from test_selenium.test_selenium_frame_window.base import Base

class TestWindows(Base):
    def test_window(self):
        self.driver.get("http://www.baidu.com")
        # self.driver.find_element_by_link_text("登陆").click()
        self.driver.find_element_by_xpath('//*[@id="u1"]/a').click()
        self.driver.find_element_by_link_text("立即注册").click()
        #打印窗口句柄
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        sleep(1)
        #切换窗口
        windows = self.driver.window_handles    #存贮window_handles变量
        self.driver.switch_to_window(windows[-1])
        #打印窗口句柄
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        sleep(1)
        #注册页面
        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("username")
        self.driver.find_element_by_id("TANGRAM__PSP_4__phone").send_keys("18600000000")

        sleep(1)
        self.driver.switch_to_window(windows[0])
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__footerULoginBtn"]').click()
        sleep(2)
        self.driver.find_element_by_id('TANGRAM__PSP_11__userName').send_keys('username')
        self.driver.find_element_by_id('TANGRAM__PSP_11__password').send_keys('123456')
        self.driver.find_element_by_id('TANGRAM__PSP_11__submit').click()
        sleep(2)