# import asyncio
# import os
# import threading  # For multi-threading
# import edge_tts
# import pygame
#
# # Voice configuration
# VOICE = "en-AU-WilliamNeural"
# BUFFER_SIZE = 1024
#
# # Function to remove a file with retry mechanism
# def remove_file(file_path):
#     max_attempts = 3
#     attempts = 0
#     while attempts < max_attempts:
#         try:
#             with open(file_path, "wb"):
#                 pass  # Ensures the file exists before removal
#             os.remove(file_path)
#             break
#         except Exception as e:
#             print(f"Error removing file: {e}")
#             attempts += 1
#
# # Async function to generate TTS
# async def generate_tts(TEXT, output_file):
#     try:
#         print("\033[92mGenerating TTS...\033[0m")  # Green text
#         cm_txt = edge_tts.Communicate(TEXT, VOICE)
#         await cm_txt.save(output_file)
#         print("\033[94mTTS Generation Complete.\033[0m")  # Blue text
#     except Exception as e:
#         print(f"\033[91mError during TTS generation: {e}\033[0m")  # Red text
#
# # Function to play audio
# def play_audio(file_path):
#     print("\033[92mPlaying audio...\033[0m")  # Green text
#     pygame.mixer.init()
#     pygame.mixer.music.load(file_path)
#     pygame.mixer.music.play()
#     while pygame.mixer.music.get_busy():
#         continue
#     pygame.mixer.quit()
#
# # Function to handle TTS and playback using threads
# def speak(TEXT):
#     output_file = "output.mp3"
#     # Thread for TTS generation
#     tts_thread = threading.Thread(target=lambda: asyncio.run(generate_tts(TEXT, output_file)))
#     tts_thread.start()
#     tts_thread.join()  # Wait for TTS to finish
#
#     # Thread for audio playback
#     if os.path.exists(output_file):
#         play_thread = threading.Thread(target=play_audio, args=(output_file,))
#         play_thread.start()
#         play_thread.join()
#
#     # Clean up the file
#     remove_file(output_file)
# while True:
#    speak(input("Text to speak: "))

import pyttsx3
from body.listen import listen

# Initialize the text-to-speech engine once
engine = pyttsx3.init()

# Configure voice properties
engine.setProperty('rate', 180)        # Speed of speech (180 is fast but clear)
engine.setProperty('volume', 1.0)      # Max volume is 1.0

# Select female voice if available
voices = engine.getProperty('voices')
if len(voices) > 1:
    engine.setProperty('voice', voices[1].id)  # Index 1 is often female

# Speak function
def speak(text):
    print("\033[92mSpeaking:\033[0m", text)  # Green text
    engine.say(text)
    engine.runAndWait()

# Test loop
# while True:
#     text = listen()
#     print("Heard:", text)
#     speak(text)
