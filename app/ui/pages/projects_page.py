from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QListWidget,
)

from app.ui.dialogs.new_project_dialog import NewProjectDialog
from app.services.project_service import ProjectService
from app.services.workspace_service import WorkspaceService


class ProjectsPage(QWidget):

    def __init__(self):
        super().__init__()

        self.build_ui()
        self.load_projects()

        self.new_btn.clicked.connect(self.new_project)

    def new_project(self):

        dialog = NewProjectDialog()

        if dialog.exec():

            service = ProjectService()

            project = service.create_project(
                restaurant_name=dialog.name_edit.text(),
                project_location=dialog.location_edit.text(),
                menu_folder=dialog.menu_edit.text(),
                bulk_images_folder=dialog.bulk_edit.text(),
            )

            workspace = WorkspaceService()
            workspace.add_project(project)

            self.load_projects()

    def load_projects(self):

        self.project_list.clear()

        workspace = WorkspaceService()

        projects = workspace.get_projects()

        for project in projects:

            self.project_list.addItem(
                f"🏪 {project['name']}\n📂 {project['path']}"
            )

    def build_ui(self):

        layout = QVBoxLayout(self)

        title = QLabel("Projects")
        title.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
        """)

        layout.addWidget(title)

        btn_layout = QHBoxLayout()

        self.new_btn = QPushButton("➕ New Project")
        self.open_btn = QPushButton("📂 Open")
        self.delete_btn = QPushButton("🗑 Delete")

        btn_layout.addWidget(self.new_btn)
        btn_layout.addWidget(self.open_btn)
        btn_layout.addWidget(self.delete_btn)
        btn_layout.addStretch()

        layout.addLayout(btn_layout)

        self.project_list = QListWidget()

        layout.addWidget(self.project_list)