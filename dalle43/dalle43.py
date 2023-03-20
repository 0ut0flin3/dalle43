import webbrowser
import os
import sys
from random import randint
import requests

if os.name=='nt':
   print("WINDOWS NOT SUPPORTED")
   sys.exit()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

os.system("clear")

global USER;USER=os.getlogin()
global DIR_PATH

DIR_PATH="/home/"+USER+"/Pictures/generated_images"

print(f'''
{bcolors.BOLD}Welcome to DALL-E 43 - by 0ut0flin3{bcolors.ENDC}\n Generated images will be saved in {DIR_PATH}
''')



if os.path.isdir(DIR_PATH)==False:
        os.mkdir(DIR_PATH)




A_0=104
A_1=116
A_2=116
A_3=112
A_4=115
A_5=58
A_6=47
A_7=47
A_8=111
A_9=112
A_10=101
A_11=110
A_12=46
A_13=97
A_14=105
A_15=47
A_16=105
A_17=109
A_18=97
A_19=103
A_20=101
A_21=115
A_22=63
A_23=112
A_24=114
A_25=111
A_26=109
A_27=112
A_28=116
A_29=61
xx=chr(A_0)+chr(A_1)+chr(A_2)+chr(A_3)+chr(A_4)+chr(A_5)+chr(A_6)+chr(A_7)+chr(A_8)+chr(A_9)+chr(A_10)+chr(A_11)+chr(A_12)+chr(A_13)+chr(A_14)+chr(A_15)+chr(A_16)+chr(A_17)+chr(A_18)+chr(A_19)+chr(A_20)+chr(A_21)+chr(A_22)+chr(A_23)+chr(A_24)+chr(A_25)+chr(A_26)+chr(A_27)+chr(A_28)+chr(A_29)


def get_img_url(prompt):
    prompt=prompt.replace(" ","%20")
    try:
        from pyvirtualdisplay import Display
    except Exception as ex:
        print(ex)
        sys.exit()
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.common.by import By
    import time
    display = Display(visible=0, size=(800, 600))
    display.start()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    gg=xx+prompt
    driver.get(gg)
    time.sleep(5)
    myImg = driver.find_element(By.TAG_NAME, 'img')
    return myImg.get_attribute("src")
while True:
    q=input('\033[96m'+'Description of the image you want to generate'+'\033[0m'+'\n > ')
    url=get_img_url(q)
    r=requests.get(url)
    newpath=DIR_PATH+"/"+str(randint(100000000,999999999))+".jpg"
    f=open(newpath,"wb")
    f.write(r.content)
    f.close()
    
    webbrowser.open_new_tab("file:///"+newpath)

    
  