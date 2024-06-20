import gpiozero
from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD
from time import *
lcd = LCD()
def safe_exit(signum, frame):
    exit(1)
try:
    k = 0
    button = gpiozero.Button(15)
    signal(SIGTERM, safe_exit)
    signal(SIGHUP, safe_exit)

       
    while True:
            lcd.text("SYNCHRONIZATION", 1)
            lcd.text("COUNTER: " + str(k), 2)
            if(button.is_pressed):
                k+= 1
            
        
except KeyboardInterrupt:
    pass
finally:
    lcd.clear()
    lcd.backlight(0)

