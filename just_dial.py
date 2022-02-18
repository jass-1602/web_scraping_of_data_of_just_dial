from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
# PROXY = '91.214.31.234:8080'
#
# webdriver.DesiredCapabilities.FIREFOX['proxy'] = {
#     "httpProxy": PROXY,
#     "sslProxy": PROXY,
#     "proxyType": "MANUAL",
# }
driver = webdriver.Firefox()
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException

# driver = webdriver.Chrome('/usr/bin/chromedriver')

# driver = webdriver.Chrome(ChromeDriverManager().install())
options = Options()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
# driver=webdriver.Firefox()
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.justdial.com/")
driver.maximize_window()

driver.find_element(By.XPATH, '/html/body/div[2]/section[1]/section[2]/section/div[2]/div/div[1]').click()
# driver.find_element(By.XPATH, '/html/body/div[3]/section[2]/section/div/div[1]/div/figure[3]/figcaption').click()
driver.implicitly_wait(3)
city = driver.find_element(By.XPATH, '//*[@id="city"]')
driver.implicitly_wait(10)
city.send_keys('ludhiana ')
driver.implicitly_wait(3)
driver.find_element(By.XPATH, '//*[@id="Ludhiana"]').click()
driver.implicitly_wait(3)
driver.find_element(By.XPATH, '/html/body/div[2]/section[2]/section/div/div[1]/div/figure[3]/div/a/img').click()
driver.implicitly_wait(3)
driver.find_element(By.XPATH, '//*[@id="srchbx"]').click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH,'//*[@id="cross_S"]').click()
driver.implicitly_wait(5)
add_item=driver.find_element(By.XPATH, '//*[@id="srchbx"]')
# driver.implicitly_wait(5)

add_item.send_keys('Grocery')
driver.implicitly_wait(5)
driver.find_element(By.XPATH,'//*[@id="10237947~1~1~Ludhiana~~Grocery%20Stores~~~~0~0~0~undefined~undefined~10237947~~~~Grocery%20Stores~~0~~~0~~Grocery~0~Ludhiana~0~0~0~"]').click()
driver.find_element(By.XPATH,'//*[@id="srIcon"]').click()
driver.implicitly_wait(5)

driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[2]/div[2]/div[1]/div/section/div/ul/li[1]/section/div[1]/section/div[1]').click()

# c=driver.find_element(By.XPATH,'//*[@id="ht_lk_sub_0_22"]').click()
Name = []
name = driver.find_elements(By.CLASS_NAME, 'lng_cont_name')
driver.implicitly_wait(10)
for names in name:
    # print(names)
    names_list = names.text
    Name.append(names_list)

addressList = []
# print(len(Name))
driver.implicitly_wait(10)
# driver.quit()
# for i in range(len(addressList)):
# driver.find_element(By.CLASS_NAME,'ncard0').click()

a=driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[2]/div[2]/div[1]/div/section/div/ul/li[1]/section/div[1]/section/div[1]/p[2]/span/a/b').text
driver.implicitly_wait(10)
print(a)
driver.quit()
# for i in a:
#     i.click()
    # driver.find_element(By.XPATH,'/html/body/div/div/section[1]/div[2]/div/div/ul/li[3]/a').click()
    # driver.find_element(By.XPATH,'/html/body/div/div/section[1]/div[3]/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/div[2]').click()
    # p=driver.find_elements(By.XPATH,'/html/body/div[2]/div[2]/div[2]/div[2]/div[1]/div/section/div/ul/li/section/div[1]/section/div[1]/p[2]/span/a').get_attribute('innerText')
    # for ps in p:
    #     number_list = ps.text
    #     addressList.append(number_list)





# print(p)





# Name=[]
# name = driver.find_elements(By.CLASS_NAME,'lng_cont_name')

# print(p)
# print(addressList)