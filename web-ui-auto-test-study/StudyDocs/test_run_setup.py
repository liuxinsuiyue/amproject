#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project : 
@File : 
@Author : zhuchunmei
@Date : 2021/9/30 22:29
'''
import pytest

def setup_module():
    print("\nsetup_module，只执行一次，当有多个测试类的时候使用")

def teardown_module():
    print("\nteardown_module，只执行一次，当有多个测试类的时候使用")

def setup_function():
    print("\nsetup_function")

def teardown_function():
    print("\nteardown_function")

def add(x, y):
    # print("开始执行 add 函数")
    return x + y

def test_add_1():
    print("开始执行 test_add_1 函数")
    assert add(1, 10) == 11
    assert add(1, 1) == 2
    assert add(1, 99) == 100

def test_add_2():
    print("开始执行 test_add_2 函数")
    assert add(1, 10) == 11
    assert add(1, 1) == 2
    assert add(1, 99) == 100

class TestClass1:

    @classmethod
    def setup_class(cls):
        print("\nsetup_class1，只执行一次")

    @classmethod
    def teardown_class(cls):
        print("\nteardown_class1，只执行一次")

    def setup_method(self):
        print("\nsetup_method1，每个测试方法都执行一次")

    def teardown_method(self):
        print("\nteardown_method1，每个测试方法都执行一次")

    def setup(self):
        print("\nsetup1")

    def teardown(self):
        print("\nteardown1")

    def test_one(self):
        print("执行 test_one 方法")

    def test_two(self):
        print("开始执行 test_two 方法")

    def test_three(self):
        print("开始执行 test_three 方法")

class TestClass2:

    @classmethod
    def setup_class(cls):
        print("\nsetup_class2，只执行一次")

    @classmethod
    def teardown_class(cls):
        print("\nteardown_class2，只执行一次")

    def setup_method(self):
        print("\nsetup_method2，每个测试方法都执行一次")

    def teardown_method(self):
        print("\nteardown_method2，每个测试方法都执行一次")

    def setup(self):
        print("\nsetup2")

    def teardown(self):
        print("\nteardown2")

    def test_one(self):
        print("开始执行 test_one 方法")

    def test_two(self):
        print("开始执行 test_two 方法")

    def test_three(self):
        print("开始执行 test_three 方法")