from PySide6.QtWidgets import (
    QWidget,
    QGridLayout,
)

from app.ui.widgets.image_card import ImageCard


class ImageGallery(QWidget):

    def __init__(self):
        super().__init__()

        self.grid = QGridLayout(self)

        self.grid.setSpacing(15)

        self.grid.setContentsMargins(10, 10, 10, 10)

    def clear(self):

        while self.grid.count():

            item = self.grid.takeAt(0)

            widget = item.widget()

            if widget:
                widget.deleteLater()

    def load_images(self, images):

        self.clear()

        row = 0
        col = 0

        for image in images:

            card = ImageCard(image)

            self.grid.addWidget(card, row, col)

            col += 1

            if col == 4:
                col = 0
                row += 1