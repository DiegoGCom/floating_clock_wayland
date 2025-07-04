#!/usr/bin/env python3

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

class AyudaWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)

        ayuda_label = QLabel("""
        <h2>Instrucciones de uso</h2>
        <ul>
            <li><b>Clic izquierdo:</b> Mantén pulsado para mover el reloj por la pantalla.</li>
            <li><b>Clic central (rueda del ratón):</b> Mantén pulsado para redimensionar el reloj.</li>
        </ul>
        <h2>Atajos de teclado</h2>
        <ul>
            <li><b>Meta + Z:</b> Mostrar u ocultar el reloj.</li>
        </ul>
        """)
        ayuda_label.setTextFormat(Qt.TextFormat.RichText)
        ayuda_label.setWordWrap(True)
        ayuda_label.setStyleSheet("""
            QLabel {
                font-size: 13px;
                color: wheat;
            }
        """)

        layout.addWidget(ayuda_label)
        layout.addStretch()

        self.setLayout(layout)
