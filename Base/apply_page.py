import json
import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.select import Select

from Base.base_page import BasePage


class ApplyPage(BasePage):
    # 加载页面
    def toPage(self, driver: WebDriver, url):
        driver.get(url)
        # 输入文本

    # 输入文本
    def sendText(self, driver: WebDriver, keyName, text):
        # 通过keyName从json文件中获取对应的元素定位方式和值
        by_ditc = getJsonData(keyName)
        by_type = by_ditc.get("by")
        by_value = by_ditc.get("value")

        self.findElement(driver, by_type, by_value).send_keys(text)

    # 选择选项
    def select(self, driver: WebDriver, keyName, text):
        # 通过keyName从json文件中获取对应的元素定位方式和值
        by_ditc = getJsonData(keyName)
        by_type = by_ditc.get("by")
        by_value = by_ditc.get("value")

        xueli_et = self.findElement(driver, by_type, by_value)
        Select(xueli_et).select_by_value(text)

    # 点击
    def click(self, driver: WebDriver, keyName):
        # 通过keyName从json文件中获取对应的元素定位方式和值
        by_ditc = getJsonData(keyName)
        by_type = by_ditc.get("by")
        by_value = by_ditc.get("value")

        self.findElement(driver, by_type, by_value).click()

    # 获取结果
    def getResult(self, driver):
        # text = driver.switch_to.alert.text
        # driver.switch_to.alert.dismiss()
        alert = self.getAlert(driver, 30)
        text = alert.text
        alert.dismiss()
        return text

    def getAlert(slef, driver: WebDriver, timeout):
        i = 0
        while True:
            if timeout == i:
                return False
            try:
                return driver.switch_to.alert
            except Exception:
                pass
            finally:
                time.sleep(1)


def getJsonData(keyName) -> dict:
    apply_json_path = "D:\\Python_Code\\test_one\\Data\\element.json"
    with open(apply_json_path, mode="r", encoding="utf-8") as f:
        jsonStr = f.read()
        json_dict = json.loads(jsonStr)
        print(type(json_dict))
        print(json_dict)
    return json_dict.get(keyName)

# if __name__ == '__main__':
#     getJsonData()
