from dataclasses import dataclass


@dataclass
class MenuItem:

    name: str

    category: str

    price: float

    description: str

    image: str