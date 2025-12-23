import speech_recognition as sr
from colorama import Fore, init
import time

init(autoreset=True)

def listen():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = True
    recognizer.pause_threshold = 1
    recognizer.phrase_threshold = 0.3
    recognizer.non_speaking_duration = 0.5
    # recognizer.adjust_for_ambient_noise(source, duration=1)  
    # time.sleep(0.3)
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)

        try:
            print(Fore.GREEN + "Listening....", end='\r', flush=True)
            audio = recognizer.listen(source, timeout=None)
            print(Fore.YELLOW + "Recognizing...   ", end='\r', flush=True)

            recognized_text = recognizer.recognize_google(audio, language='en-US').lower()
            print(Fore.CYAN + "Mr.Demon (English): " + recognized_text)
            return recognized_text  # ✅ Return the recognized text

        except sr.UnknownValueError:
            print(Fore.RED + "Speech not recognized.")
            return ""  # Return empty string on failure
        except sr.RequestError as e:
            print(Fore.RED + f"API error: {e}")
            return ""  # Return empty string on failure
        except KeyboardInterrupt:
            print(Fore.YELLOW + "\nStopped by user.")
            return ""  # Return empty string or handle it as you want
