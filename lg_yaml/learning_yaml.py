# -*- coding: utf-8 -*-
# @Time : 2021/2/15 13:52
# @Author : zhangyawei
# @Email : zhangyawei209@163.com
# @File : learning_yaml.py
# @Software: PyCharm


import yaml

file = r"D:\my_workspace\testpy\lg_yaml\env.yml"
# file = "D:\\my_workspace\\testpy\\lg_yaml\\env.yml"

print(yaml.safe_load(open(file)))
