##system file automation using whatsapp
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os, re

chromepath = r'H:\\chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_argument("C:\\Users\\Chaitanya\\AppData\\Local\\Google\\Chrome\\User Data")
#options.add_argument("user-data-dir=C:\\Users\\Chaitanya\\AppData\\Local\\Google\\Chrome\\User Data")
driver = webdriver.Chrome(executable_path=chromepath, chrome_options=options)
driver.get('https://web.whatsapp.com/')
driver.maximize_window()
wait = WebDriverWait(driver, 600)
print("press any key after qr code scanning")
#input = ("press any key after qr code scanning")
print("enter user name to send message \t")
#target = input()
target = "kavya wats app"
print("enter the message you want to send \t ")
string = input()
def send_msg_to_user(string,target=target):
    user = driver.find_element_by_xpath("//span[@title= '{}']".format(target))  # entering name of chat
    user.click()
    #msg_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")  # Entering text message
    msg_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/div/div[2]/div[1]/div/div[2]")  # Entering text message
    #//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]
    msg_box.send_keys(string)
    #driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button").click()  # send button
    driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/div/div[2]/div[2]/button").click()  # send button

send_msg_to_user(string,target)
first_message=re.findall(r"[A-Z]+:.*$", os.popen("mountvol /").read(), re.MULTILINE)
print(first_message)
# y=((input("please select a local disk \t :")).upper())+':'
y = first_message
send_msg_to_user(target=target,string=y)

##upto here message of local disks is sent
##################################################################################################################
#this function reads the input from the user and  returns the message
def read_last_in_message(driver):
    """
    Reading the last message that you got in from the chatter
    """
    for messages in driver.find_elements_by_xpath("//div[contains(@class,'message-in')]"):
        try:
            message = ""
            emojis = []
            message_container = messages.find_element_by_xpath(".//div[@class='copyable-text']")
            message = message_container.find_element_by_xpath(".//span[contains(@class,'selectable-text invisible-space copyable-text')]").text
            for emoji in message_container.find_elements_by_xpath(".//img[contains(@class,'selectable-text invisible-space copyable-text')]"):
                emojis.append(emoji.get_attribute("data-plain-text"))

        except NoSuchElementException:  # In case there are only emojis in the message
            try:
                message = ""
                emojis = []
                message_container = messages.find_element_by_xpath(".//div[@class='copyable-text']")
                for emoji in message_container.find_elements_by_xpath(".//img[contains(@class,'selectable-text invisible-space copyable-text')]"):
                    emojis.append(emoji.get_attribute("data-plain-text"))
            except NoSuchElementException:
                pass

    return message

previous_in_message = None

while True:
        last_in_message = read_last_in_message(driver)
        j = ''
        if previous_in_message != last_in_message:
            print(last_in_message)
            previous_in_message = last_in_message
            y = y + '\{}'.format(last_in_message)
            if os.path.isdir(y):
                r = os.listdir(y)
                send_msg_to_user(r)
            elif last_in_message == 'b' or 'B':
                s = y.split('\\')
                del s[-1]
                y = '\\'.join(s)
                for k in s:
                    j = j + k + '\\'
                e=os.listdir(j)
                send_msg_to_user(e)
        time.sleep(1)













