import json
from pathlib import Path


class ImageDatabaseService:

    def __init__(self, project_path):

        self.file = Path(project_path) / "images.json"

        if not self.file.exists():

            with open(self.file, "w", encoding="utf-8") as f:
                json.dump([], f)

    def load(self):

        with open(self.file, "r", encoding="utf-8") as f:
            return json.load(f)

    def save(self, data):

        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def add_upload(self, result):

        data = self.load()

        data.append(result)

        self.save(data)