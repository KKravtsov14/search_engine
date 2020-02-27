# file system search engine
# Kravtsov - %
import os

def main():

    pass

def acceptCommand():

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