Диалоговый бот Олег на Python. Автор Федосов Никита

Репозиторий проекта на гитхаб: https://github.com/bolgaro4ka/project_oleg

Использованные проекты:
QRTetris: https://github.com/Firemoon777/qrtetris

Версия 1.4.1-github

Рекомендуется использовать Python 3.10.0

Необходимые модули для работы:
pyttsx3
colorama
os
webbrowser
sys
subprocess
requests
datetime
pygame
random
sklearn
sounddevice
vosk
json
queue
tkinter
pyAesCrypt
qrcode
numpy
imageio

Скорее всего у вас не заработает model_small, если это так то:
1. Удалите содержимое папки
2. Перейдите на https://alphacephei.com/vosk/models/vosk-model-small-ru-0.22.zip
3. Вставте содержимое архива в папку model_small

Для запуска: 
1. Установить выше перечисленные модули.
2. Запустить main.py через командную строку командой python3 main.py, находясь в папке с проектом.
