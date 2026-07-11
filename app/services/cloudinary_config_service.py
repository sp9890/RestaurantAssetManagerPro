import json
from dataclasses import asdict

from app.models.cloudinary_model import CloudinaryModel
from app.services.project_context import ProjectContext


class CloudinaryConfigService:

    def __init__(self):

        self.file = ProjectContext.project_file(
            "cloudinary.json"
        )

    def save(self, config):

        with open(self.file, "w", encoding="utf-8") as f:

            json.dump(
                asdict(config),
                f,
                indent=4,
            )

    def load(self):

        if self.file is None:
            return None

        if not self.file.exists():
            return None

        with open(self.file, "r", encoding="utf-8") as f:

            data = json.load(f)

        return CloudinaryModel(**data)