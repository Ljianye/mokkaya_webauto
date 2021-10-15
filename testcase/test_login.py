import pytest
import yaml
import time
from Page.loginpage import LoginPage
from Tool.getyaml import GetYaml


class TestLogin():
    def setup_class(self):
        # 第一次实例化
        self.loginpage = LoginPage()

    @pytest.mark.parametrize("data",GetYaml("../Data/logindata.yml").get_data("正确数据"))
    def test_login(self,data:dict):
        #self.loginpage.open("https://test.admin.mokkaya.com/#/login")
        print(data)
        print(type(data))
        # self.loginpage.inputname("邮箱",data["name"])
        # self.loginpage.inputpwd("密码", data["pwd"])
        # self.loginpage.clicklogin("登录")

