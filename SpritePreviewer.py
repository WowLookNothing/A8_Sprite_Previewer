import math

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

# This function loads a series of sprite images stored in a folder with a
# consistent naming pattern: sprite_# or sprite_##. It returns a list of the images.
def load_sprite(sprite_folder_name, number_of_frames):
    frames = []
    padding = math.ceil(math.log(number_of_frames - 1, 10))
    for frame in range(number_of_frames):
        folder_and_file_name = sprite_folder_name + "/sprite_" + str(frame).rjust(padding, '0') + ".png"
        frames.append(QPixmap(folder_and_file_name))

    return frames

class SpritePreview(QMainWindow):

    def __init__(self, image):
        super().__init__()
        self.setWindowTitle("Sprite Animation Preview")
        # This loads the provided sprite and would need to be changed for your own.
        self.num_frames = 21
        self.frames = load_sprite('spriteImages',self.num_frames)

        # Add any other instance variables needed to track information as the program
        # runs here

        self.label = QLabel()
        self.image = image

        # Make the GUI in the setupUI method
        self.setupUI()


    def setupUI(self):
        # An application needs a central widget - often a QFrame
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
        # Add a lot of code here to make layouts, more QFrame or QWidgets, and
        # the other components of the program.
        # Create needed connections between the UI components and slot methods
        # you define in this class.

        self.setCentralWidget(frame)


    # You will need methods in the class to act as slots to connect to signals


def main():
    app = QApplication([])
    image = QImage('ColorfulTown.png')
    window = SpritePreview(image)

    window.show()
    app.exec()


if __name__ == "__main__":
    main()
