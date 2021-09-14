try:
    import pyfiglet
    import subprocess
    from subprocess import Popen
    import os
    import re
    import sys
    from colorama import * 
    import platform
    from tkinter import*
    from tkinter.ttk import*


except ImportError:
    os.system("pip3 install pyfiglet", shell=True)
    os.system("pip3 install coloroma", shell=True)


os.system("cls")

ascii_banner = pyfiglet.figlet_format("Ross")
print(ascii_banner)
init()
print(' ')
print(Fore.GREEN + " [+] Setting up Ross")
print(Fore.RED + "-----------------------------------------------------")
print(Fore.WHITE + "App Version : 1.0.0")
print(Fore.WHITE + "Detected OS: " + platform.system())
print(Fore.WHITE + "OS Release: " + platform.release())
print(Fore.RED + "-----------------------------------------------------")
print(Fore.GREEN + "Developer : Jehan Patel")

input('\n [=] Press Enter to download modules')
print("Please wait")

module = ["pyttsx3","SpeechRecognition","wikipedia"]
for i in module :
    os.system('pip install ' + i)
root=Tk()
root.title("Setup")
def starty():
   
    Popen('Ross.py', shell=True)


label1=Label(root,text="Setup Completed .  You can start your app now\nby clicking on the button below").pack()
buttonstart=Button(root, text="Start App",command=starty).pack()
root.mainloop()

