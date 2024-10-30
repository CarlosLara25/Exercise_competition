# Only needed for access to command line arguments
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QDialog
from PyQt5.uic import loadUi
# Only needed for access to command line arguments
import sys

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("Game.ui", self)



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()