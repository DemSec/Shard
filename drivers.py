import time
import math
import RPi.GPIO as GPIO

MotorA_1 = 17
MotorA_2 = 27
MotorA_PWM = 18
MotorB_1 = 22
MotorB_2 = 23
MotorB_PWM = 13
LED_WhiteL = 24
LED_WhiteR = 25
LED_RedL = 26
LED_RedR = 16

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(MotorA_1, GPIO.OUT)
GPIO.setup(MotorA_2, GPIO.OUT)
GPIO.setup(MotorB_1, GPIO.OUT)
GPIO.setup(MotorB_2, GPIO.OUT)
GPIO.setup(LED_WhiteL, GPIO.OUT)
GPIO.setup(LED_WhiteR, GPIO.OUT)
GPIO.setup(LED_RedL, GPIO.OUT)
GPIO.setup(LED_RedR, GPIO.OUT)
GPIO.setup(MotorA_PWM, GPIO.OUT)
GPIO.output(MotorA_PWM, GPIO.HIGH)
GPIO.setup(MotorB_PWM, GPIO.OUT)
GPIO.output(MotorB_PWM, GPIO.HIGH)

#motorPWM = GPIO.PWM(MotorA_PWM,30)
#motorPWM.start(0)
#turnPWM = GPIO.PWM(MotorB_PWM,30)
#turnPWM.start(0)


def setup():
	#Empty for now, must resolve PWM global variable problem
	#PWM must be in a variable, but when executed here, the variable is lost
	return 'null'

def clamp(n,n_min,n_max): return max(n_min, min(n,n_max))

def motor(speed):
	speed = clamp(speed,-100,100)
	if speed > 0:
		GPIO.output(MotorA_1, GPIO.LOW)
		GPIO.output(MotorA_2, GPIO.HIGH)
	elif speed < 0:
		speed = -speed
		GPIO.output(MotorA_1, GPIO.HIGH)
		GPIO.output(MotorA_2, GPIO.LOW)
	else:
		GPIO.output(MotorA_1, GPIO.LOW)
		GPIO.output(MotorA_2, GPIO.LOW)
	#motorPWM.ChangeDutyCycle(speed)

def turn(angle):
	angle = clamp(angle,-100,100)
	if angle > 0:
		GPIO.output(MotorB_1, GPIO.HIGH)
		GPIO.output(MotorB_2, GPIO.LOW)
	elif angle < 0:
		angle = -angle
		GPIO.output(MotorB_1, GPIO.LOW)
		GPIO.output(MotorB_2, GPIO.HIGH)
	else:
		GPIO.output(MotorB_1, GPIO.LOW)
		GPIO.output(MotorB_2, GPIO.LOW)
	#turnPWM.ChangeDutyCycle(angle)

def ledFL(state):
	if state > 0:
		GPIO.output(LED_WhiteL, GPIO.HIGH)
	else:
		GPIO.output(LED_WhiteL, GPIO.LOW)

def ledFR(state):
	if state > 0:
		GPIO.output(LED_WhiteR, GPIO.HIGH)
	else:
		GPIO.output(LED_WhiteR, GPIO.LOW)

def ledRL(state):
	if state > 0:
		GPIO.output(LED_RedL, GPIO.HIGH)
	else:
		GPIO.output(LED_RedL, GPIO.LOW)

def ledRR(state):
	if state > 0:
		GPIO.output(LED_RedR, GPIO.HIGH)
	else:
		GPIO.output(LED_RedR, GPIO.LOW)

def lights(state):
	if state == 0:
		ledFL(0)
		ledFR(0)
		ledRL(0)
		ledRR(0)
	else:
		ledFL(1)
		ledFR(1)
		ledRL(1)
		ledRR(1)
