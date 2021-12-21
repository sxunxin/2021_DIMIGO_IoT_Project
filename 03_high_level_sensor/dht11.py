import Adafruit_DHT
import time

sensor = Adafruit_DHT.DHT11
PIN = 4

try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, PIN)
        if humidity is not None and temperature is not None:
            print(f"Temperature= %.1f* ,Humidity:humidity=%.1f%" % (temperature,humidity))
        else:
            print('Read error')
        time.sleep(1)
        

finally :
    print('End of Program')

