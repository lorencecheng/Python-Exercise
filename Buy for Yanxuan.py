from selenium import webdriver
import time
import random

def newlogin0202():
    options=webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    b=webdriver.Chrome(chrome_options=options)
    b = webdriver.Chrome()
    b.maximize_window()
    b.get("https://you.163.com/")
    ele = b.find_element_by_xpath("//*[@class='j-yx-cp-topLogin']")  #定位注册登录
    ele.click()
    time.sleep(1)
    ele1_1=b.find_element_by_xpath("//*[@id='j-yx-loginFormWrap']/div/div[1]/div[2]/div[3]")  #定位登录框
    ele1_1.click()
    time.sleep(1)
    ele1 = b.find_element_by_xpath("//*[@id='j-yx-mailLoginWrap']/iframe")  #定位邮箱登录
    b.switch_to_frame(ele1)
    time.sleep(1)
    ele2 = b.find_element_by_xpath("//*[@class='j-inputtext dlemail j-nameforslide']")  #定位账户栏
    ele2.send_keys("xxxxxxx")  #输入账户
    ele3 = b.find_element_by_xpath("//*[@class='j-inputtext dlpwd']")  #定位密码栏
    ele3.send_keys("xxxxx")   #输入密码
    time.sleep(1)
    ele4 = b.find_element_by_xpath("//*[@id='dologin']")  #定位登录按钮
    ele4.click() #点击登录
    print("Login Success")
    time.sleep(5)
    ele5 = b.find_element_by_xpath("//*[@class='yx-cp-searchInput']")  #定位主页的搜索栏
    ele5.send_keys("3988533")   #输入已知商品的ID  
    #口罩的ID是3401036，其他商品就要更改上面的ID
    ele6=b.find_element_by_class_name("yx-cp-searchButton")  #定位搜索
    ele6.click() #点击搜索
    time.sleep(1)
    #搜索出商品后，加入购物车
    while True:
        try:
            if b.find_element_by_xpath("//*[@id='j-searchContainer']/div/div/div/div[2]/div[2]/div[1]/ul/li/div/div[2]/div[2]/a"):
                ele7=b.find_element_by_xpath("//*[@id='j-searchContainer']/div/div/div/div[2]/div[2]/div[1]/ul/li/div/div[2]/div[2]/a") #定位搜索结果的加入购物车按钮
                print(ele7)
                time(60)
                ele7.click()  #点击加入购物车
                print("Add to cart")
                ele8=b.find_element_by_xpath("//*[@id='j-yx-cp-m-top']/div[2]/div/div[1]/div[1]") #定位页面顶部的购物车
                ele8.click()  #点击购物车，进入购物车页面
                time.sleep(1)
                ele9=b.find_element_by_xpath("//*[@id='j-cartPage']/div/div/div[2]/div[2]/div[2]/button") #定位下单按钮
                ele9.click() #点击下单按钮
                print("Order is ok, pending for pay")
                time.sleep(1)
                ele10=b.find_element_by_xpath("//*[@id='confirmRoot']/div/div[3]/div[2]/div[2]/div[2]/div/div[2]/input") #定位付款按钮
                ele10.click() #点击付款
                print("Please pay at once!")
                time.sleep(20)
                break
        except:
            print("No stock now.....")
            time.sleep(10)
            #time.sleep(random.randint(15,30))
            b.refresh()
            time.sleep(2)

newlogin0202()
