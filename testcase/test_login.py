import pytest
from Page.loginpage import LoginPage
from Tool.getyaml import GetYaml


class TestLogin():
    def setup_class(self):
        # 第一次实例化
        self.loginpage = LoginPage()
    def teardown(self):
        self.loginpage.driver.quit()


    @pytest.mark.parametrize("data",GetYaml("../Data/logindata.yml").get_data("success"))
    def test_login(self,data):
        name=data["name"]
        pwd=data["pwd"]
        self.loginpage.open("https://test.admin.mokkaya.com/#/login")
        self.loginpage.login(name,pwd)


