from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

pettite_db = [{'ciudad': 'Montevideo'},{'work': "el suenno"},{'Salary': 2500}]
class User(BaseModel):
    name: str
    lastname: str
    solapin: int

class ModelName(str, Enum):
    alex = 'Alex'
    pedro = 'Pedro'
    victor = 'Victor'

class Response(BaseModel):
    resp: str

@app.post('/create_user/')
async def create_user(user: User):
    return f"Hola: soy {user.name} con solapin-> {user.solapin}" 

@app.get('/print/')
async def resp(resp: Response):
    return f'Hola a todos imprime {resp.resp}'

@app.get('/test/{items}')
async def resp(items: float):
    return f'Los elementos son los siguientes: {items}'

@app.get('/models/{models_name}')
async def resp_model_name(model_name: ModelName):
    if model_name in ModelName.alex:
        return f"El muchacho es: {model_name}"
    if model_name.value == 'Pedro':
        return f"Hola a todos soy{model_name.value}"
    else:
        return 'No se encuentra el muchacho'

@app.get('/item/')
async def mostrar(key: int = 0, limit: int = 10):
    total = len(pettite_db)
    end = min(key + limit, total)
    resultado = pettite_db[key:end]

    next_key = end if end < total else None

    return {
        "total": total,
        "items": resultado,
        "start": key,
        "end": end - 1,
        "next_key": next_key
    }

@app.get('elem2')
async def mostrar2(uno: Optional[int] = 0):
    return {'uno': uno}