from machine import I2C, Pin

import aht20
import bmp280
import ssd1306

i2c = I2C(0, scl=Pin(5), sda=Pin(4))  # correct for ESP32-C3

sensor = aht20.AHT20(i2c)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
bmp = bmp280.BMP280(i2c, addr=0x77)

while True:
    oled.fill(0)
    oled.text("Airis", 0, 0)
    oled.text("T: {:.1f}C".format(sensor.temperature), 0, 16)
    oled.text("H: {:.1f}%".format(sensor.relative_humidity), 0, 32)
    oled.text("P: {:.1f}".format(bmp.pressure), 0, 48)
    oled.show()
