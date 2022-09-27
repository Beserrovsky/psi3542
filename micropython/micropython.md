# Using MicroPython in microcontoler via terminal

## Tools

- ampy -> ls, put and run python scripts in module
- picocom -> REPL
- esptool -> erase and flash firmware

## Keep in Mind

Baudrate: 115200
Port: Normally /dev/ttyUSB0

## Getting micropython

[ESP32](https://micropython.org/download/esp32/)
[ESP8266](https://micropython.org/download/esp8266-1m/)

## Flashing micropython

`esptool.py --port /dev/ttyUSB0 erase_flash`
> Erase old firm

`esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 FIRMWARE.bin`
> Flash new firm

## REPL -> Read Eval Print Loop

`picocom -b 115200 /dev/ttyUSB0`
> Start REPL

## Managing scripts

`ampy -p /dev/ttyUSB0 -b 115200 ls`
> List stuff in microcontroler

`ampy -p /dev/ttyUSB0 -b 115200 put FILE.py`
> Put file/library in microcontroler

`ampy -p /dev/ttyUSB0 -b 115200 run FILE.py`
> Run file in microcontroler

