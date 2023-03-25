import webbrowser
import os
import sys
from random import randint
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

global USER;USER=os.getlogin()
global DIR_PATH
if os.name=='nt':
   DIR_PATH="C:/Users/"+USER+"/Pictures/generated_images"
if os.name=='posix':
   DIR_PATH="/home/"+USER+"/Pictures/generated_images"
if os.path.isdir(DIR_PATH)==False:
        os.mkdir(DIR_PATH)
global URL;URL='https://open.ai/images?prompt='





def show_img(prompt):
    prompt=prompt.replace(" ","%20")
    REQURL=URL+prompt
    driver.get(REQURL)
    time.sleep(5)
    myImg = driver.find_element(By.TAG_NAME, 'img')
    url= myImg.get_attribute("src")
    r=requests.get(url)
    newpath=DIR_PATH+"/"+str(randint(100000000,999999999))+".jpg"
    f=open(newpath,"wb")
    f.write(r.content)
    f.close()
    webbrowser.open_new_tab("file:///"+newpath)

