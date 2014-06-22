import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import simpleguitk as simplegui



def draw_handler(canvas):
    canvas.draw_image(image, (1521 / 2, 1818 / 2), (1521, 1818), (50, 50), (100, 100))

image = simplegui.load_image('http://commondatastorage.googleapis.com/codeskulptor-assets/gutenberg.jpg')

frame = simplegui.create_frame('Testing', 100, 100)
frame.set_draw_handler(draw_handler)
frame.start()