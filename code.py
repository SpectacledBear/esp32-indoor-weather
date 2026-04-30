import time

import adafruit_bh1750
import adafruit_sht4x
import board

from display import Display

i2c = board.STEMMA_I2C()

display = Display(i2c)

sht = adafruit_sht4x.SHT4x(i2c)
print("Found SHT4x with serial number", hex(sht.serial_number))
sht.mode = adafruit_sht4x.Mode.NOHEAT_HIGHPRECISION

bh1750 = adafruit_bh1750.BH1750(i2c)

while True:
    temperature, relative_humidity = sht.measurements
    lux = bh1750.lux
    print(f"{temperature:>7.2f} C   {relative_humidity:>6.2f} % RH   {lux:>7.2f} lux")

    display.set_temperature(temperature)
    display.set_relative_humidity(relative_humidity)
    display.set_lux(lux)

    time.sleep(60)
