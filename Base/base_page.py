import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    # 获取元素
    def findElement(self, driver: WebDriver, by_type: str, by_value) -> WebElement:
        by_type = by_type.lower()
        tep_by = None
        if by_type == "id":
            tep_by = By.ID
        elif by_type == "name":
            tep_by = By.NAME
        elif by_type == "class":
            tep_by = By.CLASS_NAME
        elif by_type == "tag":
            tep_by = By.TAG_NAME
        elif by_type == "link":
            tep_by = By.LINK_TEXT
        elif by_type == "partial_link":
            tep_by = By.PARTIAL_LINK_TEXT
        elif by_type == "xpath":
            tep_by = By.XPATH
        elif by_type == "css":
            tep_by = By.CSS_SELECTOR
        try:
            # 显示获取等待获取元素lambda dr: dr.find_element(tep_by, by_value)
            return WebDriverWait(driver, 30000, 1).until(expected_conditions.element_to_be_clickable((tep_by, by_value)))
        except Exception:
            return None
