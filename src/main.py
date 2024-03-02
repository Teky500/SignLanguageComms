from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.window import Window
from backend import translate_words
import time

class ASLInterpreterApp(App):
    def build(self):
        Window.clearcolor = (0.8, 0.9, 1, 1)
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        # Create a label for the title
        title_label = Label(text='English to ASL Translator', font_size=24, size_hint_y=None, height=50)
        self.layout.add_widget(title_label)

        # Create a text input box for English input
        self.text_input = TextInput(
            hint_text='Enter an English phrase...',
            size_hint=(1, None),
            height=50,
            multiline=False,
            font_size=18,
            foreground_color=(0.2, 0.2, 0.2, 1),  # Dark gray text color
            background_color=(0.9, 0.9, 0.9, 1),  # Light gray background
        )
        self.layout.add_widget(self.text_input)

        # Create a translate button
        translate_button = Button(
            text='Translate to ASL',
            size_hint=(1, None),
            height=50,
            background_color=(0.2, 0.6, 0.8, 1),  # Light blue button color
            font_size=16,
        )
        translate_button.bind(on_press=self.on_translate)
        self.layout.add_widget(translate_button)

        self.asl_signs_layout = BoxLayout(spacing=10)

        self.layout.add_widget(self.asl_signs_layout)

        return self.layout

    def on_translate(self, instance):
        self.asl_signs_layout.clear_widgets()
        # Get the English text from the input box
        english_text = self.text_input.text
        # TODO: Implement ASL translation logic here
        asl_text = f"ASL: {english_text}"  # Placeholder for ASL translation
        asl_text_list = translate_words(english_text)
        for i in asl_text_list:
            for j in i:
                asl_a_image = Image(source=j, size_hint=(None, None), size=(100, 100))

                self.asl_signs_layout.add_widget(asl_a_image)



if __name__ == '__main__':
    ASLInterpreterApp().run()
