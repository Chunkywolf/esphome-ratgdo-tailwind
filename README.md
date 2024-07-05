
# ratgdo for ESPHome for Tailwind use on a security 2.0+ opener with a 2.5i board

This is a fork of the port of the ratgdo software for the v2.5 board to ESPHome. It allows the use of a ratgdo with a tailwind iq3 connected to the dry contacts.
It has been modified from the normal esphome-ratgdo firmware in the following ways:
1. Both the open and close dry contact inputs have been changed to be door toggle inputs. This allows the Tailwind's door button output to connect to one of them and the ground pin to allow it to trigger both opening and closing the door. The other of the open/closed input pins can be used to wire up a simple doorbell button to actuate the door.
2. The door open output pin has been adjusted to tie to ground only when the door is fully closed. This allows the use of a Tailwind without needing to wire a magentic switch to sense open.

Most of this content was created and is maintained by Paul Wieland 

[Visit the github.io page to purchase boards](https://paulwieland.github.io/ratgdo/#order)

## Installation
- Install with the original esphome firmware

- In esphome, edit the device, replace:
    
packages:<br>
&nbsp;ratgdo.esphome: github://ratgdo/esphome-ratgdo/v25iboard.yaml@main

- with:

packages:<br>
&nbsp;ratgdo.esphome: github://Chunkywolf/esphome-ratgdo-tailwind/v25iboard.yaml@main

- Click install, and choose wirelessly.
