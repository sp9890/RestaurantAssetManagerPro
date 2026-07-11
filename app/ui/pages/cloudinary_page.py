from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTextEdit,
    QMessageBox,
    QFileDialog,
)

from PySide6.QtCore import QThread

from app.services.cloudinary_service import CloudinaryService
from app.services.cloudinary_config_service import CloudinaryConfigService
from app.services.project_context import ProjectContext
from app.services.image_database_service import ImageDatabaseService

from app.models.cloudinary_model import CloudinaryModel

from app.workers.upload_worker import UploadWorker

from app.ui.dialogs.upload_progress_dialog import UploadProgressDialog


class CloudinaryPage(QWidget):

    def __init__(self):
        super().__init__()

        self.config_service = CloudinaryConfigService()

        self.thread = None
        self.worker = None
        self.progress_dialog = None

        self.build_ui()
        self.load_settings()

    def build_ui(self):

        layout = QVBoxLayout(self)

        title = QLabel("☁ Cloudinary")
        title.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
        """)
        layout.addWidget(title)

        layout.addWidget(QLabel("Cloud Name"))
        self.cloud_name = QLineEdit()
        layout.addWidget(self.cloud_name)

        layout.addWidget(QLabel("API Key"))
        self.api_key = QLineEdit()
        layout.addWidget(self.api_key)

        layout.addWidget(QLabel("API Secret"))
        self.api_secret = QLineEdit()
        self.api_secret.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.api_secret)

        buttons = QHBoxLayout()

        self.test_btn = QPushButton("🔗 Test Connection")
        self.save_btn = QPushButton("💾 Save")
        self.upload_btn = QPushButton("☁ Upload Folder")

        buttons.addWidget(self.test_btn)
        buttons.addWidget(self.save_btn)
        buttons.addWidget(self.upload_btn)

        layout.addLayout(buttons)

        self.log = QTextEdit()
        self.log.setReadOnly(True)

        layout.addWidget(self.log)

        self.test_btn.clicked.connect(self.test_connection)
        self.save_btn.clicked.connect(self.save_settings)
        self.upload_btn.clicked.connect(self.upload_folder)

    # -----------------------------------------------------

    def test_connection(self):

        service = CloudinaryService(
            self.cloud_name.text(),
            self.api_key.text(),
            self.api_secret.text(),
        )

        ok, message = service.test_connection()

        if ok:

            self.log.append("✅ Connected Successfully")

            QMessageBox.information(
                self,
                "Cloudinary",
                "Connection Successful",
            )

        else:

            self.log.append(message)

            QMessageBox.warning(
                self,
                "Cloudinary",
                message,
            )

    # -----------------------------------------------------

    def save_settings(self):

        config = CloudinaryModel(
            cloud_name=self.cloud_name.text(),
            api_key=self.api_key.text(),
            api_secret=self.api_secret.text(),
        )

        self.config_service.save(config)

        QMessageBox.information(
            self,
            "Saved",
            "Cloudinary settings saved.",
        )

    # -----------------------------------------------------

    def load_settings(self):

        config = self.config_service.load()

        if config is None:
            return

        self.cloud_name.setText(config.cloud_name)
        self.api_key.setText(config.api_key)
        self.api_secret.setText(config.api_secret)

    # -----------------------------------------------------

    def upload_folder(self):

        folder = QFileDialog.getExistingDirectory(
            self,
            "Select Images Folder",
        )

        if not folder:
            return

        self.progress_dialog = UploadProgressDialog()
        self.progress_dialog.show()

        self.thread = QThread()

        self.worker = UploadWorker(
            self.cloud_name.text(),
            self.api_key.text(),
            self.api_secret.text(),
        )

        self.worker.moveToThread(self.thread)

        self.thread.started.connect(
            lambda: self.worker.upload_folder(folder)
        )

        self.worker.progress.connect(
            self.progress_dialog.update_progress
        )

        self.worker.finished.connect(
            self.upload_finished
        )

        self.worker.error.connect(
            self.upload_error
        )

        self.worker.finished.connect(
            self.thread.quit
        )

        self.thread.finished.connect(
            self.thread.deleteLater
        )

        self.thread.start()

    # -----------------------------------------------------

    def upload_error(self, message):

        if self.progress_dialog:
            self.progress_dialog.close()

        QMessageBox.warning(
            self,
            "Upload Error",
            message,
        )

        self.log.append(message)

    # -----------------------------------------------------

    def upload_finished(self, results):

        if self.progress_dialog:
            self.progress_dialog.finish()

        project = ProjectContext.get_current_project()

        print("=" * 60)
        print("Current Project :", project)
        print("Exists :", project.exists() if project else None)
        print("=" * 60)

        db = ImageDatabaseService(project)

        print("Images JSON :", db.file)

        success = 0

        for result in results:

            print(result)

            if result.get("success"):

                db.add_upload({
                    "name": result["name"],
                    "local_file": result["local_file"],
                    "cloudinary_url": result["url"],
                    "public_id": result["public_id"],
                })

                success += 1

            else:

                self.log.append(
                    f"❌ {result.get('name','')} : {result.get('error','Unknown Error')}"
                )

        QMessageBox.information(
            self,
            "Upload Complete",
            f"{success} images uploaded successfully.",
        )

        self.log.append(
            f"Uploaded {success} images."
        )