import json
from pathlib import Path


class SettingsService:

    def __init__(self):

        self.settings_file = Path("app/config/settings.json")

    def load(self):

        if not self.settings_file.exists():

            return {
                "workspace": ""
            }

        with open(self.settings_file, "r", encoding="utf-8") as f:
            return json.load(f)

    def save(self, data):

        with open(self.settings_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def get_workspace(self):

        return self.load()["workspace"]

    def set_workspace(self, folder):

        data = self.load()

        data["workspace"] = folder

        self.save(data)