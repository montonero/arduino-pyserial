# Arduino Communication over USB with PySerial Code

This project demonstrates a way of communication PySerial code on a host machine with Arduino.

## Prerequisites
* Linux (or other *nix flavour) machine (e.g. Nonia N810, MacBook, etc).
* PySerial, PyGame installed.
* USB cable connecting host machine with Arduino (in case of N810 you need a female-female adapter).

## Instructions
1. Upload Arduino sketch (sketch/physical_pixel.ino) to it.
2. Run PySerial program on a host PC (code/arduino_led.py) in a console (this way you shall see debug output).
3. Click a square in the centre of the window to change LED's status on Arduino.


## Extra Instruction for N810
0. Arduino UNO r3 does not work - I am using Seeduino v3.
1. Flash N810 with a new kernel image:
```
./flasher-xyz --kernel zImage --flash --reboot
```
2. Install USB OTG Statusbar Plugin from here: https://garage.maemo.org/projects/usb-otg-plugin
3. Connect your arduino to N810 via USB, enable 'USB UTG Host Mode' and make sure that '/dev/ttyUSB0' does exist.
4. wget PySerial from http://sourceforge.net/projects/pyserial/files/ and copy 'serial' folder to '/usr/lib/python2.5/site-packages/'
5. Follow instruction for PC above.

### Copy-Paste Commands for N810
```
apt-get install python2.5-runtime
```