import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QStatusBar
from PySide6.QtWidgets import QVBoxLayout, QGridLayout, QLabel, QPushButton, QWidget, QSlider
from PySide6.QtWidgets import QFileDialog, QListWidget
from PySide6.QtGui import QAction, QImage, QPixmap
from PySide6.QtCore import Qt
from pathlib import Path
import cv2
import numpy as np

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 1. Configure general window properties
        self.setWindowTitle("QMainWindow Example")
        self.setGeometry(100, 100, 640, 480)
        
        self.file_list = QListWidget(self)

        self.label = QLabel("Hello World!")
        grid_layout = QGridLayout()

        self.button1 = QPushButton("Read")
        self.button1.clicked.connect(self.on_button1_click)

        self.button2 = QPushButton("File")
        self.button2.clicked.connect(self.on_button2_click)

        self.button3 = QPushButton("Folder")
        self.button3.clicked.connect(self.on_button3_click)

        self.button4 = QPushButton("Original")
        self.button4.clicked.connect(self.on_button4_click)

        self.button5 = QPushButton("Negative")
        self.button5.clicked.connect(self.on_button5_click)

        self.button6 = QPushButton("Log Trans")
        self.button6.clicked.connect(self.on_button6_click)

        self.button7 = QPushButton("HSV")
        self.button7.clicked.connect(self.on_button7_click)

        self.button8 = QPushButton("LAB")
        self.button8.clicked.connect(self.on_button8_click)

        self.button9 = QPushButton("GRAY")
        self.button9.clicked.connect(self.on_button9_click)

        grid_layout.addWidget(self.button1, 0, 0)
        grid_layout.addWidget(self.button2, 1, 0)
        grid_layout.addWidget(self.button3, 2, 0)
        grid_layout.addWidget(QLabel("width"), 7, 0)
        grid_layout.addWidget(QLabel("height"), 8, 0)
        grid_layout.addWidget(QSlider(orientation=Qt.Orientation.Horizontal), 9, 0, 1, 3)
        grid_layout.addWidget(self.label, 0, 1, 9, 1)
        grid_layout.addWidget(self.button4, 0, 2)
        grid_layout.addWidget(self.button5, 1, 2)
        grid_layout.addWidget(self.button6, 2, 2)
        grid_layout.addWidget(self.button7, 3, 2)
        grid_layout.addWidget(self.button8, 4, 2)
        grid_layout.addWidget(self.button9, 5, 2)
        grid_layout.addWidget(QPushButton("Button 10"), 6, 2)
        grid_layout.addWidget(QPushButton("Button 11"), 7, 2)
        grid_layout.addWidget(QPushButton("Button 12"), 8, 2)

        widget = QWidget()
        widget.setLayout(grid_layout)
        self.setCentralWidget(widget)
        
        # 3. Create the Menu Bar and add an Action
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")
        
        exit_action = QAction("&Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # 4. Create the Status Bar
        self.status_bar = QStatusBar(self)
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Ready", 3000) # Displays message for 3 seconds

    def on_button1_click(self):
        print('on_button1_click')

        cv_img = cv2.imread("geese.png")
        if cv_img is None:
            print("Error: Could not load image")
        resized_cv_img = cv2.resize(cv_img, (800, 600))
        self.rgb_img = cv2.cvtColor(resized_cv_img, cv2.COLOR_BGR2RGB)
        self.height, self.width, channels = self.rgb_img.shape
        self.bytes_per_line = channels * self.width

        self.q_img = QImage(
            self.rgb_img.data, self.width, self.height, self.bytes_per_line,
            QImage.Format.Format_RGB888
        )

        self.label.setPixmap(QPixmap.fromImage(self.q_img))

    def on_button2_click(self):
        print("on_button2_click")
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        dialog.setDirectory(r'.')
        dialog.setNameFilter("Images (*.png *.jpg)")
        dialog.setViewMode(QFileDialog.ViewMode.List)
        if dialog.exec():
            filenames = dialog.selectedFiles()
            if filenames:
                self.file_list.addItems([str(Path(filename)) for filename in filenames])
        print(f"File name: {self.file_list}")

    def on_button3_click(self):
        print("on_button3_click")

    def on_button4_click(self):
        self.q_img = QImage(
            self.rgb_img.data, self.width, self.height, self.bytes_per_line,
            QImage.Format.Format_RGB888
        )
        self.label.setPixmap(QPixmap.fromImage(self.q_img))

    def on_button5_click(self):
        print('on_button4_click')

        negative_img = 255 - self.rgb_img
        self.q_img = QImage(
            negative_img.data, self.width, self.height, self.bytes_per_line,
            QImage.Format.Format_RGB888
        )
        self.label.setPixmap(QPixmap.fromImage(self.q_img))

    def on_button6_click(self):
        print('on_button6_click')

        c = 255 / (np.log(1 + np.max(self.rgb_img)))
        log_transformed = c * np.log(1 + self.rgb_img)
        log_transformed = np.array(log_transformed, dtype=np.uint8)

        self.q_img = QImage(
            log_transformed.data, self.width, self.height, self.bytes_per_line,
            QImage.Format.Format_RGB888
        )
        self.label.setPixmap(QPixmap.fromImage(self.q_img))

    def on_button7_click(self):
        print('on_button7_click')

        hsv_img = cv2.cvtColor(self.rgb_img, cv2.COLOR_RGB2HSV)
        self.q_img = QImage(
            hsv_img.data, self.width, self.height, self.bytes_per_line,
            QImage.Format.Format_RGB888
        )
        self.label.setPixmap(QPixmap.fromImage(self.q_img))

    def on_button8_click(self):
        print('on_button8_click')

        lab_img = cv2.cvtColor(self.rgb_img, cv2.COLOR_RGB2LAB)
        self.q_img = QImage(
            lab_img.data, self.width, self.height, self.bytes_per_line,
            QImage.Format.Format_RGB888
        )
        self.label.setPixmap(QPixmap.fromImage(self.q_img))

    def on_button9_click(self):
        print('on_button9_click')

        gray_img = cv2.cvtColor(self.rgb_img, cv2.COLOR_RGB2GRAY)
        bytes_per_line = self.width
        self.q_img = QImage(
            gray_img.data, self.width, self.height, bytes_per_line,
            QImage.Format.Format_Grayscale8
        )
        self.label.setPixmap(QPixmap.fromImage(self.q_img))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
