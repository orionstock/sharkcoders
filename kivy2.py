from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.recycleview import RecycleView
from kivy.properties import ObjectProperty
from kivy.clock import Clock


noticias = [
    {"titulo": "Noticia 1", "descricao": "Descricao curta da noticia 1", "detalhes": "Detalhes completos da noticia 1..."},
    {"titulo": "Noticia 2", "descricao": "Descricao curta da noticia 2", "detalhes": "Detalhes completos da noticia 2..."},
    {"titulo": "Noticia 3", "descricao": "Descricao curta da noticia 3", "detalhes": "Detalhes completos da noticia 3..."},
    {"titulo": "Noticia 4", "descricao": "Descricao curta da noticia 4", "detalhes": "Detalhes completos da noticia 4..."},
    {"titulo": "Noticia 5", "descricao": "Descricao curta da noticia 5", "detalhes": "Detalhes completos da noticia 5..."},
    {"titulo": "Noticia 6", "descricao": "Descricao curta da noticia 6", "detalhes": "Detalhes completos da noticia 6..."},
    {"titulo": "Noticia 7", "descricao": "Descricao curta da noticia 7", "detalhes": "Detalhes completos da noticia 7..."},
    {"titulo": "Noticia 8", "descricao": "Descricao curta da noticia 8", "detalhes": "Detalhes completos da noticia 8..."},
    {"titulo": "Noticia 9", "descricao": "Descricao curta da noticia 9", "detalhes": "Detalhes completos da noticia 9..."},
]


class TelaPrincipal(Screen):
    lista = ObjectProperty(None)

    def on_enter(self):
        Clock.schedule_once(lambda dt: self.carregar()) #Necessario para esperar que a lista seja criada

    def carregar(self):
        self.lista.data = []
        for item in noticias:
            noticia = {
                "text": f"{item['titulo']}\n{item['descricao']}",
                "on_release": lambda x=item: self.abrir_detalhes(x)
            }
            self.lista.data.append(noticia)


    def abrir_detalhes(self, noticia):
        tela_detalhes = self.manager.get_screen('detalhes')
        tela_detalhes.atualizar_conteudo(noticia)
        self.manager.current = 'detalhes'


class TelaDetalhes(Screen):
    titulo = ObjectProperty(None)
    descricao = ObjectProperty(None)

    def atualizar_conteudo(self, noticia):
        self.titulo.text = noticia['titulo']
        self.descricao.text = noticia['detalhes']


class ListaNoticias(RecycleView): pass


class Gerenciador(ScreenManager): pass


class NoticiasApp(App):
    def build(self): return Gerenciador()


NoticiasApp().run()