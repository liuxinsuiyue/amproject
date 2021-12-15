#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project : 
@File : 
@Author : zhuchunmei
@Date : 2021/10/16 10:27
'''

#导入依赖
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

"""
但是有些时候的场景
expected_conditions
库并不能很好的解决，这个时候就需要通过自己写方法来满足特定场景。
假设：要判断某个元素超过指定的个数，就可以执行下面的操作。
示例：
"""


def ceshiren():
    # 定义一个方法
    def wait_ele_for(driver):
        # 将找到的元素个数赋值给 eles
        eles = driver.find_elements(By.XPATH, '//*[@id="site-text-logo"]')
        # 放回结果
        return len(eles) > 0

    driver = webdriver.Chrome()
    driver.get('https://ceshiren.com')
    # 显示等待10秒，直达 wait_ele_for 方法返回 true
    WebDriverWait(driver, 10).until(wait_ele_for)

class TestHogwarts():
    def setup(self):
        self.driver = webdriver.Chrome()
        # self.driver.get('https://ceshiren.com/') 谷歌上打不开，所以改用百度网
        self.driver.get('https://www.baidu.com/')
        #加入隐式等待
        self.driver.implicitly_wait(5)

    def teardown(self):
        #强制等待
        time.sleep(10)
        self.driver.quit()

    def test_hogwarts(self):
        #元素定位，这里的category_name是一个元组。
        # category_name = (By.LINK_TEXT, "开源项目")
        category_name = (By.LINK_TEXT, "贴吧")
        # 加入显式等待
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(category_name))
        # 点击开源项目
        """
        这里的*category_name是为了将category_name元组拆开
        因为find_element需要传递两个参数，所以要将category_name拆成两个参数
        """
        self.driver.find_element(*category_name).click()

