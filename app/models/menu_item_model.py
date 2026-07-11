from dataclasses import dataclass


@dataclass
class MenuItem:

    name: str

    category: str

    price: float

    description: str

    # Local image filename
    image: str

    # Cloudinary image URL
    cloudinary_url: str = ""

    # Cloudinary public id
    public_id: str = ""