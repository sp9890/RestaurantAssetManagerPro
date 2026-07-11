from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QFormLayout,
    QLineEdit,
    QTextEdit,
    QComboBox,
    QPushButton,
    QHBoxLayout,
    QLabel,
)

from app.services.category_service import CategoryService
from app.services.image_service import ImageService
from app.core.image_matcher import ImageMatcher


class MenuItemDialog(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Add Menu Item")
        self.resize(550, 480)

        self.images = []

        self.build_ui()

    def build_ui(self):

        layout = QVBoxLayout(self)

        form = QFormLayout()

        self.name_edit = QLineEdit()

        self.category_combo = QComboBox()

        for category in CategoryService().get_categories():
            self.category_combo.addItem(category.name)

        self.price_edit = QLineEdit()

        self.description_edit = QTextEdit()

        self.image_combo = QComboBox()

        self.images = ImageService().get_last_images()

        for image in self.images:
            self.image_combo.addItem(image["name"])

        self.match_label = QLabel("")

        form.addRow("Menu Name", self.name_edit)
        form.addRow("Category", self.category_combo)
        form.addRow("Price", self.price_edit)
        form.addRow("Description", self.description_edit)
        form.addRow("Image", self.image_combo)
        form.addRow("", self.match_label)

        layout.addLayout(form)

        buttons = QHBoxLayout()

        cancel = QPushButton("Cancel")
        save = QPushButton("Save")

        cancel.clicked.connect(self.reject)
        save.clicked.connect(self.accept)

        buttons.addStretch()
        buttons.addWidget(cancel)
        buttons.addWidget(save)

        layout.addLayout(buttons)

        self.name_edit.textChanged.connect(
            self.auto_match_image
        )

    def auto_match_image(self):

        image_names = [
            image["name"]
            for image in self.images
        ]

        match = ImageMatcher.find_best_match(
            self.name_edit.text(),
            image_names,
        )

        if not match:

            self.match_label.setText(
                "❌ No matching image found"
            )

            return

        index = self.image_combo.findText(match)

        if index >= 0:

            self.image_combo.setCurrentIndex(index)

            self.match_label.setText(
                f"✅ Auto matched: {match}"
            )