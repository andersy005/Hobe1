import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BOARD)  # tells RPI.GPIO to use the board numbering on RPI

Motor1A = 16  # pin 16 to turn the motor in one direction 
Motor1B = 18  # pin 18 to turn the motor in the other direction
Motor1E = 22  # Enable pin to turn the motor on

GPIO.setup(Motor1A, GPIO.OUT)
GPIO.setup(Motor1B, GPIO.OUT)
GPIO.setup(Motor1E, GPIO.OUT)

print "Turning motor on"
GPIO.output(Motor1A, GPIO.HIGH)
GPIO.output(Motor1B, GPIO.LOW)
GPIO.output(Motor1E, GPIO.HIGH)

sleep(10)  # turn the motors for 10 seconds then turn them off again.

print "Stopping motor"
GPIO.output(Motor1E, GPIO.LOW)

GPIO.cleanup()