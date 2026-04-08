import math

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtCore import QTimer

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
        self.frames = load_sprite('spriteImages', self.num_frames)

        self.image = QLabel()
        self.current_image = 0
        self.timer = QTimer()
        self.timer_on = False
        self.current_fps = 0
        self.slider = QSlider()
        self.slider.setTickInterval(20)
        self.slider.setTickPosition(QSlider.TickPosition.TicksLeft)
        self.fps_label = QLabel("FPS:" + str(self.current_fps))
        self.start_stop_button = QPushButton("Start")

        self.setupUI()


    def setupUI(self):
        frame = QFrame()
        self.image.setPixmap(self.frames[self.current_image])


        self.timer.timeout.connect(self.animate)
        self.timer_on = False
        # self.timer.start(200)


        self.start_stop_button.clicked.connect(self.start_or_stop)

        slider_label = QLabel("FPS Adjuster")

        self.slider.setRange(1, 100)
        self.slider.valueChanged.connect(self.adjust_speed)


        button_layout = QHBoxLayout()
        button_layout.addWidget(self.start_stop_button)

        slider_layout = QVBoxLayout()
        slider_layout.addWidget(slider_label)
        slider_layout.addWidget(self.slider)


        picture_layout = QHBoxLayout()
        picture_layout.addStretch()
        picture_layout.addWidget(self.image)
        picture_layout.addStretch()
        picture_layout.addLayout(slider_layout)
        picture_layout.addStretch()

        label_layout = QHBoxLayout()
        label_layout.addStretch()
        label_layout.addWidget(self.fps_label)
        label_layout.addStretch()

        application_layout = QVBoxLayout()
        application_layout.addLayout(picture_layout)
        application_layout.addLayout(label_layout)
        application_layout.addLayout(button_layout)


        frame.setLayout(application_layout)

        self.setCentralWidget(frame)


    # You will need methods in the class to act as slots to connect to signals
    def animate(self):
        self.current_image += 1
        if self.current_image >= self.num_frames:
            self.current_image = 0

        self.image.setPixmap(self.frames[self.current_image])

        self.repaint()

    def adjust_speed(self, value):
        if self.timer_on:
            delay_in_ms = int(1000 / value)
            self.timer.start(delay_in_ms)
            self.current_fps = value
        else:
            self.slider.setValue(0)

        self.fps_label.setText("FPS:" + str(self.current_fps))


    def start_or_stop(self):
        if self.timer_on:
            self.timer_on = False
            self.timer.stop()
            self.adjust_speed(0)
            self.start_stop_button.setText("Start")
        else:
            self.timer_on = True
            self.adjust_speed(1)
            self.start_stop_button.setText("Stop")


def main():
    app = QApplication([])
    image = QImage('ColorfulTown.png')
    window = SpritePreview(image)

    window.show()
    app.exec()


if __name__ == "__main__":
    main()
