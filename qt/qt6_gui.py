import sys
# Import required Qt modules
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 1. Configure the main window properties
        self.setWindowTitle("My First Qt Python App")
        self.resize(400, 200)

        # 2. Create the core interactive widgets
        self.label = QLabel("Enter something below and click the button:")
        self.label.setAlignment(Qt.AlignCenter) # Center the text
        
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Type text here...")

        self.button = QPushButton("Click Me!")
        
        # 3. Connect the button click event (Signal) to a function (Slot)
        self.button.clicked.connect(self.handle_button_click)

        # 4. Arrange widgets vertically using a Layout Manager
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input_field)
        layout.addWidget(self.button)

        # 5. Set the layout inside a central widget container
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def handle_button_click(self):
        """This function executes whenever the button is clicked."""
        user_text = self.input_field.text()
        if user_text.strip():
            self.label.setText(f"You typed: {user_text}")
        else:
            self.label.setText("Please type something first!")

# 6. Initialize and start the application event loop
if __name__ == "__main__":
    app = QApplication(sys.argv) # Coordinates the application setup
    window = MainWindow()        # Instantiate the window class
    window.show()                # Windows are hidden by default, make it visible
    sys.exit(app.exec())         # Start the event loop and safely exit on close
