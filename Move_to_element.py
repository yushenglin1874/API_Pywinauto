# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
#
# firefox = webdriver.Chrome()
# firefox.get('http://foo.bar')
# element_to_hover_over = firefox.find_element_by_id("baz")
#
# hover = ActionChains(firefox).move_to_element(element_to_hover_over)  # 找到元素
# hover.perform()  # 悬停
# hover = ActionChains(firefox).move_to_element(element_to_hover_over)  # 找到元素

from selenium import webdriver

# 创建 WebDriver 对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome(r'C:\Program Files\Google\Chrome\Application\chromedriver.exe')

# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
# wd.get('https://www.baidu.com')
wd.get("https://10.136.106.42:30090/datamanage/DataManagement/DataMenu/Add")
wd.find_element_by_id("details-button").click()
wd.find_element_by_id("proceed-link").click()