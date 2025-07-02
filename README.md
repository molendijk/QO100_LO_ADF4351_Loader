# QO100_LO_ADF4361_Loader

## Purpose

In order to create an 2.4 GHz uplink to the QO100 geostationary satelite 
using a standard HF transmitter operating at maximally 50 MHz (6m), the
up-converter needs to be supplied with an LO of 2350 MHz. Such an LO can
be easily created by using the ADF4361 synthesizer evaluation board as
available from multiple sources at AliExpress.

The only issue with these evaluation boards is the necessity to connect
an external ADF4351 register loader to the SPI-like port.

This project proposes a micropython based ADF4361 register loader for QO100,
that writes all required registers for the generation of a 2350 MHz LO.
The python source ... can be uploaded to a micropython system.

## Getting Started



## Implementation
