from pathlib import Path

import cloudinary
import cloudinary.api
import cloudinary.uploader


class CloudinaryService:

    def __init__(self, cloud_name, api_key, api_secret):

        cloudinary.config(
            cloud_name=cloud_name,
            api_key=api_key,
            api_secret=api_secret,
            secure=True,
        )

    # -------------------------
    # Connection
    # -------------------------

    def test_connection(self):

        try:
            cloudinary.api.ping()
            return True, "Connected successfully"

        except Exception as e:
            return False, str(e)

    # -------------------------
    # Upload One Image
    # -------------------------

    def upload_image(
        self,
        image_path,
        folder="restaurant-assets",
    ):

        try:

            image_path = Path(image_path)

            result = cloudinary.uploader.upload(
                str(image_path),
                folder=folder,
                overwrite=True,
                resource_type="image",
            )

            return {
                "success": True,
                "name": image_path.name,
                "local_file": str(image_path),
                "url": result["secure_url"],
                "public_id": result["public_id"],
                "width": result.get("width"),
                "height": result.get("height"),
                "format": result.get("format"),
                "bytes": result.get("bytes"),
            }

        except Exception as e:

            return {
                "success": False,
                "name": Path(image_path).name,
                "local_file": str(image_path),
                "error": str(e),
            }

    # -------------------------
    # Delete Image
    # -------------------------

    def delete_image(self, public_id):

        try:

            result = cloudinary.uploader.destroy(public_id)

            return result.get("result") == "ok"

        except Exception:
            return False

    # -------------------------
    # Upload Multiple Images
    # -------------------------

    def upload_folder(
        self,
        folder,
        extensions=None,
    ):

        if extensions is None:

            extensions = {
                ".jpg",
                ".jpeg",
                ".png",
                ".webp",
                ".bmp",
            }

        folder = Path(folder)

        results = []

        for file in folder.iterdir():

            if not file.is_file():
                continue

            if file.suffix.lower() not in extensions:
                continue

            results.append(
                self.upload_image(file)
            )

        return results