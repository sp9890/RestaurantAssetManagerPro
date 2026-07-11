from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QFileDialog,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
)

from app.services.settings_service import SettingsService


class SettingsPage(QWidget):

    def __init__(self):

        super().__init__()

        self.service = SettingsService()

        self.build_ui()

        self.load_workspace()

    def build_ui(self):

        layout = QVBoxLayout(self)

        title = QLabel("Settings")

        title.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
        """)

        layout.addWidget(title)

        layout.addSpacing(20)

        layout.addWidget(QLabel("Workspace Folder"))

        self.workspace_edit = QLineEdit()

        layout.addWidget(self.workspace_edit)

        buttons = QHBoxLayout()

        browse = QPushButton("Browse")

        save = QPushButton("Save")

        buttons.addWidget(browse)

        buttons.addWidget(save)

        layout.addLayout(buttons)

        layout.addStretch()

        browse.clicked.connect(self.select_folder)

        save.clicked.connect(self.save_workspace)

    def load_workspace(self):

        self.workspace_edit.setText(
            self.service.get_workspace()
        )

    def select_folder(self):

        folder = QFileDialog.getExistingDirectory(self)

        if folder:

            self.workspace_edit.setText(folder)

    def save_workspace(self):

        self.service.set_workspace(
            self.workspace_edit.text()
        )