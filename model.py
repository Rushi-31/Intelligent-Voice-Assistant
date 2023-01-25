import webbrowser
import speech_recognition as sr
import os
from datetime import datetime
import random
import pyttsx3 as tts
from time import gmtime, strftime
import wikipedia
import pyautogui as at
from functools import cache
import pywhatkit
import requests
from bs4 import BeautifulSoup

engine = tts.init('sapi5')
engine.setProperty('rate', 150)
engine.setProperty('volume', 1)
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)
# for i in range(0,8):
#     print(voices[i])
def GoogleSearch(voice,reply):
                try:
                    
                    
                    voice = voice.replace("wikipedia", "")
                    results = wikipedia.summary(voice, sentences=1)
                    return results

                except:
                    topic =  voice.replace('search', '')
                    search= topic.replace('google', '')
                    
                    url =f"https://www.google.com/search?q={search}"
                    r  = requests.get(url) 
                    data= BeautifulSoup(r.text, "html.parser")
                    results = data.find("div", class_ = "BNeawe").text
                    return results
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def playJarvis(voice,reply):   
          
        
            if 'search' in reply:
             
                   reply=reply.replace('search', "")
                   temp=GoogleSearch(voice, reply)
                   speak(f"{temp}")
                
                
            elif "code" in reply:
                path = 'C:\\Users\\Rushikesh Chopade\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
                os.startfile(path)
                
            elif  'search' in reply:
                   
                   temp=GoogleSearch(voice, reply)
                   speak(f"{temp}")
                #  pywhatkit.search(topic)
                 
                
            elif 'time' in reply:
                 strTime =datetime.now().strftime("%H:%M")    
                 #print(f"Sir, the time is {strTime}")
                 reply=reply.replace("time", "")
                 d = datetime.strptime(strTime, "%H:%M")
                 currentTime=d.strftime("%I:%M %p")
                 #print("sir time is "+ d.strftime("%I:%M %p"))
                 speak(f"sir the time is {currentTime}")
          
                
            elif 'Whatsapp' in reply:
                way = "C:\\Users\\Rushikesh Chopade\\Desktop\\WhatsApp.lnk"
                os.startfile(way)
            elif "android studio" in reply:
                        os.startfile("C:\\Users\\Rushikesh Chopade\\Desktop\\Android Studio.lnk")
            elif 'youtube'  in reply:
                 voice = voice.replace('play','') 
                 voice = voice.replace('on youtube', '')
                 reply=reply.replace("youtube", " ")
                 speak(f" playing {voice} on youtube")
                 pywhatkit.playonyt(voice)

                 
            elif 'spotify' in reply:
                path1 = "C:\\Users\\Rushikesh Chopade\\Desktop\\Spotify.lnk"
                os.startfile(path1)
            elif "remember for me" in voice:
                speak("why not , just tell me what I am gona remember")
                remember = listen()
                speak("ok I saved ")
            
            elif 'what i told you' in voice:
                speak("you told me that "+" "+remember)
            elif "volume up" in voice:
              for i in range(1,10):
                at.press('volumeup')
                
            elif "volume down" in voice:
                at.press('volumedown')
                at.press('volumedown')
                at.press('volumedown')
                at.press('volumedown')
            elif "mute" in voice:
                at.press("volumemute")
            elif "minimize" in voice or 'minimise' in voice:
                        speak('Minimizing Sir')
                        at.hotkey('win', 'down','down')
                        at.hotkey('win', 'down','down')

            elif "maximize" in voice or 'maximise' in voice:
                        speak('Maximizing Sir')
                        at.hotkey('win', 'up','up')
            elif "closing "  in reply:  
                        at.hotkey('ctrl','w')
            elif "screenshot" in voice:
                        speak("Taking Screenshot sir...")
                        at.hotkey('win','prtsc')
            elif "open notepad" in voice:
                os.startfile("C:\\Users\\Rushikesh Chopade\\Desktop\\Notepad.lnk") 
                speak("Opening Notepad")
                while True:
                    notepadvoice=listen()
                    if "paste" in notepadvoice:
                        at.hotkey('ctrl','v')
                        speak("Done Sir!")
                    elif "save this file" in notepadvoice:
                        at.hotkey('ctrl','s')
                        speak("Sir, tell a name for this file")
                        at.write(notepadSavingvoice)
                        at.press('enter')
                    elif 'type' in notepadvoice:
                        speak("Please Tell me what should I Write...")
                        while True:
                            writeInNotepad=listen()
                            if writeInNotepad == 'exit typing':
                                speak("Done Sir.")
                                break
                            else:
                                at.write(writeInNotepad)
                    elif "exit notepad" in notepadvoice or 'close notepad' in notepadvoice:
                        speak('quiting Notepad Sir...')
                        at.hotkey('ctrl', 'w')
            return reply