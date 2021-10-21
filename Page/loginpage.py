from  selenium import webdriver
import time

from Base.apply_page import ApplyPage


class LoginPage(ApplyPage):
    driver : webdriver =None
    def __init__(self):
        self.driver = webdriver.Chrome()
    def open(self,url):
        self.driver.get(url)

    def login(self,name,pwd):
        self.sendText(self.driver, "邮箱", name)
        self.sendText(self.driver, "密码", pwd)
        self.click(self.driver,"登录")

