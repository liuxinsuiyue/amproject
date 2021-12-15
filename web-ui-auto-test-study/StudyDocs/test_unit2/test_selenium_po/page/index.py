#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project : 
@File : 
@Author : zhuchunmei
@Date : 2021/10/16 7:50
'''
from selenium.webdriver.common.by import By

from test_selenium_po.page.base_page import BasePage
from test_selenium_po.page.login import Login
from test_selenium_po.page.register import Register


class Index(BasePage):
    _base_url = "https://work.weixin.qq.com/"
    # 进入注册页面
    def goto_register(self):
        self._driver.find_element(By.LINK_TEXT, "立即注册").click()
        # 创建Register实例后，可调用Register中的方法
        return Register(self._driver)
    # 进入登录页面
    def goto_login(self):
        self._driver.find_element(By.LINK_TEXT, "企业登录").click()
        # 创建Login实例后，可调用Login中的方法
        return Login(self._driver)