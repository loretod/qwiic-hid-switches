# qwiic-hid-switches
A circuitpython project using Milador's Qwiic (https://github.com/milador/Qwiic-Adaptive-Switch) no solder boards for HID switch access to computers and mobile devices.

This is a simplified code that sends a HID keycode (SW1 => SPACE and SW2 => TAB) when a wired switch is connected at each jack.

The project uses circuitpython (version 7) to encourage novice users to modify and use the code.

The following circuitpython stock libraries are needed in the lib folder:
- adafruit_bus_device
- adafruit_hid
- adafruit_pixelbuf.mpy
- neopixel.mpy

The following additional library is needed in the lib folder: Community_CircuitPython_TCA9534 (https://github.com/milador/Community_CircuitPython_TCA9534) library is used.

The following wiring is needed:

USB cable => MCU/ board (this project uses the QTpy ESP32-S2) => Qwiic Adaptive Switch Input board => Assistive tech switches

*With the addition of a USB to Lightning dongle, this set up may be used for switch access on iOS devices.

Image:
![USB cable connected to a controller with a custom board connected via grove wire. two switches are connected to the custom board](/qwiic-hid-setup.jpg "Qwiic HID Set Up")


To modify the keycode being sent on switch press, visit the Adafruit HID documentation: https://docs.circuitpython.org/projects/hid/en/latest/_modules/adafruit_hid/keycode.html

** If you would like to use this set up for iOS access, do not use any number or letter codes as the iOS will not recognize those as a switch press. The use of modifier and function keys is successful.

See image below for a demo of the set up to use 2 switch scanning for general iOS navigation:
![hand pressing one switch to navigate through icons. Second switched pressed to select highlighted icon](/iOS-demo.gif "iOS Demo")
