import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLineEdit, QPushButton, QLabel, QVBoxLayout
)

app = QApplication(sys.argv)
window = QWidget()

window.setWindowTitle("Saudação")


# Widgets
name_input = QLineEdit()
name_input.setPlaceholderText("Introduz o teu nome...")

button = QPushButton("Saudar")
label = QLabel("")


# Action
def saudar():
    name = name_input.text()
    label.setText(f"Olá {name}!")

button.clicked.connect(saudar)


# Layout
layout = QVBoxLayout()
layout.addWidget(name_input)
layout.addWidget(button)
layout.addWidget(label)

window.setLayout(layout)
window.show()

sys.exit(app.exec_())