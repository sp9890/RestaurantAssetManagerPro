from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QListWidget,
    QMessageBox,
)

from app.models.menu_item_model import MenuItem
from app.services.menu_service import MenuService
from app.ui.dialogs.menu_item_dialog import MenuItemDialog


class MenuPage(QWidget):

    def __init__(self):
        super().__init__()

        self.service = MenuService()

        self.build_ui()
        self.load_menu()

    def build_ui(self):

        layout = QVBoxLayout(self)

        buttons = QHBoxLayout()

        self.add_btn = QPushButton("➕ Add Item")
        self.delete_btn = QPushButton("🗑 Delete")

        buttons.addWidget(self.add_btn)
        buttons.addWidget(self.delete_btn)

        layout.addLayout(buttons)

        self.menu_list = QListWidget()

        layout.addWidget(self.menu_list)

        self.add_btn.clicked.connect(self.add_item)
        self.delete_btn.clicked.connect(self.delete_item)

    def load_menu(self):

        self.menu_list.clear()

        for item in self.service.get_menu():

            self.menu_list.addItem(
                f"{item.name} | ₹{item.price} | {item.category}"
            )

    def add_item(self):

        dialog = MenuItemDialog()

        if not dialog.exec():
         return

        try:
            price = float(dialog.price_edit.text())
        except ValueError:
            price = 0

        item = MenuItem(
            name=dialog.name_edit.text(),
            category=dialog.category_combo.currentText(),
            price=price,
            description=dialog.description_edit.toPlainText(),
            image=dialog.image_combo.currentText(),
        )

        self.service.add_item(item)

        self.load_menu()

    def delete_item(self):

        row = self.menu_list.currentRow()

        if row == -1:

            QMessageBox.information(
                self,
                "Delete",
                "Select a menu item first.",
            )

            return

        self.service.delete_item(row)

        self.load_menu()