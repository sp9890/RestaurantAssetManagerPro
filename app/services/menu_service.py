import json
from dataclasses import asdict

from app.models.menu_item_model import MenuItem
from app.services.project_context import ProjectContext


class MenuService:

    def __init__(self):

        self.menu_file = ProjectContext.project_file("menu.json")

    def get_menu(self):

        if self.menu_file is None:
            return []

        if not self.menu_file.exists():

            with open(self.menu_file, "w", encoding="utf-8") as f:
                json.dump([], f, indent=4)

        with open(self.menu_file, "r", encoding="utf-8") as f:

            data = json.load(f)

        return [MenuItem(**item) for item in data]

    def save_menu(self, menu):

        if self.menu_file is None:
            return

        with open(self.menu_file, "w", encoding="utf-8") as f:

            json.dump(
                [asdict(item) for item in menu],
                f,
                indent=4,
            )

    def add_item(self, item):

        menu = self.get_menu()

        menu.append(item)

        self.save_menu(menu)

    def delete_item(self, index):

        menu = self.get_menu()

        if 0 <= index < len(menu):

            menu.pop(index)

            self.save_menu(menu)