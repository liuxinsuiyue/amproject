#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project : 
@File : 
@Author : zhuchunmei
@Date : 2021/10/10 12:23
'''
import allure
import pytest
import yaml
from selenium import webdriver
import time

@allure.testcase("http://www.github.com")
@allure.severity(allure.severity_level.NORMAL)
@allure.feature("百度搜索")
@allure.story('百度搜索story')
@allure.title('百度搜索title')
@allure.description("百度搜索description")
@pytest.mark.parametrize('test_data1', yaml.safe_load(open("data/data.yml")))
def test_steps_demo(test_data1):
    with allure.step("打开百度网页"):
        driver = webdriver.Chrome()
        driver.get("http://www.baidu.com")
        driver.maximize_window()

    with allure.step(f"输入搜索词：{test_data1}"):
        driver.find_element_by_id("kw").send_keys(test_data1)
        time.sleep(2)
        driver.find_element_by_id("su").click()
        time.sleep(2)

    with allure.step("保存图片"):
        driver.save_screenshot("./result/b.png")
        allure.attach.file("./result/b.png", attachment_type=allure.attachment_type.PNG)
    with allure.step("关闭浏览器"):
        driver.quit()