#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project : 
@File : 
@Author : zhuchunmei
@Date : 2021/10/1 0:52
'''
import pytest


@pytest.fixture(scope="session")
def open():
    print("打开浏览器")
    yield

    print("执行teardown")
    print("最后关闭浏览器")

