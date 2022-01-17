import time

import yaml
from selenium import webdriver


class TestWework:
  # 复用浏览器
  def test_demo(self):
    opt = webdriver.ChromeOptions()
    # 设置debug地址

    driver = webdriver.Chrome()

    driver.get("https://test.admin.mokkaya.com/#/login")
    # driver.find_element_by_xpath("//*[@id='pane-0']/form/div[15]/div/button[2]v").click()
    # cookies=driver.get_cookies()
    # with open("ckk.yml","w",encoding="utf-8") as ck:
    #       for c in cookies:
    #           yaml.dump(c)



# 使用cookie登录
def test_cookie():
  driver = webdriver.Chrome()
  driver.implicitly_wait(5)
  driver.get("https://test.admin.mokkaya.com/")
  cookies=yaml.safe_load(open("ckk.yml"))
  for cookie in cookies:
    driver.add_cookie(cookie)
  driver.get("https://test.admin.mokkaya.com/#/orders/list")
  driver.find_element_by_id("menu_contacts").click()
  time.sleep(5)
  driver.quit()

# 获取cookie，序列化后存入yaml文件内
def test_get_cookie():
  opt = webdriver.ChromeOptions()
  # 设置debug地址
  opt.debugger_address = "127.0.0.1:9222"
  driver = webdriver.Chrome(options=opt)
  driver.implicitly_wait(5)
  driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
  cookie = driver.get_cookies()
  print(cookie)
  with open("data.yaml","w",encoding="UTF-8") as f:
    yaml.dump(cookie,f)

# 使用序列化cookie的方法进行登录
def test_login():
  driver = webdriver.Chrome()
  driver.implicitly_wait(5)
  driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
  with open("data.yaml",encoding="UTF-8") as f:
    yaml_data = yaml.safe_load(f)
    for cookie in yaml_data:
      driver.add_cookie(cookie)
  driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
  time.sleep(10)