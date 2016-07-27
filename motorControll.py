from gpiozero import Motor
from time import sleep

motor1 = Motor(16,20)
motor2 = Motor(23,24)

print "Moving the motors forwards"
motor1.forward(speed=0.5)
motor2.forward(speed=0.5)
sleep(2)
motor1.stop()
motor2.stop()

print "Moving the motors backwards"
motor1.backward()
motor2.backward()
sleep(3)

print "Changing speeds of the motors"
motor1.backward(speed=0.7)
motor2.backward(speed=0.3)

print "Moving the motors in different directions"
motor1.forward()
motor2.backward(speed=0.8)
sleep(3)

print "Stopping the motors"
motor1.stop()
motor2.stop()

