import pytest
import yaml
import time

from selenium import  webdriver

from Base.apply_page import ApplyPage
from Base.base_page import BasePage
driver=webdriver.Chrome()

class TestCase():
    applyPage: ApplyPage = None
    def setup_class(self):
      self.applyPage=ApplyPage()
      self.driver=webdriver.Chrome()

    def teardown_class(self):
       time.sleep(5000)
       self.driver.quit()
    @pytest.mark.parametrize("name,pwd",yaml.safe_load(open("./data/logindata.yml","r")))
    def test_three(self, name, pwd):
        self.applyPage.toPage(self.driver,"https://test.admin.mokkaya.com/")
        self.applyPage.sendText(self.driver,"邮箱",name)
        self.applyPage.sendText(self.driver,"密码",pwd)
        self.applyPage.click(self.driver,"登录")
        try:
            self.driver.find_element_by_xpath("/html/body/section/div/ul/li[1]/div/span")
        except:
            print("没有到下一个页面")


