# -*- coding: utf-8 -*-
# @Time : 2021/2/10 11:30
# @Author : zhangyawei
# @Email : zhangyawei209@163.com
# @File : second.py
# @Software: PyCharm
from test_selenium.selenium_js.base import Base
from time import sleep

class TestJS(Base):
    def test_js_scroll(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_id('kw').send_keys('selenium')

        # 执行js命令，查找定位id="su"的按钮，并返回付给变量。
        element_su = self.driver.execute_script("return document.getElementById('su')")
        element_su.click()
        sleep(1)

        #向下滑动到页面底部
        self.driver.execute_script('document.documentElement.scrollTop=10000')
        #点击下一页
        self.driver.find_element_by_xpath('//*[@id="page"]/div/a[10]').click()
        sleep(2)

        #打印当前页面的title、和性能数据。并return出来。注意return一定是和js命令是一起的。
        for code in ['return document.title', 'return JSON.stringify(performance.timing)']:
            print(self.driver.execute_script(code))

    def test_datetime(self):
        self.driver.get("https://www.12306.cn/index/")
        #在driver.execute_script('js命令1;js命令2')，两条命令可写在一个方法里，js命令1的变量 js命令2可以直接用。
        self.driver.execute_script('time=document.getElementById("train_date");time.removeAttribute("readonly")')
        #重新找到时间元素，修改value值。
        self.driver.execute_script('document.getElementById("train_date").value="2021-3-4"')
        sleep(2)
        #打印出需改的值
        print(self.driver.execute_script('return document.getElementById("train_date").value'))
