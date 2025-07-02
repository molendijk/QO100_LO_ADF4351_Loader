# ADF4351 Loader configured for f-out = 2350MHz using Integer synthesis.
# RF Frequency = 2350 MHz, Reference Frequency = 25 MHz, R counter = 1,
# Pre-scaler = 4/5, Feedback signal = fundamental, N = 94, Frac = 0,
# Low-noise mode, Double-buf = disabled, Charge-pump crrent = 5 mA, LDF = INT_N,
# LDP = 10 ns, PD Polariry = positive, Clock Divider Value = 0, Clock Div Mode = Off,
# ABP = 3 ns (INT_N), CSR = disabled, Aux Output Enable = Disabled,
# RF Output Enable = Enabled, RF Output Power = +5 dBm, Band Select Clock = Auto set.

version = 20250701

from machine import Pin, SPI
import time

# The 6 ADF435x registers, 32-bit each
# The order R5 downto R0 is critical for the loading of the synthesizer
registers = [
    0x00580005,  # R5
    0x008C803C,  # R4
    0x00400003,  # R3
    0x00005F42,  # R2
    0x00008011,  # R1
    0x002F0000   # R0 (Dbl buffer = off, no need to write twice)
]

# Reverse the order is required by the ADF435x (R5 down to R0)
# registers.reverse()

# Initialize SPI @1Mbps
spi = SPI(1, baudrate=1000000, polarity=0, phase=0) 

cs = Pin(4, mode=Pin.OUT, value=1)      # Create chip-select on pin 4 = D2.

def send_register(value):
    # Convert 32-bit value to a bytearray with 4 bytes (MSB first)
    # data = bytearray([
        # (value >> 24) & 0xFF,
        # (value >> 16) & 0xFF,
        # (value >> 8) & 0xFF,
        # value & 0xFF
    # ])
    data = value.to_bytes(4)
    
    # for bt in data:
        # print(bt)
    cs(0) # select peripheral
    spi.write(data)
    cs(1) # deselect peripheral

# Send registers
time.sleep(1.0) # Wait one second to allow the ADF4351 to power-up
for reg in registers:
    send_register(reg)

print('ADF4351_Loader, version: ', version,' Registers successfully written.')