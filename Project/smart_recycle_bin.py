from grove.factory import Factory
from grove.grove_servo import GroveServo
import time

pir = Factory.getGpioWrapper("PIRMotion", 5)
servo = GroveServo(16)

servo.setAngle(0)

while True:
    if pir.has_motion():
        print('Motion detected!')
        # for x in range(150, 0, -1):
        #     servo.setAngle(x)
        #     time.sleep(0.01)
        servo.setAngle(150)
        time.sleep(2)
    else:
        servo.setAngle(0)
        print('Waiting ...')
    
    time.sleep(0.5)

