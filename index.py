from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



PATH = "Your path" #Enter the path of the chrome driver
driver = webdriver.Chrome(PATH)

#open a file
fname= "data_1.txt"
f = open(fname, "a", encoding="utf-8")

#open twitter on the web browser
driver.get("https://twitter.com/login")

#enter the username
username = driver.find_element_by_name("session[username_or_email]")
username.send_keys("username") #enter your username
driver.implicitly_wait(1)

#enter the password
password = driver.find_element_by_name("session[password]")
password.send_keys("password") #enter your password
driver.implicitly_wait(1)

#hits enter to login
password.send_keys(Keys.ENTER)
driver.implicitly_wait(1) #increase the delay time incase of slow internet connection

#navigate to the profile tab
profile = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[7]/div")
profile.click()
driver.implicitly_wait(5)

#navigate to tweets and replies
tab = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/nav/div/div[2]/div/div[2]/a/div/span")
tab.click()
driver.implicitly_wait(5)

#scroll down
SCROLL= 2.0
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    time.sleep(SCROLL)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	
    driver.implicitly_wait(2)
    time.sleep(SCROLL)
    new_height = driver.execute_script("return document.body.scrollHeight")
    driver.implicitly_wait(2)
    if new_height == last_height:
        break
    last_height = new_height
driver.implicitly_wait(10)


#scrap the tweets and write to the file
data = driver.find_elements_by_css_selector('[data-testid="tweet"]')
for item in data:
    f.write(item.text)



#close the file
f.close()




