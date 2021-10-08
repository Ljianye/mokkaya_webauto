import pytest
import yaml
import time

from selenium import  webdriver
from selenium.webdriver.support import expected_conditions


from Base.apply_page import ApplyPage
class TestCase():
    applyPage: ApplyPage = None
    def setup_class(self):
      self.applyPage=ApplyPage()
      self.driver=webdriver.Chrome()

    def teardown_class(self):
       time.sleep(5000)
       self.driver.quit()
    def teardown(self):
        self.driver.quit()
    @pytest.mark.parametrize("name,pwd",yaml.safe_load(open("D:\\Python_Code\\test_one\\test_web\\data\\logindata.yml","r")))
    def test_three(self, name, pwd):
        self.applyPage.toPage(self.driver,"https://test.admin.mokkaya.com/")
        self.applyPage.sendText(self.driver,"邮箱",name)
        self.applyPage.sendText(self.driver,"密码",pwd)
        self.applyPage.click(self.driver,"登录")
        assert expected_conditions.presence_of_element_located("/html/body/section/div/ul/li[1]/div/span")


