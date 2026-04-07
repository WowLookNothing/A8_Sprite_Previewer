def switch_image(self):
    if self.use_image_one:
        self.label.setPixmap(self.image2)
        self.use_image_one = False
    else:
        self.label.setPixmap(self.image1)
        self.use_image_one = True
    # Force a redraw of the UI
    self.repaint()
