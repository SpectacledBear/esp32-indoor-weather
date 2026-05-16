import time

import adafruit_bh1750
import adafruit_sht4x
import board

from display import Display

MEASUREMENT_INTERVAL_SECONDS = 60

# TODO: Handle i2C sensors not being present, and display an error message on the display instead of crashing.
i2c = board.STEMMA_I2C()

display = Display(i2c)

sht = adafruit_sht4x.SHT4x(i2c)
sht.mode = adafruit_sht4x.Mode.NOHEAT_HIGHPRECISION

bh1750 = adafruit_bh1750.BH1750(i2c)

next_measurement_time = time.monotonic()

while True:
    display.update()  # update display state

    if time.monotonic() > next_measurement_time:
        next_measurement_time += MEASUREMENT_INTERVAL_SECONDS

        temperature, relative_humidity = sht.measurements
        temperature = round(temperature)
        relative_humidity = round(relative_humidity)
        lux = round(bh1750.lux)
        print(f"{temperature:>3} C  {relative_humidity:>3} % RH  {lux:>4} lux")

        display.set_temperature(temperature)
        display.set_relative_humidity(relative_humidity)
        display.set_lux(lux)

