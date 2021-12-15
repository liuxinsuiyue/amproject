#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project : 
@File : 
@Author : zhuchunmei
@Date : 2021/10/16 7:51
'''
from selenium.webdriver.common.by import By
from test_selenium_po.page.base_page import BasePage
from test_selenium_po.page.register import Register

class Login(BasePage):
    # 扫描二维码
    def scan_qrcode(self):
        pass
    # 进入注册页面
    def goto_registry(self):
        self._driver.find_element(By.LINK_TEXT, "企业注册").click()
        return Register(self._driver)