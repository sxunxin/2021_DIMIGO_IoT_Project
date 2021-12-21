import Adafruit_DHT
from lcd import drivers
import datetime
import time

display = drivers.Lcd()
sensor = Adafruit_DHT.DHT11
PIN = 4

try:
    while True:
        now = datetime.datetime.now()
        display.lcd_display_string(now.strftime("%x%X"), 1)
        
        humidity, temperature = Adafruit_DHT.read_retry(sensor, PIN)
        if humidity is not None and temperature is not None:
            display.lcd_display_string(f"%.1f*C, %.1f%%" % (temperature,humidity), 2)
        else:
            print('Read error')


finally:
    print("Cleaning up!")
    display.lcd_clear()
