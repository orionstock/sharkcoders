import sys
import datetime
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QTimeEdit, QMessageBox
)
from PyQt5.QtCore import QTimer, QTime


app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("Relógio Digital")
window.setGeometry(300, 300, 300, 200)

central = QWidget()
layout = QVBoxLayout()


def atualizar_hora():
    agora = QTime.currentTime()
    texto_hora = agora.toString("HH:mm:ss")
    label_hora.setText(texto_hora)

    if 'alarme_hora' in globals():
        if agora.toString("HH:mm") == alarme_hora.toString("HH:mm"):
            disparar_alarme()


def disparar_alarme():
    global alarme_hora
    QTimer.singleShot(1000, limpar_alarme)
    QMessageBox.information(window, "Alarme", "Alarme! Hora definida atingida!")


def limpar_alarme():
    global alarme_hora
    alarme_hora = None
    label_alarme.setText("Alarme: (nenhum definido)")


def definir_alarme():
    global alarme_hora
    alarme_hora = input_alarme.time()
    label_alarme.setText("Alarme: " + alarme_hora.toString("HH:mm"))


label_hora = QLabel()
label_hora.setStyleSheet("font-size: 32px; text-align: center")
layout.addWidget(label_hora)

label_alarme = QLabel("Alarme: (nenhum definido)")
layout.addWidget(label_alarme)

input_alarme = QTimeEdit()
input_alarme.setDisplayFormat("HH:mm")
layout.addWidget(input_alarme)

button_definir = QPushButton("Definir Alarme")
button_definir.clicked.connect(definir_alarme)
layout.addWidget(button_definir)


central.setLayout(layout)
window.setCentralWidget(central)



timer = QTimer()
timer.timeout.connect(atualizar_hora)
timer.start(1000)

atualizar_hora
window.show()
sys.exit(app.exec_())