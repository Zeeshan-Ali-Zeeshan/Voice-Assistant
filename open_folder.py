# open_folder.py
import os
import json
import subprocess
from body.speak import speak

def open_folder_by_voice(folder_name):
    folder_name = folder_name.strip().lower()

    # Load folder index
    try:
        with open("folder_index.json", "r") as f:
            folder_index = json.load(f)
    except FileNotFoundError:
        speak("The folder index file is missing.")
        return False
    except json.JSONDecodeError:
        speak("The folder index file is corrupted.")
        return False

    # Build name-to-paths mapping
    name_to_paths = {}
    for full_path in folder_index.keys():
        base_name = os.path.basename(full_path).lower()
        name_to_paths.setdefault(base_name, []).append(full_path)

    matches = name_to_paths.get(folder_name, [])

    if not matches:
        speak(f"No folder found by the name {folder_name}.")
        return False

    if len(matches) == 1:
        folder_path = matches[0]
        subprocess.run(["explorer", folder_path])  # Ensures it opens visibly
        speak(f"Opening folder: {os.path.basename(folder_path)}")
        return True
    else:
        speak(f"I found {len(matches)} folders named {folder_name}. Please specify which one by number.")
        for i, path in enumerate(matches[:5]):
            speak(f"{i + 1}. {os.path.basename(path)}")
        return matches[:5]



def open_this_pc():
    os.system("explorer shell:MyComputerFolder")

# ❌ REMOVE or COMMENT THIS if present outside of any function:
# speak("Which folder should I open?")  ❌ <-- REMOVE THIS FROM TOP-LEVEL

# ✅ If you want to test this module separately:
# if __name__ == "__main__":
#     speak("Which folder should I open?") 
#     text = input() # Safe test block
#     open_folder_by_voice(text)