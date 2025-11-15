import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget

app = QApplication(sys.argv) #(cada app precisa de apenas um) precisa de existir em todas as apps pyqt. gere a "event loop"

window = QWidget() #janela base. podemos adicionar outros widgets
window.setWindowTitle("Olá PyQt!")
window.setGeometry(100, 100, 300, 100)

label = QLabel('<h1>Bem-vindo ao PyQt</h1>', parent=window) #exibe texto ou imagens
label.move(50, 20)

window.show() #exibe a janela
sys.exit(app.exec_()) #sys.exit() = garante saída limpa. exec_() = inicia a aplicação. mantém a app em execução até o utilizador fechar.