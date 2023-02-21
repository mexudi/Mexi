import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia

def recordAudio():
    # record the audio
    r = sr.Recognizer() #creating a recongnizer object

    # Open the microphone and start recording
    with sr.Microphone() as source:
        print('Say something!')
        audio = r.listen(source)

    # Use Googles speecg recognition

    data = ''
    try:
        data = r.recognize_google(audio)
        print('You said: '+data)
    except sr.UnknownValueError:
        print('Google Speech Recognition could not understand the audio, unkown error')
    except sr.RequestError as e:
        print('request results from Google Speech recognition service error '+e)


    return data
