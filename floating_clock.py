#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QApplication 
from RelojFlotante import RelojFlotante


if __name__ == "__main__":
    app = QApplication(sys.argv)
    reloj = RelojFlotante()
    reloj.show()
    app.exec_()