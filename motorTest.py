from gpiozero import OutputDevice
from gpiozero import Servo 
from time import sleep

a = OutputDevice(6)
b = OutputDevice(13)
c = OutputDevice(19)
d = OutputDevice(26) 
gunMotor = OutputDevice(20)

delay = 0.01 

#@paramater: delay amount, SpinAmount
def SpinMotor(delayAmount, SpinAmount):
    print("Spining Motor...")
    delay = delayAmount
    if SpinAmount >= 0:
        for x in range(SpinAmount):
           #print(x)
           #0111
           sleep(delay)
           a.off()
           b.on()
           c.on()
           d.on()
           #0011
           sleep(delay)
           a.off()
           b.off()
           c.on()
           d.on()
           #1011
           sleep(delay)
           a.on()
           b.off()
           c.on()
           d.on()
           #1001
           sleep(delay)
           a.on()
           b.off()
           c.off()
           d.on()
           #1101
           sleep(delay)
           a.on()
           b.on()
           c.off()
           d.on()
           #1100
           sleep(delay)
           a.on()
           b.on()
           c.off()
           d.off()
           #1110
           sleep(delay)
           a.on()
           b.on()
           c.on()
           d.off()
           #0110
           sleep(delay)
           a.off()
           b.on()
           c.on()
           d.off()
    else:
        SpinAmount *= -1
        for x in range(SpinAmount):
            #0110
           sleep(delay)
           a.off()
           b.on()
           c.on()
           d.off()
           #1110
           sleep(delay)
           a.on()
           b.on()
           c.on()
           d.off() 
           #1100
           sleep(delay)
           a.on()
           b.on()
           c.off()
           d.off()
           #1101
           sleep(delay)
           a.on()
           b.on()
           c.off()
           d.on()
           #1001
           sleep(delay)
           a.on()
           b.off()
           c.off()
           d.on()
           #1011
           sleep(delay)
           a.on()
           b.off()
           c.on()
           d.on()
           #0011
           sleep(delay)
           a.off()
           b.off()
           c.on()
           d.on()
           #0111
           sleep(delay)
           a.off()
           b.on()
           c.on()
           d.on()

    a.off()
    b.off()
    c.off()
    d.off()

def KillToMotorInfo(CurrentKillCount, SavedKillCount):
    
    #format for conversion, str to int
    CurrentKillCount = CurrentKillCount.replace(",","")
    SavedKillCount = SavedKillCount.replace(",","")

    CurrentKillCount = int(CurrentKillCount)
    SavedKillCount = int(SavedKillCount)
    print("\bAmount of kills Detected")
    
    # Kill Detection Amount vvv
    print(CurrentKillCount - SavedKillCount)
    
    SpinMotor(delay, (CurrentKillCount - SavedKillCount)*100)

def ShootGun(bulletAmt):
    servo = Servo(14)
    print("shooting gun")
    gunMotor.on()
    print ("on")
    sleep(2.5)
    for x in range(bulletAmt):
        #shoot function; where a servo would make a piece go back and forth to move neft dart
        #move servo up
        servo.value = 1
        #wait
        sleep(1)
        #move servo down 
        servo.close()
        sleep(1)    

        

    gunMotor.off()  
    print("off")
    sleep(3.5)

#ShootGun(1)