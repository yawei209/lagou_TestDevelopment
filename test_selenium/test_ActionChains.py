# -*- coding: utf-8 -*-
# @Time : 2021/2/18 14:11
# @Author : zhangyawei
# @Email : zhangyawei209@163.com
# @File : test_ActionChains.py
# @Software: PyCharm
import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class TestActionChains():

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()
    @pytest.mark.skip
    def test_case_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        #定义元素变量
        element_click = self.driver.find_element_by_xpath('//input[@value="click me"]')
        element_doubleclick= self.driver.find_element_by_xpath('//input[@value="dbl click me"]')
        element_rightclick = self.driver.find_element_by_xpath('//input[@value="right click me"]')

        actions =ActionChains(self.driver)

        #点击
        actions.click(element_click)
        #右击
        actions.context_click(element_rightclick)
        #双击
        actions.double_click(element_doubleclick)

        sleep(1)
        actions.perform()
        sleep(1)
    @pytest.mark.skip
    def test_dragdrop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        # 一定注意，action方法中是需要的找到的元素，而不是直接的一个xpath地址
        element_drag = self.driver.find_element_by_xpath('//div[@id="dragger"]')
        element_drop1 = self.driver.find_element_by_xpath("/html/body/div[2]")
        element_drop2 = self.driver.find_element_by_xpath("/html/body/div[3]")
        element_drop3 = self.driver.find_element_by_xpath("/html/body/div[4]")
        element_drop4 = self.driver.find_element_by_xpath("/html/body/div[5]")

        #写法一：链式写法
        # ActionChains(self.driver).click_and_hold(element_drag).release(element_drop1).perform()

        #写法二：分布写法
        actions = ActionChains(self.driver)

        #方法一：action.drap_and_drop()
        # actions.drag_and_drop(element_drag, element_drop1)

        #方法二：action.click_and_hold(target).release(target)  两个方法可以链式写在一个ActionChains对象之后
        actions.click_and_hold(element_drag).release(element_drop1)
        actions.perform()
        sleep(1)


    def test_keys1(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        element = self.driver.find_element_by_xpath('/html/body/label[1]/input')    #输入框元素
        chains = ActionChains(self.driver)
        chains.click(element)   #光标先在输入框元素点击
        chains.send_keys("username").pause(1)   #输入”username“，并等待1秒
        chains.send_keys(Keys.SPACE).pause(1)   #输入空格键，并等待1秒
        chains.send_keys("tom").pause(1)        #输入”tom“，并等待1秒
        chains.send_keys(Keys.BACKSPACE).perform()  #输入删除键，并等待1秒
        sleep(2)

    def test_keys2(self):
        #ctrl+a：action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL)
        #ctrl+c：action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL)
        self.driver.get("http://sahitest.com/demo/label.htm")
        element_input1 = self.driver.find_element_by_xpath('/html/body/label[1]/input')
        element_input2 = self.driver.find_element_by_xpath('/html/body/label[2]/table/tbody/tr/td[2]/input')
        chains = ActionChains(self.driver)
        chains.click(element_input1)
        chains.send_keys("username tom").pause(1)
        chains.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).pause(1)
        chains.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).pause(1)
        chains.click(element_input2).pause(1)
        chains.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).pause(1)
        chains.perform()
        sleep(1)

if __name__ == '__main__':
    # pytest.main(['-v','-s','test_ActionChains.py'])
    pytest.main()