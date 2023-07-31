from machine import Pin, PWM
from utime import sleep

# Connect piezo buzzer to pin 15 (GP11). Refer to Pi Pico pinout.

# Set pin number of buzzer.
buzzerPIN=11

# Define the buzzer object
buzzerObject = PWM(Pin(buzzerPIN))

def buzzer(buzzerPinObject,frequency,sound_duration,silence_duration):

    # Set buzzer volume
    buzzerPinObject.duty_u16(1000)
    # Set frequency
    buzzerPinObject.freq(frequency)
    # Set duration of sound
    sleep(sound_duration)
    # Set volume to zero for silence
    buzzerPinObject.duty_u16(0)
    # Set duration of silence until next sound
    sleep(silence_duration)


# Define frequency of notes
G3=196
A3=220
B3=247
C4=262
D4=294
E4=330
F4=349
G4=392
A4=440
B4=494
C5=523
D5=587
E5=659
F5=698
G5=784

# Play tune
# In this example, eighth notes play for 0.10 sec with a typical 0.05 sec pause between notes.
buzzer(buzzerObject,E4,0.10,0.05)
buzzer(buzzerObject,E4,0.10,0.20) # Add 0.15 sec eighth-note pause to 0.05 sec standard pause
buzzer(buzzerObject,E4,0.15,0.15) # Play longer note without pause; Add 0.15 sec eighth-note pause after
buzzer(buzzerObject,C4,0.10,0.05)
buzzer(buzzerObject,E4,0.25,0.05)
buzzer(buzzerObject,G4,0.25,0.35) # Add 0.30 sec eighth-note pause to 0.05 sec standard pause
buzzer(buzzerObject,G3,0.25,0.05)

#Deactivates the buzzer
buzzerObject.deinit()


# Inspired by Avram Piltch / TomsHardware; https://www.tomshardware.com/how-to/buzzer-music-raspberry-pi-pico
# Inspired by peppe8o; https://peppe8o.com/passive-buzzer-with-raspberry-pi-pico-and-micropython/
# Tune Inspired by Super Mario Bros. Theme by Koji Kondo