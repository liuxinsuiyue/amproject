# 导入selenium包
import logging
import os
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

"""
定位元素常用方法,脚本不能运行
"""
def test_find_element():
    driver = webdriver.Chrome()
    driver.find_element_by_id('site-logo')
    driver.find_element_by_name('wd')

    driver.find_element_by_xpath("//form[@id='form']/./..span[@class='bg s_ipt_wr new-pmd quickdelete-wrap']/input")
    driver.find_element_by_xpath("//form[@id='form']//input[@id='kw']")
    driver.find_element_by_xpath("//div[(@class,top)= and contains(text(),)='']")
    driver.find_element_by_css_selector('.active>a')

    driver.find_element_by_link_text('欢迎光临霍格沃兹测试学院')
    driver.find_element_by_partial_link_text('霍格沃兹测试学院')

    driver.find_element_by_tag_name('input')

    driver.find_element_by_class_name('active')
"""
常见操作,脚本不能运行
"""
def test_do_element():
    driver = webdriver.Chrome()
    # 输入、点击、清除
    driver.find_element_by_name('wd').send_keys('霍格沃兹测试学院')
    driver.find_element_by_id('su').click()
    driver.find_element_by_name('wd').clear()
    # 关闭当前窗口
    driver.close()
    # 关闭浏览器
    driver.quit()

    search = driver.find_element_by_id('su')
    logging.basicConfig(level=logging.INFO)
    # 获取search的value属性值并打印
    logging.info(search.get_attribute('value'))
    # 打印search的位置坐标
    logging.info(search.location)
    # 打印search的元素大小
    logging.info(search.size)

    # 刷新页面
    driver.refresh()
    logging.basicConfig(level=logging.INFO)
    # 打印当前页面的源代码
    logging.info(driver.page_source)
"""
键盘鼠标操作（ActionChains）,脚本不能运行
click(on_element=None) ——单击鼠标左键
click_and_hold(on_element=None) ——点击鼠标左键，不松开
context_click(on_element=None) ——点击鼠标右键
double_click(on_element=None) ——双击鼠标左键
drag_and_drop(source, target) ——拖拽到某个元素然后松开
drag_and_drop_by_offset(source, xoffset, yoffset) ——拖拽到某个坐标然后松开
key_down(value, element=None) ——按下某个键盘上的键
key_up(value, element=None) ——松开某个键
move_by_offset(xoffset, yoffset) ——鼠标从当前位置移动到某个坐标
move_to_element(to_element) ——鼠标移动到某个元素
move_to_element_with_offset(to_element, xoffset, yoffset) ——移动到距某个元素（左上角坐标）多少距离的位置
perform() ——执行链中的所有动作
release(on_element=None) ——在某个元素位置松开鼠标左键
send_keys(*keys_to_send) ——发送某个键到当前焦点的元素
send_keys_to_element(element, *keys_to_send) ——发送某个键到指定元素
"""
def test_action_chains_键盘():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get('http://sahitest.com/demo/clicks.htm')

    click_btn = driver.find_element_by_xpath('//input[@value="click me"]')  # 单击按钮
    doubleclick_btn = driver.find_element_by_xpath('//input[@value="dbl click me"]')  # 双击按钮
    rightclick_btn = driver.find_element_by_xpath('//input[@value="right click me"]')  # 右键单击按钮

    ActionChains(driver).click(click_btn).double_click(doubleclick_btn).context_click(rightclick_btn).perform()  # 链式用法
    print(driver.find_element_by_name('t2').get_attribute('value'))
    time.sleep(2)
    driver.quit()
def test_action_chains_鼠标():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get('http://sahitest.com/demo/mouseover.htm')

    write = driver.find_element_by_xpath('//input[@value="Write on hover"]')  # 鼠标移动到此元素，在下面的input框中会显示“Mouse moved”
    blank = driver.find_element_by_xpath('//input[@value="Blank on hover"]')  # 鼠标移动到此元素，会清空下面input框中的内容

    result = driver.find_element_by_name('t1')

    action = ActionChains(driver)
    action.move_to_element(write).perform()  # 移动到write元素，显示“Mouse moved”

    print(result.get_attribute('value'))

    # action.move_to_element(blank).perform()
    action.move_by_offset(10, 50).perform()  # 移动到距离当前位置(10,50)的点，与上句效果相同，移动到blank上，清空
    print(result.get_attribute('value'))

    action.move_to_element_with_offset(blank, 10, -40).perform()  # 移动到距离blank元素(10,-40)的点，可移动到write上
    print(result.get_attribute('value'))

    time.sleep(2)
    driver.quit()

