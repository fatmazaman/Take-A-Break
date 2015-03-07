'''# First Method
import pygame
pygame.mixer.init()
pygame.mixer.music.load('song.mp3')
pygame.mixer.music.play()
while pygame.mixercontinue.music.get_busy() == True:
    

#Second Method
import os

os.system('vlc song.mp3 &')'''
# chalo isi tarah sab kar lenege ok ?
#test on mac
import subprocess
import os
#print os.path.exists("C:/Users/Dhruv/Desktop/Motivation/RiseShine.mp4") 
#p = subprocess.Popen(["/Applications/VLC.app/Contents/MacOS/VLC","./veg_girl.mp4"])

os.system('/Applications/VLC.app/Contents/MacOS/VLC veg_girl.mp4')