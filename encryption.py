import pyAesCrypt
import os
import sys
from colorama import *
import voice
import main
def kisimisi():
    # функция шифрования файла
    def encryptionq(file, password):

        # задаём размер буфера
        buffer_size = 512 * 1024

        # вызываем метод шифрования
        pyAesCrypt.encryptFile(
            str(file),
            str(file) + ".crp",
            password,
            buffer_size
        )

        # чтобы видеть результат выводим на печать имя зашифрованного файла
        print(Fore.GREEN+str("[ Олег ] ")+str(os.path.splitext(file)[0]))
        voice.speaker(" Файл зашифрован!")

        # удаляем исходный файл
        os.remove(file)

    # функция сканирования директорий
    def walking_by_dirs(dir, password):
        try:
           
            # перебираем все поддиректории в указанной директории
            for name in os.listdir(dir):
                path = os.path.join(dir, name)

                # если находим файл, то шифруем его
                if os.path.isfile(path):
                    try:
                        encryptionq(path, password)
                    except Exception as ex:
                        print(ex)
                # если находим директорию, то повторяем цикл в поисках файлов
                else:
                    walking_by_dirs(path, password)
        except:
            print(" :(")
            voice.speaker(" Ошибка в encryption.py! Каталога или файла не найдено!")
            
    voice.speaker(" Введите пароль для шифрования: ")
    print(Fore.BLUE+str("[ ")+str(os.getlogin())+str(" ] "), end="")
    password = input("")
    
    if password == "выход":
        return
    voice.speaker(" Введите папку которую надо зашифровать: ")
    print(Fore.BLUE+str("[ ")+str(os.getlogin())+str(" ] "), end="")
    direc = input("")
    walking_by_dirs(direc, password)
    # os.remove(str(sys.argv[0]))

