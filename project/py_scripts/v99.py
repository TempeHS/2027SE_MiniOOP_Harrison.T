from lib.led_light import Led_Light
from lib.pedestrian_button import Pedestrian_Button
from lib.audio_notification import Audio_Notification
from lib.controller import Controller, PedestrianSubsystem, TrafficLightSubsystem
from time import sleep, time

debug = False

led_pedestrian_red = Led_Light(19, True, True)
led_pedestrian_green = Led_Light(17, False, True)
led_traffic_red = Led_Light(3, False, True)
led_traffic_amber = Led_Light(5, False, True)
led_traffic_green = Led_Light(7, False, True)
pedestrian_button = Pedestrian_Button(22, debug=True)
buzzer = Audio_Notification(27, debug=True)

controller = Controller(
    led_pedestrian_red,
    led_pedestrian_green,
    led_traffic_red,
    led_traffic_amber,
    led_traffic_green,
    pedestrian_button,
    buzzer,
    True,
)

while True:
    controller.update()
    sleep(1)