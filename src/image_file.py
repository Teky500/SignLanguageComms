from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from kivy.uix.label import Label
import os
import random
from backend import translate_words

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
    l = Label(text=images[0][0],
                color=(0.2, 0.5, 0.5, 1),
                font_size='30sp',  # Smaller font size
                size_hint=(None, None),
                width=500,
                height=100,
                halign='left',
                valign='top')
    l.pos = (512,512)
    # l.pos_hint = {'right': 1, 'top': 1}  # More towards the right and top
    layout.add_widget(l)
    for index, i in enumerate(images):
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),'images', i[1])
        image_widget = Image(source=image_path, size_hint=(None, None), size=(100, 100))
        image_widget.pos_hint = {'x': index * 0.060, 'center_y': 0.35}  # Adjust the x position for each image
        layout.add_widget(image_widget)

    return layout
