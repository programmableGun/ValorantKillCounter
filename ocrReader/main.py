from time import sleep
import cv2
from cv2 import waitKey
import numpy
import pytesseract
from mss import mss
import pyttsx3 as os
import requests

url = 'http://192.168.1.165:42069'
#x = requests.post(url, "death")
#print(x.text)
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe' 
cong = r'--oem 3 --psm 6 outputbase digits'
bounding_box = {'top':1000, 'left':575, 'width':75, 'height':50}

sct = mss()

playerHP = 100
newHP = 100

while True:
    sct_img = sct.grab(bounding_box)
    sct_img = cv2.cvtColor(numpy.array(sct_img),cv2.COLOR_RGB2GRAY)
    try:
        newHP = int(pytesseract.image_to_string(numpy.array(sct_img),config=cong))
    except ValueError:
        pass
    if (newHP != playerHP):
        if(newHP > playerHP and newHP <= 100):
            #healing or new round
            playerHP = newHP
            print(playerHP)
        elif (newHP < playerHP and newHP != 0 and newHP != 10 and newHP != 1 and newHP != 4 and newHP != 40):
            #if damge taken  is greater than 30 in one shot then shoot gun
            if (playerHP - newHP >= 11 and playerHP - newHP <= 50):
             playerHP = newHP
             print("\n\n")
             print(playerHP)
             print("shootingGun!!!!")
             requests.post(url, "death")
             os.speak("hurt")
            else:
             playerHP = newHP
             print("\n\n")
             print(playerHP)
            
    cv2.imshow('screen', numpy.array(sct_img))
    
    if (waitKey(1) & 0XFF == ord('q')):
        cv2.destroyAllWindows()
        break
        

#img = cv2.imread('C:\\Users\\aluck\\Desktop\\ocrReader\\1.png')
#img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#print(pytesseract.image_to_string(img))
#cv2.imshow('result',img)
#cv2.waitKey(0)

#cap =  cv2.VideoCapture()
#
#cap.open(5,cv2.CAP_DSHOW)
#while(True):
#    sleep(0.3)
#    rec,frame=cap.read()
#    cv2.imshow('frame',frame)
#    #print("\n\n\t" + pytesseract.image_to_string(frame))
#    if (waitKey(1) & 0XFF == ord('q')):
#        break

#cap.release()


