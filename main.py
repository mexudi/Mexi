import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia
from audio_record import recordAudio
from resp_assistant import assistaneResponse
from wake_words.py import  wakeWord 

# Ignore any warning messages
warnings.filterwarnings('ignore')

# Test record audio
#recordAudio()

text  = 'This is a test'
assistaneResponse(text)
