import os

def saveProgress(n) :
    file = open(f'{os.path.dirname(os.path.realpath(__file__))}\\progress.txt', 'w')
    file.write(f"{n}")
    file.close()

def getProgress() :
    file = open(f'{os.path.dirname(os.path.realpath(__file__))}\\progress.txt', 'r')
    n = int(file.readline())
    file.close()
    return n