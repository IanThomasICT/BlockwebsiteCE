#! python3

# This requires the Covenant Eyes account to be using the Screen Accountability software (not the Legacy Internet Accountability software)

import keyboard
import webbrowser
import pyautogui as pya
import pyperclip
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import os
import subprocess

# Insert your Covenant Eyes login information here:
username = "____"
password = "____"

def copyurl():
    global url
    hotkey1 = "alt+d"

    pya.click(5, 200) # a random click for focusing the browser
    keyboard.send(hotkey1) # hotkey to focus on the browser's url
    pya.hotkey('ctrl', 'c') # copy URL
    time.sleep(0.5)
    fullurl = pyperclip.paste() # store copied URL to a variable
    parsedurl = urlparse(fullurl)
    url = parsedurl.netloc

def opencovenanteyes():
    # Visible Chrome Broswer:
    # global driver
    # driver = webdriver.Chrome()
    
    # Headless Chrome Browser:
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    global driver
    driver = webdriver.Chrome(options=chrome_options)

    driver.get(f"https://covenanteyes.com/myaccount/filter/users/{username}/custom-block-allow-lists") # Open CE filter list page

def covenanteyeslogin():
    time.sleep(1)
    user = driver.find_element_by_id("id_sign_in_username")
    user.click()
    user.send_keys(username)
    time.sleep(0.25)
    pw = driver.find_element_by_id("id_sign_in_password")
    pw.click()
    pw.send_keys(password)
    time.sleep(0.25)
    driver.find_element_by_css_selector("#sign_in_form > div:nth-child(4) > div > button").click()
    time.sleep(3)

def addtoblocklist():
    blockfield = driver.find_element_by_id("add_domain")
    blockfield.click()
    blockfield.send_keys(url)
    time.sleep(0.25)

    submit = driver.find_element_by_id("add_domain_submit")
    submit.click()
    time.sleep(2)

    print(f"{url} has been added to the block list")

    driver.close()

def restartcovenanteyes():
    os.startfile("C:\Program Files\CE\RestartCEClientOnly.exe")
    time.sleep(12)
    subprocess.call(["taskkill","/F","/IM","C:\Program Files\CE\RestartCEClientOnly.exe"])

def BlockWebsite():
    copyurl() # Extract current website url and store as variable "url"

    opencovenanteyes() # Open chrome and navigate to Covenant Eyes filter list

    covenanteyeslogin() # CovenantEyes login

    addtoblocklist() # add variable "url" to CE block list

    restartcovenanteyes() # Restart CovenantEyes

    # Enter back into True loop

def main():
    executehk = "alt+`"
    killkey = "ctrl+alt+-"
    while True:
        if keyboard.is_pressed(executehk):          
            BlockWebsite()
        if keyboard.is_pressed(killkey):
            break
        else:
            continue

main()
