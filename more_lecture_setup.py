from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt, QTimer


class ImageSwitch(QWidget):
    def __init__(self, image1, image2):
        super().__init__()
        self.image1 = image1
        self.image2 = image2
        self.use_image_one = True
        self.setupUI()

    def setupUI(self):
        # The button to change the image
        switch = QPushButton('Switch Image')
        switch.clicked.connect(self.switch_image)
        # Make label an instance variable so we can
        # access it in other methods
        self.label = QLabel()
        self.label.setPixmap(self.image1)

        layout = QVBoxLayout()
        layout.addWidget(switch)
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.switch_image)
        self.timer.start(500)

    def switch_image(self):
        if self.use_image_one:
            self.label.setPixmap(self.image2)
            self.use_image_one = False
        else:
            self.label.setPixmap(self.image1)
            self.use_image_one = True
        # Force a redraw of the UI
        self.repaint()


class CustomWindow(QMainWindow):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.setupUI()

    def setupUI(self):
        frame = QWidget()
        layout = QHBoxLayout()


        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        file_menu = menubar.addMenu('&File')
        load_action = QAction('&Load', self)
        load_action.triggered.connect(self.load_image)
        file_menu.addAction(load_action)
        exit_action = QAction('&Exit', self)
        exit_action.triggered.connect(self.quit_program)
        file_menu.addAction(exit_action)

        self.original_image = QPixmap(self.image)
        self.image_view = QLabel();
        self.image_view.setPixmap(self.original_image)
        layout.addWidget(self.image_view)
        slider = QSlider()
        slider.setRange(0, 100)
        slider.setValue(50)
        slider.valueChanged.connect(self.resize_trigger)
        layout.addWidget(slider)


        frame.setLayout(layout)

        self.setCentralWidget(frame)

    def quit_program(self):
        self.close()

    def load_image(self):
        # A dialog open a "predefined window" for a specific purpose, e.g: FileDialog is the window that shows up when choosing a file
        filepath, _ = QFileDialog.getOpenFileName(
            self,
            "Open Image File",
            "",
            "Images (*.png *.jpg *.jpeg *.bmp)"
        )
        if filepath:
            print("Loading image:", filepath)
            self.image = filepath
            self.original_image = QPixmap(self.image)
            self.image_view.setPixmap(self.original_image)
            self.repaint()

    def resize_trigger(self, value):
        scale = value / 100
        width = max(1, self.original_image.width() * scale)
        height = max(1, self.original_image.height() * scale)
        print("0")
        print(width, height)
        # scaled = self.original_image.scaled(
        #     width, height,
        #     Qt.AspectRatioMode.KeepAspectRatio,
        #     Qt.TransformationMode.SmoothTransformation)
        scaled = self.original_image
        # print("0.5")
        self.image_view.setPixmap(scaled)
        # print("1")
        self.repaint()
        # print("2")


def main():
    app = QApplication([])
    image1 = QPixmap("ColorfulTown.png")
    window = CustomWindow(image1)

    # window = QWidget()
    # layout = QVBoxLayout()
    # window.setLayout(layout)
    # image1 = QPixmap("spriteImages/sprite_00.png")
    # image2 = QPixmap("spriteImages/sprite_01.png")
    # layout.addWidget(ImageSwitch(image1, image2))

    window.show()
    app.exec()


if __name__ == "__main__":
    main()
