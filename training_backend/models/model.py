from pydantic import BaseModel
from typing import List, Dict, Optional

class Product(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    tags: List[str] = []
    car: Dict[str, str] = {}