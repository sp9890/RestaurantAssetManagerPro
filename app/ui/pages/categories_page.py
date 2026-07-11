from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QListWidget,
    QInputDialog,
    QMessageBox,
)

from app.services.category_service import CategoryService


class CategoriesPage(QWidget):

    def __init__(self):
        super().__init__()

        self.service = CategoryService()

        self.build_ui()

        self.load_categories()

    def build_ui(self):

        layout = QVBoxLayout(self)

        buttons = QHBoxLayout()

        self.add_btn = QPushButton("➕ Add Category")
        self.delete_btn = QPushButton("🗑 Delete")

        buttons.addWidget(self.add_btn)
        buttons.addWidget(self.delete_btn)

        layout.addLayout(buttons)

        self.list = QListWidget()

        layout.addWidget(self.list)

        self.add_btn.clicked.connect(self.add_category)
        self.delete_btn.clicked.connect(self.delete_category)

    def load_categories(self):

        self.list.clear()

        for category in self.service.get_categories():

            self.list.addItem(category.name)

    def add_category(self):

        name, ok = QInputDialog.getText(
            self,
            "Category",
            "Category Name",
        )

        if not ok or not name:
            return

        self.service.add_category(name)

        self.load_categories()

    def delete_category(self):

        row = self.list.currentRow()

        if row == -1:

            QMessageBox.information(
                self,
                "Delete",
                "Select a category first.",
            )

            return

        categories = self.service.get_categories()

        categories.pop(row)

        import json
        from dataclasses import asdict

        with open("app/database/categories.json", "w") as f:

            json.dump(
                [asdict(c) for c in categories],
                f,
                indent=4,
            )

        self.load_categories()