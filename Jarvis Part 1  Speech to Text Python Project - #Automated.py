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

        except:
            print('Sorry Sir I did not get that')

        if(format(text)=='exit'):
            sys.exit('Have a nice day sir')
            
        time.sleep(5)
