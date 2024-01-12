import tkinter as tk
import pygame
import time

# Define Morse code to English language dictionary
morse_to_eng = {
    ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E",
    "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J",
    "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O",
    ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
    "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y",
    "--..": "Z", "-----": "0", ".----": "1", "..---": "2", "...--": "3",
    "....-": "4", ".....": "5", "-....": "6", "--...": "7", "---..": "8",
    "----.": "9"
}

# Define English language to Morse code dictionary
eng_to_morse = {value: key for key, value in morse_to_eng.items()}

# Define Morse code signal to audio beep duration dictionary
morse_signal = {
    ".": 0.2, "-": 0.5, " ": 0.2
}

# Initialize Pygame for audio playback
pygame.mixer.init()

# Create a function to convert Morse code to English
def convert_morse_to_eng():
    morse_code = morse_entry.get()
    english_text = ""
    # Split the input Morse code into individual letters
    letters = morse_code.split(" ")
    # Convert each letter from Morse code to English
    for letter in letters:
        if letter in morse_to_eng:
            english_text += morse_to_eng[letter]
        else:
            english_text += "  "
    # Update the English output label
    eng_output.config(text=english_text)

# Create a function to convert English to Morse code
def convert_eng_to_morse():
    english_text = eng_entry.get().upper()
    morse_code = ""
    # Convert each letter from English to Morse code
    for letter in english_text:
        if letter in eng_to_morse:
            morse_code += eng_to_morse[letter] + " "
        else:
            morse_code += "  "
    # Update the Morse code output label
    morse_output.config(text=morse_code)

# Create a function to play the Morse code audio
def play_morse_audio():
    morse_code = morse_entry.get()
    for signal in morse_code:
        if signal in morse_signal:
            beep_duration = morse_signal[signal]
            pygame.mixer.Sound("C:/Users/pratik/Desktop/MorseCodeProj/beep.WAV").play()
            time.sleep(beep_duration)
        else:
            time.sleep(0.2)

# Create a function to display the Morse code signal
def display_morse_signal():
    morse_code = morse_entry.get()
    signal_text = ""
    for signal in morse_code:
        if signal in morse_signal:
            signal_text += signal
        else:
            signal_text += "  "
    morse_signal_output.config(text=signal_text)

# Create the main window
window = tk.Tk()
window.title("Morse Code Converter")
window.geometry("800x600")

# Create the Morse code entry label and entry box
morse_label = tk.Label(window    , text="Enter Morse Code:")
morse_label.pack(pady=10)
morse_entry = tk.Entry(window, font=("Arial", 14))
morse_entry.pack()

# Create the English entry label and entry box
eng_label = tk.Label(window, text="Enter English Text:")
eng_label.pack(pady=10)
eng_entry = tk.Entry(window, font=("Arial", 14))
eng_entry.pack()

# Create the Morse code output label
morse_output_label = tk.Label(window, text="Morse Code:")
morse_output_label.pack(pady=10)
morse_output = tk.Label(window, font=("Arial", 14))
morse_output.pack()

# Create the English output label
eng_output_label = tk.Label(window, text="English Text:")
eng_output_label.pack(pady=10)
eng_output = tk.Label(window, font=("Arial", 14))
eng_output.pack()

# Create the buttons for conversion and audio playback
convert_button = tk.Button(window, text="Convert to English", command=convert_morse_to_eng)
convert_button.pack(pady=10)
play_audio_button = tk.Button(window, text="Play Morse Code Audio", command=play_morse_audio)
play_audio_button.pack(pady=10)
convert_button = tk.Button(window, text="Convert to Morse Code", command=convert_eng_to_morse)
convert_button.pack(pady=10)

# Create the Morse code signal output label
morse_signal_label = tk.Label(window, text="Morse Code Signal:")
morse_signal_label.pack(pady=10)
morse_signal_output = tk.Label(window, font=("Arial", 20))
morse_signal_output.pack()

# Create the button for displaying the Morse code signal
display_signal_button = tk.Button(window, text="Display Morse Code Signal", command=display_morse_signal)
display_signal_button.pack(pady=10)

# Run the main window loop
window.mainloop()

