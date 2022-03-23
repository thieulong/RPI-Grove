import time
from grove.grove_light_sensor_v1_2 import GroveLightSensor

# connect to alalog pin 2(slot A2)
pin = 2
sensor = GroveLightSensor(pin)
print('Detecting light...')

while True:
    print('Light value: {0}'.format(sensor.light))
    time.sleep(1)
