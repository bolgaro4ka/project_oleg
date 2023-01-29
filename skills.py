import os
import webbrowser
import sys
import subprocess
import voice
import requests		#pip install requests
from datetime import datetime
import pygame
import random
from pygame.locals import *
import game

def browser():
	'''Открывает браузер заданнный по уполчанию в системе с url указанным здесь'''

	webbrowser.open("https://www.google.com", new=2)
    
def github():
    webbrowser.open("https://github.com/", new=2)
   
def game1():
	'''Нужно разместить путь к exe файлу любого вашего приложения'''
	try:
		subprocess.Popen("C:\WINDOWS\system32\mspaint.exe")
	except:
		voice.speaker('Путь к файлу не найден, проверьте, правильный ли он')

def calc():
    voice.speaker(" Введите ваше арифметическое действие ниже")
    calcp = str(eval(input()))
    voice.speaker(str(" ")+str(calcp))
    
def offpc():
	os.system('shutdown \s')

def gsk():
    game.gamesh()
    
def weather():
	'''Для работы этого кода нужно зарегистрироваться на сайте
	https://openweathermap.org или переделать на ваше усмотрение под что-то другое'''
	try:
		params = {'q': 'Novodugino,RU', 'units': 'metric', 'lang': 'ru', 'appid': '136685f6888cfc350553618a17bf9544'}
		response = requests.get(f'https://api.openweathermap.org/data/2.5/weather', params=params)
		if not response:
			raise
		w = response.json()
		voice.speaker(f" На улице {w['weather'][0]['description']} {round(w['main']['temp'])} градусов")
		
	except:
		voice.speaker('Произошла ошибка при попытке запроса к ресурсу API, проверь код')

def exp():
    os.startfile(r"links\exp.lnk")
    
def task_man():
    os.startfile(r"C:\WINDOWS\system32\Taskmgr.exe")

def paint():
	subprocess.Popen(r"C:\WINDOWS\system32\mspaint.exe")
    
def note():
	subprocess.Popen(r"C:\Program Files\Notepad++\notepad++.exe")

def music():
    os.startfile(r"music\music1.mp3")
   
def offBot():
	'''Отключает бота'''
	sys.exit()

def passive():
	'''Функция заглушка при простом диалоге с ботом'''
	pass

def time_o():
	voice.speaker(str(" Сейчас ")+str(datetime.now()))

def color_o():
    colorist_text = random.choice(['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'])
    colorist_back = random.choice(['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'])
    os.system('color '+str(colorist_text)+str(colorist_back))
    
def randomig():
    voice.speaker(str(" "+str(random.randint(1,100))))
    
def systemo():
    if os.name == 'nt':
        voice.speaker(' Ваша система Windows')
    if os.name == 'mac':
        voice.speaker(' Вы пользователь Мак ОС')
    if os.name == 'os2': #playstation
        voice.speaker(' Эм... Python на Playstation 2?')
    
def reco():
    voice.speaker(" Введите вашу фразу ниже, а я озвучу! (Для выхода напишите exit или выход)")
    while True:
        recop = input(">>> ")
        if recop == "exit" or recop == "Exit" or recop == "Выход" or recop == "выход":
            break
        voice.speaker(str(" ")+str(recop))

def pythoh():
    os.startfile(r"links\py310.lnk")

def random_money():
    rmoney=random.randint(1,3)
    if rmoney == 1:
        voice.speaker(" Выпала решка!")
    if rmoney == 2:
        voice.speaker(" Выпал орёл!")
    if rmoney == 3:
        voice.speaker(" Ой, укатилась!")
        
def clear_o():
	os.system('CLS')