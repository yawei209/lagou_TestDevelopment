# -*- coding: utf-8 -*-
# @Time : 2021/2/10 11:30
# @Author : zhangyawei
# @Email : zhangyawei209@163.com
# @File : second.py
# @Software: PyCharm
import pytest
from test_pytest.core.calc import Calc
class TestCalc:
    def setup_class(self):
        self.calc = Calc()
    @pytest.mark.parametrize('a, b, c', [
        [1, 2, 2],
        [-1, 1, -1],
        [1, -1, 1]
    ])
    def test_mul(self, a, b, c):
        assert self.calc.mul(a, b) == c