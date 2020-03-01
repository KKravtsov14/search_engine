# file system search engine
# Kravtsov - %
import os

def main():

    pass

def acceptCommand(n_command):
    lst = ['1', '2', '3', '4', '5', '6', '7']
    while n_command not in lst:
        n_command = input('Некорректный ввод. Пожалуйста, повторите попытку')
    return int(n_command)
    pass

def runCommand(command):

    pass

def moveUp():
    os.chdir('../')

def moveDown(currentDir):
    currentDir = str(currentDir)
    try:
        os.chdir(currentDir)
    except FileNotFoundError:
        print('некорректный ввод') #надо будет придумать, что тут выводить

def countFiles(path):

    pass

def countBytes(path):

    pass

def findFiles(target, path):

    pass