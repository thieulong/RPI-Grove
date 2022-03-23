import time
from grove.grove_sound_sensor import GroveSoundSensor

# connect to alalog pin 2(slot A2)
PIN = 2

sensor = GroveSoundSensor(PIN)

print('Detecting sound...')
while True:
    print('Sound value: {0}'.format(sensor.sound))
    time.sleep(.3)
