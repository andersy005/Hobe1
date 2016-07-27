from time import sleep, time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO_TRIG = 8   # sends the signal
GPIO_ECHO = 7   # listens for the signal

print "Distance Measurement in Progress"
GPIO.setup(GPIO_TRIG, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

GPIO.output(GPIO_TRIG, False)
print "Waiting for sensor to settle"
sleep(2)

GPIO.output(GPIO_TRIG, True)
sleep(0.00001)
GPIO.output(GPIO_TRIG, False)

while GPIO.input(GPIO_ECHO) == 0:
	pulse_start = time()

while GPIO.input(GPIO_ECHO)== 1:
	pulse_end = time()

pulse_duration = pulse_end - pulse_start

distance = pulse_duration * 17150

distance = round(distance, 3)

print "Distance: ",distance, "cm"

GPIO.cleanup()

