from wsgiref.util import application_uri

from PyQt6 import QtGui
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

class ImageFormat(QMainWindow):

    def __init__(self, image):
        super().__init__()
        self.setWindowTitle("Image Viewer")
        self.image = image
        self.label = QLabel()
        self.setupUI()


    def setupUI(self):
        # An application needs a central widget - often a QFrame
	# A QFrame adds a border while a QWidget does not
        frame = QFrame()
        pixmap = QPixmap(self.image)
        self.label.setPixmap(pixmap)

        application_layout = QVBoxLayout()
        application_layout.addWidget(self.label)

        color_button = QPushButton("Colored Image")
        grayscale_button = QPushButton("Grayscale Image")

        button_layout = QHBoxLayout()
        button_layout.addWidget(color_button)
        button_layout.addWidget(grayscale_button)

        application_layout.addLayout(button_layout)

        frame.setLayout(application_layout)

        self.setCentralWidget(frame)


def main():
    app = QApplication([])
    image = QImage('ColorfulTown.png')
    window = ImageFormat(image)
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
