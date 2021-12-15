#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project : 
@File : 
@Author : zhuchunmei
@Date : 2021/10/19 23:38
'''
from selenium import webdriver
from selenium.webdriver.common.by import By



class TestWework:
    def setup(self):
        # 浏览器复用
        options = webdriver.ChromeOptions()     # 初始化一个ChromeOptions实例
        options.debugger_address = "127.0.0.1:9222"     # 指定调试模式地址  Windows/Linux浏览器启动命令为：chrome --remote-debugging-port=9222 (9222为端口号，可以换成任意一个没有被占用的端口)
        self.driver = webdriver.Chrome(options=options)     #给Chrome传递一个ChromeOptions实例
        self.driver.implicitly_wait(2)

    def test_upload(self):
        element_add = self.driver.find_element(By.CSS_SELECTOR,".js_upload_file_selector")
        self.driver.execute_script("argument[0].click();", element_add)









