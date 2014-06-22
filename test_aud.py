#import wave
#wave.open('adios.wav','r')



#import os
#os.startfile('song.mp3')

import subprocess
PLAYERPATH = "C:/Program Files (x86)/VideoLAN/VLC/vlc.exe"
subprocess.call([PLAYERPATH, FILEPATH])