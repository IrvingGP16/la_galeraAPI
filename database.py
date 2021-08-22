from peewee import *


"--------------------aqui se crea la conexión a la base de datos------------------------"
database = MySQLDatabase(
    'la_galera',
    user='root',
    password='rootpass',
    host='localhost', port=3306
)

"--------------Aqui se crean los modelos de las tablas--------------------"
class Product(Model):
    nombre = CharField(max_length=50)
    variante = CharField(max_length=50)
    presentacion = CharField(max_length=50)
    marca = CharField(max_length=50)
    cont_neto = CharField(max_length=50)
    image = CharField(max_length=100)
    price = IntegerField(0)

    def __str__(self):
        return self.nombre
    
    class Meta:
        database = database
        table_name = 'products'

class Precio(Model):
    consumidor = FloatField = None
    comicionista = FloatField = None
    distribuidor = FloatField = None

    def __str__(self):
        return self.consumidor
    
    class Meta:
        database = database
        table_name = 'precios'