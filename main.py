import machine

import ssd1306

i2c = machine.I2C(0, scl=machine.Pin(5), sda=machine.Pin(4))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

oled.fill(0)
oled.text("driver works", 0, 0)
oled.show()
