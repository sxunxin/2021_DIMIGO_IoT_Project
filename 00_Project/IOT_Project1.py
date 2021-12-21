import RPi.GPIO as GPIO
import time

TRIGGER_PIN = 27                                   # 핀 설정
ECHO_PIN = 17
LED_PIN1 = 25
LED_PIN2 = 24
LED_PIN3 = 23
BUZZER_PIN = 22
SWITCH_PIN = 21

GPIO.setmode(GPIO.BCM)                              # GPIO 설정
GPIO.setup(TRIGGER_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(LED_PIN1, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)
GPIO.setup(LED_PIN3, GPIO.OUT)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

try:
    pwm = GPIO.PWM(BUZZER_PIN, 262)                 # 피에조 부저 설정
    while True:                                     # while문 무한반복으로 코드 실행
        GPIO.output(TRIGGER_PIN, True)              # 초음파 센서로 위치 측정
        time.sleep(0.00001)
        GPIO.output(TRIGGER_PIN, False)

        while GPIO.input(ECHd O_PIN) == 0:
            pass
        start = time.time()

        while GPIO.input(ECHO_PIN) == 1:
            pass
        stop = time.time() 

        duration_time = stop - start
        distance = 17160 * duration_time
        val = GPIO.input(SWITCH_PIN)                # 스위치 값 받기
        print('Distance : %.1fcm' % distance)       # 초음파 센서 값 출력

                                                    # 원래 거리는 2m를 기준으로 하지만 원활한 값 출력을 위해 20cm를 기준으로 함
        if distance <= 25 and val == 0:             # 스위치가 눌려있지 않고 거리가 25cm 안이면 
            GPIO.output(LED_PIN3, GPIO.HIGH)        # 빨강,노랑,초록 불 모두 킨다.
            GPIO.output(LED_PIN2,GPIO.HIGH)
            GPIO.output(LED_PIN1,GPIO.HIGH)
        elif distance <= 30 and val == 0:           # 스위치가 눌려있지 않고 거리가 30cm 안이면
            GPIO.output(LED_PIN1,GPIO.HIGH)         # 노랑,초록 불을 킨다.
            GPIO.output(LED_PIN2,GPIO.HIGH)
            GPIO.output(LED_PIN3, GPIO.LOW)
        elif distance <= 40 and val == 0:           # 스위치가 눌려있지 않고 거리가 40cm 안이면 
            GPIO.output(LED_PIN1,GPIO.HIGH)         # 초록 불만 킨다.
            GPIO.output(LED_PIN2, GPIO.LOW)
            GPIO.output(LED_PIN3, GPIO.LOW)
        else:                                       # 40cm보다 멀리 있으면 아무런 LED도 키지않는다.
            GPIO.output(LED_PIN1, GPIO.LOW)
            GPIO.output(LED_PIN2, GPIO.LOW)
            GPIO.output(LED_PIN3, GPIO.LOW)

        if distance <= 20 and val == 0:             # 거리가 20cm 안에 들어오고 스위치가 눌려있지 않으면
            pwm.start(50)                           # 피에조 부저음을 울렸다 끄며 LED가 빨강,초록 불과 노랑 불이 교차하며 꺼졌다 켜진다.
            GPIO.output(LED_PIN3, GPIO.HIGH)
            GPIO.output(LED_PIN2, GPIO.LOW)
            GPIO.output(LED_PIN1,GPIO.HIGH)
            time.sleep(1)
            pwm.ChangeDutyCycle(0)
            GPIO.output(LED_PIN1, GPIO.LOW)
            GPIO.output(LED_PIN2,GPIO.HIGH)
            GPIO.output(LED_PIN3, GPIO.LOW)
        else:
            pwm.stop()                              

        
        time.sleep(0.1)
finally :
    GPIO.cleanup()                                 # 종료 
    print('cleanup and exit')


        
