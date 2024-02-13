from fastapi import FastAPI
from pydantic import BaseModel


class Produto(BaseModel):
    id: int
    nome: str
    preco: float
    em_oferta: bool = False

app = FastAPI()

produtos = [
    Produto(id=1, nome='Play 5', preco=5745.55, em_oferta=True),
    Produto(id=2, nome='Nintendo', preco=2654.12),
    Produto(id=3, nome='X360', preco=1755.34, em_oferta=True),
    Produto(id=4, nome='Super Nintendo', preco=234.67),
    Produto(id=5, nome='Atari 2600', preco=199.90, em_oferta=True)
]

@app.get('/')
async def index():
    return {"Geek": "University"}


@app.get('/produtos/{id}')
async def buscar_produto(id: int):
    for p in produtos:
        if p.id == id:
            return p
    return None


@app.put('/produtos/{id}')
async def atualizar_produto(id: int, produto: Produto):
    for p in produtos:
        if p.id == id:
            p = produto
            return p
    return None