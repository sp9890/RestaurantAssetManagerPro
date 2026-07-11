from pathlib import Path
from PIL import Image


class ImageEngine:

    def convert_to_webp(self, source, destination, quality=85):

        source = Path(source)
        destination = Path(destination)

        destination.parent.mkdir(parents=True, exist_ok=True)

        with Image.open(source) as img:

            img = img.convert("RGB")

            img.save(
                destination,
                "WEBP",
                quality=quality,
                optimize=True
            )

        return destination