# image_file.py
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from kivy.uix.label import Label
import os
import random
from backend import translate_words

def create_image_layout(images):
    layout = BoxLayout(orientation='horizontal', spacing=10)
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
                    font_size='67sp',
                    size_hint_y=None,
                    height=100,                       
halign='center', valign='top',
                      size_hint=(1, 1))
    l.pos_hint = {'center_x': 0.8, 'center_y': 0.8}
    layout.add_widget(l)
    for i in images:
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),'images', i[1])
        image_widget = Image(source=image_path)
        image_widget.pos_hint = {'center_x': 0.35, 'center_y': 0.35}
        layout.add_widget(image_widget)

    # Display the random image


    return layout
