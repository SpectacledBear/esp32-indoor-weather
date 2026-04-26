import time

import adafruit_displayio_sh1107
import adafruit_sht4x
import board
import displayio
import terminalio
from adafruit_display_text import label
from i2cdisplaybus import I2CDisplayBus

displayio.release_displays()

i2c = board.STEMMA_I2C()

# SH1107 is vertically oriented 64x128
WIDTH = 128
HEIGHT = 64
BORDER = 2
display_bus = I2CDisplayBus(i2c, device_address=0x3C)
display = adafruit_displayio_sh1107.SH1107(display_bus, width=WIDTH, height=HEIGHT)
display.auto_refresh = True
# Make the display context
splash = displayio.Group()
display.root_group = splash

text1 = "T:  0.0 C"  # overly long to see where it clips
text_area = label.Label(terminalio.FONT, text=text1, color=0xFFFFFF, x=8, y=8)
splash.append(text_area)
text2 = "RH: 0.00 %%"
text_area2 = label.Label(terminalio.FONT, text=text2, color=0xFFFFFF, x=8, y=20)
splash.append(text_area2)

sht = adafruit_sht4x.SHT4x(i2c)
print("Found SHT4x with serial number", hex(sht.serial_number))
sht.mode = adafruit_sht4x.Mode.NOHEAT_HIGHPRECISION

while True:
    temperature, relative_humidity = sht.measurements
    print(f"{temperature:>7.2f} C   {relative_humidity:>6.2f} % RH")

    text_area.text = "T:  %0.1f C" % temperature
    text_area2.text = "RH: %0.2f %%" % relative_humidity

    time.sleep(60)
