# This is a CircuitPython program tested on a Pico W.
# The Pico is connected via a USB cable to a computer and acting as a keyboard.
# This program uses the CAPS_LOCK status to control the starting and pausing of the program.
# It may be possible to use NUMS_LOCK as well as an additional control mechanism.
import board
import digitalio
import time
import usb_hid
# download the CircuitPython bundle from https://circuitpython.org/libraries
# from the bundle, copy the adafruit_hid directory to the pico lib directory
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

print("-----------------------------------------------------")
print("[Program is paused. Press CAPS_LOCK to start program]")
paused = True

while True:

    if paused:
        # if paused, check if CAPS_LOCK is ON
        if kbd.led_on(Keyboard.LED_CAPS_LOCK):
            paused = False
            print("-------------------------------------------")
            print("User turned CAPS_LOCK on. Starting program.")
            time.sleep(.1)
            print("Turning CAPS_LOCK off so the computer keyboard can continue to be used as normal.")
            print("-")
            kbd.send(Keycode.CAPS_LOCK)
            time.sleep(.3)
        else:
            #print("Program is paused. [Press CAPS_LOCK to start program...]")
            time.sleep(1)

            
    else:
        if kbd.led_on(Keyboard.LED_CAPS_LOCK):
            paused = True
            print("----------------------------------------------------------------------------------------")
            print("User turned CAPS_LOCK on while program was running. Pausing program and turning LED off.")
            print("Turning CAPS_LOCK off so the computer keyboard can continue to be used as normal.")
            print("-")
            print("[Program is paused. Press CAPS_LOCK to start program...]")
            kbd.send(Keycode.CAPS_LOCK)
            time.sleep(.3)
            led.value = False
        else:
            print("Program is running, LED is on. [Press CAPS_LOCK to pause program]")
            led.value = True
            time.sleep(1)
            
