from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QProgressBar,
)


class UploadProgressDialog(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Uploading Images")
        self.resize(450, 150)

        layout = QVBoxLayout(self)

        self.title = QLabel("Uploading images to Cloudinary...")

        self.current = QLabel("Waiting...")

        self.progress = QProgressBar()

        self.progress.setMinimum(0)

        self.progress.setValue(0)

        layout.addWidget(self.title)
        layout.addWidget(self.current)
        layout.addWidget(self.progress)

    def update_progress(self, current, total):

        self.progress.setMaximum(total)

        self.progress.setValue(current)

        self.current.setText(
            f"{current} / {total} Images Uploaded"
        )