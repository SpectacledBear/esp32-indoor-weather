# ESP32 Indoor Weather Station

## Requirements

**Adafruit ESP32 Feather V2.**

**Thonny.** A lightweight Python IDE that offers debugging and file utilities for my ESP32 device. This is how I transfer files and run scripts on the ESP32 device.

**CircuitPython**.
I used the [CircuitPython made for the Adafruit Feather ESP32 V2](https://circuitpython.org/board/adafruit_feather_esp32_v2/).
Specifically [this one](https://downloads.circuitpython.org/bin/adafruit_feather_esp32_v2/en_US/adafruit-circuitpython-adafruit_feather_esp32_v2-en_US-10.0.3.bin). I've included this binary file in the repo, for archival purposes.

**Adafruit BME280 CircuitPython library.**
The [BME280 library](https://github.com/adafruit/Adafruit_CircuitPython_BME280) and the [BusDevice library](https://github.com/adafruit/Adafruit_CircuitPython_BusDevice) are used.
Alternatively you could use the comprehensive [CircuitPython driver bundle](https://github.com/adafruit/Adafruit_CircuitPython_Bundle).
The required libraries are included in the `lib/` directory.

## Setup

I used ESP-IDF and its esptool.py to flash CircuitPython onto the device.

    esptool.py --port <COM_PORT> erase_flash

    esptool.py --port <COM_PORT> write_flash -z 0x0 adafruit-circuitpython-adafruit_feather_esp32_v2-en_US-10.0.3.bin

Then copied the `adafruit_bme280` and `adafruit_bus_device` libraries from the `lib/` directory to the ESP32 device using Thonny.
