import time
from grove.grove_loudness_sensor import GroveLoudnessSensor

# connect to alalog pin 2(slot A2)
PIN = 2

sensor = GroveLoudnessSensor(PIN)

print('Detecting loud...')
while True:
    value = sensor.value
    if value > 10:
        print("Loud value {}, Loud Detected.".format(value))
        time.sleep(.5)