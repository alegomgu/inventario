from sqlalchemy import Column, Integer, String, ForeignKey, Date, Numeric
from sqlalchemy.orm import sessionmaker, relationship
from .database import Base

# Definición de los modelos
class Ubicacion(Base):
    __tablename__ = 'ubicaciones'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)

class Categoria(Base):
    __tablename__ = 'categorias'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)

class Bebida(Base):
    __tablename__ = 'bebidas'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)

class Inventario(Base):
    __tablename__ = 'inventario'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    cantidad = Column(Integer)
    unidad_medida = Column(String(50))
    fecha_caducidad = Column(Date)
    fecha_compra = Column(Date)
    ubicacion_id = Column(Integer, ForeignKey('ubicaciones.id'))
    categoria_id = Column(Integer, ForeignKey('categorias.id'))
    bebida_id = Column(Integer, ForeignKey('bebidas.id'), nullable=True)
    observaciones = Column(String(255))
    precio = Column(Numeric(10, 2))
    proveedor = Column(String(100))

    ubicacion = relationship("Ubicacion")
    categoria = relationship("Categoria")
    bebida = relationship("Bebida")
