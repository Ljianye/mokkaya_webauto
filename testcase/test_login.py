import pytest
import yaml

from Page.loginpage import LoginPage


class TestLogin():
    loginpage:LoginPage=None
    def setupclass(self):
        #初始化登录页面
       loginpage=LoginPage()

    @pytest.mark.parametrize("name,pwd", yaml.safe_load(open("../Data/logindata.yml", "r")))
    def test_login(self,name,pwd):
        loginpage = LoginPage()
        loginpage.open("https://test.admin.mokkaya.com/")
        loginpage.inputname("邮箱", name)
        loginpage.inputpwd("密码", pwd)
        loginpage.clicklogin("登录")