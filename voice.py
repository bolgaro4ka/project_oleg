import pyttsx3
from colorama import *
#Инициализация голосового "движка" при старте программы
#Голос берется из системы, первый попавшийся

engine = pyttsx3.init()
engine.setProperty('rate', 180)				#скорость речи

def speaker(text):
	'''Озвучка текста'''
	print(Fore.GREEN+str("[ Олег ]")+str(text))
	engine.say(text)
	engine.runAndWait()