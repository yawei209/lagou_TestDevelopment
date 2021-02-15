# -*- coding: utf-8 -*-
# @Time : 2021/2/15 13:43
# @Author : zhangyawei
# @Email : zhangyawei209@163.com
# @File : test_demo.py
# @Software: PyCharm

import pytest
import yaml

file = r"D:\my_workspace\testpy\lg_yaml\env.yml"


class TestDemo:
    '''@pytest.mark.parametrize("变量名",“变量值”) 变量值需要的是一个可迭代对象，这里取到的是列表[{'dev': '127.0.0.1'}]，也就是env = {'dev': '127.0.0.1'}'''
    @pytest.mark.parametrize("env", yaml.safe_load(open(file)))
    def test_demo(self, env):
        if "test" in env:
            print("这是测试环境")
            print("测试环境的ip地址是：", env["test"])
        elif "dev" in env:
            print("这是开发环境")
            print("开发环境的ip地址是：", env["dev"])

    @pytest.mark.parametrize("env", yaml.safe_load(open(file)))
    def test_print(self, env):
        print("打印env：",env)
        print(yaml.safe_load(open(file)))
