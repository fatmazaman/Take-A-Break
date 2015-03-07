import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import simpleguitk as simplegui
import math
import random
import time
import webbrowser
import os

#Global variables
message = "Take A Break"

#Handler for audio file    
def click_aud():
    os.system('vlc aud.mp3 &')

# Handler for Image file
def click_img():
	os.system('"eog" "Fatma.png"')
    
#Handler for Website
def click_url():
    webbrowser.open("https://www.facebook.com/")
#Handler for Video file
def click_vid():
	os.system('vlc veg_girl.mp4')


# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, [100,212], 48, "Red")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Take A Break", 600, 400)
frame.add_button(" Video ", click_vid)
frame.add_button(" Audio ", click_aud)
frame.add_button(" Image ", click_img)
frame.add_button("Website", click_url)
frame.set_draw_handler(draw)

# Start the frame animation
time.sleep(12)
frame.start() 




