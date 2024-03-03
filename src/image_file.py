# image_file.py
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
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

    # Select a random image from the directory
    for i in images:
        image_path = os.path.join(os.getcwd(), i)
        image_widget = Image(source=image_path)
        layout.add_widget(image_widget)
    # Display the random image


    return layout
