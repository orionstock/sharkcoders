import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLineEdit, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
)

app = QApplication(sys.argv)
window = QWidget()

window.setWindowTitle("Calculadora")
window.setGeometry(300, 300, 600, 400)

# Widgets
name_input = QLineEdit()
name_input.setPlaceholderText("Número 1")
name_input2 = QLineEdit()
name_input2.setPlaceholderText("Número 2")


button = QPushButton("+")
button2 = QPushButton("-")
button3 = QPushButton("x")
button4 = QPushButton("%")
label = QLabel("Resultado:")


def calcular():
    try:
        a = float(name_input.text())
        b = float(name_input2.text())

        if calcular() == 



layout = QVBoxLayout()
layout.addWidget(name_input)
layout.addWidget(name_input2)

layout2 = QHBoxLayout()
layout2.addWidget(button)
layout2.addWidget(button2)
layout2.addWidget(button3)
layout2.addWidget(button4)

layout.addLayout(layout2)
layout.addWidget(label)



window.setLayout(layout)
window.show()
sys.exit(app.exec_())