from machine import Pin, PWM
from time import sleep, time


class Audio_Notification(PWM):
    def __init__(self, pin, debug=False):
        super().__init__(Pin(pin))
        self.__debug = debug
        self.duty_u16(0)
        self.__last_toggle_time = time()

    def warning_on(self):
        if self.__debug:
            print("Warning On")
        now = time()
        if now - last_toggle_time >= 0.5:
            self.beep(freq=500, duration=100)
            self.__last_toggle_time = now

    def beep(self, freq=100, duration=500):
        self.freq(freq)
        self.duty_u16(32768)
        sleep(duration / 1000)
        self.duty_u16(0)
        if self.__debug:
            print("Beep")
