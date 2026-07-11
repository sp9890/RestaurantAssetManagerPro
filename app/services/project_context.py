from pathlib import Path
import json


class ProjectContext:

    FILE = Path("app/database/workspace.json")

    @classmethod
    def get_current_project(cls):

        if not cls.FILE.exists():
            return None

        with open(cls.FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        project = data.get("last_project", "")

        if not project:
            return None

        return Path(project)

    @classmethod
    def project_file(cls, filename):

        project = cls.get_current_project()

        if project is None:
            return None

        return project / filename