#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import (
    QLabel,QVBoxLayout, QListWidget, QStackedWidget,
    QDialog, QSplitter, QDialogButtonBox
)
from PyQt5.QtCore import Qt

from BorderConfigWidget import BorderConfigWidget
from BackgroundConfigWidget import BackgroundConfigWidget
from VisibilityOptionsWidget import VisibilityOptionsWidget
from HelpWidget import HelpWidget
from Translator import Translator
from LanguageClass import LanguageClass


class ConfigDialog(QDialog):
    def __init__(self, parent, translator):
        super().__init__(parent)
        self.translator = translator
        
        self.setWindowTitle(self.translator.tr("dialog_title"))
        self.resize(800, 500)
        
        # Crear layout principal
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        
        # Splitter para dividir la ventana
        splitter = QSplitter()
        main_layout.addWidget(splitter)
        
        # Lista de categorías
        self.setup_ui(splitter)
        
        
        # Widget apilado para las configuraciones
        self.stacked_widget = QStackedWidget()
        splitter.addWidget(self.stacked_widget)
        
        # Crear las páginas de configuración
        self.background_widget = BackgroundConfigWidget(parent, self.translator)
        self.border_widget = BorderConfigWidget(parent, self.translator)
        self.visibility_widget = VisibilityOptionsWidget(parent, self.translator)
        self.language_options = LanguageClass(parent,self.translator)
        self.help_widget = HelpWidget(self.translator, parent )
        
        self.stacked_widget.addWidget(self.background_widget)
        self.stacked_widget.addWidget(self.border_widget)
        self.stacked_widget.addWidget(self.visibility_widget)
        self.stacked_widget.addWidget(self.language_options)
        self.stacked_widget.addWidget(self.help_widget)
        
        # Conectar selección de lista a widget apilado
        self.category_list.currentRowChanged.connect(self.stacked_widget.setCurrentIndex)
        self.category_list.setCurrentRow(0)
        
        # Botones de control
        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        main_layout.addWidget(button_box)
        
    def setup_ui(self, splitter):
        # Crear lista de categorías
        self.category_list = QListWidget()
        self.category_list.setFixedWidth(150)
        categories = ["background", "border", "display", "language" , "help"]
        
        for cat_key in categories:
            item = self.translator.get_category(cat_key)
            self.category_list.addItem(item)
        
        splitter.addWidget(self.category_list) 