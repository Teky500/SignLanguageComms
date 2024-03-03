from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from kivy.uix.label import Label
import os
import random
from backend import translate_words
from kivy.core.window import Window

def create_image_layout(images):
    layout = FloatLayout(size=(300, 300))
    rect = None
    with layout.canvas.before:
        Color(1, 1, 1, 1)  # white
        rect = Rectangle(size=layout.size, pos=layout.pos)
    def update_rect(instance, value):
        rect.pos = instance.pos
        rect.size = instance.size
    layout.bind(size=update_rect, pos=update_rect)
    screen_width = Window.width
    screen_height = Window.height
    l = Label(text=images[0][0],
                color=(0.2, 0.5, 0.5, 1),
                font_size='77sp',  # Smaller font size
                size_hint=(None, None),
                width=500,
                height=100,
                halign='left',
                valign='top')
    l.pos = (screen_width/2 - 300,screen_height/2 + 200)
    # l.pos_hint = {'right': 1, 'top': 1}  # More towards the right and top
    
    layout.add_widget(l)
    for index, i in enumerate(images):
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),'images', i[1])
        image_widget = Image(source=image_path, size_hint=(None, None), size=(120, 120))
        image_widget.pos =(screen_width/2  + index * 120 - len(images)/2 * 120 - 175, screen_height/2)
        layout.add_widget(image_widget)
    return layout
