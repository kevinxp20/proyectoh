# Guía de Conversión de .NET a Python

## ¿Cómo proporcionar archivos que no están en el repositorio?

Si tienes archivos .NET que necesitas convertir a Python pero no están en el repositorio de GitHub, tienes varias opciones:

### Opción 1: Agregar los archivos al repositorio

La forma más directa es agregar tus archivos .NET al repositorio:

```bash
# Copia tus archivos al repositorio
cp /ruta/a/tu/archivo.cs /ruta/del/repositorio/

# Agrega los archivos a Git
git add archivo.cs

# Crea un commit
git commit -m "Agregar archivo .NET para conversión"

# Sube los cambios
git push
```

### Opción 2: Crear un Issue con el código

Si no quieres agregar archivos .NET al repositorio permanentemente:

1. Ve a la pestaña "Issues" en GitHub
2. Crea un nuevo issue
3. Pega el código .NET en un bloque de código markdown:

```csharp
// Tu código .NET aquí
```

4. Describe qué necesitas convertir

### Opción 3: Usar Gist de GitHub

1. Ve a https://gist.github.com/
2. Crea un nuevo Gist con tu código .NET
3. Comparte el enlace del Gist en el issue o pull request

### Opción 4: Pegar el código directamente

Si el archivo es pequeño, puedes pegar el código directamente en:
- Un comentario de issue
- Un comentario de pull request
- Una descripción de commit

## Proceso de Conversión de .NET a Python

### 1. Análisis del código .NET

Identifica los elementos clave en tu código .NET:
- Clases y estructuras
- Métodos y propiedades
- Tipos de datos
- Namespaces y using statements
- Manejo de excepciones

### 2. Equivalencias comunes

| .NET (C#) | Python |
|-----------|--------|
| `int`, `long` | `int` |
| `float`, `double`, `decimal` | `float` |
| `string` | `str` |
| `bool` | `bool` |
| `List<T>` | `list` |
| `Dictionary<K,V>` | `dict` |
| `null` | `None` |
| `namespace` | módulo/paquete |
| `class` | `class` |
| `interface` | clase base abstracta |

### 3. Patrones de conversión

#### Clases y constructores

**.NET:**
```csharp
public class Usuario
{
    public string Nombre { get; set; }
    public int Edad { get; set; }
    
    public Usuario(string nombre, int edad)
    {
        Nombre = nombre;
        Edad = edad;
    }
}
```

**Python:**
```python
class Usuario:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad
```

#### Métodos

**.NET:**
```csharp
public string ObtenerDescripcion()
{
    return $"{Nombre} tiene {Edad} años";
}
```

**Python:**
```python
def obtener_descripcion(self) -> str:
    return f"{self.nombre} tiene {self.edad} años"
```

#### Propiedades

**.NET:**
```csharp
private string _nombre;
public string Nombre 
{ 
    get { return _nombre; }
    set { _nombre = value; }
}
```

**Python:**
```python
@property
def nombre(self) -> str:
    return self._nombre

@nombre.setter
def nombre(self, value: str):
    self._nombre = value
```

#### Manejo de excepciones

**.NET:**
```csharp
try
{
    // código
}
catch (Exception ex)
{
    Console.WriteLine(ex.Message);
}
finally
{
    // limpieza
}
```

**Python:**
```python
try:
    # código
except Exception as ex:
    print(str(ex))
finally:
    # limpieza
```

#### LINQ a comprensiones de lista

**.NET:**
```csharp
var numeros = new List<int> { 1, 2, 3, 4, 5 };
var pares = numeros.Where(n => n % 2 == 0).ToList();
```

**Python:**
```python
numeros = [1, 2, 3, 4, 5]
pares = [n for n in numeros if n % 2 == 0]
```

### 4. Consideraciones especiales

#### Tipos estáticos vs dinámicos

.NET es fuertemente tipado, mientras que Python es dinámicamente tipado. Usa type hints en Python para mantener claridad:

```python
from typing import List, Dict, Optional

def procesar_datos(items: List[str]) -> Dict[str, int]:
    return {item: len(item) for item in items}
```

#### Async/Await

Ambos lenguajes soportan programación asíncrona:

**.NET:**
```csharp
public async Task<string> ObtenerDatosAsync()
{
    await Task.Delay(1000);
    return "datos";
}
```

**Python:**
```python
async def obtener_datos_async() -> str:
    await asyncio.sleep(1)
    return "datos"
```

## Herramientas útiles

### Script de conversión

El repositorio incluye `dotnet_to_python_converter.py` que puede ayudarte con conversiones básicas:

```bash
python dotnet_to_python_converter.py archivo.cs
```

### Librerías de Python para reemplazar .NET

- **ASP.NET → Flask/Django/FastAPI**: Frameworks web
- **Entity Framework → SQLAlchemy**: ORM
- **Newtonsoft.Json → json**: Manipulación JSON
- **HttpClient → requests/httpx**: Cliente HTTP
- **Serilog → logging**: Logging
- **xUnit/NUnit → pytest**: Testing

## Ejemplos prácticos

### Ejemplo 1: Clase de modelo de datos

**.NET:**
```csharp
using System;

namespace MiApp.Models
{
    public class Producto
    {
        public int Id { get; set; }
        public string Nombre { get; set; }
        public decimal Precio { get; set; }
        
        public string ObtenerEtiqueta()
        {
            return $"{Nombre} - ${Precio:F2}";
        }
    }
}
```

**Python:**
```python
from dataclasses import dataclass
from decimal import Decimal

@dataclass
class Producto:
    id: int
    nombre: str
    precio: Decimal
    
    def obtener_etiqueta(self) -> str:
        return f"{self.nombre} - ${self.precio:.2f}"
```

### Ejemplo 2: Controlador API

**.NET:**
```csharp
[ApiController]
[Route("api/[controller]")]
public class ProductosController : ControllerBase
{
    [HttpGet]
    public IActionResult GetAll()
    {
        var productos = _service.ObtenerTodos();
        return Ok(productos);
    }
}
```

**Python (FastAPI):**
```python
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/api/productos")

@router.get("/")
async def get_all():
    productos = service.obtener_todos()
    return productos
```

## Recursos adicionales

- [Python Official Documentation](https://docs.python.org/3/)
- [C# to Python Quick Reference](https://www.pythonsheets.com/)
- [Type Hints in Python](https://docs.python.org/3/library/typing.html)

## Preguntas frecuentes

**P: ¿Puedo convertir automáticamente todo mi proyecto .NET?**
R: No existe una conversión automática perfecta. Necesitarás revisar y adaptar el código manualmente.

**P: ¿Qué hago con las dependencias de NuGet?**
R: Busca paquetes equivalentes en PyPI (pip) o implementa la funcionalidad necesaria.

**P: ¿Cómo manejo las diferencias de rendimiento?**
R: Python es generalmente más lento que .NET. Usa PyPy para mejor rendimiento o considera Cython para código crítico.

## Contacto y soporte

Si necesitas ayuda con la conversión:
1. Crea un issue en este repositorio
2. Incluye el código .NET que necesitas convertir
3. Describe el contexto y propósito del código
4. Menciona cualquier requisito especial
