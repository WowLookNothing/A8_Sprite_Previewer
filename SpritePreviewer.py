#Cassandra Manning u1577928
#GitHub repo = https://github.com/WowLookNothing/A8_Sprite_Previewer

import math
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import QTimer

def load_sprite(sprite_folder_name, number_of_frames):
    frames = []
    padding = math.ceil(math.log(number_of_frames - 1, 10))
    for frame in range(number_of_frames):
        folder_and_file_name = sprite_folder_name + "/sprite_" + str(frame).rjust(padding, '0') + ".png"
        frames.append(QPixmap(folder_and_file_name))
    return frames

class SpritePreview(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sprite Animation Preview")
        self.num_frames = 21
        self.frames = load_sprite('spriteImages', self.num_frames)
        self.image = QLabel()
        self.current_image = 0

        self.timer = QTimer()
        self.timer_on = False
        self.current_fps = 0
        self.slider = QSlider()
        self.slider.setTickInterval(20)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self.fps_label = QLabel(str(self.current_fps))
        self.start_stop_button = QPushButton("Start")

        self.setupUI()

    def setupUI(self):
        frame = QFrame()

        self.image.setPixmap(self.frames[self.current_image])
        self.timer.timeout.connect(self.animate)
        self.timer_on = False

        self.start_stop_button.clicked.connect(self.start_or_stop)

        self.slider.setRange(1, 100)
        self.slider.valueChanged.connect(self.adjust_speed)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        menu = menubar.addMenu("&Menu")
        pause_action = QAction("&Pause", self)
        pause_action.triggered.connect(self.stop)
        exit_action = QAction("&Exit", self)
        exit_action.triggered.connect(self.quit_program)

        menu.addAction(pause_action)
        menu.addAction(exit_action)

        slider_label = QLabel("FPS Adjuster")
        fps_label = QLabel("Frames per second:")

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
        label_layout.addWidget(fps_label)
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
            self.current_fps = 0

        self.fps_label.setText(str(self.current_fps))


    def start_or_stop(self, *args):
        if not self.timer_on:
            self.start()

        else:
            self.stop()

    def stop(self):
        self.timer_on = False
        self.timer.stop()
        self.adjust_speed(0)
        self.start_stop_button.setText("Start")

    def start(self):
        self.timer_on = True
        self.adjust_speed(1)
        self.start_stop_button.setText("Stop")

    def quit_program(self):
        self.close()



def main():
    app = QApplication([])
    window = SpritePreview()

    window.show()
    app.exec()


if __name__ == "__main__":
    main()
