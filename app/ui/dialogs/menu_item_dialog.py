from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QFormLayout,
    QLineEdit,
    QTextEdit,
    QComboBox,
    QPushButton,
    QHBoxLayout,
)

from app.services.category_service import CategoryService
from app.services.image_service import ImageService
from app.core.image_matcher import ImageMatcher


class MenuItemDialog(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Add Menu Item")
        self.resize(550, 420)

        self.build_ui()

    def build_ui(self):

        layout = QVBoxLayout(self)

        form = QFormLayout()

        # Menu Name
        self.name_edit = QLineEdit()

        # Category
        self.category_combo = QComboBox()

        for category in CategoryService().get_categories():
            self.category_combo.addItem(category.name)

        # Price
        self.price_edit = QLineEdit()

        # Description
        self.description_edit = QTextEdit()

        # Images
        self.image_combo = QComboBox()

        images = ImageService().get_last_images()

        for image in images:
            self.image_combo.addItem(image["name"])

        form.addRow("Menu Name", self.name_edit)
        form.addRow("Category", self.category_combo)
        form.addRow("Price", self.price_edit)
        form.addRow("Description", self.description_edit)
        form.addRow("Image", self.image_combo)

        layout.addLayout(form)

        # Buttons
        buttons = QHBoxLayout()

        cancel = QPushButton("Cancel")
        save = QPushButton("Save")

        cancel.clicked.connect(self.reject)
        save.clicked.connect(self.accept)

        buttons.addStretch()
        buttons.addWidget(cancel)
        buttons.addWidget(save)

        layout.addLayout(buttons)

        # Auto image matching
        self.name_edit.editingFinished.connect(
            self.auto_match_image
        )

    def auto_match_image(self):

        image_names = []

        for i in range(self.image_combo.count()):
            image_names.append(
                self.image_combo.itemText(i)
            )

        match = ImageMatcher.find_best_match(
            self.name_edit.text(),
            image_names,
        )

        if match:

            index = self.image_combo.findText(match)

            if index >= 0:
                self.image_combo.setCurrentIndex(index)