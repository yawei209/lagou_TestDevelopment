# -*- coding: utf-8 -*-
# @Time : 2021/2/10 11:30
# @Author : zhangyawei
# @Email : zhangyawei209@163.com
# @File : second.py
# @Software: PyCharm
import shelve
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestWx:
    def setup(self):
        option = Options()
        option.debugger_address = "127.0.0.1:9222"  # 需要提前在命令行中运行Chrome --remote-debugging-port=9222
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def test_case1(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        self.driver.find_element_by_xpath('//*[@id="menu_contacts"]').click()

    def test_cookie(self):
        cookies = self.driver.get_cookies()
        print(cookies)#打印cookie

        for cookie in cookies:
            #如果cookie的'expiry'是小数的话，add_cookie(cookie)方法会报错。这个'expiry'也没有用就索性删掉
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        self.driver.refresh()


    def test_case2(self):
        #Mac 格式话代码 pycharm快捷键：command+option+L
        # cookies = [
        #     {'domain': '.lagou.com', 'expiry': 7921716569, 'httpOnly': False, 'name': 'sensorsdata2015jssdkcross',
        #      'path': '/', 'secure': False,
        #      'value': '%7B%22distinct_id%22%3A%224204971%22%2C%22first_id%22%3A%22177e36a4f574d6-0631928aa6ae1c-123b6a5a-2073600-177e36a4f5810b%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_utm_source%22%3A%22baidujava%22%2C%22%24latest_utm_medium%22%3A%22sspc%22%2C%22%24latest_utm_term%22%3A%22java20913%22%2C%22%24os%22%3A%22MacOS%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2278.0.3904.70%22%7D%2C%22%24device_id%22%3A%2217583e94f8a438-008ff1eb77b40a-123b6a5a-1024000-17583e94f9166a%22%7D'},
        #     {'domain': 'kaiwu.lagou.com', 'httpOnly': False, 'name': 'WEBTJ-ID', 'path': '/', 'secure': False,
        #      'value': '20210228204928-177e8afc39944d-09a2173f93de15-123b6a5a-2073600-177e8afc39a428'},
        #     {'domain': '.lagou.com', 'httpOnly': False, 'name': 'sensorsdata2015session', 'path': '/', 'secure': False,
        #      'value': '%7B%7D'},
        #     {'domain': '.lagou.com', 'expiry': 1615121344.610581, 'httpOnly': False, 'name': 'gate_login_token',
        #      'path': '/', 'secure': False, 'value': 'a96393aa65cfcb0001a6c638ed4cfc2885e643a3c6af1a7a'},
        #     {'domain': '.lagou.com', 'httpOnly': True, 'name': 'EDUJSESSIONID', 'path': '/', 'secure': False,
        #      'value': 'ABAAAECABCAAACDC4BFD7094D8BE50477635FD00FDE58BC'},
        #     {'domain': '.lagou.com', 'expiry': 3761920603.404295, 'httpOnly': False, 'name': 'LG_LOGIN_USER_ID',
        #      'path': '/', 'secure': False, 'value': '410cbbd8783dcf3da05fa47f74e4da48efd24cf9e922811a'},
        #     {'domain': '.lagou.com', 'expiry': 1615032932, 'httpOnly': False, 'name': 'thirdDeviceIdInfo', 'path': '/',
        #      'secure': False,
        #      'value': '%5B%7B%22channel%22%3A1%2C%22thirdDeviceId%22%3A%22WHJMrwNw1k/EpoiBjIMJKo8xaTlKOFYJ4NiNabPk024G5zUkuRzoBFATCLb2S4HFQebxxhUbVdTM2ww3do1IjcgieZBKlBl5odCW1tldyDzmQI99+chXEiln6qz0MuWn/9lCUKKcsmkTaFO8webhNijYmmmXo8LlTkQE5YcNLqNriNYPfoOP/bsQXyw9xzi14W09UQAX97XLQqSN07G/tn+8Vg+5pExYXaImmzqUscAowwy7YLAZobtsTMC+cbOmt1487582755342%22%7D%2C%7B%22channel%22%3A2%2C%22thirdDeviceId%22%3A%22140%23sXso3y+azzWTAQo23xDQ4pN8s7O2H7jLGtQ2Y3Y5kR8Rw0PKy37+i/8jF/LGXoXsKVT276hqzznUrJH1c5OzzZIdIamqlQzx2DD3VthqzFcYLX8+lpYazDrbV2QVoRP2ONdOHaU+PQbp4suDHWfsl7m1FH6hx04L2RtjBLtaxj3NCl5ZmgFAyIeaZ2SNCJJEz0LC7V4z24EiUlInhdBeqd0UAS58oqwuLjshSOQcIJfvjI0eHvSYTjTu+cBoJj/i/UJ5fH1umrYvPD6DCRQhnkZEab8RUJeEl+NQwCKLQvqbd0BshvZyVEiYuCawrsBHOJ7QJhkmnJpenouKafcyKuAqCN27iyGY/7F94vlAJsJDTyANBiWFMlOT0kiTgJuNIlCCHf/DdYLiWpUyGG//ssKShWWlOnLmbia9e57H1Xq6/07Xerw0t7c8QE058Q+u8EvPxKoSe/hakXRFUiN52VU64ZsEELLcRM/uSAzB+qoOoMezDv0TnU//rpd1BiEIcG9rrYswZLJbnzfVm1qgwY9eiIEg/XmncsvU1Dp0d4cA16vNQ98ranIDH4+x0x/S57YsivmeqzApQCukbECtoVzxNrHw/1IOXo1V7b7HRWj2lCwdsxFJA46gIn27Pr1LAJxWRBct1Ffb2O8qV4NkVoVpIjBLpdgyl03s29KWtiLm8LUkkKq/73WJMsBbS11X6U+Csihv9B/JEfsJ8BLfYTb6Cizehwcx+zuVcPsinFg4o8u%3D%2Cundefined%22%7D%5D'},
        #     {'domain': '.lagou.com', 'expiry': 1614523303, 'httpOnly': False, 'name': '_gid', 'path': '/',
        #      'secure': False, 'value': 'GA1.2.2047767104.1614428060'},
        #     {'domain': '.lagou.com', 'expiry': 1645972903, 'httpOnly': False,
        #      'name': 'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6', 'path': '/', 'secure': False, 'value': '1613495062'},
        #     {'domain': '.lagou.com', 'expiry': 1677508903, 'httpOnly': False, 'name': '_ga', 'path': '/',
        #      'secure': False, 'value': 'GA1.2.1062150530.1605287704'},
        #     {'domain': '.lagou.com', 'expiry': 1614518344.610313, 'httpOnly': False, 'name': 'kw_login_authToken',
        #      'path': '/', 'secure': True,
        #      'value': '"b0l0LrCqbaP6uluvSjq6ZmXfwbJaGyvIqrL1Zjs8Rzk9FEgMSZ3HOG1HLwftl2zRtOmayXctRUDK7OXeG5GH5x08I9/q/lui1aQ2gk1hQzQjgnkKDd6fkb6s3PIHka8EZ1oBja2er5cXdwQNDBvF9TmoZ0MJ0/U8L8BMorU1ot54rucJXOpldXhUiavxhcCELWDotJ+bmNVwmAvQCptcy5e7czUcjiQC32Lco44BMYXrQ+AIOfEccJKHpj0vJ+ngq/27aqj1hWq8tEPFFjdnxMSfKgAnjbIEAX3F9CIW8BSiMHYmPBt7FDDY0CCVFICHr2dp5gQVGvhfbqg7VzvNsw=="'},
        #     {'domain': '.lagou.com', 'expiry': 1920647704.183147, 'httpOnly': False, 'name': 'LGUID', 'path': '/',
        #      'secure': False, 'value': '20201114011504-352a7757-fb50-4c41-8429-96718dc64d3b'},
        #     {'domain': '.lagou.com', 'expiry': 1920647704.182955, 'httpOnly': False, 'name': 'user_trace_token',
        #      'path': '/', 'secure': False, 'value': '20201114011504-ede26af9-5046-4aed-80fe-f171508098a1'},
        #     {'domain': '.lagou.com', 'expiry': 1615032933, 'httpOnly': False, 'name': 'user-finger', 'path': '/',
        #      'secure': False, 'value': 'd0a979be7250f628a919be5a220f376c'},
        #     {'domain': '.lagou.com', 'expiry': 3761920603.40433, 'httpOnly': False, 'name': 'LG_HAS_LOGIN', 'path': '/',
        #      'secure': False, 'value': '1'},
        #     {'domain': '.lagou.com', 'expiry': 1676724569, 'httpOnly': False, 'name': 'smidV2', 'path': '/',
        #      'secure': False, 'value': '2020110121050625e861f0a7749183aaf93fad6f42aa9300080bdd0bc721a10'},
        #     {'domain': 'kaiwu.lagou.com', 'expiry': 1667308966, 'httpOnly': False, 'name': 'p_h5_u',
        #      'path': '/xunlianying', 'secure': False, 'value': '2C8B0427-9604-4E47-84EB-10F1C9A8E31F'}]
        #shelve模块，python自带的对象持久化存储。相当于小型数据库，直接使用不需要安装，直接可以导入。
        # db = shelve.open('cookies')   #打开shelve，并创建一个cookies.db文件。
        # db['cookie'] = cookies    #将变量cookies存入到db['cookie']中。
        # db.close()    #使用完成之后需要关闭shevle。

        #从shelve中取'cookie'的值
        db = shelve.open('cookies') #打开shelve，并创建一个cookies.db文件。
        cookies = db['cookie']  #取出库中'cookie'的值，赋给cookies变量。
        db.close()  #使用完成之后需要关闭shevle。

        for cookie in cookies:
            #如果cookie的'expiry'是小数的话，add_cookie(cookie)方法会报错。这个'expiry'也没有用就索性删掉
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        # self.driver.refresh()

        self.driver.find_element_by_css_selector('.index_service_cnt_itemWrap:nth-child(2)').click()
        # self.driver.find_element_by_css_selector('.import_settingStage_upload_inputWrap').click()
        self.driver.find_element_by_css_selector('.import_settingStage_upload_inputWrap').send_keys("/Users/lihui/Downloads/index.xlsx")