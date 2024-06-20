import gpiozero
from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD
from time import *
from datetime import datetime
lcd = LCD()
def safe_exit(signum, frame):
    exit(1)
try:
    k = 0
    button = gpiozero.Button(15)
    led = gpiozero.LED(21)
    signal(SIGTERM, safe_exit)
    signal(SIGHUP, safe_exit)
    
    ping = gpiozero.PingServer('google.com')
    led.on()
    
    #Hello screen
    lcd.text("Hello world", 1)
    lcd.text("Raspberry PI 4", 2)
    sleep(1)
    #Loading screen
    lcd.text("Loading...", 1)
    for i in range(16):
        lcd.text(i*'-',2)
        sleep(0.1)
    #Wait for button to be pused
    lcd.text("PUSH THE BUTTON",1)
    lcd.text("TO CONTINUE",2)
    button.wait_for_press()
    led.off()
    
    #GREAT!
    lcd.clear()
    lcd.text("GREAT!",1)
    sleep(1)
       
    while True:
        led.on()
        while(k==0):
            lcd.text("TIME", 1)
            lcd.text(datetime.now().strftime('%b %d  %H:%M:%S\n'), 2)
            if(button.is_pressed):
                k=1
                led.off()
            sleep(0.1)
        while(k==1):
            lcd.text("CPU TEMP", 1)
            lcd.text(str(gpiozero.CPUTemperature().temperature) + "C",2)
            if(button.is_pressed):
                k = 2;
                led.off()
            sleep(0.1)
        while(k==2):
            lcd.text("INTERNET",1)
            ping.when_deactivated = lcd.text("not connected",2)
            ping.when_activated = lcd.text("    connected",2)
            if(button.is_pressed):
                k = 0;
                led.off()
            sleep(0.1)

except KeyboardInterrupt:
    pass
finally:
    lcd.clear()
    lcd.backlight(0)
    led.off()

