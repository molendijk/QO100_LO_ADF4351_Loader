# QO100_LO_ADF4351_Loader

## Purpose

In order to create an 2.4 GHz uplink to the QO100 geostationary satelite 
using a standard HF transmitter operating at maximally 50 MHz (6m), the
up-converter needs to be supplied with an LO of 2350 MHz. Such an LO can
be easily created by using the ADF4351 synthesizer evaluation board as
available from multiple sources at AliExpress.

The only issue with these evaluation boards is the necessity to connect
an external ADF4351 register loader to the SPI-like port.

This project proposes a micropython based ADF4351 register loader for QO100,
that writes all required registers for the generation of a 2350 MHz LO.
The python source ADF4351_Loader.py can be uploaded to a micropython system.

## Getting Started

Download the basic micropython for the D1-mini (or other ESP8266) **.bin** file
from:
https://micropython.org/download/?mcu=esp8266
Connect the D1-mini USB port with a USB data-cable to the PC.
You may need to install the CH340 COM port driver:
https://github.com/SoldierJazz/CH341SER-Driver-For-ch340-ch341 or directly
from china: https://www.wch-ic.com/downloads/ch341ser_exe.html
to see the D1-mini's COM port under the Windows device manager.

Once this works get a D1-mini flash tool, like for instance Tasmotizer:
https://github.com/tasmota/tasmotizer/releases
Open tasmotizer, browse to the bin file and hit "Tasmotize".
After a successful erase and flash, reboot the device, close Tamotizer
and download Thonny from:
https://thonny.org/

From thonny:
- Tools -> Options -> Interpreter
	- select: "MicroPython (ESP8266) from the dropdown menu
	- Port or WebREPL, select like: "USB Serial @ COM8"
	
- File -> Open -> This Computer
	- browse to and load the ADF4351_Loader.py
Now flash this file to the D1-mini:
- File -> Save Copy "MicroPython device"
	- On the target device either click on main.py or enter the name on
	the target as "main.py".

Done.

## Connections D1-mini to ADF4351 Eval board V1.4

D1-mini	ADF4351	SPI
D2		LE		CS
D5		CLK		SCK
D7		DAT		MOSI
Gnd		Gnd

Enable the chip:
ADF4351 ADF4351
CE		3V3

## Load the ADF4351 registers

A reboot of the D1-mini will execute the code and load the ADF4351 
registers to generate the 2350 MHz LO.

## Implementation

The goal is to achieve the cleanest possible spectrum.
Using the ADF4351 in Integer mode, spurs are naturally absent.
The LO frequency was choden to be 2350 MHz, which is an exact 
integer multiple of the on-board reference clock, 25 MHz,
of the ADF4351 Eval board.

In addition the idea is even to replace the local 25 MHz oscillator 
with an externally generated GPS Diciplined Oscillator 
reference of 25 MHz to achieve a very precise LO frequency not subject
to drift.

![The ADF4351 Software](/Images/ADF435x_Software_Main.png)