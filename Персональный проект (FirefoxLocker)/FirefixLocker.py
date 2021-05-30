import pyAesCrypt
import os
import shutil
import ctypes
import time
import getpass
import tarfile

class FirefixLocker:
    def __init__(self):
        self.BUFFERSIZE = 64 * 1024
        self.clear = lambda: os.system('cls')

        self.ORIGINALDIR = os.getcwd()
        self.FOLDER = "FirefoxPortable"
        self.FILENAME = "FirefoxPortable.exe"
        self.TARNAME = "FirefoxPortable.tar"
        self.TARAESNAME = self.TARNAME + ".aes"
        self.PASSWORD = ''

    def unlock(self):
        try:
            self.PASSWORD = getpass.getpass(prompt="Введите пароль: ")
            if os.path.isdir(self.FOLDER) == False:
                pyAesCrypt.decryptFile(self.TARAESNAME, self.TARNAME, self.PASSWORD, self.BUFFERSIZE)
                tar = tarfile.open(self.TARNAME, 'r:')
                tar.extractall(".")
                tar.close()

                shutil.copy(self.TARAESNAME, self.TARAESNAME + ".bak")
                os.remove(self.TARAESNAME)
                os.remove(self.TARNAME)

                self.clear()
                print("Браузер успешно разблокирован!\n")
                os.startfile(self.FOLDER + "\\" + self.FILENAME)
                self.chosing()
            else:
                self.clear()
                print("Браузер уже разблокирован!\n")
                self.chosing()
            
        except ValueError:
            self.clear()
            print("Неверный пароль! Повторите ввод.\n")
            self.chosing()

    def lock(self):
        if os.path.isdir(self.FOLDER) == True:
            if self.PASSWORD == '':
                print("Пароль отсутствует в системе!")
                self.PASSWORD = getpass.getpass(prompt="Введите пароль: ")

            os.system('taskkill /f /im firefox.exe')
            time.sleep(3)

            tar = tarfile.open(self.TARNAME, "x:")
            tar.add(self.FOLDER)
            tar.close()

            pyAesCrypt.encryptFile(self.TARNAME, self.TARAESNAME, self.PASSWORD, self.BUFFERSIZE)
            os.remove(self.TARNAME)
            shutil.rmtree(self.FOLDER)

            self.clear()
            print("Браузер успешно заблокирован!\n")
            self.chosing()
        else:
            self.clear()
            print("Браузер уже заблокирован!\n")
            self.chosing()

    def chosing(self):
        print("Выберите действие:\n1 - Разблокировать браузер\n2 - Заблокировать браузер\nВвод: ")
        action = input()

        if action == "1":
            self.unlock()
        elif action == "2":
            self.lock()
        else:
            print("Неверное действие! Повторите ввод!\nВвод: ")
            self.chosing()


try:
    is_admin = os.getuid() == 0
except AttributeError:
    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

if is_admin == True:
    os.system('mode con: cols=39 lines=7')
    pl = FirefixLocker()
    pl.chosing()
else:
    os.system('mode con: cols=72 lines=7')
    for i in range(4):
        print("Для корректной работы скрипта требуется запуск от имени администратора!")
        print("Время до выхода: " + str(i+1) + "/5")
        time.sleep(1)
        clear()
    exit(0)