import time
from selenium import webdriver


from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains





# 启动Chrome浏览器
driver = webdriver.Chrome()
# 设置浏览器窗口大小
driver.set_window_size(480, 800)
# 窗口最大化
driver.maximize_window()
# 打开百度
driver.get('http://www.baidu.com')

#清除输入框已经存在的老数据
#driver.find_element_by_id('kw').clear()
driver.find_element(By.ID, 'kw').clear()

# 在搜索输入框中输入‘selenium’
#driver.find_element_by_id('kw').send_keys('apple')
driver.find_element(By.ID, 'kw').send_keys('搜索')
driver.save_screenshot("pic_name.png")




#Click方法只适用于button,而submit可以用于提交表单
# 提交表单
#driver.find_element_by_id('su').submit()
# 单击搜索按钮
driver.find_element(By.ID, 'su').click()

# 等待3秒
time.sleep(3)
driver.quit()
