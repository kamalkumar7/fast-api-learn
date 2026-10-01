from pydantic import BaseModel

class MenuItem(BaseModel):
    id: int
    name: str
    description: str
    price: float
    category: str
    available: bool

class  MenuResponse(BaseModel):
    status: str ="success",
    count: int
    menu_items: list[MenuItem]