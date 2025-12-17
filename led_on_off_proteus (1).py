from machine import Pin
import time

# Initialize LED pin
led = Pin(15, Pin.OUT)

while True:
    led.on()          # Turn LED ON
    time.sleep(1)     # Delay 1 second

    led.off()         # Turn LED OFF
    time.sleep(1)     # Delay 1 second
