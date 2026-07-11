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
        self.resize(500, 170)

        layout = QVBoxLayout(self)

        self.title = QLabel("☁ Uploading Images to Cloudinary")
        self.title.setStyleSheet("""
            font-size:18px;
            font-weight:bold;
        """)

        self.current = QLabel("Preparing...")

        self.progress = QProgressBar()
        self.progress.setMinimum(0)
        self.progress.setValue(0)

        self.status = QLabel("")

        layout.addWidget(self.title)
        layout.addWidget(self.current)
        layout.addWidget(self.progress)
        layout.addWidget(self.status)

    def update_progress(self, current, total):

        self.progress.setMaximum(total)
        self.progress.setValue(current)

        self.current.setText(
            f"Uploading {current} of {total}"
        )

    def set_status(self, text):

        self.status.setText(text)

    def finish(self):

        self.progress.setValue(
            self.progress.maximum()
        )

        self.current.setText("Upload Complete ✅")

        self.status.setText(
            "All images uploaded successfully."
        )

    def reset(self):

        self.progress.setValue(0)

        self.current.setText("Preparing...")

        self.status.clear()