import yaml

from Tool.getyaml import GetYaml
from selenium import  webdriver

def read():
    get=GetYaml("Data\\logindata.yml").get_data("正确数据")
    print(get)
    print(type(get))
    return get


read()