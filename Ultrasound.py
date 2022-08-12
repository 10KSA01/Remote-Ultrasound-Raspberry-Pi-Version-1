import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)

TRIG = 13
ECHO = 25

# print "Distance Measurement In Progress"

GPIO.setwarnings(False)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
#Then, ensure that the Trigger pin is set low, and give the sensor a second to settle.
GPIO.output(TRIG, False)

# print "Waiting For Sensor To Settle"
time.sleep(2)

# print "1"
GPIO.output(TRIG, True)
# print "2"
time.sleep(0.00001)
GPIO.output(TRIG, False)

# print "3"
pulse_start = time.time()
while GPIO.input(ECHO)==0:
  pulse_start = time.time()
# print "4"
while GPIO.input(ECHO)==1:
  pulse_end = time.time()

pulse_duration = pulse_end - pulse_start

distance = pulse_duration * 17150
distance = round(distance, 2)

print(distance)

GPIO.cleanup()

