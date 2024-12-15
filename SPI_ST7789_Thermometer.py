# The Pico Explorer from Pimoroni has an SPI connected ST7789 display

# Use the driver found: https://github.com/russhughes/st7789_mpy/

# A micropython build with this built in is provided for the Pico here: 
# https://github.com/russhughes/st7789_mpy/blob/master/firmware/RP2/firmware.uf2

import machine
import time
import st7789
import vga1_16x16 as font

sck = machine.Pin(18)
mosi = machine.Pin(19)
cs = machine.Pin(17, machine.Pin.OUT)

# order appears to be significant for initialisation of the st7789 driver
spi = machine.SPI(0, baudrate=6250000, sck=sck, mosi=mosi)
miso = machine.Pin(16, machine.Pin.OUT)

display = st7789.ST7789(spi, 240, 240, cs=cs, dc=miso)

adc = machine.ADC(4)
conversion_factor = 3.3 / 65535

display.init()
display.fill(st7789.BLACK)

while True:
    reading = adc.read_u16() * conversion_factor
    temperature = 25 - (reading - 0.706) / 0.001721

    display.text(font, f"Temp: {temperature}", 0, 0, st7789.WHITE, st7789.BLACK)
    time.sleep(2)