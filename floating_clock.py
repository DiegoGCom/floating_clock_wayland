#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QApplication 
from ClockApp import ClockApp


if __name__ == "__main__":
    app = QApplication(sys.argv)
    reloj = ClockApp()
    reloj.show()
    app.exec_()