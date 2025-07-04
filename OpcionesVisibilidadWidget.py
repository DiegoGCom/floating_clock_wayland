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

class OpcionesVisibilidadWidget(QWidget):
    def __init__(self, parent, type=QWidget):
        super().__init__()
        self.parent = parent
        
        self.main_window= parent.parentWidget()
        
        vbox = QVBoxLayout()
        vbox.setContentsMargins(20, 20, 20, 20)
        
        # Checkbox mostrar segundos
        self.chk_segundos = QCheckBox("Mostrar segundos")
        self.chk_segundos.setChecked(parent.show_seconds)
        self.chk_segundos.stateChanged.connect(self.toggle_segundos)
        vbox.addWidget(self.chk_segundos)

        # Checkbox mostrar fecha
        self.chk_fecha = QCheckBox("Mostrar fecha")
        self.chk_fecha.setChecked(parent.show_date)
        self.chk_fecha.stateChanged.connect(self.toggle_fecha)
        vbox.addWidget(self.chk_fecha)

        # Selector de formato de fecha
        vbox.addWidget(QLabel("Formato de fecha:"))
        self.date_format = QComboBox()
        self.date_format.addItems(["dd/MM/yyyy", "MM/dd/yyyy", "yyyy-MM-dd", "ddd, MMM d"])
        self.date_format.setCurrentText(parent.date_format)
        self.date_format.currentTextChanged.connect(self.cambiar_formato_fecha)
        vbox.addWidget(self.date_format)

        # Selector de fuente
        vbox.addWidget(QLabel("Fuente:"))
        self.font_combo = QFontComboBox()
        self.font_combo.setCurrentFont(QFont(parent.font_family, parent.font_size))
        self.font_combo.currentFontChanged.connect(self.cambiar_fuente)
        vbox.addWidget(self.font_combo)

        # Tamaño de fuente
        vbox.addWidget(QLabel("Tamaño de fuente:"))
        self.font_size = QSpinBox()
        self.font_size.setRange(8, 72)
        self.font_size.setValue(parent.font_size)
        self.font_size.valueChanged.connect(self.cambiar_tamano_fuente)
        vbox.addWidget(self.font_size)

        # Control de tamaño de ventana
        vbox.addWidget(QLabel("<b>Tamaño de ventana:</b>"))
        
        grid = QGridLayout()
        vbox.addLayout(grid)

        # Ancho
        grid.addWidget(QLabel("Ancho:"), 0, 0)
        self.spin_width = QSpinBox()
        self.spin_width.setRange(100, 1000)
        self.spin_width.setValue(parent.width())
        self.spin_width.valueChanged.connect(parent.set_window_width)
        grid.addWidget(self.spin_width, 0, 1)
        
        # Alto
        grid.addWidget(QLabel("Alto:"), 1, 0)
        self.spin_height = QSpinBox()
        self.spin_height.setRange(50, 500)
        self.spin_height.setValue(parent.height())
        self.spin_height.valueChanged.connect(parent.set_window_height)
        grid.addWidget(self.spin_height, 1, 1)
    
        # Espaciador
        vbox.addStretch()
        
        self.setLayout(vbox)

    def update_position_values(self):
        """Actualiza los valores de posición en los spinboxes"""
        self.spin_x.setValue(self.parent.x())
        self.spin_y.setValue(self.parent.y())

    def toggle_segundos(self, state):
        try:
            self.parent.show_seconds = (state == Qt.Checked)
            self.parent._update_display()
        except Exception as e:
            print(f"Error cambiando visibilidad segundos: {e}")

    def toggle_fecha(self, state):
        try:
            self.parent.show_date = (state == Qt.Checked)
            self.parent._update_display()
        except Exception as e:
            print(f"Error cambiando visibilidad fecha: {e}")

    def cambiar_formato_fecha(self, formato):
        try:
            self.parent.date_format = formato
            self.parent._update_display()
        except Exception as e:
            print(f"Error cambiando formato fecha: {e}")

    def cambiar_fuente(self, font):
        try:
            self.parent.font_family = font.family()
            self.parent._apply_fonts()
        except Exception as e:
            print(f"Error cambiando fuente: {e}")

    def cambiar_tamano_fuente(self, size):
        try:
            self.parent.font_size = size
            self.parent._apply_fonts()
        except Exception as e:
            print(f"Error cambiando tamaño de fuente: {e}")