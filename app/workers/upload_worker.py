from pathlib import Path

from PySide6.QtCore import QObject, Signal

from app.services.cloudinary_service import CloudinaryService


class UploadWorker(QObject):

    progress = Signal(int, int)
    finished = Signal(list)
    error = Signal(str)

    def __init__(self, cloud_name, api_key, api_secret):
        super().__init__()

        self.service = CloudinaryService(
            cloud_name,
            api_key,
            api_secret,
        )

    def upload_folder(self, folder):

        folder = Path(folder)

        if not folder.exists():
            self.error.emit("Folder not found")
            return

        images = []

        for ext in (
            "*.jpg",
            "*.jpeg",
            "*.png",
            "*.webp",
            "*.bmp",
        ):
            images.extend(folder.glob(ext))

        images.sort()

        total = len(images)

        if total == 0:
            self.error.emit("No images found.")
            return

        results = []

        for index, image in enumerate(images, start=1):

            result = self.service.upload_image(image)

            result["name"] = image.name
            result["local_file"] = str(image)

            results.append(result)

            self.progress.emit(index, total)

        self.finished.emit(results)