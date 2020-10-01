# Import the required module for text 
# to speech conversion 
import pyttsx3
import speech_recognition as sr
import sys
import time




v=sr.Recognizer()

while(1):
    with sr.Microphone() as source:
        print('Jarvis : Speak Anything Sir')
        audio=v.listen(source)

        try:
            text=v.recognize_google(audio)
            print('Vivek said : ', format(text))
            engine = pyttsx3.init() # object creation
            voices = engine.getProperty('voices')#getting details of current voice
            engine.setProperty('voice', voices[1].id)#changing index, changes voices. 1 for female
            volume = engine.getProperty('volume')#getting to know current volume level (min=0 and max=1)
            engine.setProperty('volume',1.0)  # setting up volume level  between 0 and 1
            # say method on the engine that passing input words to be spoken 
            engine.say(format(text))
            # run and wait method, it processes the voice commands.
            engine.runAndWait()

        except:
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)
            engine.say('Sorry Sir I did not get that')
            engine.runAndWait()
            print('Sorry Sir I did not get that')

        if(format(text)=='exit'):
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)
            engine.say('Have a nice day sir')
            engine.runAndWait()
            sys.exit('Have a nice day sir')
            
            
            
        time.sleep(5)







