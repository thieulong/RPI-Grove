from grove.grove_light_sensor_v1_2 import GroveLightSensor
from grove.factory import Factory

# connect to alalog pin 2(slot A2)
sensor = GroveLightSensor(2)
### connect relay to pin 16
relay = Factory.getGpioWrapper("Relay",16)

while True:
    if sensor.light >= 30:
        relay.off()
    elif sensor.light < 30:
        relay.on()

