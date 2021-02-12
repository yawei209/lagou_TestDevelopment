# -*- coding: utf-8 -*-
# @Time : 2021/2/12 22:02
# @Author : zhangyawei
# @Email : zhangyawei209@163.com
# @File : test_a.py.py
# @Software: PyCharm
import pytest


def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 5

def test_answer1():
    assert inc(4) == 5

class TestDemo:
    def test_a(self):
        print("a")
    def test_b(self):
        print('b')
    def c(self):
        print('c')
#作为入口函数，python 文件名运行
if __name__ == '__main__':
    # pytest.main(['test_a.py']) #pytest.main() 运行文件中所有已“test_”的用例
    pytest.main(["test_a.py::TestDemo", '-v'])    #pytest.main() 指定“文件::类”, -v 指定详细日志。