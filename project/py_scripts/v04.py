from lib.led_light import Led_Light
from time import sleep, time

red_light = Led_Light(6, True, True)

while True:
    red_light.flash()
    print(1)
    sleep(0.1)
