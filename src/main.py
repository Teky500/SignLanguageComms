# main.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color, Rectangle
import os
from image_file import create_image_layout

from backend import translate_words
from kivy.clock import Clock
import time
from functools import partial
from speech_to_text import record_and_convert
import threading
import time
from kivy.core.window import Window

# Get the width and height of the screen

class ASLInterpreterApp(App):
    def build(self):
        self.sm = ScreenManager()

        # First screen
        self.buildScr()

        # Second screen


        return self.sm
    def buildScr(self):
        global screen1
        screen1 = Screen(name='screen1')
        layout1 = BoxLayout(orientation='vertical', spacing=10, padding=20)
        # ... add your widgets to layout1 ...
        with layout1.canvas.before:
            Color(1, 1, 1, 1)  # white
            self.rect = Rectangle(size=layout1.size, pos=layout1.pos)
        layout1.bind(size=self._update_rect, pos=self._update_rect)

        self.text_input = TextInput(
            hint_text='Enter sentence to translate here:',
            size_hint=(1, None),
            height=50,
            multiline=False,
            font_size=18,
            foreground_color=(0.2, 0.2, 0.2, 1),  # Dark gray text color
            background_color=(0.9, 0.9, 0.9, 1),  # Light gray background
        )
        layout1.add_widget(self.text_input)

        self.record_button = Button(
            text='Record Speech',
            size_hint=(1, None),
            height=50,
            background_color=(0.2, 0.6, 0.8, 1),  # Light blue button color
            font_size=16,
        )
        self.record_button.bind(on_press=self.thread_start)
        layout1.add_widget(self.record_button)

        translate_button = Button(
            text='Translate to ASL',
            size_hint=(1, None),
            height=50,
            background_color=(0.2, 0.6, 0.8, 1),  # Light blue button color
            font_size=16,
        )
        translate_button.bind(on_press=self.on_translate)
        layout1.add_widget(translate_button)
        screen1.add_widget(layout1)
        self.sm.add_widget(screen1)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
    def do_nothing(self, dt):
        pass

    def on_translate(self, instance):
        te = self.text_input.text
        img = translate_words(te)
        counter = 0
        for i in img:
            Clock.schedule_once(partial(self.do_stuff, i), counter)
            counter += 1
        Clock.schedule_once(self.ret, counter+3)
    def ret(self, *largs):
        self.buildScr()
        self.sm.current = 'screen1'
    def do_stuff(self, im, *largs):
        self.sm.clear_widgets()
        screen2 = Screen(name='screen2')
        layout2 = create_image_layout(im)
        screen2.add_widget(layout2)
        self.sm.add_widget(screen2)
        self.sm.current = 'screen2'
    def thread_start(self, instance):
        self.record_thread = threading.Thread(target=self.on_record)
        self.record_button.disabled = True
        self.record_thread.start()
        self.record_thread.join()
        self.set_text()
    def on_record(self):

        # Record speech and convert to text
        self.recorded_text = record_and_convert()
        
    def set_text(self):
        self.text_input.text = self.recorded_text
        self.record_button.disabled = False


if __name__ == '__main__':
    ASLInterpreterApp().run()
