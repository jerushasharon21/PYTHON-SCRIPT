from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



PATH = "C:\Program Files (x86)\chromedriver.exe" #path of the chrome driver
driver = webdriver.Chrome(PATH)

fname= "data_1.txt"
f = open(fname, "a", encoding="utf-8")


driver.get("https://twitter.com/login")
username = driver.find_element_by_name("session[username_or_email]")
username.send_keys("username") #enter your username
driver.implicitly_wait(1)

password = driver.find_element_by_name("session[password]")
password.send_keys("password") #enter your password
driver.implicitly_wait(1)

password.send_keys(Keys.ENTER)
driver.implicitly_wait(1)

profile = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[7]/div")
profile.click()
driver.implicitly_wait(5)

tab = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/nav/div/div[2]/div/div[2]/a/div/span")
tab.click()
driver.implicitly_wait(5)


tweets = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main")
driver.find_elements_by_class_name("css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0")
f.write(tweets.text)






