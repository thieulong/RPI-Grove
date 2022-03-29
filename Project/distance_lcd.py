from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger
from grove.factory import Factory
import time

sonar = GroveUltrasonicRanger(12) # pin12, slot D12

dobj = Factory.getDisplay("JHD1802")
rows, cols = dobj.size()
dobj.setCursor(0, 0)
dobj.write("Distance:")

while True:
    dobj.setCursor(rows - 1, 0)
    dobj.write('{} cm'.format(round(sonar.get_distance(),2)))
    time.sleep(1)
