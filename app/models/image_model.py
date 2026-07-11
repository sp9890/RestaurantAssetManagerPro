from dataclasses import dataclass
from pathlib import Path

@dataclass
class ImageModel:

    name: str

    path: Path

    width: int

    height: int

    size: int

    extension: str