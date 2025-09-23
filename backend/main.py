from fastapi import FastAPI, Query, Path, Body, Cookie
from enum import Enum
from pydantic import BaseModel, AfterValidator, Field, HttpUrl
from typing import Annotated, List, Set
import random
from datetime import datetime, time, timedelta
from uuid import UUID

class Image(BaseModel):
    url: HttpUrl
    name: str

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float 
    tax: float | None = None
    tags: Set[float]
    image: Image

class User(BaseModel):
    user_name : str
    full_name : str
    cedula: str = Field(default=None, description='Format cedula with Uruguay', min_length=6, max_digits=10)

class ShopingCar(BaseModel):
    user: User
    pending: bool = Field(default=False, description="Pedido pendiente de aceptar")
    images: List[Image]
    items: List[Item]


class ModelName(str, Enum):
    yoe = "Yoeny",
    duni = "Dunia",
    sifi = "Sofia",
    samu = "Samuel"


app = FastAPI()

@app.get('/item/elem')
def init(elem: int):
    if elem:
        return {'msg': f'elemento es: {elem **2}'}
    else:
        return {'msg':'emty'}

@app.get('/item/{elem}')
def init_me(elem):
    return {'elem': elem}

@app.get('/model/{model_name}')
def model(model_name: ModelName):
    json = {}
    if model_name is ModelName.yoe:
        json = {'in model': 1, "es": f"{model_name.value}"}
    elif model_name is ModelName.duni:
        json = {'in model': 1, "es": f"{model_name.value}"}
    elif model_name is ModelName.sifi:
        json = {'in model': 1, "es": f"{model_name.value}"}
    elif model_name is ModelName.samu:
        json = {'in model': 1, "es": f"{model_name.value}"}
    return json

@app.get('/path/{file_path: path}')
async def path(file_path: str):
    return {'direct': file_path}

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get('/query')
async def get_query(start: int = 0, stop: int = 10):
    return fake_items_db[start: stop]

@app.get('/items/{user_id}')
async def users(user_id: int, name: str | None = None):
    if name:
        return {'user_id': user_id, 'name': name}
    return {'user_id': user_id}

@app.get('/user/{item_id}')
async def user_items(item_id, needy: str, skip: int = 0, limit: int | None = None):
    user = {'item_id': item_id, 'needy': needy, 'skip': skip, 'limit': limit }
    return user

@app.get("/items")
async def cooki_ads(ads_ad: Annotated[str | None, Cookie()]= None):
    return {'ads_ad': ads_ad}

@app.post('/items/{user_id}')
async def input_item(item:Item, user_id: Annotated[int, Path(
                        title="User ID",
                        description="The unique identifier of the user",
                        ge=1,
                        le=99,
                        example=123
                        )],
                        q:bool | None = None,
                        pluss_description: Annotated[str | None,
                                                    Query(max_length=20, min_length=2)] = None):
    user_id = user_id
    item_dict = item.model_dump()
    if item.tax:
        price_with_tax = item.tax + item.price
        item_dict.update({'price_with_tax': price_with_tax})
    if q and pluss_description:
        item_dict.update({'user_id': user_id, **item_dict, 'q': q, 'more_description':pluss_description})
    else:
        item_dict.update({'user_id': user_id, **item_dict})
    return item_dict

@app.post('/items')
async def multiple_items(q:Annotated[List[str], Query()] = ['food', 'Bar', 'home']):
    if q:
        return {'q': q}
    return {}

data = {
    "isbn-9781529046137": "The Hitchhiker's Guide to the Galaxy",
    "imdb-tt0371724": "The Hitchhiker's Guide to the Galaxy",
    "isbn-9781439512982": "Isaac Asimov: The Complete Stories, Vol. 2",
}

def check_id(id:str):
    if not id.startswith('isbn-', 'imdb-'):
        raise ValueError('Invalid ID format, it must start with "isbn-" or "imdb-"')
    return id

@app.post('/items_id')
async def book_read(id: Annotated[str | None, AfterValidator(check_id)] = None):
    if id:
        item = data.get(id)
    else:
       id, item = random.choice(list(data.items()))
    return id, item

@app.post('/users/{user_id}')
async def user_item(id_user: int, item:Item, 
                    user:User, description:Annotated[str, Body()], shoping:ShopingCar):
    user_shop = {"id_user":id_user, 'item':shoping, "user": user, 'descriptions': description}
    return user_shop

@app.put("/items/{item_id}")
async def read_items(
    item_id: UUID,
    start_datetime: Annotated[datetime, Body()],
    end_datetime: Annotated[datetime, Body()],
    process_after: Annotated[timedelta, Body()],
    repeat_at: Annotated[time | None, Body()] = None,
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "process_after": process_after,
        "repeat_at": repeat_at,
        "start_process": start_process,
        "duration": duration,
    }