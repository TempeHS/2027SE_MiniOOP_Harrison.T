from lib.led_light import Led_Light
from lib.controller import PedestrianSubsystem
from lib.pedestrian_button import Pedestrian_Button
from lib.audio_notification import Audio_Notification
from time import sleep, time

red = Led_Light(19, True, True)
green = Led_Light(17, False, False)
button = Pedestrian_Button(22, debug=True)
buzzer = Audio_Notification(27, debug=True)

light = PedestrianSubsystem(red, green, button, buzzer, True)


def Pedestrian_Subsystem_Driver():
    print("Testing Traffic Light in 5 seconds")
    sleep(5)

    light.show_stop()
    print("Pass if: Red ON & Green OFF")
    sleep(5)
    print("Testing Traffic Light in 5 seconds")

    light.show_walk()
    print("Pass if: Red OFF & Green ON")
    sleep(5)

    warning_start = time()
    while time() - warning_start < 50:
        light.show_warning()
        sleep(0.5)
    print("Pass if: Ped red FLASHING, Ped Green OFF & Buzzer OFF")

    #light.show_warning()
    #print("Pass if: Pedestrian Buzzer ON")
    #sleep(5)

    print("Press Button Within 5 Seconds")
    sleep(5)
    if light.is_button_pressed():
        print("Pass if: Pedestrian button State ON")
    else:
        print("Fail: Button State OFF")

    sleep(5)

    light.reset_button()
    if not light.is_button_pressed():
        print("Pass : Pedestrian button State Reset")
    else:
        print("Fail: Pedestrian button State not Reset")

    sleep(5)


Pedestrian_Subsystem_Driver()
