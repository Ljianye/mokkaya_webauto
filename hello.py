from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://test.admin.mokkaya.com/")


driver.find_element_by_id("login").click()

