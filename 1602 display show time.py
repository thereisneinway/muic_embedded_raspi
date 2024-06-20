#Using i2c protocal
#https://www.electroniclinic.com/raspberry-pi-16x2-lcd-i2c-interfacing-and-python-programming/
#SCL=GPIO3 ; SDA=GPIO02 ; 5V
from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD
from time import *
from datetime import datetime
lcd = LCD()
def safe_exit(signum, frame):
    exit(1)
try:
    signal(SIGTERM, safe_exit)
    signal(SIGHUP, safe_exit)
    lcd.text("Hello world", 1)
    lcd.text("Good to see you", 2)
    sleep(1)
    while True:
        lcd.text("It's now", 1)
        lcd.text(datetime.now().strftime('%b %d  %H:%M:%S\n'), 2)

        sleep(1)

except KeyboardInterrupt:
    pass
finally:
    lcd.clear()
    lcd.backlight(0)