from  selenium import webdriver
import time

from Base.apply_page import ApplyPage


class LoginPage(ApplyPage):
    driver : webdriver =None
    def __init__(self):
        self.driver = webdriver.Chrome()
    def open(self,url):
        self.driver.get(url)
    #输入用户名
    def inputname(self,keyname,text):
        self.sendText(self.driver,keyname,text)
    #输入密码
    def inputpwd(self,keyname,text):
        self.sendText(self.driver,keyname,text)
      # 点击登录
    def clicklogin(self,keyname):
        self.click(self.driver,keyname)

