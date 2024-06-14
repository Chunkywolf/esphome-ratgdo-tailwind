
# ratgdo for ESPHome for Tailwind use

This is a fork of the port of the ratgdo software for the v2.0/v2.5 board to ESPHome. It allows the use of a ratgdo with a tailwind iq3 connected to the dry contacts.
It has been modified from the normal esphome-ratgdo firmware in the following ways:
1. Both the open and close dry contact inputs have been changed to be door toggle inputs. This allows the Tailwind's door button output to connect to one of them and the ground pin to allow it to trigger both opening and closing the door. The other of the open/closed input pins can be used to wire up a simple doorbell button to actuate the door.
2. The door open output pin has been adjusted to tie to ground only when the door is fully closed. This allows the use of a Tailwind without needing to wire a magentic switch to sense open.

Most of this content was created and is maintained by Paul Wieland 

[Visit the github.io page to purchase boards](https://paulwieland.github.io/ratgdo/#order)

## Installation

- Flash the ESPHome based firmware using the [Web Installer](https://ratgdo.github.io/esphome-ratgdo/)

It is no longer necessary to save the rolling code counter when switching between firmware.

## First use after adding to Home Assistant

The ESPHome firmware will allow you to open the door to any position after calibration. To calibrate the door, open and close it once without stopping.

<img width="560" alt="position_demo" src="https://github.com/RATGDO/esphome-ratgdo/assets/663432/22a9873e-67bb-4b2f-bb32-70047cfe666d">

## ESPHome config

- [Security+ 2.0 for v2.0 board with ESP8266 D1 Mini](https://github.com/RATGDO/esphome-ratgdo/blob/main/static/v2board_esp8266_d1_mini.yaml)
- [Security+ 2.0 for v2.0 board with ESP8266 D1 Mini lite](https://github.com/RATGDO/esphome-ratgdo/blob/main/static/v2board_esp8266_d1_mini_lite.yaml)
- [Security+ 2.0 for v2.0 board with ESP32 D1 Mini](https://github.com/RATGDO/esphome-ratgdo/blob/main/static/v2board_esp32_d1_mini.yaml)
- [Security+ 2.0 for v2.0 board with ESP32 Lolin D2 Mini](https://github.com/RATGDO/esphome-ratgdo/blob/main/static/v2board_esp32_lolin_s2_mini.yaml)
- [Security+ 2.0 for v2.5 board with ESP8266 D1 Mini](https://github.com/RATGDO/esphome-ratgdo/blob/main/static/v25board_esp8266_d1_mini.yaml)
- [Security+ 1.0 for v2.5 board with ESP8266 D1 Mini](https://github.com/RATGDO/esphome-ratgdo/blob/main/static/v25board_esp8266_d1_mini_secplusv1.yaml)
- [Security+ 2.0 for v2.5 board with ESP8266 D1 Mini lite](https://github.com/RATGDO/esphome-ratgdo/blob/main/static/v25board_esp8266_d1_mini_lite.yaml)
- [Security+ 1.0 for v2.5 board with ESP8266 D1 Mini lite](https://github.com/RATGDO/esphome-ratgdo/blob/main/static/v25board_esp8266_d1_mini_lite_secplusv1.yaml)
- [Security+ 2.0 for v2.5 board with ESP32 D1 Mini](https://github.com/RATGDO/esphome-ratgdo/blob/main/static/v25board_esp32_d1_mini.yaml)
- [Security+ 1.0 for v2.5 board with ESP32 D1 Mini](https://github.com/RATGDO/esphome-ratgdo/blob/main/static/v25board_esp32_d1_mini_secplusv1.yaml)
- [Security+ 2.0 for v2.5i/2.52i/2.53i board](https://github.com/RATGDO/esphome-ratgdo/blob/main/static/v25iboard.yaml)
- [Security+ 1.0 for v2.5i/2.52i/2.53i board](https://github.com/RATGDO/esphome-ratgdo/blob/main/static/v25iboard_secplusv1.yaml)

- [Web Installer](https://ratgdo.github.io/esphome-ratgdo/)

![Home Assistant Screen Shot](static/hass.png)
