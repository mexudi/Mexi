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
from wake_words import  wakeWord
from get_date import getDate

# Ignore any warning messages
warnings.filterwarnings('ignore')

# Test record audio
#recordAudio()

text  = 'This is a test'
#assistaneResponse(text)

# Test get date function
getDate()
