import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import simpleguitk as simplegui
import math
import random
import time
import sound
import webbrowser

message = "Take A Break"

# Handler for mouse click
def click():
    global message
    message = "Wait"
def click_aud():
    s = Sound() 
    s.read('adios.wav') 
    s.play()
# Handler for Image
def click_img():
	pass
    #def draw_handler1(canvas):
    #    canvas.draw_image(image, (1521 / 2, 1818 / 2), (1521, 1818), (50, 50), (100, 100))
    #image = simplegui.load_image('http://commondatastorage.googleapis.com/codeskulptor-assets/gutenberg.jpg')
    
#Handler for Website
def click_url():
    webbrowser.open("http://www.youtube.com/watch?v=AKKT7zE_0Zg")


# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, [100,212], 48, "Red")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Take A Break", 600, 400)
frame.add_button("Video", click)
frame.add_button("Audio", click_aud)
frame.add_button("Image", click_img)
#frame.set_draw_handler(draw_handler1)
frame.add_button("Website", click_url)
frame.set_draw_handler(draw)

# Start the frame animation
#time.sleep(10)
frame.start()







