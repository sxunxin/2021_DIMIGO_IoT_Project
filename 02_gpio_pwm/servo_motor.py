import RPi.GPIO as GPIO


SERVO_MOTOR_PIN = 19
GPIO.setmode(GPIO.BCM) 
GPIO.setup(SERVO_MOTOR_PIN, GPIO.OUT)

pwm = GPIO.PWM(SERVO_MOTOR_PIN, 50)
pwm.start(7.5)

try:
    while True:
        val = input('1 : 0도, 2: -90도, 3: 90도, 9:exit > ')
        if val == '1':
            pwm.ChangeDutyCycle(7.5)
        elif val == '2':
            pwm.ChangeDutyCycle(2.5)
        elif val == '3':
            pwm.ChangeDutyCycle(12.5)
        elif val == '9':
            break
finally:
    pwm.stop()
    GPIO.cleanup()
    