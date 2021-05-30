import pyAesCrypt
import getpass
import tarfile
import os
import shutil


FOLDER = "FirefoxPortable"
TARNAME = FOLDER + ".tar"
TARAESNAME = TARNAME + ".aes"

BUFFERSIZE = 64 * 1024


def main():
    print("Установка нового пароля для разблокировки браузера\n")
    PASSWORD = getpass.getpass(prompt="Введите новый пароль: ")
    PASSWORD2 = getpass.getpass(prompt="Введите новый пароль еще раз: ")
    
    if PASSWORD == PASSWORD2:
        os.remove(TARAESNAME)
        os.remove(TARNAME)
        
        tar = tarfile.open(TARNAME, "x:")
        tar.add(FOLDER)
        tar.close()
        
        pyAesCrypt.encryptFile(TARNAME, TARAESNAME, PASSWORD, BUFFERSIZE)
        
        shutil.rmtree(FOLDER)
        os.remove(TARNAME)
        
        print("Пароль успешно установлен! Создан файл " + TARAESNAME)
    else:
        os.system('cls')
        print("Введенные пароли не совпадают! Повторите ввод.")
        main()


if __name__ == "__main__":
    main()
