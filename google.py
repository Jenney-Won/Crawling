from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

driver = webdriver.Chrome()
driver.get("https://www.google.com/imghp?hl=ko&tab=ri&ogbl")
elem = driver.find_element_by_name("q")
elem.send_keys("best hiking trail around the world")
elem.send_keys(Keys.RETURN)
images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
count = 1

# # until the END OF LOADING!!
SCROLL_PAUSE_TIME = 3
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element_by_css_selector(".mye4qd").click()
        except:
            break
    last_height = new_height
    
WEBPAGE_LOADING_TIME = 3
for image in images:
    try:
        image.click()
        time.sleep(WEBPAGE_LOADING_TIME)
        imgUrl = driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img').get_attribute("src")

        # Deceiveing as browser :D
        opener=urllib.request.build_opener()
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(imgUrl, str(count) +".jpg") # string typecast
        count = count + 1
    except:
        pass

# driver.close()

