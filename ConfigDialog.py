#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import (
    QApplication, QLabel, QWidget, QMenu, QColorDialog,
    QSlider, QCheckBox, QVBoxLayout, QListWidget, QStackedWidget,
    QDialog, QPushButton, QHBoxLayout, QSplitter,
    QComboBox, QFontComboBox, QSpinBox, QDialogButtonBox, QGridLayout, QSizePolicy
)
from PyQt5.QtCore import Qt, QTimer, QTime, QDate, QSettings, QPoint
from PyQt5.QtGui import QFont, QColor, QPainter, QBrush, QPen, QKeyEvent

from BordeConfigWidget import BordeConfigWidget
from FondoConfigWidget import FondoConfigWidget
from OpcionesVisibilidadWidget import OpcionesVisibilidadWidget
from AyudaWidget import AyudaWidget


class ConfigDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Configuración del Reloj")
        self.resize(800, 500)
        
        # Crear layout principal
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        
        # Splitter para dividir la ventana
        splitter = QSplitter()
        main_layout.addWidget(splitter)
        
        # Lista de categorías
        self.category_list = QListWidget()
        self.category_list.setFixedWidth(150)
        self.category_list.addItems(["Fondo", "Borde", "Visualización", "Ayuda"])
        splitter.addWidget(self.category_list)
        
        # Widget apilado para las configuraciones
        self.stacked_widget = QStackedWidget()
        splitter.addWidget(self.stacked_widget)
        
        # Crear las páginas de configuración
        self.fondo_widget = FondoConfigWidget(parent)
        self.borde_widget = BordeConfigWidget(parent)
        self.visualizacion_widget = OpcionesVisibilidadWidget(parent)
        self.ayuda_widget = AyudaWidget(parent)
        
        self.stacked_widget.addWidget(self.fondo_widget)
        self.stacked_widget.addWidget(self.borde_widget)
        self.stacked_widget.addWidget(self.visualizacion_widget)
        self.stacked_widget.addWidget(self.ayuda_widget)
        
        # Conectar selección de lista a widget apilado
        self.category_list.currentRowChanged.connect(self.stacked_widget.setCurrentIndex)
        self.category_list.setCurrentRow(0)
        
        # Botones de control
        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        main_layout.addWidget(button_box)