# picow-hid-example

## Control Pico W with Caps Lock Key

The CircuitPython program [code.py](code.py) was tested on a Pico W and uses the CAPS_LOCK keyboard key as a control mechanism.

The Pico W is connected via a USB cable to a computer and acting as a keyboard HID device.

The sample code uses the CAPS_LOCK status to control the starting and pausing of the program.

Being that Pico W does not have a user button, this is a great alternative for a push button that does not require soldering.

It may be possible to use NUMS_LOCK as an additional control mechanism.
