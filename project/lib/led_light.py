from machine import Pin
from time import sleep, time


class Led_Light(Pin):
    """Control an LED connected to a Raspberry Pi Pico GPIO pin.

    Args:
        pin (int): GPIO pin number connected to the LED.
        flashing (bool, optional): Enable timed flashing logic in `flash()`.
        debug (bool, optional): Print debug messages when LED state changes.

    Example:
        led = Led_Light(25, flashing=True, debug=True)
        led.on()
        led.off()
        led.toggle()
        led.flash()
    """

    # Sub Class inherits the 'Pin' Class
    def __init__(self, pin, flashing=False, debug=False):
        super().__init__(pin, Pin.OUT)
        self.__debug = debug
        self.__pin = pin
        self.__flashing = flashing
        self.led_light_state
        self.__last_toggle_time = time()

    def on(self):
        """Turn the LED on (set pin high)."""

        self.high()
        if self.__debug:
            print(f"LED connected to pin {self.__pin} is high")

    def off(self):
        """Turn the LED off (set pin low)."""

        self.low()
        if self.__debug:
            print(f"LED connected to pin {self.__pin} is low")

    def toggle(self):
        """Toggle the LED state."""
        if self.value() == 0:
            self.on()
        elif self.value() == 1:
            self.off()

    @property
    def led_light_state(self):
        """Return the current LED pin value (0 or 1)."""

        # Getter Method
        return self.value

    @led_light_state.setter
    def led_light_state(self, value):
        """Set LED state.

        Args:
            value (int | bool): 1/True for on, 0/False for off.
        """

        # Setter Method
        if value == 1:
            self.off()
        elif value == 0:
            self.on()

    def flash(self):
        """Toggle the LED every 0.5 seconds when flashing is enabled."""

        now = time()
        if self.__flashing and now - self.__last_toggle_time >= 0.5:
            self.toggle()
            self.__last_toggle_time = now
