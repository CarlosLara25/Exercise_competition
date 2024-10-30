import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QInputDialog

class WaitForInputExample(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the window
        self.setWindowTitle("Wait for Input Example")
        self.setGeometry(100, 100, 300, 200)

        # Create a button to trigger the event
        self.button = QPushButton("Get Input")
        self.button.clicked.connect(self.get_input)

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

    def get_input(self):
        # Show an input dialog and wait for user input
        text, ok = QInputDialog.getText(self, "Input Dialog", "Enter some text:")

        # Check if the user clicked OK and provided some input
        if ok and text:
            print(f"User entered: {text}")
        else:
            print("No input provided or dialog was canceled")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WaitForInputExample()
    window.show()
    sys.exit(app.exec_())