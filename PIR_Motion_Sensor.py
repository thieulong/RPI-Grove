import time
from grove.factory import Factory

### connect to pin 5(slot D5)
pir = Factory.getGpioWrapper("PIRMotion", 5)
while True:
    if pir.has_motion():
        print("Hi, people is moving")
    else:
        print("Watching")
    time.sleep(1)