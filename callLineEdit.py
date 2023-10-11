import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QDialog, QApplication

from ELO import *


class MyForm(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi("ELO.ui", self)
        #self.ui = Ui_Dialog()
        #.ui.setupUi(self)
        self.ui.ButtonClick.clicked.connect(self.dispmessage)
        self.show()

    def dispmessage(self):
        self.ui.label.setText("masz " + self.ui.lineEditIQ.text() + " iq XD")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyForm()
    window.show()
    sys.exit(app.exec())