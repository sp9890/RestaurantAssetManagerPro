from pathlib import Path
import json


class ProjectService:

    def create_project(
        self,
        restaurant_name: str,
        project_location: str,
        menu_folder: str,
        bulk_images_folder: str,
    ):

        print("=" * 50)
        print("ProjectService Started")
        print("Restaurant:", restaurant_name)
        print("Project Location:", project_location)
        print("Menu Folder:", menu_folder)
        print("Bulk Images:", bulk_images_folder)

        project_path = Path(project_location) / restaurant_name

        print("Creating:", project_path)
        print("=" * 50)

        folders = [
            "config",
            "images",
            "banners",
            "exports",
            "backups",
            "temp",
            "logs",
        ]

        # Create project folder
        project_path.mkdir(parents=True, exist_ok=True)

        # Create sub folders
        for folder in folders:
            (project_path / folder).mkdir(exist_ok=True)

        # Restaurant information
        restaurant = {
            "restaurant_name": restaurant_name,
            "project_path": str(project_path),
            "menu_folder": menu_folder,
            "bulk_images_folder": bulk_images_folder,
            "version": "1.0.0",
        }

        cloudinary = {
            "cloud_name": "",
            "api_key": "",
            "api_secret": "",
        }

        firebase = {
            "project_id": "",
            "storage_bucket": "",
        }

        menu = []
        categories = []

        with open(project_path / "restaurant.json", "w", encoding="utf-8") as f:
            json.dump(restaurant, f, indent=4)

        with open(project_path / "cloudinary.json", "w", encoding="utf-8") as f:
            json.dump(cloudinary, f, indent=4)

        with open(project_path / "firebase.json", "w", encoding="utf-8") as f:
            json.dump(firebase, f, indent=4)

        with open(project_path / "menu.json", "w", encoding="utf-8") as f:
            json.dump(menu, f, indent=4)

        with open(project_path / "categories.json", "w", encoding="utf-8") as f:
            json.dump(categories, f, indent=4)

        print("✅ Project Created Successfully!")

        return project_path