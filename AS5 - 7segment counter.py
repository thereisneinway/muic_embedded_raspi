import time
from datetime import datetime
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi,noop
from luma.core.virtual import viewport, sevensegment
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40,GPIO.IN,pull_up_down=GPIO.PUD_UP)

k=0
#6380145
def button_pressed_callback(Channel):
	global k
	k+=1
	
GPIO.add_event_detect(40,GPIO.FALLING,callback=button_pressed_callback,bouncetime=200)


def main():
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=1)
    seg = sevensegment(device)
    while True:
        global k
        print(k)
        seg.text = str(k)
        time.sleep(0.01)
        k+=1

if __name__ == '__main__':
    main()
