from pathlib import Path

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QFileDialog,
    QVBoxLayout,
    QScrollArea,
)

from app.services.image_service import ImageService
from app.core.image_engine import ImageEngine
from app.ui.widgets.image_gallery import ImageGallery


class ImagesPage(QWidget):

    def __init__(self):
        super().__init__()

        self.image_service = ImageService()
        self.image_engine = ImageEngine()

        self.images = []

        self.build_ui()

    def build_ui(self):

        layout = QVBoxLayout(self)

        # ---------------- Title ----------------

        title = QLabel("Images")
        title.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
        """)

        layout.addWidget(title)

        # ---------------- Buttons ----------------

        self.import_btn = QPushButton("📂 Import Folder")
        self.convert_btn = QPushButton("⚡ Convert to WebP")

        layout.addWidget(self.import_btn)
        layout.addWidget(self.convert_btn)

        # ---------------- Gallery ----------------

        self.gallery = ImageGallery()

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setWidget(self.gallery)

        layout.addWidget(scroll)

        # ---------------- Signals ----------------

        self.import_btn.clicked.connect(self.import_folder)
        self.convert_btn.clicked.connect(self.convert_images)

    def import_folder(self):

        folder = QFileDialog.getExistingDirectory(self)

        if not folder:
            return

        self.images = self.image_service.scan_folder(folder)

        self.image_service.save_last_images(self.images)

        self.gallery.load_images(self.images)

    def convert_images(self):

        if not self.images:
            print("No images loaded.")
            return

        output_folder = Path("outputs")
        output_folder.mkdir(exist_ok=True)

        for image in self.images:

            destination = output_folder / f"{image.name}.webp"

            self.image_engine.convert_to_webp(
                image.path,
                destination
            )

        print("✅ All images converted successfully!")