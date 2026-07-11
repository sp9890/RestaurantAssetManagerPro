from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
)


class ImageCard(QFrame):

    def __init__(self, image):
        super().__init__()

        self.image = image

        self.build_ui()

    def build_ui(self):

        self.setFixedSize(220, 300)

        self.setStyleSheet("""
        QFrame{
            background:white;
            border:1px solid #DDDDDD;
            border-radius:10px;
        }

        QLabel{
            border:none;
        }
        """)

        layout = QVBoxLayout(self)

        # Thumbnail
        thumbnail = QLabel()
        thumbnail.setAlignment(Qt.AlignCenter)

        pixmap = QPixmap(str(self.image.path))

        if not pixmap.isNull():

            pixmap = pixmap.scaled(
                180,
                180,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation,
            )

            thumbnail.setPixmap(pixmap)

        layout.addWidget(thumbnail)

        # Name
        name = QLabel(self.image.name)
        name.setAlignment(Qt.AlignCenter)
        name.setStyleSheet("font-weight:bold;font-size:14px;")
        layout.addWidget(name)

        # Resolution
        layout.addWidget(
            QLabel(
                f"📐 {self.image.width} × {self.image.height}"
            )
        )

        # Size
        kb = round(self.image.size / 1024, 1)

        layout.addWidget(
            QLabel(
                f"💾 {kb} KB"
            )
        )

        # Extension
        layout.addWidget(
            QLabel(
                f"📄 {self.image.extension.upper()}"
            )
        )

        layout.addStretch()