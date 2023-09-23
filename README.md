# picow-hid-example

## Control Pico with Caps Lock Key

The [code.py](code.py) file is a CircuitPython program tested on a Pico W that uses CAPS_LOCK as a control mechanism.

The Pico is connected via a USB cable to a computer and acting as a keyboard HID device.

The sample code uses the CAPS_LOCK status to control the starting and pausing of the program.

Being that Pico does not have a user button, this is a great alternative for a push button that does not require soldering.

It may be possible to use NUMS_LOCK as an additional control mechanism.
