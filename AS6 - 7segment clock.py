import time
from datetime import datetime
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi,noop
from luma.core.virtual import viewport, sevensegment
import RPi.GPIO as GPIO


#6380145


def main():
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=1)
    seg = sevensegment(device)
    while True:
        seg.text = str(datetime.now().strftime('%H.%M.%S'))
        time.sleep(0.1)

if __name__ == '__main__':
    main()

