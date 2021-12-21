from flask import Flask
import RPi.GPIO as GPIO

LED_PIN1 = 22
LED_PIN2 = 27

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN1, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)

@app.route("/")
def home():
    return '''
        <p>Hello, Flask!</p>
        <a href="/led/red/on">RED LED ON</a>
        <a href="/led/red/off">RED LED OFF</a>
        <br>
        <a href="/led/blue/on">BLUE LED ON</a>
        <a href="/led/blue/off">BLUE LED OFF</a>
    '''
@app.route("/led/<color>/<op>")
def led_op(color,op):
    if color == "red":
        if op == "on":
            GPIO.output(LED_PIN1, GPIO.HIGH)
            return'''
            <p>RED LED ON</p>
            <a href="/">Go Home</a>
        '''
        elif op == "off":
            GPIO.output(LED_PIN1, GPIO.LOW)
            return'''
            <p>RED LED OFF</p>
            <a href="/">Go Home</a>
        '''
    elif color == "blue":
        if op == "on":
            GPIO.output(LED_PIN2, GPIO.HIGH)
            return'''
            <p>BLUE LED ON</p>
            <a href="/">Go Home</a>
        '''
        elif op == "off":
            GPIO.output(LED_PIN2, GPIO.LOW)
            return'''
            <p>BLUE LED OFF</p>
            <a href="/">Go Home</a>
        '''
        

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()