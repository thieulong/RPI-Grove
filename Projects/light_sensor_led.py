from grove.grove_light_sensor_v1_2 import GroveLightSensor
from grove.grove_led import GroveLed

# connect to alalog pin 2(slot A2)
sensor = GroveLightSensor(2)
### connect led to pin 12
led = GroveLed(12)

while True:
    if sensor.light >= 50:
        led.off()
    elif sensor.light < 50:
        led.on()

