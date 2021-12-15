#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project : 
@File : 
@Author : zhuchunmei
@Date : 2021/10/3 11:40
'''
import pytest
import yaml


"""
代码分析：yaml文件里定义了列表数据
通过open()方法获取data.yaml文件对象
使用yaml.safe_load()加载文件对象，将yaml格式文件转换为python值，列表中的元素分别传到用例中生成多条用例分别执行
"""

@pytest.mark.parametrize("a,b",yaml.safe_load(open("data.yaml",encoding='utf-8')))
def test_foo(a,b):
    print(f"\n a + b = {a + b} ")