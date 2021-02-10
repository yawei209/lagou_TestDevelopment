# -*- coding: utf-8 -*-
# @Time : 2021/2/10 11:30
# @Author : zhangyawei
# @Email : zhangyawei209@163.com
# @File : second.py
# @Software: PyCharm
import random

print("Hello world")

#三木云运算
a = 5
b = 2
print("a 大于 b") if a > b else print("a 不大于 b")

list = [x for x in range(80,101)]
print(f"list is {list}")


#生产随机数的方法（两种）
c = random.choice(list)
print(c)
d = random.randint(80,100)
print(d)