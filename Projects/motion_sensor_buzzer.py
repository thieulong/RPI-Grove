from grove.factory import Factory
from grove.factory import Factory

### connect motion sensor to pin 5 (slot D5)
pir = Factory.getGpioWrapper("PIRMotion", 5)

### connect buzzer to pin 12
buzzer = Factory.getGpioWrapper("Buzzer", 12)

while True:
    if pir.has_motion():
        buzzer.on()
    else:
        buzzer.off()
