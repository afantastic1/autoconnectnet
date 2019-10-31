# coding: utf-8
# -*- coding: utf-8 -*-
#author _Revy_
import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
#等待Win连上wifi
time.sleep(5)
#此处的driver要自己下载，路径自己调
#driver = webdriver.Firefox(executable_path = 'D:\新建文件夹\压缩\geckodriver.exe',log_path=r"D:\新建文件夹\压缩\AutoConnectWHUnet-master\geckodriver.log")
driver = webdriver.Chrome(executable_path = 'D:\新建文件夹\压缩\chromedriver.exe')
driver.get("http://202.118.253.94:8080/")
driver.find_element_by_id("username").click()
driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys("xxxxxxxx")#学号
driver.find_element_by_id("pwd_hk_posi").click()
driver.find_element_by_id("pwd").clear()
driver.find_element_by_id("pwd").send_keys("xxxxxx")#密码
driver.find_element_by_id("SLoginBtn_1").click()
driver.implicitly_wait(10)
driver.find_element_by_id("loginLink_div").click()

time.sleep(1)
driver.close()
#调通之后，设置开机自启,如下两步走
'''(1）首先，需要新建一个.bat文件（用来运行脚本），格式如下，红色部分为python脚本的位置（写完之后保存）：

python D:\AutoConnectWHUnet-master\autoconnectnet.py

pause

（2）点击开始--所有程序--启动--右击--打开，将已经保存的.bat文件复制到该目录（C:\用户\Administrator\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup）下
，可能杀毒软件会阻止，选择允许，然后重启电脑即可。
这里的Administrator可以是你的账户。如果不想要pause也许可以删掉这行(反正我最后是删掉了的)
注：开机自启以后会打开一个cmd窗口，关闭窗口，python程序将停止运行。
'''

