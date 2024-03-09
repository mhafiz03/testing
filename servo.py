import RPi.GPIO as GPIO
import time

# Set GPIO numbering mode
def init_servo():
    global servo1
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11,GPIO.OUT)
    servo1 = GPIO.PWM(11,50) # pin 11 for servo1, pulse 50Hz
    servo1.start(0)

def rotate_servo(angle):
    global servo1
    angle = float(angle)
    servo1.ChangeDutyCycle(2+(angle/18))
    time.sleep(0.5)
    servo1.ChangeDutyCycle(0)

def stop_servo():
    global servo1
    servo1.stop()
    GPIO.cleanup()