from time import localtime
from time import sleep
from pygame import mixer


H = input("digite a hora: ")
M = input("digite o minuto: ")

while True:
    if localtime().tm_hour == int(H) and localtime().tm_min == int(M):
        print("acorde")
        mixer.init()
        mixer.music.load("ani.mp3")
        mixer.music.play()
        sleep(200)
        break




