from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton
)
import sys

app = QApplication(sys.argv)
window = QWidget()

layout = QVBoxLayout()
layout.addWidget(QPushButton("Botão 1"))
layout.addWidget(QPushButton("Botão 2"))


window.setLayout(layout)
window.show()
sys.exit(app.exec_())