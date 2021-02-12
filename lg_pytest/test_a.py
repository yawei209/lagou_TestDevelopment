# -*- coding: utf-8 -*-
# @Time : 2021/2/12 22:02
# @Author : zhangyawei
# @Email : zhangyawei209@163.com
# @File : test_a.py.py
# @Software: PyCharm
import pytest


def inc(x):
    return x + 1

#pytest的参数化
@pytest.mark.parametrize('a,b',[
    (1,2),
    (10,20),
    ('a','a1'),
    (3,4),
    (5,6)
])

def test_answer(a,b):
    assert inc(a) == b

def test_answer1():
    assert inc(4) == 5

#pytest.fixture() 装饰过的函数，类似unittest中的一个setup，在执行用例之间会先执行login函数
@pytest.fixture()
def login():
    username = "Jerry"
    return username

class TestDemo:
    def test_a(self, login):  #方法中传入login，会先执行login函数
        print(f"a username = {login}")  #这个方法的名字就代表着方法return的值
    def test_b(self):
        print('b')
    def test_c(self, login):  #方法中传入login，会先执行login函数
        print(r'c username = {login}')  #这个方法的名字就代表着方法return的值
#作为入口函数，python 文件名运行
if __name__ == '__main__':
    # pytest.main(['test_a.py']) #pytest.main() 运行文件中所有已“test_”的用例
    pytest.main(["test_a.py::TestDemo", '-v'])    #pytest.main() 指定“文件::类”, -v 指定详细日志。