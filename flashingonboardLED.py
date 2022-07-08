# sometimes when you plug the pico in it doesnt work.
# this works on the pico w (wireless)
# so download the latest and greatest firmware from here
# https://www.raspberrypi.com/documentation/microcontrollers/micropython.html#drag-and-drop-micropython


import machine
import time
print("Hello")
led = machine.Pin("LED",machine.Pin.OUT)
while True:
   time.sleep(1)
   led.on()
   time.sleep(2)
   led.off()
