import adafruit_displayio_sh1107
import displayio
import terminalio
from adafruit_display_text import label
from i2cdisplaybus import I2CDisplayBus

from buttons import Buttons

# SH1107 is vertically oriented 64x128
WIDTH = 128
HEIGHT = 64
BORDER = 2

displayio.release_displays()


class Display:
    def __init__(self, i2c):
        self.display_bus = I2CDisplayBus(i2c, device_address=0x3C)
        self.display = adafruit_displayio_sh1107.SH1107(
            self.display_bus, width=WIDTH, height=HEIGHT
        )
        self.display.auto_refresh = True
        # Make the display context
        self.splash = displayio.Group()
        self.display.root_group = self.splash

        text1 = "T:  0 C"  # overly long to see where it clips
        self.text_area = label.Label(
            terminalio.FONT, text=text1, color=0xFFFFFF, x=8, y=8
        )
        self.splash.append(self.text_area)
        text2 = "RH: 0 %"
        self.text_area2 = label.Label(
            terminalio.FONT, text=text2, color=0xFFFFFF, x=8, y=20
        )
        self.splash.append(self.text_area2)
        text3 = "L:  0 lux"
        self.text_area3 = label.Label(
            terminalio.FONT, text=text3, color=0xFFFFFF, x=8, y=32
        )
        self.splash.append(self.text_area3)

        self.buttons = Buttons()

        self.display_hidden = False

    def set_temperature(self, temperature):
        self.text_area.text = f"T:  {round(temperature)} C"

    def set_relative_humidity(self, relative_humidity):
        self.text_area2.text = f"RH: {round(relative_humidity)} %"

    def set_lux(self, lux):
        self.text_area3.text = f"L:  {round(lux)} lux"

    def update(self):
        self.buttons.update()

        if self.buttons.button_a_pressed():
            self.splash.hidden = not self.splash.hidden
