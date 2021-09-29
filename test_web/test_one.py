from selenium import  webdriver

driver=webdriver.Chrome()
driver.get("https://test.admin.mokkaya.com")
driver.find_element_by_xpath("//input[@type='text']").send_keys("aaaaaaa")
driver.find_element_by_xpath("//input[@type='password']").send_keys("bbbb")
driver.find_element_by_xpath("//span[text()='Go!']").click()
