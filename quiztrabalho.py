from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from perguntasquiz import todas_perguntas

# ----------------- Dados -----------------
artistas = ["MichaelJackson","TheBeatles","Queen", "MarvinGaye", "FrankSinatra"]
desbloqueados = ["MichaelJackson"]

# Agrupa perguntas por artista
perguntas_por_artista = {}
for p in todas_perguntas:
    artista = p.get("artista")
    if artista:
        perguntas_por_artista.setdefault(artista, []).append(p)
    else:
        print("Aviso: pergunta sem artista:", p)

cores_artista = {
    "MichaelJackson": (0.8,0.2,0,1),
    "TheBeatles": (0.2,0.4,0.8,1),
    "Queen": (0.6,0,0.8,1),
    "MarvinGaye": (0.2,0.4,0.8,1),
    "FrankSinatra": (0.5,0.5,0.5,1)
}

# ----------------- Lobby -----------------
class LobbyScreen(Screen):
    def on_enter(self):
        # Limpa qualquer widget antigo
        self.clear_widgets()

        # Cria BoxLayout para os botões dos artistas
        box_layout = BoxLayout(orientation="horizontal", spacing=20, padding=20)
        self.add_widget(box_layout)

        for artista in artistas:
            btn = Button(text=artista, size_hint=(None,None), size=(200,100))
            if artista in desbloqueados:
                btn.disabled = False
                btn.bind(on_release=lambda b, a_corrente=artista: self.iniciar_quiz(a_corrente))
            else:
                btn.disabled = True
                btn.background_color = (0.5,0.5,0.5,1)
            box_layout.add_widget(btn)

    def iniciar_quiz(self, artista):
        perguntas = perguntas_por_artista.get(artista)
        if not perguntas:
            print(f"Atenção: Não há perguntas para {artista}")
            return
        quiz_screen = self.manager.get_screen("quiz")
        quiz_screen.iniciar_quiz(perguntas)
        self.manager.current = "quiz"


# ----------------- Quiz -----------------
class QuizScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.quiz_perguntas = []
        self.index = 0
        self.pontuacao = 0
        self.artista_anterior = None
        self.tempo_restante = 10
        self.timer_event = None

    def iniciar_quiz(self, perguntas):
        self.quiz_perguntas = perguntas
        self.index = 0
        self.pontuacao = 0
        self.artista_anterior = None
        self.mostrar_pergunta()

    def mostrar_pergunta(self):
        self.clear_widgets()
        if self.index >= len(self.quiz_perguntas):
            # Fim do quiz
            ...
            return

        p = self.quiz_perguntas[self.index]

        # Separador de artista se mudou de artista
        if self.artista_anterior != p["artista"]:
            self.artista_anterior = p["artista"]
            lbl = Label(text=f"Próximo: {p['artista']}", font_size=32, size_hint=(1, 0.1))
            self.add_widget(lbl)
            Clock.schedule_once(lambda dt, pergunta_corrente=p: self.mostrar_pergunta_real(pergunta_corrente), 2)
        else:
            self.mostrar_pergunta_real(p)

    def mostrar_pergunta_real(self, p):
        self.clear_widgets()
        self.add_widget(Label(text=p["pergunta"], font_size=24, size_hint=(1,0.2), color=cores_artista.get(p["artista"],(1,1,1,1))))
        for r in p["respostas"]:
            btn = Button(text=r, size_hint=(1,0.1))
            btn.bind(on_release=lambda b, r_corrente=r: self.checar_resposta(r_corrente))
            self.add_widget(btn)

        self.tempo_restante = 10
        self.timer_label = Label(text=f"Tempo: {self.tempo_restante}s", size_hint=(1,0.05), color=(1,0,0,1))
        self.add_widget(self.timer_label)
        if self.timer_event:
            self.timer_event.cancel()
        self.timer_event = Clock.schedule_interval(self.contador, 1)

        self.feedback_label = Label(text="", size_hint=(1,0.05))
        self.add_widget(self.feedback_label)

    def contador(self, dt):
        self.tempo_restante -=1
        if self.tempo_restante >=0:
            self.timer_label.text = f"Tempo: {self.tempo_restante}s"
        if self.tempo_restante <=0:
            self.timer_event.cancel()
            self.timer_label.text = "Tempo esgotado!"
            self.checar_resposta(None)

    def checar_resposta(self, resp):
        if self.timer_event:
            self.timer_event.cancel()
        p = self.quiz_perguntas[self.index]
        correto = False
        if resp and resp.strip().lower() == p["correta"].strip().lower():
            correto = True
            self.pontuacao += 1

        self.feedback_label.text = "✅ Correto!" if correto else f"❌ Errado! Resposta: {p['correta']}"

        self.index +=1
        Clock.schedule_once(lambda dt: self.mostrar_pergunta(), 1.5)

# ----------------- App -----------------
from kivy.lang import Builder

KV = """
ScreenManager:
    LobbyScreen:
        name: "lobby"
        BoxLayout:
            id: box
            orientation: "horizontal"
            spacing: 20
    QuizScreen:
        name: "quiz"
"""

class QuizApp(App):
    def build(self):
        return Builder.load_string(KV)

if __name__ == "__main__":
    QuizApp().run()

