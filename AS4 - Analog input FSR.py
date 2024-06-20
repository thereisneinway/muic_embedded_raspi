import time
import Adafruit_ADS1x15
import RPi.GPIO as GPIO
#6380145
adc = Adafruit_ADS1x15.ADS1115()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40,GPIO.OUT)
p = GPIO.PWM(40,100) 
p.start(0)


GAIN = 1

while True:
    value = adc.read_adc(0,gain=GAIN)
    k = value*100/30672
    if k < 0:
        k = 0
    if k> 100:
        k = 100
    print(k)
    p.ChangeDutyCycle(k)
    time.sleep(0.05)