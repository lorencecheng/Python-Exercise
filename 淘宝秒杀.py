# encoding:utf-8

import time
from selenium import webdriver
import datetime
import sys
class Spider:
    def __init__(self, url):
        self.__base_url = url
        self.__headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
        }
    def get_url(self):
        global driver
        driver.get(self.__base_url)
    def login(self):
        global driver
        if driver.find_element_by_link_text("亲，请登录"):
            driver.find_element_by_link_text("亲，请登录").click()
            print(u"请在30秒内扫描登陆")
            time.sleep(30)
            driver.get("https://cart.taobao.com/cart.htm")
    def selectAll(self,method):
        global driver
        # 打开购物车列表页面
        driver.get("https://cart.taobao.com/cart.htm")
        time.sleep(3)

        # 是否全选购物车
        if method == 0:
            while True:
                try:
                    if driver.find_element_by_id("J_SelectAll1"):
                        driver.find_element_by_id("J_SelectAll1").click()
                        break
                except:
                    # print(f"找不到购买按钮")
                    pass
        if method ==1 :
            print(u"请手动勾选需要购买的商品")
            time.sleep(30)

    def buy(self,times):
        global driver
        while True:
            now = datetime.datetime.now()
            # 对比时间，时间到的话就点击结算
            if now > times:
                # 点击结算按钮
                while True:
                    try:
                        if driver.find_element_by_link_text("结 算"):
                            driver.find_element_by_link_text("结 算").click()
                            print(u"结算成功，准备提交订单")
                            break
                    except:
                        pass
                # 点击提交订单按钮
                while True:
                    try:
                        if driver.find_element_by_link_text('提交订单'):
                            driver.find_element_by_link_text('提交订单').click()
                            print(u"抢购成功，请尽快付款")
                    except:
                        # print(f"再次尝试提交订单")
                        pass
                time.sleep(0.01)

print(u" 按格式 年,月,日,小时,分钟")
print(u"例如输入2020,2,2,21,00。这就代表是2020年2月2日晚上21点整开始抢拍")
t=input(u"请输入预定抢拍时间: ")

option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')
driver = webdriver.Chrome(chrome_options=option)
spider = Spider("https://www.taobao.com")
spider.get_url()
spider.login()
#设置0为全选、1为手动
spider.selectAll(0)
# 设置抢购时间

set_time=datetime.datetime(t)
#set_time = datetime.datetime(2020,2,2,21,47)
spider.buy(set_time)
