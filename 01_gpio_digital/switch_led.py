import RPi.GPIO as GPIO
import time

LED_PIN = 6
SWITCH_PIN = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

try:
    while True:
        val = GPIO.input(SWITCH_PIN)
        print(val)
        GPIO.output(LED_PIN, val)

finally :
    GPIO.cleanup() 
    print("clean up and exit")