#!/usr/bin/env python3

import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QLabel, QWidget, QMenu, QVBoxLayout, QDialog, QSizePolicy
)
from PyQt5.QtCore import Qt, QTimer, QTime, QDate, QSettings, QPoint
from PyQt5.QtGui import QFont, QColor, QPainter, QBrush, QPen

from ConfigDialog import ConfigDialog


class RelojFlotante(QWidget):
    def __init__(self):
        super().__init__()
        self.settings = QSettings("FloatingClock", "Config")
        self._load_settings()

        self.bg_color = QColor(self.settings.value("color_fondo", "#000000", type=str))
        self.text_color = QColor(self.settings.value("text_color", "#FFFFFF", type=str))
        self.border_color = QColor(self.settings.value("borde_color", "#FF0000", type=str))

        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |
            Qt.Tool |
            Qt.X11BypassWindowManagerHint
        )
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(self.window_width, self.window_height)

        self._create_widgets()
        self._apply_fonts()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self._update_display)
        self.timer.start(1000)
        self._update_display()

        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.open_config_menu)

        self.is_wayland = "wayland" in os.getenv("XDG_SESSION_TYPE", "").lower()
        print(f"Entorno Wayland detectado: {self.is_wayland}")

    def _load_settings(self):
        s = self.settings
        self.border_radius = s.value("border_radius", 20, type=int)
        self.border_thickness = s.value("border_thickness", 3, type=int)
        self.opacity = s.value("opacity", 0.6, type=float)
        self.bg_color = QColor(s.value("bg_color", "#000000", type=str))
        self.text_color = QColor(s.value("text_color", "#FFFFFF", type=str))
        self.border_color = QColor(s.value("border_color", "#FF0000", type=str))
        self.font_family = s.value("font_family", "Monospace", type=str)
        self.font_size = s.value("font_size", 30, type=int)
        self.show_seconds = s.value("show_seconds", True, type=bool)
        self.show_date = s.value("show_date", False, type=bool)
        self.date_format = s.value("date_format", "dd/MM/yyyy", type=str)
        self.window_width = s.value("window_width", 300, type=int)
        self.window_height = s.value("window_height", 150, type=int)
        self.window_x = s.value("window_x", 200, type=int)
        self.window_y = s.value("window_y", 200, type=int)

    def _create_widgets(self):
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.time_label = QLabel(self)
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setFixedHeight(90)
        self.time_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.time_label.setStyleSheet(f"color: {self.text_color.name()}; background: transparent; ")

        self.date_label = QLabel(self)
        self.date_label.setAlignment(Qt.AlignCenter)
        self.date_label.setFixedHeight(40)
        self.date_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.date_label.setStyleSheet(f"color: {self.text_color.name()}; background: transparent; margin:0px 10px 10px 10px")

        self.layout.addWidget(self.time_label)
        self.layout.addWidget(self.date_label)
        self.setLayout(self.layout)

    def _apply_fonts(self):
        try:
            font = QFont(self.font_family, self.font_size)
            font.setBold(True)
            self.time_label.setFont(font)

            date_font = QFont(self.font_family, max(12, self.font_size - 6))
            self.date_label.setFont(date_font)
        except Exception as e:
            print(f"Error actualizando estilo de fuente: {e}")

    def open_config_menu(self, pos):
        try:
            menu = QMenu(self)
            menu.addAction("Configuración").triggered.connect(self.abrir_dialog_config)
            menu.addAction("Salir").triggered.connect(self.close)
            menu.exec_(self.mapToGlobal(pos))
        except Exception as e:
            print(f"Error abriendo menú contextual: {e}")

    def abrir_dialog_config(self):
        try:
            dlg = ConfigDialog(self)
            self.config_dialog = dlg
            if dlg.exec_() == QDialog.Accepted:
                self._save_settings()
            self.config_dialog = None
        except Exception as e:
            print(f"Error abriendo diálogo de configuración: {e}")

    def _update_display(self):
        try:
            fmt = "HH:mm:ss" if self.show_seconds else "HH:mm"
            hora_actual = QTime.currentTime().toString(fmt)
            self.time_label.setText(hora_actual)

            if self.show_date:
                fecha_actual = QDate.currentDate().toString(self.date_format)
                self.date_label.setText(fecha_actual)
                self.date_label.setVisible(True)
            else:
                self.date_label.setVisible(False)
        except Exception as e:
            print(f"Error actualizando hora: {e}")

    def paintEvent(self, event):
        try:
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing)

            fondo = QColor(self.bg_color)
            fondo.setAlphaF(self.opacity)
            painter.setBrush(QBrush(fondo))
            painter.setPen(Qt.NoPen)

            rect = self.rect()
            painter.drawRoundedRect(rect, self.border_radius, self.border_radius)

            if self.border_thickness > 0:
                pen = QPen(self.border_color, self.border_thickness)
                pen.setJoinStyle(Qt.RoundJoin)
                painter.setPen(pen)
                painter.setBrush(Qt.NoBrush)

                margin = int(self.border_thickness / 2)
                border_rect = rect.adjusted(margin, margin, -margin, -margin)
                painter.drawRoundedRect(border_rect, self.border_radius, self.border_radius)
        except Exception as e:
            print(f"Error en paintEvent: {e}")

    def mousePressEvent(self, ev):
        if ev.button() == Qt.LeftButton:
            handle = self.windowHandle()
            if handle:
                handle.startSystemMove()
            ev.accept()
        elif ev.button() == Qt.MiddleButton:
            handle = self.windowHandle()
            if handle:
                handle.startSystemResize(Qt.RightEdge | Qt.BottomEdge)
            ev.accept()
        else:
            super().mousePressEvent(ev)

    # Métodos de modificación
    def _save_settings(self):
        try:
            s = self.settings
            s.setValue("border_radius", self.border_radius)
            s.setValue("border_thickness", self.border_thickness)
            s.setValue("opacity", self.opacity)
            s.setValue("bg_color", self.bg_color.name())
            s.setValue("text_color", self.text_color.name())
            s.setValue("border_color", self.border_color.name())
            s.setValue("font_family", self.font_family)
            s.setValue("font_size", self.font_size)
            s.setValue("show_seconds", self.show_seconds)
            s.setValue("show_date", self.show_date)
            s.setValue("date_format", self.date_format)
            s.setValue("window_width", self.window_width)
            s.setValue("window_height", self.window_height)
            s.setValue("window_x", self.window_x)
            s.setValue("window_y", self.window_y)
        except Exception as e:
            print(f"Error guardando configuración: {e}")

    def set_window_width(self, width): self.window_width = width; self.resize(self.window_width, self.window_height)
    def set_window_height(self, height): self.window_height = height; self.resize(self.window_width, self.window_height)
    def set_window_x(self, x): self.window_x = x; self.move(self.window_x, self.window_y)
    def set_window_y(self, y): self.window_y = y; self.move(self.window_x, self.window_y)
    def set_fondo(self, color: QColor): self.bg_color = color; self.update()
    def set_text_color(self, color: QColor): self.text_color = color; self.time_label.setStyleSheet(f"color: {color.name()}; background: transparent;"); self.date_label.setStyleSheet(f"color: {color.name()}; background: transparent;"); self.update()
    def set_border_radius(self, value): self.border_radius = value; self.update()
    def set_border_color(self, color): self.border_color = color; self.update()
    def set_border_thickness(self, thickness): self.border_thickness = thickness; self.update()
    def set_opacity(self, value): self.opacity = max(0.1, min(1.0, value)); self.update()


