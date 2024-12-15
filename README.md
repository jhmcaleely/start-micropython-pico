# start-micropython-pico
Exercises from "Get Started with MicroPython on Raspberry Pi Pico"

> [!NOTE]
> Wifi based exercises need a 'wifi.py' file adding alongside them, eg:

`wifi.py`:
```python
ssid = "Your 2.4GHz WiFi Name"
psk = "Your WiFi Password"
```

Parts Needed:

- Raspberry Pi Pico WH (W variant needed for chapter 11 & 12 only) (x2 for chapter 12)
- Breadbaord
- LED (Red, green, amber)
- 330ohm Resistor (x3)
- Jumper Leads
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
 
Parts are just examples I selected that I either had on hand or could easily source.
  
[pihutlarge]: https://thepihut.com/products/pir-motion-sensor-module?variant=758602485
[pihutmini]: https://thepihut.com/products/breadboard-friendly-mini-pir-motion-sensor-with-3-pin-header?variant=39749999788227
[pihuti2c]: https://thepihut.com/products/0-96-oled-display-module-128x64?variant=42810024820931
[pimoronispi]: https://shop.pimoroni.com/products/pico-explorer-base?variant=32369514315859
