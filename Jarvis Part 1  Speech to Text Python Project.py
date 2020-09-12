import speech_recognition as sr

v=sr.Recognizer()

with sr.Microphone() as source:
    print('Jarvis : Speak Anything Sir')
    audio=v.listen(source)

    try:
        text=v.recognize_google(audio)
        print('Vivek said : ', format(text))

    except:
        print('Sorry Sir I did not get that')
