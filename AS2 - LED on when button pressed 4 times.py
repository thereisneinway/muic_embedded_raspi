import RPi.GPIO as GPIO
import time
#6380145
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10,GPIO.IN)
GPIO.setup(40,GPIO.OUT)
k = 0

while True:
    time.sleep(1)
    print(k)
    if(GPIO.input(10) == 0):
        k+= 1
        
    if(k %4 == 0):
        GPIO.output(40,GPIO.HIGH)
    else:
        GPIO.output(40,GPIO.LOW)


