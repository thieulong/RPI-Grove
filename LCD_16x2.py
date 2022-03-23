import time
from grove.factory import Factory
#I2C Camera
# LCD 16x2 Characters
dobj = Factory.getDisplay("JHD1802")
# If it's OLED Display 1.12"
# dobj = Factory.getDisplay("SH1107G")
rows, cols = dobj.size()
print("LCD model: {}".format(dobj.name))
print("LCD type : {} x {}".format(cols, rows))

dobj.setCursor(0, 0)
dobj.write("hello world!")
dobj.setCursor(0, cols - 1)
dobj.write('X')
dobj.setCursor(rows - 1, 0)
for i in range(cols):
    dobj.write(chr(ord('A') + i))

time.sleep(3)
dobj.clear()