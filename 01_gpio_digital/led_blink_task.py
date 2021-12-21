import RPi.GPIO as GPIO
import time

LED_PIN1 = 5
LED_PIN2 = 6
LED_PIN3 = 13
GPIO.setmode(GPIO.BCM) # GPIO.BCM or GPIO.BOARD
GPIO.setup(LED_PIN1, GPIO.OUT) # GPIO.OUT or GPIO.IN
GPIO.setup(LED_PIN2, GPIO.OUT)
GPIO.setup(LED_PIN3, GPIO.OUT)

GPIO.output(LED_PIN1, GPIO.HIGH) 
print("Red led on")
time.sleep(2)
GPIO.output(LED_PIN1, GPIO.LOW) 
GPIO.output(LED_PIN2, GPIO.HIGH) 
print("Red led off")
print("Yellow led on")
time.sleep(2)
GPIO.output(LED_PIN2, GPIO.LOW) 
GPIO.output(LED_PIN3, GPIO.HIGH)
print("Yellow led off")
print("Green led on")
time.sleep(2)
GPIO.output(LED_PIN3, GPIO.LOW)
print("Green led off")

GPIO.cleanup() #GPIO 핀상태 초기화
