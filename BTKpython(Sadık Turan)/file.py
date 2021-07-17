from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request as rq
import time

import requests
"TEMEL DRİVER İŞLEMLERİ"
#  driver= webdriver.Chrome("chromedriver.exe").get("https://www.youtube.com/")  hızlı bir şekilde tek satırda web açar

# driver= webdriver.Chrome("chromedriver.exe")
# driver.get("https://www.youtube.com/")
# time.sleep(2)
# driver.maximize_window() # tam ekran yapar
# driver.save_screenshot("deneme.png") # deneme adından ss alıp save eder
# driver.close() # son olarak kapatır
# driver.back() # bu şekilde bir sayfa gelir
# driver.forward() # ile de bir sayfa  ileri gider
# driver.title # ile driverın başlığını alıyoruz
# # driver.get("https://www.youtube.com/")

# PARİ İLE OTOMATION

"SELENİUM İLE BINANCE"

# driver = webdriver.Chrome("chromedriver.exe")
#
# driver.get(r"https://www.binance.com/en/markets")
#
# input_ = driver.find_element_by_xpath(r'//*[@id="__APP"]/div[1]/main/div/div[2]/div/div[1]/div[2]/div/input')
#  #input_.send_keys(Keys.ENTER) # bu şekilde de enter tuşuna basılır.
# input_.send_keys("btt")
#
# sales = driver.find_element_by_xpath(r'//*[@id="__APP"]/div[1]/main/div/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div/div[3]/div[2]')
#
#
# print(sales.text) # be şekilde  ne kadar dolar olduğunu anladık
# driver.close()

"SELENİUM İELE GİTHUB TAKİPÇİLERİ ALMAK"

# driver = webdriver.Chrome()
#
# driver.get(r"https://github.com/tahayagma?tab=followers")
#
# print(driver.find_element_by_xpath(r'//*[@id="js-pjax-container"]/div[2]/div/div[2]/div[2]/div').text)

"SELENİUM İLE İNSTAGRAMDAN VERİ TOPLAMAK"

driver = webdriver.Chrome()
# --------------------------INSTAGRAM LOGIN----------------------------
# driver.get(r"https://www.instagram.com/accounts/login/")
# time.sleep(3) # beklemesi gerekiyor aksi takdirde elementleri bulamaz
# driver.find_element_by_name("username").send_keys(username)
# driver.find_element_by_name('password').send_keys(password)
# driver.find_element_by_xpath(r'//*[@id="loginForm"]/div[1]/div[3]/button/div').click()
# time.sleep(2)
# ------------------TAKİPÇİ ALMA-----------------------------------------
# driver.get("https://www.instagram.com/freedom.code")
# time.sleep(2)
# followers = driver.find_element_by_xpath(r'//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').text
# followers = followers.split(" ")
# driver.find_element_by_xpath(r'//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
# time.sleep(2)
# dialog = driver.find_element_by_css_selector("div[role=dialog] ul")
# follower_count = len((dialog.find_elements_by_css_selector("li")))
# time.sleep(1)
# while True:
#     dialog.click()
#     webdriver.ActionChains(driver).key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
#     time.sleep(2)
#     new = len((dialog.find_elements_by_css_selector("li")))
#     if int(followers[0])!=new:
#         follower_count = new
#         time.sleep(2)
#     else:
#         break
#
# followers_son = dialog.find_elements_by_css_selector("li")
# counter = 1
# for user in followers_son:
#     link = user.find_element_by_css_selector("a").get_attribute("href")
#     print(counter,link)
#     counter+=1
# driver.close()
# ---------------------TARAYICIDA DİL AYARLAMALARI ---------------------------------------
# web_options = webdriver.ChromeOptions()
# web_options.add_experimental_option('prefs',{'intl.accept_languages':'en,en_US'})
# ingilizce_driver = webdriver.Chrome('chromedriver.exe',chrome_options=web_options)
#---------------------------------------------------------------------------------------------

#---------------------TAG SEARCH İN İNSTAGRAM(TAG ARAMA VE VERİ ALMA )----------------------------------------------------
# time.sleep(3)
# driver.get("https://www.instagram.com/explore/tags/kedi/") # tag kısmını kullanıcıdan alabiliriz
# time.sleep(3)
# out = driver.find_elements_by_class_name("KL4Bh")
# limit_img = 30
# while True:
#     webdriver.ActionChains(driver).key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
#     time.sleep(2)
#     new_img_count = len(driver.find_elements_by_class_name("KL4Bh"))
#     if limit_img <= new_img_count:
#         break
#     else:
#         pass
#
# c = 1
# for son in driver.find_elements_by_class_name("KL4Bh")[0:limit_img]:
#     src = son.find_element_by_css_selector("img").get_attribute("src")
#     rq.urlretrieve(src,"kedi-{}.png".format(c)) # url adresinden resimleri kaydeder
#     c+=1
# time.sleep(3)
# driver.close()
"SELENİUM İLE TWİTTE BOT"
#--------------------TWİTTER LOGIN---------------------------------------

driver.get("https://twitter.com/login")
time.sleep(5)
driver.find_element_by_name("session[username_or_email]").send_keys("username")
driver.find_element_by_name("session[password]").send_keys("password")
driver.find_element_by_xpath(r'//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div').click()
# -----------------TWİTTER TRENDS CHECK---------------------------------------------
# time.sleep(5)
# driver.get("https://twitter.com/i/trends")
# time.sleep(3)
# trends_count = 0
# while True:
#     webdriver.ActionChains(driver).key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
#     time.sleep(2)
#     new_tr_counts = len(driver.find_elements_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div'))
#     if new_tr_counts >= trends_count:
#         trends_count = new_tr_counts
#         time.sleep(2)
#     else:break

# trends = driver.find_elements_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div')
# for i in range(2,len(trends)):
#     time.sleep(2)
#     names = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div[%d]/div/div/div/div[2]'%i)
#     print(names.text)
# driver.close()

# -------------------------özellikle tag ile arama-----------------------------------------------------
driver.get("https://twitter.com/search?q=%23ÜmitCanUygun&src=typed_query") # %23 işareti # işaretine denk gelir
time.sleep(3)
list = driver.find_elements_by_xpath(r"//div[@data-testid ='tweet']/div[2]/div[2]") #tweetler alındı
c = 1
for item in list:
    print(c,"************************")
    print(item.text)
    c+=1
# tweetter son yüklenen 4 yada5 tan gösterir sayfanın hızlı çalışması ve şişmesi için
# çözüm olarak her döngüde twitleri alıp kaydedebilirsiniz


