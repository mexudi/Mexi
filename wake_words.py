import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia


def wakeWord(text):
    # A list of wake words
    wake_words = ['hey computer','okay computer']

    # Converting the est to all lower case words
    text = text.lower()

    # Check to see if the users command /  text contans a wake word/phrase
    for phrase in wake_words:
        if phrase in text:
            return True
    # If the wake word is not found in the text, then return False
    return False
