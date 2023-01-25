import speech_recognition as sr
import pyttsx3 
import model as f
from neuralintents import GenericAssistant
import sys
import threading
import tkinter as tk




engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 150)
engine.setProperty('volume', 1)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
class assistant:
    def __init__(self):
        
       
        self.assistant = GenericAssistant('intents.json',intent_methods={
            
        })
       
        self.assistant.train_model()
        
        self.root = tk.Tk()
        engine = pyttsx3.init('sapi5')
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 1)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.setProperty('rate', 210)
        self.root.title("")
        self.label = tk.Label(text="🤖", font=("Arial", 120, "bold"))
        self.label.pack()
        threading.Thread(target=self.run_assistant).start()
        self.root.mainloop()

    


    def listen(self):
       
        r=sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            try:
                r.adjust_for_ambient_noise(source,duration=0.2)
                audiosaid = r.recognize_google(audio, language='en-in')
            except:
        
                return " "
        return audiosaid.lower()
            
    
   
    def run_assistant(self):
        while True:
            try:
                cmd=self.listen()
                
                if cmd=="wake up":
                    while True:
                        
                            self.label.config(fg="red")
                            cmd= self.listen()
                            reply = self.assistant.request(cmd)
                            if "bye" in reply: 
                                self.root.destroy()
                                sys.exit()
                                break
                      
                            else:
                                 
                                 
                                 reply = f.playJarvis(cmd, reply)            
                                 engine.say(reply)
                                 print(reply)
                                 engine.runAndWait()
            except:
                self.label.config(fg="black")
                continue
  
  
assistant()