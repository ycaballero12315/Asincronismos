from fastapi import APIRouter
from models.model import Product
from sqlmodel import Session, select


router = APIRouter(prefix="/products", tags=["products"])

@router.get("/", summary="Get all products")
async def get_products():
    return {"message": "List of products"}

@router.post("/", summary="Create a new product")
async def create_product(product: dict):
    return {"message": "Product created", "product": product}