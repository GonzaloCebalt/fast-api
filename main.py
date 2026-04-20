from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

productos = []

class Producto(BaseModel):
    nombre: str
    precio: float
    en_stock: bool

@app.get("/productos")
def read_root():
    return {"productos": productos}

@app.post("/productos")
def agregar_producto(producto: Producto):
    productos.append(producto)
    return {"mensaje": "Producto agregado", "producto": producto}


@app.put("/productos/{id}")
def actualizar_producto(id: int, nombre: str):
    productos[id] = nombre
    return {"mensaje": "Producto actualizado", "producto": nombre}


@app.delete("/productos/{id}")
def eliminar_producto(id: int):
    eliminado = productos.pop(id)
    return {"mensaje": "Producto eliminado", "producto": eliminado}