import json
from pathlib import Path
from PIL import Image

from app.models.image_model import ImageModel


class ImageService:

    IMAGE_EXTENSIONS = [
        ".jpg",
        ".jpeg",
        ".png",
        ".webp",
        ".bmp",
        ".gif",
        ".tiff",
        ".heic",
    ]

    def scan_folder(self, folder):

        folder = Path(folder)

        if not folder.exists():
            return []

        images = []

        for file in folder.iterdir():

            if not file.is_file():
                continue

            if file.suffix.lower() not in self.IMAGE_EXTENSIONS:
                continue

            try:

                with Image.open(file) as img:
                    width, height = img.size

                image = ImageModel(
                    name=file.stem,
                    path=file,
                    width=width,
                    height=height,
                    size=file.stat().st_size,
                    extension=file.suffix.lower(),
                )

                images.append(image)

            except Exception as e:
                print(f"Error reading {file.name}: {e}")

        return images

    def save_last_images(self, images):

        data = []

        for image in images:

            data.append({
                "name": image.name,
                "path": str(image.path),
            })

        Path("app/database").mkdir(parents=True, exist_ok=True)

        with open(
            "app/database/images.json",
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(data, f, indent=4)

    def get_last_images(self):

        file = Path("app/database/images.json")

        if not file.exists():
            return []

        with open(file, "r", encoding="utf-8") as f:

            return json.load(f)