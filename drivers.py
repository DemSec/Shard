import time
import math
import RPi.GPIO as GPIO

MotorA_1 = 17
MotorA_2 = 27
MotorB_1 = 22
MotorB_2 = 23

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(MotorA_1, GPIO.OUT)
GPIO.setup(MotorA_2, GPIO.OUT)
GPIO.setup(MotorB_1, GPIO.OUT)
GPIO.setup(MotorB_2, GPIO.OUT)


def run_mode():
        motor(0)
        turn(0)

def motor(speed):
        if speed > 0:
                GPIO.output(MotorA_1, GPIO.LOW)
                GPIO.output(MotorA_2, GPIO.HIGH)
        elif speed < 0:
                GPIO.output(MotorA_1, GPIO.HIGH)
                GPIO.output(MotorA_2, GPIO.LOW)
        else:
                GPIO.output(MotorA_1, GPIO.LOW)
                GPIO.output(MotorA_2, GPIO.LOW)
        return 'null'

def turn(angle):
        if angle > 0:
                GPIO.output(MotorB_1, GPIO.LOW)
                GPIO.output(MotorB_2, GPIO.HIGH)
        elif angle < 0:
                GPIO.output(MotorB_1, GPIO.HIGH)
                GPIO.output(MotorB_2, GPIO.LOW)
        else:
                GPIO.output(MotorB_1, GPIO.LOW)
                GPIO.output(MotorB_2, GPIO.LOW)
        return 'null'

