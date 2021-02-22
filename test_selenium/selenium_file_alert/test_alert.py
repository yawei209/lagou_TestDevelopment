# -*- coding: utf-8 -*-
# @Time : 2021/2/10 11:30
# @Author : zhangyawei
# @Email : zhangyawei209@163.com
# @File : second.py
# @Software: PyCharm
from time import sleep

from selenium.webdriver import ActionChains
from test_selenium.selenium_file_alert.base import Base

class TestAlert(Base):
    '''
    打开网页https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable
    操作窗口右侧页面，将元素1拖拽到元素2
    这时候会有一个alert弹框，点击弹框中的确定
    然后在按'点击运行'
    关闭页面
    
    1、切换frame：driver.switch_to_frame('frame的ID')
    切换回默认frame：driver.swithc_to_default_content()
    2、拖拽元素、到某一位置：
    action = ActionChains(driver)
    action.drag_and_drop(ele_drag, ele_drop).preform()
    3、处理弹框,并确认(accept方法)
    driver.switch_to_alert().accept()
     '''
    def test_alert(self):
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        #切换frame
        self.driver.switch_to_frame("iframeResult")
        element_drag = self.driver.find_element_by_id("draggable")
        element_drop = self.driver.find_element_by_id("droppable")
        actions = ActionChains(self.driver)
        sleep(1)
        actions.drag_and_drop(element_drag, element_drop).perform()
        #处理弹出的alert窗口,调用accept方法点击确认。
        sleep(1)
        self.driver.switch_to_alert().accept()
        #切换到默认frame，重新点击"点击运行"按钮
        self.driver.switch_to_default_content()
        self.driver.find_element_by_id('submitBTN').click()
        sleep(2)
