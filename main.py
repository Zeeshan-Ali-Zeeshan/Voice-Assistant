import random
import os
from Automation.open_website import openweb
from Automation.open import open
from Automation.search_in_google import search_google
from open_folder import open_this_pc
from open_folder import open_folder_by_voice
from Automation.close import close as cl
from body.listen import listen
from FUNCTION.function_intregation import Function_cmd
from DLG import stopcmd, cmd1
from body.speak import speak
from brain import brain
import pyautogui
from greetme import greetMe
import builtins
from plyer import notification
from pygame import mixer
# from wt_automation import sendMessage


mixer.init()
mixer.music.load("load.mp3")
mixer.music.play()

for i in range(3):
    speak("Enter the password to run shadow")
    a = input("Password: ")
    pw_file = builtins.open("password.txt", "r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
        break
    elif (i==2 and a!=pw):
        exit()

    elif (a!=pw):
        print("Try Again")

# Example replies
res1 = ["Yes, boss!", "I’m ready!", "How can I help you?"]
stopdlg_lines = ["Okay, stopping now.", "Goodbye!", "Exiting now."]

def demon():
    w_text= ""
    
    while True:
        # text = listen().lower()
        text = listen()
        if text == "wake up":
            w_text = text
        if "wake up" in w_text:
            greetMe()

            while True:
                # text = listen().lower()
                text = listen()
                if "go to sleep" in text:
                    speak("Ok sir, you can call me anytime.")
                    break  # Breaks back to waiting for "wake up"

                # text = listen()
                if not text:
                    continue  # Skip empty recognition
                text = text.lower().strip()
                print("Heard:", text)

                if text in cmd1:
                    speak(random.choice(res1))

                elif "change password" in text:
                    speak("What's the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = builtins.open("password.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir")
                    speak(f"Your new password is{new_pw}")

                elif "open this pc" in text:
                    open_this_pc()
                    speak("Command Executed Flawlessly")

                elif "open downloads" in text:
                    os.system(r'explorer "C:\Users\Zeeshan Ali\Downloads"')
                    speak("Command Executed Flawlessly")
                
                elif "open" in text and "folder" in text:
                    folder_name = text.replace("open", "").replace("folder", "").strip()
                    result = open_folder_by_voice(folder_name)

                    # If multiple folders returned, you can list them or handle it further
                    if isinstance(result, list):
                        for i, path in enumerate(result):
                            print(f"{i+1}. {path}")  # Optionally speak this
                        speak("Please enter the number of the folder you want to open.")
                        try:
                            choice = int(input("Choose folder number: ").strip())
                            if 1 <= choice <= len(result):
                                os.startfile(result[choice - 1])
                                speak(f"Opening {result[choice - 1]}")
                            else:
                                speak("Invalid choice.")
                        except ValueError:
                            speak("Invalid number format.")



                elif "schedule my day" in text:
                    tasks = [] #Empty list 
                    speak("Do you want to clear old tasks (Plz speak YES or NO)")
                    text = input()
                    if "yes" in text:
                        file = builtins.open("tasks.txt","w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = builtins.open("tasks.txt","a")
                            file.write(f"{i+1}. {tasks[i]}\n")
                            file.close()
                    elif "no" in text:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = builtins.open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()

                elif "show my schedule" in text:
                    file = builtins.open("tasks.txt","r")
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load("notification.mp3")
                    mixer.music.play()
                    notification.notify(
                        title = "My schedule :-",
                        message = content,
                        timeout = 15
                        )

                elif text in stopcmd:
                    speak(random.choice(stopdlg_lines))
                    break  # Stop current command session

                elif "open" in text or "kholo" in text:
                    cleaned_text = text.replace("open", "").replace("kholo", "").strip()

                    if "website" in cleaned_text or "web site" in cleaned_text:
                        query = cleaned_text.replace("website", "").replace("web site", "").strip()
                        openweb(query)
                    else:
                        open(cleaned_text)

                elif "search" in text:
                    query = text.replace("search", "").strip()
                    search_google(query)

                # elif any(keyword in text for keyword in ["check", "are you there", "find my ip", "what is the time", "start clap music with"]):
                #     for phrase in ["check", "are you there", "find my ip", "what is the time", "start clap music with"]:
                #         text = text.replace(phrase, "")
                #     Function_cmd(text)

                elif "check" in text or "are you there" in text or "find my ip" in text or "what is the time" in text:
                    Function_cmd(text)

                elif "screenshot" in text:
                     im = pyautogui.screenshot()
                     im.save("ss.jpg")
                     speak("screenshot is taken successfully")


                elif "close" in text or "band karo" in text:
                    query = text.replace("close", "").replace("band karo", "").strip()
                    cl()

                elif "shutdown the system" in text:
                    speak("Are you sure you want to shut down?")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no) ")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")
                    elif shutdown == "no":
                        speak("Shutdown cancelled.")

                elif "remember that" in text:
                    rememberMessage = text.replace("remember that", "").replace("Shadow", "")
                    speak("You told me to remember that " + rememberMessage)
                    with builtins.open("Remember.txt", "a") as remember:
                        remember.write(rememberMessage + "\n")

                elif "what do you remember" in text:
                    with builtins.open("Remember.txt", "r") as remember:
                        speak("You told me to remember that " + remember.read())

                # elif "whatsapp" in text:
                #     sendMessage()

                else:
                    brain(text)

if __name__ == "__main__":
    demon()


