from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.text_input = TextInput()
        self.label = Label(text="Escreve algo...")
        btn = Button(text="Atualizar")
        btn.bind(on_press=self.update_label)

        layout.add_widget(self.text_input)
        layout.add_widget(btn)
        layout.add_widget(self.label)

        return layout


    def update_label(self, instance):
        self.label.text = self.text_input.text



MyApp().run()