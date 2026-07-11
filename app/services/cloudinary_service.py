import cloudinary
import cloudinary.uploader
import cloudinary.api


class CloudinaryService:

    def __init__(self, cloud_name, api_key, api_secret):

        cloudinary.config(
            cloud_name=cloud_name,
            api_key=api_key,
            api_secret=api_secret,
            secure=True,
        )

    def test_connection(self):

        try:
            cloudinary.api.ping()
            return True, "Connected successfully"

        except Exception as e:
            return False, str(e)

    def upload_image(self, image_path, folder="restaurant-assets"):

        try:

            result = cloudinary.uploader.upload(
                image_path,
                folder=folder,
                overwrite=True,
                resource_type="image",
            )

            return {
                "success": True,
                "url": result["secure_url"],
                "public_id": result["public_id"],
            }

        except Exception as e:

            return {
                "success": False,
                "error": str(e),
            }

    def delete_image(self, public_id):

        try:

            cloudinary.uploader.destroy(public_id)

            return True

        except Exception:

            return False