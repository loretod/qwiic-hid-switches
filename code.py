# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2021 Milad Hajihassan for Milador
# Demo of reading GPIO's status in TCA9534 bus-expander and sending a HID keycode over USB- Used for switch access assistive technology
#
# SPDX-License-Identifier: MIT

from adafruit_bus_device.i2c_device import I2CDevice
import board
import busio
import time
import neopixel
import community_tca9534
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Create I2C bus. Note, this project was build using QTpy ESP32-S3 other boards may have I2C over SCL and SDA.
i2c = busio.I2C(board.SCL1, board.SDA1)

# Create bus-expander instance.
tca9534 = community_tca9534.TCA9534(i2c)

#create pixel instance
pixel = neopixel.NeoPixel(board.NEOPIXEL,1)

# The keyboard object!
time.sleep(.5)  # Sleep for a bit to avoid a race condition on some systems
keyboard = Keyboard(usb_hid.devices)

# Main loop prints the GPIO zero status every half a second:
while True:
    gpio_zero_status = tca9534.get_gpio(0)
    gpio_one_status = tca9534.get_gpio(1)
    if not gpio_zero_status:
        pixel.fill((0,255,0))
        keyboard.press(Keycode.SPACE)
        keyboard.release_all()
    if not gpio_one_status:
        pixel.fill((0,0,255))
        keyboard.press(Keycode.TAB)
        keyboard.release_all()
    # Delay for half a second.
    time.sleep(0.2)
    pixel.fill((0,0,0))
