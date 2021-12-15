#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project : 
@File : 
@Author : zhuchunmei
@Date : 2021/9/30 20:57
'''
import pytest


def add(x, y):
    # print("开始执行 add 函数")
    return x + y

def test_add():
    print("开始执行 test_add 函数")
    assert add(1, 10) == 11
    assert add(1, 1) == 2
    assert add(1, 99) == 100

class TestClass:
    def test_one(self):
        print("开始执行 test_one 方法")
        x = "this"
        assert "h" in x

    @pytest.mark.hello
    def test_two(self):
        print("开始执行 test_two 方法")
        x = "hello"
        assert hasattr(x, "check")

    @pytest.mark.hello
    def test_three(self):
        print("开始执行 test_three 方法")
        x = "hello"
        assert hasattr(x, "check")