from PyQt6.QtWidgets import *

def on_button_clicked():
    print("I was clicked!")

def main():
    app = QApplication([])
    window = QWidget()
    layout = QVBoxLayout()
    window.setLayout(layout)

    press_me = QPushButton("Press Me!")
    press_me.clicked.connect(on_button_clicked)
    layout.addWidget(press_me)
    layout.addWidget(QPushButton("Nothing"))

    slider = QSlider()
    layout.addWidget(slider)

    lcd = QLCDNumber()
    lcd.setMinimumHeight(60)

    slider.valueChanged.connect(lcd.display)

    layout.addWidget(lcd)


    window.show()
    app.exec()

if __name__ == "__main__":
    main()
