import keyboard
import webbrowser
import pyautogui as pya
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# Invisible Browser:
# chrome_options = Options()
# chrome_options.add_argument("--headless")
# driver = webdriver.Chrome(options=chrome_options)


def copyurl():
    global url
    hotkey1 = "alt+d"

    pya.click(5, 200) # a random click for focusing the browser
    keyboard.send(hotkey1) # hotkey to focus on the browser's url
    pya.hotkey('ctrl', 'c') # copy URL
    time.sleep(0.5)
    url = pyperclip.paste() # store copied URL to a variable

def main():
    executehk = "alt+`"
    while True:
        if keyboard.is_pressed(executehk):
            copyurl()
            print(type(url))
            break
            
main()


def BlockWebsite():
    # Extract current website when key was pressed and store as variable

    # Open Headless Browser with CovenantEyes website

    # CovenantEyes login
    username = "tmithomas98@gmail.com"
    password = "__"

    # Navigate to Filter block list

    # Select block field and paste website url

    # Click Block

    # Close Selenium driver

    # Refresh CE program

    # Enter back into True loop
