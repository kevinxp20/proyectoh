# Proyecto H - Conversión de .NET a Python

Este repositorio contiene herramientas y documentación para ayudar en la conversión de código .NET/C# a Python.

## 📋 Contenido

- **CONVERSION_GUIDE.md**: Guía completa de conversión con ejemplos y mejores prácticas
- **dotnet_to_python_converter.py**: Script de Python para asistir en la conversión básica
- **index.html**: Aplicación web de ejemplo (Marvel API)

## 🚀 Inicio Rápido

### ¿Cómo proporcionar archivos .NET que no están en el repositorio?

Si tienes archivos .NET que necesitas convertir pero no están en este repositorio, tienes varias opciones:

#### 1. **Agregar archivos al repositorio** (Recomendado)

```bash
# Clona el repositorio
git clone https://github.com/kevinxp20/proyectoh.git
cd proyectoh

# Copia tus archivos .NET
cp /ruta/a/tu/archivo.cs .

# Agrega y sube los archivos
git add archivo.cs
git commit -m "Agregar archivo para conversión"
git push
```

#### 2. **Crear un Issue con el código**

1. Ve a [Issues](https://github.com/kevinxp20/proyectoh/issues)
2. Crea un nuevo issue
3. Pega tu código en un bloque de código:

```markdown
### Archivo a convertir

```csharp
// Tu código .NET aquí
public class MiClase {
    // ...
}
```
```

#### 3. **Usar GitHub Gist**

1. Crea un Gist en https://gist.github.com/
2. Sube tu código .NET
3. Comparte el enlace en un issue o PR

#### 4. **Pegar código directamente en comentarios**

Para archivos pequeños, puedes pegar el código directamente en comentarios de issues o pull requests.

## 🛠️ Uso de las Herramientas

### Script de Conversión

El script `dotnet_to_python_converter.py` puede ayudarte con conversiones básicas:

#### Analizar un archivo .NET

```bash
python dotnet_to_python_converter.py archivo.cs --analyze
```

Esto te mostrará:
- Número de líneas
- Namespaces
- Clases encontradas
- Métodos
- Propiedades

#### Convertir un archivo

```bash
# Convertir y mostrar en consola
python dotnet_to_python_converter.py archivo.cs

# Convertir y guardar en archivo
python dotnet_to_python_converter.py archivo.cs -o archivo.py
```

**Nota:** La conversión es básica y requiere revisión manual. Siempre revisa y prueba el código generado.

### Ejemplo de Uso

**Archivo C# (ejemplo.cs):**
```csharp
using System;

namespace MiApp
{
    public class Usuario
    {
        public string Nombre { get; set; }
        public int Edad { get; set; }
        
        public string ObtenerDescripcion()
        {
            return $"{Nombre} tiene {Edad} años";
        }
    }
}
```

**Conversión:**
```bash
python dotnet_to_python_converter.py ejemplo.cs -o usuario.py
```

**Resultado (usuario.py):**
```python
class Usuario:
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, value: str):
        self._nombre = value
    
    @property
    def edad(self) -> int:
        return self._edad
    
    @edad.setter
    def edad(self, value: int):
        self._edad = value
    
    def obtener_descripcion(self) -> str:
        pass  # TODO: Implementar
```

## 📚 Documentación

Lee la [Guía de Conversión](CONVERSION_GUIDE.md) para:

- Equivalencias de tipos de datos
- Patrones de conversión comunes
- Ejemplos prácticos
- Mejores prácticas
- Preguntas frecuentes

### Temas cubiertos:

1. **Tipos de datos**: Conversión de tipos de C# a Python
2. **Clases y objetos**: Propiedades, métodos, constructores
3. **Colecciones**: List, Dictionary, etc.
4. **LINQ**: Conversión a comprensiones de lista
5. **Async/Await**: Programación asíncrona
6. **Manejo de excepciones**: try/catch/finally
7. **APIs Web**: ASP.NET a Flask/FastAPI

## 🔧 Requisitos

Para usar el script de conversión:

```bash
# Python 3.7 o superior
python --version

# No requiere dependencias externas
```

Para los ejemplos web en este repositorio:

- Navegador web moderno
- Conexión a internet (para APIs externas)

## 📝 Ejemplos

### Conversión de Modelo de Datos

**.NET:**
```csharp
public class Producto
{
    public int Id { get; set; }
    public string Nombre { get; set; }
    public decimal Precio { get; set; }
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
```

### Conversión de API Controller

**.NET:**
```csharp
[HttpGet]
public IActionResult GetProductos()
{
    return Ok(_service.GetAll());
}
```

**Python (FastAPI):**
```python
@app.get("/productos")
async def get_productos():
    return service.get_all()
```

## 🤝 Contribuir

Si encuentras errores o tienes sugerencias:

1. Crea un [Issue](https://github.com/kevinxp20/proyectoh/issues)
2. Describe el problema o sugerencia
3. Incluye ejemplos si es posible

## 📖 Recursos Adicionales

- [Guía oficial de Python](https://docs.python.org/3/)
- [C# to Python Quick Reference](https://www.pythonsheets.com/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Django Documentation](https://docs.djangoproject.com/)

## ❓ Preguntas Frecuentes

**P: ¿La conversión es automática al 100%?**

R: No. El script proporciona una conversión básica de sintaxis. Siempre necesitarás revisar y ajustar el código manualmente.

**P: ¿Qué hago con las librerías de .NET?**

R: Busca equivalentes en Python:
- Entity Framework → SQLAlchemy
- Newtonsoft.Json → json (built-in)
- HttpClient → requests o httpx
- Serilog → logging (built-in)

**P: ¿Puedo convertir proyectos grandes?**

R: Sí, pero hazlo por partes. Convierte primero los modelos, luego la lógica de negocio, y finalmente las APIs.

**P: ¿Cómo manejo el rendimiento?**

R: Python puede ser más lento que .NET. Considera:
- Usar PyPy para mejor rendimiento
- Cython para código crítico
- Optimizaciones específicas de Python

## 📄 Licencia

Este proyecto es de código abierto y está disponible para uso educativo y personal.

## 📧 Contacto

Para preguntas o soporte:
- Abre un [Issue](https://github.com/kevinxp20/proyectoh/issues)
- Describe tu caso de uso
- Incluye código de ejemplo cuando sea relevante
