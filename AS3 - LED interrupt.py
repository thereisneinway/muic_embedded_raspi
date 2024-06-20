import RPi.GPIO as GPIO
import time
led = 1
#6380145
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(40,GPIO.OUT)

def button_pressed_callback(Channel):
	print("button pressed")
	global led
	if led == 1:
		GPIO.output(40,GPIO.LOW)
		led = 0
	else: 
		GPIO.output(40,GPIO.HIGH)
		led = 1
	
GPIO.add_event_detect(10,GPIO.FALLING,callback=button_pressed_callback,bouncetime=200)

try:
	message = input("press enter to quit")
	GPIO.cleanup()
except:
	print("END")

