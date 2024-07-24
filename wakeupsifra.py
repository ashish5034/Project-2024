import os
import snowboydecoder
import speech_recognition as sr
import subprocess

# Snowboy model file and sensitivity
WAKE_WORD_MODEL = "path_to_your_wake_word_model.pmdl"
SENSITIVITY = 0.5

# Function to run your SIFRA assistant script
def run_sifra():
    os.system("python sifra.py")

# Callback function when wake word is detected
def detected_callback():
    print("Wake word detected!")
    run_sifra()

# Create a Snowboy detector
detector = snowboydecoder.HotwordDetector(WAKE_WORD_MODEL, sensitivity=SENSITIVITY)

# Start listening for the wake word
print("Listening for wake word 'hey sifra'...")
detector.start(detected_callback=detected_callback)
