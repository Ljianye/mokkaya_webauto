import pytest
import yaml
import time
from Page.loginpage import LoginPage
from Tool.getyaml import GetYaml


class TestLogin():
    def setup_class(self):
        # 第一次实例化
        self.loginpage = LoginPage()

    @pytest.mark.parametrize("data",GetYaml("../Data/logindata.yml").get_data("success"))
    def test_login(self,data):
        name=data["name"]
        pwd=data["pwd"]
        self.loginpage.open("https://test.admin.mokkaya.com/#/login")
        self.loginpage.login(name,pwd)


    @pytest.mark.parametrize("data", GetYaml("../Data/logindata.yml").get_data("faile"))
    def test_filelogin(self, data):
        name = data["name"]
        pwd = data["pwd"]
        self.loginpage.open("https://test.admin.mokkaya.com/#/login")
        self.loginpage.inputname("邮箱", name)
        self.loginpage.inputpwd("密码", pwd)
        self.loginpage.clicklogin("登录")