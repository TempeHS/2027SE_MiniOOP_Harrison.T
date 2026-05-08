from machine import Pin
from time import sleep

# Wait for USB to become ready
sleep(0.1)

# store desired output pin in a variable
led_pin = 25
led2_pin = 15

# configure GPIO Pin as an output pin and create and led object for Pin
led = Pin(led_pin, Pin.OUT)
led2 = Pin(led2_pin, Pin.OUT)

while True:
    led.value(True)  # turn on the LED
    led2.value(False)  # turn off the LED2
    sleep(1)  # wait for one second
    led.value(False)  # turn off the LED
    led2.value(True)  # turn on the LED2
    sleep(1)  # wait for one second
