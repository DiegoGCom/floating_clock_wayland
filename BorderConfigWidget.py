#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import (
    QLabel, QWidget,  QColorDialog,
    QSlider,  QVBoxLayout, QDialog, QPushButton, 
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import  QColor

class BorderConfigWidget(QWidget):
    def __init__(self, parent, translator):
        super().__init__()
        self.parent = parent
        self.translator = translator
        
        vbox = QVBoxLayout()
        vbox.setContentsMargins(20, 20, 20, 20)
        
        # Color del borde
        self.border_color_btn = QPushButton(self.translator.tr("border_change_color"))
        self.border_color_btn.clicked.connect(self.set_border_color)
        vbox.addWidget(self.border_color_btn)

        # Grosor del borde
        vbox.addWidget(QLabel(self.translator.tr("border_thickness")))
        self.border_slider = QSlider(Qt.Horizontal)
        self.border_slider.setRange(0, 20)
        self.border_slider.setValue(parent.border_thickness)
        self.border_slider.valueChanged.connect(self.set_border_thickness)
        vbox.addWidget(self.border_slider)

        # Radio del borde
        vbox.addWidget(QLabel(self.translator.tr("border_radius")))
        self.slider_radio = QSlider(Qt.Horizontal)
        self.slider_radio.setRange(0, 50)
        self.slider_radio.setValue(parent.border_radius)
        self.slider_radio.valueChanged.connect(self.set_border_radius)
        vbox.addWidget(self.slider_radio)

        # Espaciador
        vbox.addStretch()
        
        self.setLayout(vbox)
        
    def set_border_color(self):
        try:
            color = QColorDialog.getColor(
                initial=self.parent.border_color,
                parent=self.window(),
                options=QColorDialog.ShowAlphaChannel
            )
            if color.isValid():
                self.parent.set_border_color(color)
        except Exception as e:
            print(f"Error cambiando color de borde: {e}")

    def set_border_thickness(self, value):
        try:
            self.parent.set_border_thickness(value)
        except Exception as e:
            print(f"Error cambiando grosor de borde: {e}")

    def set_border_radius(self, value):
        try:
            self.parent.set_border_radius(value)
        except Exception as e:
            print(f"Error cambiando radio de bordes: {e}")
