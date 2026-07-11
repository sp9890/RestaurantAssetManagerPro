import json
from pathlib import Path


class WorkspaceService:

    def __init__(self):
        self.workspace_file = Path("app/database/workspace.json")

    def load_workspace(self):

        if not self.workspace_file.exists():
            return {
                "projects": [],
                "last_project": ""
            }

        with open(self.workspace_file, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_workspace(self, data):

        with open(self.workspace_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def add_project(self, project_path):

        data = self.load_workspace()

        project = {
            "name": Path(project_path).name,
            "path": str(project_path),
        }

        exists = any(
            p["path"] == str(project_path)
            for p in data["projects"]
        )

        if not exists:
            data["projects"].append(project)

        data["last_project"] = str(project_path)

        self.save_workspace(data)

    def get_projects(self):

        return self.load_workspace()["projects"]

    def get_last_project(self):

        return self.load_workspace()["last_project"]