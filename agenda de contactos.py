import sys
import json
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem
)

contactos = []
ficheiro_json = "contactos.json"


def carregar_contactos():
    try:
        with open(ficheiro_json, "r", encoding="utf-8") as f:
            contactos.extend(json.load(f))
    except FileNotFoundError:
        pass

def guardar_contactos():
    with open(ficheiro_json, "w", encoding="utf-8") as f:
        json.dump(contactos, f, indent=4, ensure_ascii=False)

def atualizar_tabela():
    tabela.setRowCount(0)
    for i, c in enumerate(contactos):
        tabela.insertRow(i)
        tabela.setItem(i, 0, QTableWidgetItem(c["nome"]))
        tabela.setItem(i, 0, QTableWidgetItem(c["telefone"]))
        tabela.setItem(i, 0, QTableWidgetItem(c["email"]))

def adicionar_contacto():
    nome = input_nome.text().strip()
    telefone = input_telefone.text().strip()
    email = input_email.text().strip()

    if nome:
        contactos.append({"nome": nome, "telefone": telefone, "email": email})
        atualizar_tabela()
        guardar_contactos()
        input_nome.clear()
        input_telefone.clear()
        input_email.clear()

def remover_contactos():
    linha = tabela.currentRow()
    if linha >= 0:
        del contactos[linha]
        atualizar_tabela()
        guardar_contactos()

def editar_contactos():
    linha = tabela.currentRow()
    if linha >= 0:
        contactos[linha] = {
            "nome": input_nome.text().strip(),
            "telefone": input_telefone.text().strip(),
            "email": input_email.text().strip()
        }
        atualizar_tabela()
        guardar_contactos()



app = QApplication(sys.argv)
janela = QMainWindow()
janela.setWindowTitle("Agenda de Contactos")
janela.setGeometry(200, 200, 600, 400)

central = QWidget()
layout = QVBoxLayout()

tabela = QTableWidget()
tabela.setColumnCount(3)
tabela.setHorizontalHeaderLabels(["Nome", "Telefone", "Email"])
tabela.cellClicked.connect(preencher_inputs)
layout.addWidget(tabela)

input_nome = QLineEdit()
input_telefone = QLineEdit()
input_email = QLineEdit()
inputs_layout = QHBoxLayout()
inputs_layout.addWidget(input_nome)
inputs_layout.addWidget(input_telefone)
inputs_layout.addWidget(input_email)
layout.addLayout(inputs_layout)

btn_adicionar = QPushButton("Adicionar")
btn_editar = QPushButton("Editar")
btn_remover = QPushButton("Remover")

btn_adicionar.clicked.connect(adicionar_contacto)
btn_editar.clicked.connect(editar_contacto)
btn_remover.clicked.connect(remover_contacto)

botoes_layout = QHBoxLayout()
botoes_layout.addWidget(btn_adicionar)
botoes_layout.addWidget(btn_editar)
botoes_layout.addWidget(btn_remover)
layout.addLayout(botoes_layout)

central.setLayout(layout)
janela.setCentralWidget(central)

carregar_contactos()
atualizar_tabela()

janela.show()
sys.exit(app.exec_())