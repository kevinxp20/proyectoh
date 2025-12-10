"""
Ejemplo de conversión de .NET a Python

Este archivo muestra la conversión del ejemplo.cs a Python,
con las mejores prácticas de Python aplicadas.
"""

from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional


# Clase de modelo de datos
@dataclass
class Producto:
    """Modelo de datos para un producto"""
    id: int
    nombre: str
    precio: Decimal
    disponible: bool = True
    categorias: List[str] = field(default_factory=list)
    
    def obtener_etiqueta(self) -> str:
        """Devuelve una etiqueta formateada del producto"""
        return f"{self.nombre} - ${self.precio:.2f}"
    
    def esta_en_categoria(self, categoria: str) -> bool:
        """Verifica si el producto está en una categoría específica"""
        return categoria in self.categorias


# Servicio de negocio
class ProductoService:
    """Servicio para gestionar productos"""
    
    def __init__(self):
        self._productos: List[Producto] = []
    
    def agregar_producto(self, producto: Producto) -> None:
        """Agrega un producto a la lista"""
        if producto is None:
            raise ValueError("El producto no puede ser None")
        self._productos.append(producto)
    
    def obtener_todos(self) -> List[Producto]:
        """Devuelve todos los productos"""
        return self._productos.copy()
    
    def obtener_disponibles(self) -> List[Producto]:
        """Devuelve solo los productos disponibles"""
        return [p for p in self._productos if p.disponible]
    
    def buscar_por_categoria(self, categoria: str) -> List[Producto]:
        """Busca productos por categoría y los ordena por nombre"""
        productos_filtrados = [
            p for p in self._productos 
            if p.esta_en_categoria(categoria)
        ]
        return sorted(productos_filtrados, key=lambda p: p.nombre)
    
    def calcular_total(self) -> Decimal:
        """Calcula el precio total de todos los productos"""
        return sum((p.precio for p in self._productos), Decimal('0'))


# Clase de utilidades
class Utilidades:
    """Funciones de utilidad para productos"""
    
    @staticmethod
    def formatear_precio(precio: Decimal) -> str:
        """Formatea un precio como string con formato de moneda"""
        return f"${precio:.2f}"
    
    @staticmethod
    def validar_nombre(nombre: str) -> bool:
        """Valida que un nombre sea válido (no vacío y al menos 3 caracteres)"""
        return nombre is not None and len(nombre.strip()) >= 3


# Ejemplo de uso
if __name__ == "__main__":
    # Crear servicio
    servicio = ProductoService()
    
    # Crear productos
    producto1 = Producto(
        id=1,
        nombre="Laptop",
        precio=Decimal("999.99"),
        disponible=True,
        categorias=["electrónica", "computadoras"]
    )
    
    producto2 = Producto(
        id=2,
        nombre="Mouse",
        precio=Decimal("25.50"),
        disponible=True,
        categorias=["electrónica", "accesorios"]
    )
    
    producto3 = Producto(
        id=3,
        nombre="Teclado",
        precio=Decimal("75.00"),
        disponible=False,
        categorias=["electrónica", "accesorios"]
    )
    
    # Agregar productos
    servicio.agregar_producto(producto1)
    servicio.agregar_producto(producto2)
    servicio.agregar_producto(producto3)
    
    # Consultas
    print("=== Todos los productos ===")
    for p in servicio.obtener_todos():
        print(f"- {p.obtener_etiqueta()} (Disponible: {p.disponible})")
    
    print("\n=== Productos disponibles ===")
    for p in servicio.obtener_disponibles():
        print(f"- {p.obtener_etiqueta()}")
    
    print("\n=== Productos en categoría 'accesorios' ===")
    for p in servicio.buscar_por_categoria("accesorios"):
        print(f"- {p.obtener_etiqueta()}")
    
    print(f"\n=== Total de precios ===")
    total = servicio.calcular_total()
    print(Utilidades.formatear_precio(total))
    
    print("\n=== Validación de nombres ===")
    print(f"'Laptop' es válido: {Utilidades.validar_nombre('Laptop')}")
    print(f"'AB' es válido: {Utilidades.validar_nombre('AB')}")
    print(f"'' es válido: {Utilidades.validar_nombre('')}")
