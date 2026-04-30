# ESP32 Indoor Weather Station

## Requirements

**Adafruit ESP32 Feather V2.**

**Adafruit 128x64 OLED FeatherWing.**

**Thonny.** A lightweight Python IDE that offers debugging and file utilities for my ESP32 device. This is how I transfer files and run scripts on the ESP32 device.

**CircuitPython.**
I used the [CircuitPython made for the Adafruit Feather ESP32 V2](https://circuitpython.org/board/adafruit_feather_esp32_v2/).
Specifically [this one](https://downloads.circuitpython.org/bin/adafruit_feather_esp32_v2/en_US/adafruit-circuitpython-adafruit_feather_esp32_v2-en_US-10.0.3.bin). I've included this binary file in the repo, for archival purposes.

**Adafruit BH1750 CircuitPython library.**
The [BH1750 library](https://github.com/adafruit/Adafruit_CircuitPython_BH1750), the [BusDevice library](https://github.com/adafruit/Adafruit_CircuitPython_BusDevice) and the [Registery library](https://github.com/adafruit/Adafruit_CircuitPython_Register) are used.

**Adafruit SHT45 CirtcuitPython library.**
The [SHT45 library](https://github.com/adafruit/Adafruit_CircuitPython_SHT4x) and the [BusDevice library](https://github.com/adafruit/Adafruit_CircuitPython_BusDevice) are used.

**Adafruit DisplayIO SH1107 CircuitPython library.**
The [SH1107 library](https://github.com/adafruit/Adafruit_CircuitPython_DisplayIO_SH1107) is used to drive the OLED FeatherWing and the [display_text library](https://github.com/adafruit/Adafruit_CircuitPython_Display_Text) is a helper library for displaying text using CircuitPython's displayio library.

**Alternative: Adafruit CircuitPython library bundle.**
Alternatively you can find all the sensor and display libraries and their dependencies in the comprehensive [CircuitPython driver bundle](https://github.com/adafruit/Adafruit_CircuitPython_Bundle).

## Setup

I used ESP-IDF and its esptool.py to flash CircuitPython onto the device.

    esptool.py --port <COM_PORT> erase_flash

    esptool.py --port <COM_PORT> write_flash -z 0x0 adafruit-circuitpython-adafruit_feather_esp32_v2-en_US-10.0.3.bin

Then copied the contents of the `lib/` directory to the root directory of the ESP32 device using the Thonny program.
