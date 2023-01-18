from pydantic import BaseModel


class Menu(BaseModel):  # menu serializer
    id: int
    name: str
    description: str
    price: float

