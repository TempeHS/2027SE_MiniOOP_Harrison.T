from machine import Pin, PWM, time_pulse_us
from time import sleep, sleep_us

# Wait for USB to become ready
sleep(0.1)

# store desired output pins in a variable
TRIG_PIN = 12
ECHO_PIN = 11
servo_pin = 10

# configure GPIO Pin as an output pin and create a servo object for Pin
servo = PWM(Pin(servo_pin))

# set the PWM frequency for a Servo
servo.freq(50)  # pulse every 20ms

# configure Echo & Trig GPIO Pins as objects for Pin
trig = Pin(TRIG_PIN, Pin.OUT)
echo = Pin(ECHO_PIN, Pin.IN)


# function to calculate pulse width in microseconds
def set_angle(angle):
    # clamps the input angle to the range 0–180
    angle = min(max(angle, 0), 180)
    # return PWM mapping 0° to 500 µs and 180° to 2500 µs (standard for many servos).
    return int(500 + (angle / 180) * 2000)


# function to linearly map values
def map_range(value, in_min, in_max, out_min, out_max):
    return int((value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)


def get_distance():
    # Send a 10us pulse to trigger
    trig.value(0)
    sleep_us(2)
    trig.value(1)
    sleep_us(10)
    trig.value(0)

    # Wait for echo, measure the duration
    try:
        pulse_time = time_pulse_us(echo, 1, 30000)  # Wait for HIGH
    except OSError as ex:
        if ex.args[0] == 110:  # Timeout
            return None
        raise ex

    # Calculate distance (speed of sound = 340 m/s)
    distance_cm = (pulse_time / 2) / 29.1
    return distance_cm


while True:
    dist = get_distance()
    if dist is not None:
        mapped_value = map_range(dist, 0, 410, 0, 180)  # adjust range as needed
        servo.duty_ns(set_angle(mapped_value) * 1000)
    else:
        print("Out of range")
    print(f"Distance: {dist} , Servo: {servo.duty_ns()}")
    sleep(0.1)
