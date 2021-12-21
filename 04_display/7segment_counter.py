import RPi.GPIO as GPIO
import time

# GPIO 7개 핀 설정

SEGMENT_PINS = [2,3,4,5,6,7,8]

GPIO.setmode(GPIO.BCM)

for segment in SEGMENT_PINS:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, GPIO.LOW)

data = [[1,1,1,1,1,1,0], 
        [0,1,1,0,0,0,0],     
        [1,1,0,1,1,0,1],
        [1,1,1,1,0,0,1],
        [0,1,1,0,0,1,1],
        [1,0,1,1,0,1,1],
        [1,0,1,1,1,1,1],
        [1,1,1,0,0,0,0],
        [1,1,1,1,1,1,1],
        [1,1,1,0,0,1,1]]

try:
    for i in range(10):
        for j in range(7): 
            GPIO.output(SEGMENT_PINS[j],data[i][j])
        time.sleep(1)


finally:
    GPIO.cleanup()
    print("bye")



