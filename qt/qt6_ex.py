
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QMainWindow
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import Qt
import cv2
import sys

class ImageWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OpenCV Image in Qt 6")
        self.resize(800, 600)

        self.label = QLabel(self)
        self.setCentralWidget(self.label)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        cv_img = cv2.imread("input_image.png")
        if cv_img is None:
            print("Error: Could not load image")
            return

        resized = cv2.resize(cv_img, (800, 600))
        rgb_img = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)

        height, width, channels = rgb_img.shape
        print(f"{width} x {height}")
        bytes_per_line = channels * width

        q_img = QImage(
            rgb_img.data,
            width,
            height,
            bytes_per_line,
            QImage.Format.Format_RGB888
        )
        self.label.setPixmap(QPixmap.fromImage(q_img))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageWindow()
    window.show()
    sys.exit(app.exec())
