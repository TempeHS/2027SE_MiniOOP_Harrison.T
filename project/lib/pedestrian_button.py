from machine import Pin
from time import ticks_ms, ticks_diff


class Pedestrian_Button(Pin):
    """Sub class inherits the Super 'Pin Class

        Arg:
            pin (int): GPIO pin number connected to the LED.
            debug (bool, optional): Print debug messages when LED state changes.
        Example:
        button = Pedestrian_button(15, debug=True)
        if button.button_state():
            # Pedestrian is waiting
            pass
    '"""

    def __init__(self, pin, debug):
        """Initialize the pedestrian button and set up the interrupt."""

        super().__init__(pin, Pin.IN, Pin.PULL_DOWN)
        self.__debug = debug
        self.__pin = pin
        self.__last_pressed = ticks_ms()  # Track the last time the button was pressed
        self.__pedestrian_waiting = False
        self.irq(trigger=Pin.IRQ_RISING, handler=self.callback)

    def button_state(self, value=None):
        """Return True if a pedestrian is waiting, else False."""
        if value is None:
            # Getter
            if self.__debug:
                print(
                    f"Button connected to Pin {self.__pin} is {'WAITING' if self.__pedestrian_waiting else 'NOT WAITING'}"
                )
            return self.__pedestrian_waiting
        else:
            # Setter
            self.__pedestrian_waiting = bool(value)
            if self.__debug:
                print(
                    f"Button state on Pin {self.__pin} set to {self.__pedestrian_waiting}"
                )

    def callback(self, pin):
        """Interrupt handler for button press. Sets waiting state with debounce."""
        current_time = ticks_ms()
        if ticks_diff(current_time, self.__last_pressed) > 200:
            self.__last_pressed = current_time
            self.__pedestrian_waiting = True
            if self.__debug:
                print(f"Button pressed on Pin {self.__pin} at {current_time}ms")
