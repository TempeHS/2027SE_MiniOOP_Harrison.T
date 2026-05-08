from machine import Pin, ADC, PWM
from time import sleep

# Wait for USB to become ready
sleep(0.1)

# store desired output pin in a variable
led_pin = 25
led2_pin = 15
data_pin = 13
analog_data_pin = 26
servo_pin = 10

# configure GPIO Pin as an output pin and create an led object for Pin
led = PWM(Pin(led_pin))
led2 = PWM(Pin(led2_pin))

# set the PWM frequency for LEDs
led.freq(1000)
led2.freq(1000)

# configure GPIO Pin as an output pin and create a servo object for Pin
servo = PWM(Pin(servo_pin))

# set the PWM frequency for a Servo
servo.freq(50)  # pulse every 20ms

# configure GPIO Pin as an input pin and create a data object for Pin
data = Pin(data_pin, Pin.IN)

# configure GPIO Pin as an ADC pin and create a data object for ADC  that is a composition of the Pin
analog_data = ADC(Pin(analog_data_pin))


# function to calculate pulse width in microseconds
def set_angle(angle):
    # clamps the input angle to the range 0–180
    angle = min(max(angle, 0), 180)
    # return PWM mapping 0° to 500 µs and 180° to 2500 µs (standard for many servos).
    return int(500 + (angle / 180) * 2000)


# function to linearly map values
def map_range(value, in_min, in_max, out_min, out_max):
    return int((value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)


while True:
    adc_value = analog_data.read_u16()  # 0-65535
    if data.value() == 1:
        led.duty_u16(adc_value)
        led2.duty_u16(adc_value)
    else:
        led.duty_u16(0)
        led2.duty_u16(0)
    mapped_value = map_range(adc_value, 0, 65535, 0, 180)
    servo.duty_ns(set_angle(mapped_value) * 1000)
    print(f"Digital: {data.value()} , Analogue: {adc_value} , Servo: {servo.duty_ns()}")
    sleep(0.1)
