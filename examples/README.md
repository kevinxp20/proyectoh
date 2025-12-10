# Ejemplos de Conversión de .NET a Python

Este directorio contiene ejemplos prácticos de conversión de código .NET/C# a Python.

## Archivos

### ejemplo.cs
Archivo .NET de ejemplo que contiene:
- Una clase de modelo de datos (`Producto`)
- Una clase de servicio con lógica de negocio (`ProductoService`)
- Una clase de utilidades estáticas (`Utilidades`)

### ejemplo.py
La conversión a Python del archivo `ejemplo.cs`, mostrando:
- Uso de `dataclass` para modelos de datos
- Type hints para documentar tipos
- Comprensiones de lista en lugar de LINQ
- Métodos estáticos con `@staticmethod`
- Código ejecutable de ejemplo en `if __name__ == "__main__"`

## Cómo usar estos ejemplos

### 1. Ver el código original

```bash
cat ejemplo.cs
```

### 2. Ver la conversión a Python

```bash
cat ejemplo.py
```

### 3. Ejecutar el ejemplo en Python

```bash
python ejemplo.py
```

Salida esperada:
```
=== Todos los productos ===
- Laptop - $999.99 (Disponible: True)
- Mouse - $25.50 (Disponible: True)
- Teclado - $75.00 (Disponible: False)

=== Productos disponibles ===
- Laptop - $999.99
- Mouse - $25.50

=== Productos en categoría 'accesorios' ===
- Mouse - $25.50
- Teclado - $75.00

=== Total de precios ===
$1100.49

=== Validación de nombres ===
'Laptop' es válido: True
'AB' es válido: False
'' es válido: False
```

### 4. Usar el conversor automático

```bash
# Analizar el archivo .NET
python ../dotnet_to_python_converter.py ejemplo.cs --analyze

# Convertir (la conversión manual en ejemplo.py es más completa)
python ../dotnet_to_python_converter.py ejemplo.cs -o ejemplo_auto.py
```

## Comparación de características

| Característica | .NET (C#) | Python |
|----------------|-----------|--------|
| Modelo de datos | Clase con propiedades | `@dataclass` |
| Tipos | Explícitos y obligatorios | Type hints opcionales |
| Colecciones | `List<T>`, `Dictionary<K,V>` | `list`, `dict` con Type hints |
| LINQ | `.Where()`, `.OrderBy()`, `.Sum()` | Comprensiones de lista, `sorted()`, `sum()` |
| Null | `null` | `None` |
| Métodos estáticos | `static` keyword | `@staticmethod` decorator |
| String interpolation | `$"{variable}"` | `f"{variable}"` |
| Decimal | `decimal` | `Decimal` (from decimal module) |

## Patrones de conversión aplicados

### 1. Propiedades auto-implementadas → Atributos de dataclass

**.NET:**
```csharp
public string Nombre { get; set; }
```

**Python:**
```python
@dataclass
class Producto:
    nombre: str
```

### 2. LINQ → Comprensiones de lista

**.NET:**
```csharp
var disponibles = _productos.Where(p => p.Disponible).ToList();
```

**Python:**
```python
disponibles = [p for p in self._productos if p.disponible]
```

### 3. LINQ OrderBy → sorted()

**.NET:**
```csharp
return _productos.OrderBy(p => p.Nombre).ToList();
```

**Python:**
```python
return sorted(self._productos, key=lambda p: p.nombre)
```

### 4. LINQ Sum → sum()

**.NET:**
```csharp
return _productos.Sum(p => p.Precio);
```

**Python:**
```python
return sum((p.precio for p in self._productos), Decimal('0'))
```

### 5. Validación de null → None

**.NET:**
```csharp
if (producto == null)
    throw new ArgumentNullException(nameof(producto));
```

**Python:**
```python
if producto is None:
    raise ValueError("El producto no puede ser None")
```

## Mejores prácticas aplicadas

1. **Type Hints**: Se usan type hints en Python para documentar tipos esperados
2. **Docstrings**: Cada función tiene un docstring explicativo
3. **Snake_case**: Los nombres siguen la convención snake_case de Python
4. **Dataclasses**: Se usan para modelos de datos simples
5. **List comprehensions**: Preferidas sobre loops explícitos
6. **Inmutabilidad**: Se devuelven copias de listas cuando es apropiado

## Aprender más

- Revisa el archivo `CONVERSION_GUIDE.md` en la raíz del proyecto
- Prueba modificar el código y ejecutarlo
- Experimenta con el conversor automático
- Compara las diferencias entre ambos lenguajes

## Agregar tus propios ejemplos

Si tienes código .NET que quieres convertir:

1. Coloca tu archivo `.cs` en este directorio
2. Usa el conversor para una primera aproximación
3. Revisa y mejora la conversión manualmente
4. Documenta los patrones que encontraste
