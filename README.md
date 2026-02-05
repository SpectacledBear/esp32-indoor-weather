# ESP32 Indoor Weather Station

## Requirements

**Thonny.**

**CircuitPython**.
I used the [CircuitPython made for the Adafruit Feather ESP32 V2](https://circuitpython.org/board/adafruit_feather_esp32_v2/).
Specifically [this one](https://downloads.circuitpython.org/bin/adafruit_feather_esp32_v2/en_US/adafruit-circuitpython-adafruit_feather_esp32_v2-en_US-10.0.3.bin).

## Setup

I used ESP-IDF and its esptool.py to flash CircuitPython onto the device.

    esptool.py --port <COM_PORT> erase_flash
    
    esptool.py --port <COM_PORT> write_flash -z 0x0 adafruit-circuitpython-adafruit_feather_esp32_v2-en_US-10.0.3.bin
