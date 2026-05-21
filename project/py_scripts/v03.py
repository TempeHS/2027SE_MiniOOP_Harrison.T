from machine import Pin
from time import sleep


class Led_light(Pin):
    # Sub Class inherits the 'Pin' Class
    def __init__(self, pin, flashing=False, debug=False):
        super().__init__(pin, Pin.OUT)
        self.__debug = debug
        self.__pin = pin
        self.__flashing = flashing

    def on(self):
        self.high()
        if self.__debug:
            print(f"LED connected to pin {self.__pin} is high")

    def off(self):
        if self.__debug:
            print(f"LED connected to pin {self.__pin} is low")

    def toggle(self):
        if self.value() == 0:
            self.high
            if self.__debug:
                print(f"LED connected to pin {self.__pin} is high")
        elif self.value() == 0:
            self.low
            if self.__debug:
                print(f"LED connected to pin {self.__pin} is low")


red_light = Led_light(3, False, True)
green_light = Led_light(6, False, False)


while True:
    red_light.on()
    green_light.on()
    sleep(1)
    red_light.off()
    green_light.off()
    sleep(1)
