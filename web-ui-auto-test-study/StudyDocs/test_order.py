#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project : 
@File : 
@Author : zhuchunmei
@Date : 2021/9/30 23:18
'''
import pytest

class TestPytest(object):

    @pytest.mark.run(order=-3)
    def test_one(self):
        print("执行 test_one 方法")

    @pytest.mark.run(order=1)
    def test_two(self):
        print("开始执行 test_two 方法")

    @pytest.mark.run(order=3)
    def test_three(self):
        print("开始执行 test_three 方法")

    @pytest.mark.run(order=-1)
    def test_four(self):
        print("开始执行 test_four 方法")

