from lib.pedestrian_button import Pedestrian_button
from time import sleep

button = Pedestrian_button(22, debug=True)

print("Please press and release the button within 5 Seconds")
pressed = False
for _ in range(50):
    if button.button_state:
        pressed = True
        break
    sleep(0.1)

if pressed:
    print
else:
