import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QAction, QFileDialog, QMessageBox
)

from PyQt5.QtGui import QKeySequence

# Criar aplicação e Janela Principal
app = QApplication(sys.argv)
janela = QMainWindow()
janela.setWindowTitle("Bloco de Notas Simples")
janela.setGeometry(300, 300, 600, 400)

# Widget Principal: QTextEdit
texto_edit = QTextEdit()
janela.setCentralWidget(texto_edit)

# Menu e Ações
menu_arquivo = janela.menuBar().addMenu("Arquivo")


def novo_arquivo():
    texto_edit.clear()


def abrir_arquivo():
    caminho, _ = QFileDialog.getOpenFileName(janela, "Abrir Ficheiro", "", "Text Files (*.txt);;All Files (*)")
    if caminho:
        try:
            with open(caminho, 'r', encoding='utf-8') as f:
                conteudo = f.read()
                texto_edit.setText(conteudo)
        except Exception as e:
            QMessageBox.warning(janela, "Erro", f"Não foi possível abrir o ficheiro:\n{e}")


def guardar_arquivo():
    caminho, _ = QFileDialog.getSaveFileName(janela, "Guardar Ficheiro", "", "Text Files (*.txt);;All Files (*)")
    if caminho:
        try:
            with open(caminho, 'w', encoding='utf-8') as f:
                f.write(texto_edit.toPlainText())
        except Exception as e:
            QMessageBox.warning(janela, "Erro", f"Não foi possível guardar o ficheiro:\n{e}")


acao_novo = QAction("Novo", janela)
acao_novo.setShortcut(QKeySequence.New)
acao_novo.triggered.connect(novo_arquivo)

acao_abrir = QAction("Abrir...", janela)
acao_abrir.setShortcut(QKeySequence.Open)
acao_abrir.triggered.connect(abrir_arquivo)

acao_guardar = QAction("Guardar...", janela)
acao_guardar.setShortcut(QKeySequence.Save)
acao_guardar.triggered.connect(guardar_arquivo)

menu_arquivo.addAction(acao_novo)
menu_arquivo.addAction(acao_abrir)
menu_arquivo.addAction(acao_guardar)


# Mostrar janela e iniciar o loop de eventos
janela.show()
sys.exit(app.exec_())