from app.services.cloudinary_service import CloudinaryService

service = CloudinaryService(
    cloud_name="diiqbcslw",
    api_key="964382126985779",
    api_secret="IXU5xF0tzMnni5USGWqWOUbd3oE",   # Replace with your actual secret
)

ok, message = service.test_connection()

print(ok)
print(message)