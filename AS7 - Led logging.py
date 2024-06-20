import time
import datetime

import gspread
from oauth2client.service_account import ServiceAccountCredentials

import RPi.GPIO as GPIO

SheetName = "API test"
GSheet_OAUTH_JSON = "trans-trees-368707-f255b9e22251.json"
scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name(GSheet_OAUTH_JSON, scope)
client = gspread.authorize(credentials)
worksheet = client.open(SheetName).sheet1
row = ["Tine","LED"]
index = 1
worksheet.insert_row(row,index)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(40,GPIO.OUT)
led = 1

def button_pressed_callback(Channel):
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    print("button pressed")
    global led
    try:
        if led == 1:
            GPIO.output(40,GPIO.LOW)
            led = 0
            worksheet.append_row([timestamp,"OFF"])
        else: 
            GPIO.output(40,GPIO.HIGH)
            led = 1
            worksheet.append_row([timestamp,"ON"])
    except Exception as ex:
        print("====Log Fail: ",ex)

GPIO.add_event_detect(10,GPIO.FALLING,callback=button_pressed_callback,bouncetime=200)

try:
    message = input("Enter to quit")
except:
    print("END")

