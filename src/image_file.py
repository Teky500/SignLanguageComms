# image_file.py
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
import os
import random

def create_image_layout():
    layout = BoxLayout(orientation='vertical', spacing=10)
    rect = None
    with layout.canvas.before:
        Color(1, 1, 1, 1)  # white
        rect = Rectangle(size=layout.size, pos=layout.pos)
    def update_rect(instance, value):
        rect.pos = instance.pos
        rect.size = instance.size
    layout.bind(size=update_rect, pos=update_rect)

    # Select a random image from the directory
    image_dir = os.path.join(os.getcwd(), 'images')
    image_files = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]
    random_image = random.choice(image_files)
    image_path = os.path.join(image_dir, random_image)

    # Display the random image
    image_widget = Image(source=image_path)
    layout.add_widget(image_widget)

    return layout
