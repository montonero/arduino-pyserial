# Arduino Communication over USB with PySerial Code

This project demonstrates a way of communication PySerial code on a host machine with Arduino.

## Prerequisites
* Linux (or other *nix flavour) machine (e.g. Nonia N810, MacBook, etc).
* PySerial, PyGame installed.
* USB cable connecting host machine with Arduino (in case of N810 you need a female-female adapter).

## Instructions
1. Connect Arduino to a host PC with a USB cable.
2. Upload Arduino sketch (sketch/physical_pixel.ino) to it.
3. Run PySerial program on a host PC (code/arduino_led.py) in a console (this way you shall see debug output).