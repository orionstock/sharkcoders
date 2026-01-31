from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
import random


perguntas_MJ = [
    {
        "pergunta": "Qual destes estilos de dança está associado com este artista?",
        "respostas": ["Moonwalk", "Breakdance", "Salsa", "Robot"],
        "correta": "1960"
    },
    {
        "pergunta": "Este artista é conhecido por ter influenciado a música com o uso de:",
        "respostas": ["Improvisação de jazz", "Riffs de guitarra de heavy metal", "Soluços vocais", "Lírica de folk"],
        "correta": "Soluços Vocais"
    },
    {
        "pergunta": "Este artista é conhecido por qual título",
        "respostas": ["Príncipe do Pop", "Rei do Rock", "Príncipe do Rock", "Rei do Pop"],
        "correta": "Rei do Pop"
    },
    {
        "pergunta": "Qual destes factos sobre o artista é verdadeiro?",
        "respostas": ["Começou a tocar quando era criança", "Famoso por música country", "Ganhou um prémio nóbel", "Tocou numa banda jazz famosa"],
        "correta": "Começou a tocar quando era criança"
    },
    {
        "pergunta": "Em que década é que este artista começou a tocar professionalmente?",
        "respostas": ["1960", "1970", "1980", "1950"],
        "correta": "1960"
    }
]


perguntas_beatles = [
    {
        "pergunta": "Qual destas músicas foi lançada na década de 1960?",
        "respostas": ["Abbey Road", "Rumours", "Hotel California", "Back in Black"],
        "correta": "Abbey Road"
    },
    {
        "pergunta": "Complete the lyric: 'Here comes the sun, doo-doo-doo-doo…'",
        "respostas": ["Hey Jude", "Here Comes The Sun", "Let It Be", "Come Together"],
        "correta": "Here Comes The Sun"
    },
    {
        "pergunta": "Which of these were members of The Beatles?",
        "respostas": ["John Lennon", "Paul McCartney", "George Harrison", "Mick Jagger"],
        "correta": ["John Lennon", "Paul McCartney", "George Harrison"]  # multiple correct
    },
    {
        "pergunta": "Order these albums chronologically: Help!, Rubber Soul, Revolver",
        "respostas": ["Help!, Rubber Soul, Revolver", "Rubber Soul, Revolver, Help!", "Revolver, Help!, Rubber Soul",
                    "Help!, Revolver, Rubber Soul"],
        "correta": "Help!, Rubber Soul, Revolver"
    },
    {
        "pergunta": "Who is this legendary band?",
        "respostas": ["The Beatles", "The Rolling Stones", "Queen", "Led Zeppelin"],
        "correta": "The Beatles"
    }
]