# First Method
import pygame
pygame.mixer.init()
pygame.mixer.music.load('song.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue

#Second Method
import os

os.system('vlc song.mp3 &')
