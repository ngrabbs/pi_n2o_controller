import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
sol_freq = 15
pwm = GPIO.PWM(18, sol_freq)
pwm.start(50)
time.sleep(1.50)
pwm.ChangeDutyCycle(90)
time.sleep(2)
pwm.ChangeDutyCycle(100)
time.sleep(2)
GPIO.cleanup()
