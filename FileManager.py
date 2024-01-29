import os

def saveProgress(n, a) :
    file = open(f'{os.path.dirname(os.path.realpath(__file__))}\\progress.txt', 'w')
    file.write(f"{n}\n")
    file.write(f"{a}")
    file.close()

def getProgress() :
    file = open(f'{os.path.dirname(os.path.realpath(__file__))}\\progress.txt', 'r')
    n = int(file.readline())
    a = int(file.readline())
    file.close()
    return n, a