def test_action_chains_拖拽():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get('http://sahitest.com/demo/dragDropMooTools.htm')

    dragger = driver.find_element_by_id('dragger')  # 被拖拽元素
    item1 = driver.find_element_by_xpath('//div[text()="Item 1"]')  # 目标元素1
    item2 = driver.find_element_by_xpath('//div[text()="Item 2"]')  # 目标2
    item3 = driver.find_element_by_xpath('//div[text()="Item 3"]')  # 目标3
    item4 = driver.find_element_by_xpath('//div[text()="Item 4"]')  # 目标4

    action = ActionChains(driver)
    action.drag_and_drop(dragger, item1).perform()  # 1.移动dragger到目标1
    time.sleep(2)
    action.click_and_hold(dragger).release(item2).perform()  # 2.效果与上句相同，也能起到移动效果
    time.sleep(2)
    action.click_and_hold(dragger).move_to_element(item3).release().perform()  # 3.效果与上两句相同，也能起到移动的效果
    time.sleep(2)
    # action.drag_and_drop_by_offset(dragger, 400, 150).perform()  # 4.移动到指定坐标
    action.click_and_hold(dragger).move_by_offset(400, 150).release().perform()  # 5.与上一句相同，移动到指定坐标
    time.sleep(2)
    driver.quit()

def test_action_chains_按键1():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get('http://sahitest.com/demo/keypress.htm')

    key_up_radio = driver.find_element_by_id('r1')  # 监测按键升起
    key_down_radio = driver.find_element_by_id('r2')  # 监测按键按下
    key_press_radio = driver.find_element_by_id('r3')  # 监测按键按下升起

    enter = driver.find_elements_by_xpath('//form[@name="f1"]/input')[1]  # 输入框
    result = driver.find_elements_by_xpath('//form[@name="f1"]/input')[0]  # 监测结果

    # 监测key_down
    key_down_radio.click()
    ActionChains(driver).key_down(Keys.CONTROL, enter).key_up(Keys.CONTROL).perform()

    print(result.get_attribute('value'))

    # 监测key_up
    key_up_radio.click()
    enter.click()
    ActionChains(driver).key_down(Keys.SHIFT).key_up(Keys.SHIFT).perform()

    print(result.get_attribute('value'))

    # 监测key_press
    key_press_radio.click()
    enter.click()
    ActionChains(driver).send_keys('a').perform()
    print(result.get_attribute('value'))
    driver.quit()

def test_action_chains_按键2():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get('http://sahitest.com/demo/label.htm')

    input1 = driver.find_elements_by_tag_name('input')[3]
    input2 = driver.find_elements_by_tag_name('input')[4]

    action = ActionChains(driver)
    input1.click()
    action.send_keys('Test Keys').perform()
    action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()  # ctrl+a
    action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()  # ctrl+c

    action.key_down(Keys.CONTROL, input2).send_keys('v').key_up(Keys.CONTROL).perform()  # ctrl+v

    print(input1.get_attribute('value'))
    print(input2.get_attribute('value'))

    driver.quit()








"""
多浏览器兼容测试
运行命令：
set browser=chrome
pytest test_seleniumwebdriver2.py::test_browser
"""
def test_browser():
    browser = os.getenv("browser").lower()
    if browser == "headless":
        driver = webdriver.PhantomJS()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    driver.get('https://www.baidu.com/')


class TestHogwarts:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def teardown_method(self, method):
        self.driver.quit()

    def test_switch_to_window(self):
        time.sleep(5)
        self.driver.get('https://www.baidu.com/')
        self.driver.find_element_by_id('kw').send_keys('霍格沃兹测试学院')
        self.driver.find_element_by_css_selector('.s_btn').click()
        self.driver.find_element_by_link_text('霍格沃兹测试开发_霍格沃兹测试开发腾讯课堂官网').click()
        handles = self.driver.window_handles            # 获取浏览器的handles
        print(handles)
        self.driver.switch_to_window(handles[-1])
        self.driver.find_element_by_partial_link_text('名企定向培养').click()



