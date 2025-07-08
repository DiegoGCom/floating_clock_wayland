#!/usr/bin/env python3

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

class HelpWidget(QWidget):
    def __init__(self,translator, parent=None):
        super().__init__(parent)
        
        self.translator= translator

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)

        ayuda_label = QLabel(
            self.translator.tr('help_title')+
            self.translator.tr('help_description')+
            self.translator.tr('help_usage'))
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
