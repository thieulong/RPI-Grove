import time
from grove.grove_led import GroveLed

led = GroveLed(12)

while True:
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(1)