import RPi.GPIO as GPIO
import time

BUZZER_PIN = 12
GPIO.setmode(GPIO.BCM) 
GPIO.setup(BUZZER_PIN, GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN, 262)
pwm.start(10)


time.sleep(2)
pwm.ChangeDutyCycle(0)

pwm.stop()
GPIO.cleanup()

