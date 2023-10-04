import sys

from PyQt6.QtWidgets import QDialog

from ELO import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog