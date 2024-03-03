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
from speech_to_text import record_and_convert

class ASLInterpreterApp(App):
    def build(self):
        self.sm = ScreenManager()

        # First screen
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

        record_button = Button(
            text='Record Speech',
            size_hint=(1, None),
            height=50,
            background_color=(0.2, 0.6, 0.8, 1),  # Light blue button color
            font_size=16,
        )
        record_button.bind(on_press=self.on_record)
        layout1.add_widget(record_button)

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

        # Second screen
        screen2 = Screen(name='screen2')
        layout2 = create_image_layout()
        screen2.add_widget(layout2)
        self.sm.add_widget(screen2)

        return self.sm

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def on_translate(self, instance):
        # Switch to the new page
        self.sm.current = 'screen2'

    def on_record(self, instance):
        # Record speech and convert to text
        text = record_and_convert()
        self.text_input.text = text


if __name__ == '__main__':
    ASLInterpreterApp().run()
