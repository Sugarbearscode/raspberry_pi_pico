#. SSD1306 GND to GND PICO (PIN 38)
#  SSD1306 VCC to 3.3 PICO (PIN 36)
#. SSD1306 
#
#
#

from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

i2c=I2C(1,sda=Pin(2), scl=Pin(3), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

oled.text("||||||||||||||||", 0, 0)
oled.text("00000000000000000", 0, 8)
oled.text("00000000000000000", 0, 16)
oled.show()
