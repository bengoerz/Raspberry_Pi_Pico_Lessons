from machine import Pin, Timer
import time

# Setup pins for each light
light1green = Pin(15, Pin.OUT)
light1yellow = Pin(16, Pin.OUT)
light1red = Pin(17, Pin.OUT)

# Start with all lights off
light1green.off()
light1yellow.off()
light1red.off()

while True:    
    # Turn Light 1 Red
    light1yellow.off()
    light1red.on()
    time.sleep(6)
    
    # Light 1 Green
    light1red.off()
    light1green.on()
    time.sleep(6)
    
    # Turn light 1 Yellow
    light1green.off()
    light1yellow.on()
    time.sleep(2)