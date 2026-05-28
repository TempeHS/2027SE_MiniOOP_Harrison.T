from time import sleep
from audio_notification import Audio_Notification

buzzer = Audio_Notification(27, debug=True)

print("Testing beep()")
buzzer.beep(freq=1000, duration=200)
print("Did you hear a beep? (Check your buzzer)")

print("Testing warning_on() (should beep every ~0.5s for 2 seconds)")
start = buzzer.__last_toggle_time
for _ in range(5):
    buzzer.warning_on()
    sleep(1)

print("Testing warning_off() (should silence the buzzer)")
buzzer.warning_off()
print("Buzzer should now be off.")

print("Manual test complete.")


def test_audio():
    audio = Audio_Notification(27)
    audio.warning_on()
    print("Audio Notification")


test_audio()
