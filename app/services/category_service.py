import json
from pathlib import Path
from dataclasses import asdict

from app.models.category_model import Category


class CategoryService:

    def __init__(self):

        self.file = Path("app/database/categories.json")

        if not self.file.exists():
            self.file.parent.mkdir(parents=True, exist_ok=True)

            with open(self.file, "w") as f:
                json.dump([], f)

    def get_categories(self):

        with open(self.file, "r") as f:

            data = json.load(f)

        return [Category(**x) for x in data]

    def add_category(self, name):

        categories = self.get_categories()

        categories.append(Category(name))

        with open(self.file, "w") as f:

            json.dump(
                [asdict(c) for c in categories],
                f,
                indent=4,
            )