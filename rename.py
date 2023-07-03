#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# rprename/rename.py

"""This module provides the Renamer class to rename multiple files."""

from pathlib import Path

from PyQt5.QtCore import QObject, pyqtSignal


class Renamer(QObject):
    # Define custom signals
    progressed = pyqtSignal(int)
    renamedFile = pyqtSignal(Path)
    finished = pyqtSignal()

    def __init__(self, files, prefix):
        super().__init__()
        self._files = files
        self._prefix = prefix

    def renameFiles(self):
        for fileNumber, file in enumerate(self._files, 1):
            newFile = file.parent.joinpath(
                f"{self._prefix}{str(fileNumber)}{file.suffix}"
            )
            file.rename(newFile)
            self.progressed.emit(fileNumber)
            self.renamedFile.emit(newFile)
        self.progressed.emit(0)
        self.finished.emit()
