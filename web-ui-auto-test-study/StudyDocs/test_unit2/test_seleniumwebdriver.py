# 导入selenium包
import time

from selenium import webdriver

# Chrome()会从环境变量中寻找浏览器驱动
driver = webdriver.Chrome() #创建一个Chromedriver的实例，这段代码会自动化的创建一个Chrome进程，除了可以打开Chrome浏览器，还可以打开IE/Firefox浏览器，前提是要将对应的driver配置到环境变量中
# driver = webdriver.Ie() #创建一个Iedriver的实例
# driver = webdriver.Firefox() #创建一个geckodriver的实例

driver.get('https://www.baidu.com')  # 测试的步骤
search = driver.find_element_by_id('su').get_attribute('value')  # "百度一下"按钮
assert search == "百度"  # 断言预期结果 失败  "百度" "百度一下"
time.sleep(3)
driver.quit()
