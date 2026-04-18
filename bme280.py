# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# From https://learn.adafruit.com/adafruit-bme280-humidity-barometric-pressure-temperature-sensor-breakout/python-circuitpython-test

import time

import adafruit_displayio_sh1107
import board
import displayio
import terminalio
from adafruit_bme280 import basic as adafruit_bme280

from adafruit_display_text import label
from i2cdisplaybus import I2CDisplayBus

displayio.release_displays()

# Create sensor object, using the board's default I2C bus.
# i2c = board.I2C()  # uses board.SCL and board.SDA
i2c = (
    board.STEMMA_I2C()
)  # For using the built-in STEMMA QT connector on a microcontroller

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


bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
# change this to match the location's pressure (hPa) at sea level
bme280.sea_level_pressure = 1010.0  # 2026-04-16T20:00-04:00

while True:
    temperature = bme280.temperature
    relative_humidity = bme280.relative_humidity
    pressure = bme280.pressure
    altitude = bme280.altitude

    # print("\nTemperature: %0.1f C" % bme280.temperature)
    # print("Humidity: %0.1f %%" % bme280.relative_humidity)
    # print("Pressure: %0.1f hPa" % bme280.pressure)
    # print("Altitude = %0.2f meters" % bme280.altitude)

    print(
        f"{temperature:>7.2f} C   {relative_humidity:>6.2f} % RH   {(pressure / 10):>6.2f} kPa"
    )

    text_area.text = "T:  %0.1f C" % temperature
    text_area2.text = "RH: %0.2f %%" % relative_humidity

    time.sleep(60)
