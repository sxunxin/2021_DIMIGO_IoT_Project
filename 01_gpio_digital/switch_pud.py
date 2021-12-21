import RPi.GPIO as GPIO
import time

SWITCH_PIN = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down= GPIO.PUD_UP)

try:
    while True:
        val = GPIO.input(SWITCH_PIN)
        print(val)
        time.sleep(0.1)

finally :
    GPIO.cleanup() 
    print("clean up and exit")