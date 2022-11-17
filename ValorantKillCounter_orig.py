import gpiozero  # raspberry pi's pin control library
import bs4
import requests
import time
from bs4 import BeautifulSoup as soup
from motorTest import KillToMotorInfo, SpinMotor
#get url and request
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n why hello there :) \t Welcome Back Home \n Name: Valorant Kill Counter \n Program Start! \n \n")
my_url = 'https://tracker.gg/valorant/profile/riot/Gun%238016/overview'
page_html = requests.get("https://tracker.gg/valorant/profile/riot/Gun%238016/overview")

# html parsing
page_soup = soup(page_html.text, "html.parser")
SpanContainer = page_soup.findAll("span",{"class":"value"})
textKillCount = SpanContainer[8]
SpinMotor(0.001, 5000)

#print out the parsed string found on the webpage
print(textKillCount.text.strip())
SavedKillCount = textKillCount.text.strip()

while(True):
    time.sleep(90)
    print("\tupdating")
    my_url = 'https://tracker.gg/valorant/profile/riot/Gun%238016/overview'
    page_html = requests.get("https://tracker.gg/valorant/profile/riot/Gun%238016/overview")
    # html parsing
    page_soup = soup(page_html.text, "html.parser")
    SpanContainer = page_soup.findAll("span",{"class":"value"})
    textKillCount = SpanContainer[8]
    if (SavedKillCount != textKillCount.text.strip()):
        print("\tKill Change Detected\n")
        print(textKillCount.text.strip())
        KillToMotorInfo(textKillCount.text.strip(), SavedKillCount)
        
        SavedKillCount = textKillCount.text.strip()
    else:
        print("no change\nupdated")
    