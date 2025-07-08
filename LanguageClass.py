#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import (
    QLabel,QWidget, QVBoxLayout,
    QHBoxLayout,QComboBox
)
from PyQt5.QtCore import Qt

class LanguageClass(QWidget):
    def __init__(self, parent, translator, type=QWidget):
        super().__init__()
        
        self.parent = parent
        self.translator = translator
        
        # Layout principal con alineación superior
        vbox = QVBoxLayout()
        vbox.setContentsMargins(0, 0, 0, 0)
        vbox.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        # Usamos QHBoxLayout para disposición horizontal
        hbox = QHBoxLayout()
        #hbox.setContentsMargins(20, 20, 20, 20)
  
        # Añadimos el label y el combobox al mismo layout horizontal
        hbox.addWidget(QLabel('Idioma: '))
        
        self.language_combo = QComboBox()
        self.language_combo.addItems(["en", "es"])
        self.language_combo.setCurrentText(parent.language)  # Asume que 'parent' tiene un atributo 'language'
        self.language_combo.currentTextChanged.connect(self.change_language)
        
        hbox.addWidget(self.language_combo)
        
        hbox.addStretch()
        
        vbox.addLayout(hbox)
        
        self.setLayout(vbox)
        
    def change_language(self, language):
        try:
            self.parent.change_language(language)
        except Exception as e:
            print(f"Error cambiando lenguage: {e}")

