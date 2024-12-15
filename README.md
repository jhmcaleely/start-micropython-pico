# start-micropython-pico
Exercises from ["Get Started with MicroPython on Raspberry Pi Pico"][gettingstarted], 2nd Edition

> [!NOTE]
> Wifi based exercises need a 'wifi.py' file adding alongside them, eg:

`wifi.py`:
```python
ssid = "Your 2.4GHz WiFi Name"
psk = "Your WiFi Password"
```

Parts Needed:

- Raspberry Pi Pico WH (W variant needed for chapter 11 & 12 only) (x2 for chapter 12)
- Micro USB cable
- Breadboard
- LED (red, green, amber)
- 330ohm Resistor (x3)
- Jumper leads
- Breadboard pushbutton (x2)
- Active Piezo Buzzer
- PIR sensors
  - [HC-SR1501 Type PIR][pihutlarge] 
  - (optional) [Mini PIR][pihutmini] 
- 10Kohm Potentiometer
- I2C Display, SSD1306 based
  - [128x64 OLED display][pihuti2c]
- SPI Display, ST7789 based
  - [Pico Exporer Display][pimoronispi]
- WS2821b/NeoPixel LEDs. I used a [Pimoroni Plasma Stick 2040W][pimoroni2040w] Kit.
 
Parts are just examples I selected that I either had on hand or could easily source.

[gettingstarted]: https://store.rpipress.cc/collections/latest-bookazines/products/get-started-with-micropython-on-raspberry-pi-pico-2nd-edition
[pihutlarge]: https://thepihut.com/products/pir-motion-sensor-module?variant=758602485
[pihutmini]: https://thepihut.com/products/breadboard-friendly-mini-pir-motion-sensor-with-3-pin-header?variant=39749999788227
[pihuti2c]: https://thepihut.com/products/0-96-oled-display-module-128x64?variant=42810024820931
[pimoronispi]: https://shop.pimoroni.com/products/pico-explorer-base?variant=32369514315859
[pimoroni2040w]: https://shop.pimoroni.com/products/wireless-plasma-kit?variant=40372594704467
