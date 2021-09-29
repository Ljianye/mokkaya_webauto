import pytest
from selenium import  webdriver




class TestCase():
    def setup_class(self):
      self.driver=webdriver.Chrome()

    def teardown_class(self):
       self.driver.quit()
    @pytest.mark.parametrize("name,pwd",[("aaaaa","bbbbbbbbb"),("jianye@newsinpalm.com","Baca@123")])
    def test_three(self,name,pwd):
        self.driver.get("https://test.admin.mokkaya.com")#打开浏览器
        self.driver.find_element_by_xpath("//input[@type='text']").send_keys(name)
        self.driver.find_element_by_xpath("//input[@type='password']").send_keys(pwd)
        self.driver.find_element_by_xpath("//span[text()='Go!']").click()
        try:
            self.driver.find_element_by_xpath("/html/body/section/div/ul/li[1]/div/span")
        except:
            print("没有到下一个页面")


    # def setup_method(self):
    #     print("==类里面每个用例执行前都会执行setup_method==")
    #
    # def teardown_method(self):
    #     print("==类里面每个用例结束后都会执行teardown_method==")
    #
    # def setup(self):
    #     print("=类里面每个用例执行前都会执行setup=")
    #
    # def teardown(self):
    #     print("=类里面每个用例结束后都会执行teardown=")

