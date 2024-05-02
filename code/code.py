import time
import board
import digitalio

from audiomp3 import MP3Decoder

try:
    from audioio import AudioOut
except ImportError:
    try:
        from audiopwmio import PWMAudioOut as AudioOut
    except ImportError:
        pass

# Define buttons
button1 = digitalio.DigitalInOut(board.GP0)
button1.switch_to_input(pull=digitalio.Pull.UP)

button2 = digitalio.DigitalInOut(board.GP3)
button2.switch_to_input(pull=digitalio.Pull.UP)

button3 = digitalio.DigitalInOut(board.GP22)  # Replace GPX with your chosen pin
button3.switch_to_input(pull=digitalio.Pull.UP)

# Define files
mp3files1 = ["green.mp3"]
mp3files2 = ["yellow.mp3"]
mp3files3 = ["red.mp3"]

# Create audio object
audio = AudioOut(board.GP1)

while True:
    if not button1.value:
        # Play files for button 1
        for filename in mp3files1:
            decoder = MP3Decoder(open(filename, "rb"))
            audio.play(decoder)
            print("playing", filename)
            time.sleep(0.5)  # Delay after each file

    elif not button2.value:
        # Play files for button 2
        for filename in mp3files2:
            decoder = MP3Decoder(open(filename, "rb"))
            audio.play(decoder)
            print("playing", filename)
            time.sleep(0.5)  # Delay after each file

    elif not button3.value:
        # Play files for button 3
        for filename in mp3files3:
            decoder = MP3Decoder(open(filename, "rb"))
            audio.play(decoder)
            print("playing", filename)
            time.sleep(0.5)  # Delay after each file
