from enum import Enum
from pydantic import BaseModel

"-----------------Aqui definimos el tipo de datos que podemo enviar al servidor-----------------"
class ProductRequestModel(BaseModel):
    nombre: str
    variante: str
    presentacion: str
    marca: str
    cont_neto: str
    image: str
    price: int

class PrecioRequestModel(BaseModel):
    consumidor: float = None
    comicionista: float = None
    distribuidor: float = None