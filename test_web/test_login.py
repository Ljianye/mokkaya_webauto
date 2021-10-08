import pytest
import yaml

from selenium import  webdriver

from Base.base_page import BasePage


class TestCase(BasePage):
    def setup_class(self):
      self.driver=webdriver.Chrome()

    def teardown_class(self):
       self.driver.quit()
    @pytest.mark.parametrize("name,pwd",yaml.safe_load(open("./data/logindata.yml","r")))
    def test_three(self, name, pwd):
        self.open("https://test.admin.mokkaya.com/")
        self.findElement("xpath","//input[@type='text']")
        self.findElement("xpath","//input[@type='password']")
        self.driver.find_element_by_xpath("//input[@type='text']").send_keys(name)
        self.driver.find_element_by_xpath("//input[@type='password']").send_keys(pwd)
        self.driver.find_element_by_xpath("//span[text()='Go!']").click()
        try:
            self.driver.find_element_by_xpath("/html/body/section/div/ul/li[1]/div/span")

        except:
            print("没有到下一个页面")


