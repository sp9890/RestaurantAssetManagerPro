from dataclasses import dataclass
from pathlib import Path


@dataclass
class AssetModel:

    name: str

    slug: str

    category: str

    original_image: Path

    webp_image: Path | None = None

    thumbnail: Path | None = None

    cloudinary_url: str = ""

    firebase_url: str = ""

    width: int = 0

    height: int = 0

    size: int = 0