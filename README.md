# Airis – ESP32-C3 Environmental Monitor

Airis is a small ESP32-C3 based environmental monitor using:

- AHT20 (temperature + humidity)
- BMP280 (barometric pressure)
- SSD1306 128x64 OLED display

All sensors run on a shared I²C bus.

---

## Features

- Live temperature, humidity, and pressure readings  
- Compact OLED UI  
- Low-power ESP32-C3 platform  
- Modular design for future expansion (battery power, enclosure, WiFi, logging)

---

## Hardware

### Required Modules
- ESP32-C3 dev board  
- AHT20 sensor  
- BMP280 sensor  
- SSD1306 OLED display (I²C)  
- Breadboard + jumpers

### I²C Wiring

| Module | Pin | ESP32-C3 |
|--------|------|-----------|
| All devices | SDA | GPIO 4 |
| All devices | SCL | GPIO 5 |
| All devices | VCC | 3.3V |
| All devices | GND | GND |

Expected I²C addresses:
- AHT20: `0x38`
- BMP280: `0x77`
- SSD1306: `0x3C`

---

## Firmware

### Dependencies
Place the following drivers in the device filesystem:
- `aht20.py`
- `bmp280.py`
- `ssd1306.py`

### Example Application

```python
from machine import I2C, Pin
import time

import aht20
import bmp280
import ssd1306

i2c = I2C(0, scl=Pin(5), sda=Pin(4))

sensor = aht20.AHT20(i2c)
bmp = bmp280.BMP280(i2c, addr=0x77)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

while True:
    oled.fill(0)
    oled.text("Airis", 0, 0)

    oled.text("T: {:.1f} C".format(sensor.temperature), 0, 16)
    oled.text("H: {:.1f} %".format(sensor.relative_humidity), 0, 32)
    oled.text("P: {:.1f}".format(bmp.pressure), 0, 48)

    oled.show()
    time.sleep(1)
    
```
    
## Roadmap

### Phase 1: MVP (done)
•	ESP32-C3 running MicroPython
•	AHT20 + BMP280 + OLED on shared I²C
•	Basic realtime UI

### Phase 2: Power System
•	Add LiPo battery
•	Add charger module (TP4056 or MCP73831)
•	Add 3.3V regulator (AP2112 / MCP1700)

### Phase 3: Hardware Consolidation
•	Move from breadboard to perfboard or custom PCB
•	Add power switch and connectors
•	Route I²C cleanly

### Phase 4: Enclosure
•	3D printed case
•	Display frame
•	Vent holes for humidity sensor
•	Mounting points for board and battery

### Phase 5: UI/Software Improvements
•	Multi-screen UI
•	Min/max readings
•	Simple data logging
•	Optional: WiFi reporting
•	Optional: graphing mode

### Phase 6: Advanced Sensors (optional)
•	VOC / CO₂ (SGP30, CCS811, MH-Z19B)
•	Particulate matter (PMS5003)

## License

MIT
