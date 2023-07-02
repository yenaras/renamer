#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# rename/app.py

"""This module proveds the Renamer application."""
import sys
from PyQt5.QtWidgets import QApplication

from views import Window


def main():
    # Create the application
    app = QApplication(sys.argv)
    # Create and show the main window
    win = Window()
    win.show()
    # Run the event loop
    sys.exit(app.exec())
