import time

import adafruit_sht4x
import board

from display import Display

i2c = board.STEMMA_I2C()

display = Display(i2c)

sht = adafruit_sht4x.SHT4x(i2c)
print("Found SHT4x with serial number", hex(sht.serial_number))
sht.mode = adafruit_sht4x.Mode.NOHEAT_HIGHPRECISION

while True:
    temperature, relative_humidity = sht.measurements
    print(f"{temperature:>7.2f} C   {relative_humidity:>6.2f} % RH")

    display.set_temperature(temperature)
    display.set_relative_humidity(relative_humidity)

    time.sleep(60)
