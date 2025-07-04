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


class FondoConfigWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        
        vbox = QVBoxLayout()
        vbox.setContentsMargins(20, 20, 20, 20)
        
        # Botón para seleccionar color de fondo
        self.color_btn = QPushButton("Cambiar color de fondo")
        self.color_btn.clicked.connect(self.set_background_color)
        vbox.addWidget(self.color_btn)

        # Slider para opacidad fondo
        vbox.addWidget(QLabel("Opacidad del fondo (%)"))
        self.slider_opacity = QSlider(Qt.Horizontal)
        self.slider_opacity.setRange(10, 100)
        self.slider_opacity.setValue(int(parent.opacity * 100))
        self.slider_opacity.valueChanged.connect(self.set_opacity)
        vbox.addWidget(self.slider_opacity)

        # Botón para color de texto
        self.text_color_btn = QPushButton("Cambiar color del texto")
        self.text_color_btn.clicked.connect(self.set_text_color)
        vbox.addWidget(self.text_color_btn)

        # Espaciador
        vbox.addStretch()
        
        self.setLayout(vbox)

    def set_background_color(self):
        try:
            color = QColorDialog.getColor(
                initial=self.parent.bg_color,
                parent=self.window(),
                options=QColorDialog.ShowAlphaChannel
            )
            if color.isValid():
                self.parent.set_fondo(color)
        except Exception as e:
            print(f"Error cambiando color de fondo: {e}")

    def set_text_color(self):
        try:
            color = QColorDialog.getColor(
                initial=self.parent.text_color,
                parent=self.window(),
                options=QColorDialog.ShowAlphaChannel
            )
            if color.isValid():
                self.parent.set_text_color(color)
        except Exception as e:
            print(f"Error cambiando color de texto: {e}")

    def set_opacity(self, value):
        try:
            self.parent.set_opacity(value / 100)
        except Exception as e:
            print(f"Error cambiando opacidad: {e}")