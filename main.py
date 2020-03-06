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
    k = 0
    if os.path.isdir(path):
        for i in os.listdir(path):
            if os.path.isdir(path + '/' + i):
                k += countFiles(path + '/' + i)
            else:
                k += 1
    return k


def countBytes(path):
    k = 0
    if os.path.isdir(path):
        for i in os.listdir(path):
            if os.path.isdir(path + '/' + i):
                k += countBytes(path + '/' + i)
            else:
                k += os.path.getsize(path + '/' + i)
    return k


def findFiles(target, path):
    k = []
    if os.path.isdir(path):
        for i in os.listdir(path):
            if os.path.isdir(path + '/' + i):
                k.extend(findFiles(target, path + '/' + i))
            elif target.lower() in i.lower():
                k.append(path + '/' + i)
    return k

print(findFiles('ooo','c:/test'))