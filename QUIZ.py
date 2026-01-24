from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty, ListProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label



perguntas = [
    {
        "pergunta": "Que civilização inventou o calendário de 365 dias?",
        "respostas": ["Egípcia", "Romana", "Persa"],
        "correta": "Egípcia"
    },
    {
        "pergunta": "Em Espanha, que cidade é conhecida como a 'Capital das Cavernas'?",
        "respostas": ["Sevilha", "Valência", "Granada"],
        "correta": "Granada"
    },
    {
        "pergunta": "Qual é a parte mais dura do nosso corpo?",
        "respostas": ["Ossos", "Dentes", "Unhas"],
        "correta": "Dentes"

    }
]


class QuizLayout(BoxLayout):
    pergunta_texto = StringProperty("")
    opcoes = ListProperty([])
    pontuacao = NumericProperty(0)
    index = NumericProperty(0)

    def on_kv_post(self, base_widget):
        self.carregar_proxima()

    def carregar_proxima(self):
        if self.index < len(perguntas):
            pergunta_atual = perguntas[self.index]
            self.pergunta_texto = pergunta_atual["pergunta"]
            self.opcoes = pergunta_atual["respostas"]
        else:
            self.pergunta_texto = "Fim do Quiz!"
            self.opcoes = []
            self.ids.resposta1.disabled = True
            self.ids.resposta2.disabled = True
            self.ids.resposta3.disabled = True

    def responder(self, resposta_escolhida):
        correta = perguntas[self.index]["correta"]
        if resposta_escolhida == correta:
            self.pontuacao += 1
            self.mostrar_popup("Certo!", "Resposta correta!")
        else:
            self.mostrar_popup("Errado!", f"A resposta correta era: {correta}")

        self.index += 1
        self.carregar_proxima()

    def mostrar_popup(selfself, titulo, mensagem):
        popup = Popup(title=titulo,
                      content=Label(text=mensagem),
                      size_hint=(None, None), size=(300, 200))
        
        popup.open()


class QuizApp(App):
    def build(self):
        return QuizLayout()

QuizApp().run()