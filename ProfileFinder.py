import time

import AUTH_KEY as KEY
import os
import re
from selenium import webdriver
ROOT_DIR = os.path.dirname(os.path.abspath("D:\\ProfileFinder"))
print("Root_Path : "+ROOT_DIR)
_names = []
urllist = []
driver = webdriver.Chrome(r"chromedriver.exe")

def cookie_fb_exits():
    return True
def fb_login():
    driver.get ("https://www.facebook.com")
    driver.find_element_by_id("email").send_keys(KEY.EMAIL_)
    driver.find_element_by_id("pass").send_keys(KEY.AUTH_)
    driver.find_element_by_id("u_0_b").click()
    time.sleep(15)


with open("names.txt", 'r') as fp:
    read_lines = fp.readlines()
    read_lines = [line.rstrip('\n') for line in read_lines]
fb_login()
for name in read_lines:
    url = "https://www.facebook.com/search/top?q={0}".format(name)
    urllist.append(url)
for url in urllist:
    try:
        print(url)
        temp = driver.get(url)
        time.sleep(5)
        str_ = driver.page_source
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str_)
        for res in urls:
            try:
                if res.endswith("?__tn__=%3C"):
                    print(res)
                    driver.get(res)
                    time.sleep(6)
                    profile_name = res[res.rindex("/"):res.rindex("?")-1]+".png"
                    screenshotpath = os.path.join(os.path.sep, ROOT_DIR, 'ProfileFinder' + os.sep)
                    print(screenshotpath)
                    driver.get_screenshot_as_file(screenshotpath + profile_name)
            except:
                print("Profile Error : "+res)
    except:
        print("Search Error : "+url)
driver.close()