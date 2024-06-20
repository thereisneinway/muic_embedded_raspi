import RPi.GPIO as GPIO
import time
#6380145
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10,GPIO.IN)
GPIO.setup(40,GPIO.OUT)

while True:
    if(GPIO.input(10) == 0):
        print("1")
        GPIO.output(40,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(40,GPIO.LOW)
        time.sleep(1)
        GPIO.output(40,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(40,GPIO.LOW)
        time.sleep(1)
        GPIO.output(40,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(40,GPIO.LOW)
        time.sleep(1)
    else:
        GPIO.output(40,GPIO.LOW)
        time.sleep(1)
        print("0")

