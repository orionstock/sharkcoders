from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label


DADOS_CLIMA = {
    "lisboa": {"temp": "22ºC", "condicao": "limpo"},
    "porto": {"temp": "19ºC", "condicao": "chuvoso"},
    "coimbra": {"temp": "21ºC", "condicao": "nublado"},
    "faro": {"temp": "25ºC", "condicao": "ensolarado"},
}



class TelaClima(BoxLayout):
    resultado = StringProperty("Insira uma cidade e carregue em Pesquisar")

    def buscar_clima(self):
        cidade = self.ids.entrada.text.lower().strip()
        if cidade in DADOS_CLIMA:
            clima = DADOS_CLIMA[cidade]
            self.resultado = f"{cidade.title()}: {clima['temp']} - {clima['condicao']}"
        else:
            self.resultado = f"Clima para '{cidade.title()}' não encontrado."



class ClimaApp(App):
    def build(self):
        return TelaClima()



ClimaApp().run()