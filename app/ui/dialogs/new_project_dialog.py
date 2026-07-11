from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QFormLayout,
    QLineEdit,
    QPushButton,
    QFileDialog,
    QHBoxLayout,
)


class NewProjectDialog(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Create New Project")
        self.resize(550, 300)

        self.build_ui()

    def build_ui(self):

        layout = QVBoxLayout(self)

        form = QFormLayout()

        self.name_edit = QLineEdit()
        self.location_edit = QLineEdit()
        self.menu_edit = QLineEdit()
        self.bulk_edit = QLineEdit()

        form.addRow("Restaurant Name:", self.name_edit)
        # form.addRow("Project Location:", self.location_edit)
        form.addRow("Menu Folder:", self.menu_edit)
        form.addRow("Bulk Images Folder:", self.bulk_edit)

        layout.addLayout(form)

        browse_layout = QHBoxLayout()

        btn_location = QPushButton("Browse Project")
        btn_menu = QPushButton("Browse Menu")
        btn_bulk = QPushButton("Browse Images")

        btn_location.clicked.connect(
            lambda: self.select_folder(self.location_edit)
        )

        btn_menu.clicked.connect(
            lambda: self.select_folder(self.menu_edit)
        )

        btn_bulk.clicked.connect(
            lambda: self.select_folder(self.bulk_edit)
        )

        browse_layout.addWidget(btn_location)
        browse_layout.addWidget(btn_menu)
        browse_layout.addWidget(btn_bulk)

        layout.addLayout(browse_layout)

        layout.addStretch()

        action_layout = QHBoxLayout()

        cancel_btn = QPushButton("Cancel")
        create_btn = QPushButton("Create Project")

        cancel_btn.clicked.connect(self.reject)
        create_btn.clicked.connect(self.accept)

        action_layout.addStretch()
        action_layout.addWidget(cancel_btn)
        action_layout.addWidget(create_btn)

        layout.addLayout(action_layout)

    def select_folder(self, line_edit):

        folder = QFileDialog.getExistingDirectory(self)

        if folder:
            line_edit.setText(folder)