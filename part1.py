from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

browser = webdriver.Chrome(executable_path="D:/file/各种文件/chromedriver_win32/chromedriver.exe")

# 打开Google网页
browser.get("https://www.google.com/imghp?hl=zh-CN&tab=ri&ogbl")

upload=browser.find_element_by_id("awyMjb")
time.sleep(12)
#本地上传
upload.send_keys("C:/Users/ZhangLijun/Pictures/Camera Roll/cat.jpg")




