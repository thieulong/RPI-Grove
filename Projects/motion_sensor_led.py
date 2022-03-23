from grove.factory import Factory
from grove.grove_led import GroveLed

### connect motion sensor to pin 5 (slot D5)
pir = Factory.getGpioWrapper("PIRMotion", 5)

### connect led to pin 12
led = GroveLed(12)

while True:
    if pir.has_motion():
        led.on()
    else:
        led.off()
