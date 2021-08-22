from schemas import PrecioRequestModel, ProductRequestModel
from fastapi import FastAPI
from database import database as conexion
from database import Product
from database import Precio
"------crear application----------"
app = FastAPI(title='APILaGalera',
            description='Esta es la API de la galera')

"-----Aquí se abre la conexión a la base de datos----------"
@app.on_event('startup')
async def startup():
    if conexion.is_closed():
        conexion.connect()
    conexion.create_tables([Product,Precio])

@app.on_event('shutdown')
async def shutdown():
    if not conexion.is_closed():
        conexion.close()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post('/products')
async def create_product(product_request: ProductRequestModel):
    User = Product.create(
        nombre=product_request.nombre,
        variante=product_request.variante,
        presentacion=product_request.presentacion,
        marca=product_request.marca,
        cont_neto=product_request.cont_neto,
        image=product_request.image,
        price=product_request.cont_neto
    )
    return product_request

@app.post('/precios')
async def create_precio(precio_request: PrecioRequestModel):
    user = Precio.create(
        consumidor=precio_request.consumidor,
        comicionista=precio_request.comicionista,
        distribuidor=precio_request.distribuidor
    )
    return precio_request