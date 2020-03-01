#voice assitant using python
from tkinter import * #ignore this warning
from ttkthemes import themed_tk as tk
from tkinter import ttk 
from time import ctime
import time
import speech_recognition as sr 
import pyaudio
import webbrowser
import os
import playsound
import random
from gtts import gTTS 
# end of imports
# root window
root = tk.themed_tk()
root.get_themes()
root.set_theme("scidgreen")
root.resizable(0,0)
root.configure(background="white")
root.title("Voice Assitant")

#buttons
task_btn = ttk.Button(root,text="Command", width=10,command=task).grid(row=0,column=0, ipady=20, ipadx=90)
save_btn = ttk.Button(root,text="Exit",width=10,command=root.destroy).grid(row=1,column=0, ipady=20, ipadx=90)

root.mainloop()

#defs
def speak(audio_string):
    tts = gTTS(text=audio_string,Lang='en')

    r = random.randint(1,100000)
    audio_file = 'audio-'-str(r)-'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    os.remove(audio_file)

def record_audio(ask=False):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        
        audio = r.listen(source)
        voice_data=''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            speak('Did not get that')
        
        except sr.RequestError:
            speak('Server is down')

        return voice_data
