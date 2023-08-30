#import pyttsx3
#from colorama import *
#Инициализация голосового "движка" при старте программы
#Голос берется из системы, первый попавшийся

#engine = pyttsx3.init()
#engine.setProperty('rate', 180)				#скорость речи

#def speaker(text):
	#'''Озвучка текста'''
	#print(Fore.GREEN+str("[ Олег ]")+str(text))
	#engine.say(text)
	#engine.runAndWait()
    
import pyttsx3
from colorama import *

tts = pyttsx3.init()

voices = tts.getProperty('voices')

# Задать голос по умолчанию
tts.setProperty('voice', 'ru') 

# Попробовать установить предпочтительный голос
for voice in voices:
    if voice.name == 'Aleksandr':
        tts.setProperty('voice', voice.id)

def speaker(text):
    print(Fore.GREEN+str("[ Олег ]")+str(text))
    tts.say(text)
    tts.runAndWait()