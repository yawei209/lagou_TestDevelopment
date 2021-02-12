# -*- coding: utf-8 -*-
# @Time : 2021/2/12 0:53
# @Author : zhangyawei
# @Email : zhangyawei209@163.com
# @File : test_unittest.py
# @Software: PyCharm


import unittest


class TestDemo(unittest.TestCase):

    #setUp和 tearDown方法是在每条测试用例前后分别调用的
    def setUp(self):
        print("setup")

    def tearDown(self):
        print("teardown\n")
    @classmethod
    def setUpClass(cls) -> None:
        print("set up class")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tear down class")

    def test_abc(self):
        print("test abc")

    def test_upper(self):
        print("test_upper")
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        print("test_isupper")
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        print('test_split')
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    #f方法一：unitest.main() 执行所有测试用例（test_开头的）
    # unittest.main()

    #方法二：创建一个《测试套件》，testsuite,只执行添加的一条用例、或几条。
    suite = unittest.TestSuite()
    suite.addTest(TestDemo("test_abc"))      #addTest(类名("用例名"))
    unittest.TextTestRunner().run(suite)    #然后运行测试套件

    #测试三：执行某个测试类