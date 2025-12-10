# Inicio Rápido: Conversión de .NET a Python

## 🎯 Pregunta: ¿Cómo puedo pasar de .NET a Python un archivo que no tengo en el repositorio de GitHub?

Esta guía responde específicamente a esa pregunta con soluciones prácticas.

## 📤 4 Formas de Proporcionar tu Archivo .NET

### 1️⃣ Agregar al Repositorio (Más Simple)

```bash
# Clona el repo
git clone https://github.com/kevinxp20/proyectoh.git
cd proyectoh

# Copia tu archivo
cp /mi/ruta/MiClase.cs .

# Sube el archivo
git add MiClase.cs
git commit -m "Agregar archivo para conversión"
git push
```

### 2️⃣ Crear un Issue con el Código

1. Ve a: https://github.com/kevinxp20/proyectoh/issues/new
2. Título: "Convertir archivo MiClase.cs a Python"
3. Pega tu código:

```markdown
### Código .NET a convertir

\```csharp
using System;

public class MiClase 
{
    public string Nombre { get; set; }
    public void MiMetodo() { }
}
\```

### ¿Qué hace este código?
[Describe brevemente la funcionalidad]
```

### 3️⃣ Usar GitHub Gist

1. Navega a: https://gist.github.com/
2. Crea un nuevo Gist con tu código .NET
3. Copia el enlace del Gist
4. Comparte el enlace en un issue o comentario

### 4️⃣ Pegar Directamente en Comentarios

Para archivos pequeños (< 100 líneas):
- Pega el código en un comentario de issue
- Usa bloques de código con \```csharp

## 🔧 Usar las Herramientas de Conversión

### Opción A: Análisis Automático

```bash
python dotnet_to_python_converter.py tu_archivo.cs --analyze
```

**Resultado:**
```
=== Análisis del archivo .NET ===

Total de líneas: 88
Clases encontradas: 3
  - Producto
  - ProductoService
  - Utilidades
Métodos encontrados: 4
Propiedades encontradas: 4
```

### Opción B: Conversión Básica

```bash
python dotnet_to_python_converter.py tu_archivo.cs -o salida.py
```

**⚠️ Nota:** La conversión automática es básica. Revisa y mejora el código generado.

### Opción C: Ver Ejemplo Completo

```bash
# Ver código .NET original
cat examples/ejemplo.cs

# Ver conversión manual completa
cat examples/ejemplo.py

# Ejecutar el ejemplo
python examples/ejemplo.py
```

## 📚 Documentación Completa

| Archivo | Descripción |
|---------|-------------|
| [README.md](README.md) | Documentación general y guía de uso |
| [CONVERSION_GUIDE.md](CONVERSION_GUIDE.md) | Guía completa con patrones de conversión |
| [examples/](examples/) | Ejemplos prácticos de conversión |

## 💡 Ejemplo Rápido

**Entrada (.NET):**
```csharp
public class Usuario
{
    public string Nombre { get; set; }
    public int Edad { get; set; }
    
    public string GetDescripcion()
    {
        return $"{Nombre} tiene {Edad} años";
    }
}
```

**Salida (Python):**
```python
from dataclasses import dataclass

@dataclass
class Usuario:
    nombre: str
    edad: int
    
    def get_descripcion(self) -> str:
        return f"{self.nombre} tiene {self.edad} años"
```

## ⚡ Conversiones Comunes

| .NET | Python | Ejemplo |
|------|--------|---------|
| `List<T>` | `list` o `List[T]` | `List<string>` → `List[str]` |
| `Dictionary<K,V>` | `dict` o `Dict[K,V]` | `Dictionary<int, string>` → `Dict[int, str]` |
| `null` | `None` | `if (x == null)` → `if x is None:` |
| `string.IsNullOrEmpty()` | `not string or not string.strip()` | Verificación de cadena vacía |
| `.Where()` | List comprehension | `items.Where(x => x > 5)` → `[x for x in items if x > 5]` |
| `.Select()` | List comprehension | `items.Select(x => x * 2)` → `[x * 2 for x in items]` |
| `var` | Type inference | `var x = 5` → `x = 5` o `x: int = 5` |
| `async/await` | `async/await` | Similar, usando `asyncio` |

## 🎓 Próximos Pasos

1. **Lee la documentación completa**: [CONVERSION_GUIDE.md](CONVERSION_GUIDE.md)
2. **Estudia los ejemplos**: Directorio [examples/](examples/)
3. **Prueba el conversor**: Con tu propio código
4. **Experimenta**: Modifica y ejecuta los ejemplos

## ❓ Preguntas Frecuentes

**P: ¿El conversor hace todo automáticamente?**
R: No. Hace una conversión básica de sintaxis. Siempre revisa y ajusta manualmente.

**P: ¿Puedo convertir proyectos grandes?**
R: Sí, pero hazlo por partes: primero modelos, luego lógica, finalmente APIs.

**P: ¿Qué pasa con las librerías de NuGet?**
R: Busca equivalentes en PyPI o implementa la funcionalidad necesaria.

**P: Mi archivo tiene código privado/sensible**
R: Usa un repo privado o comparte solo las partes que necesites convertir.

## 🆘 Obtener Ayuda

1. **Crea un Issue**: https://github.com/kevinxp20/proyectoh/issues
2. **Incluye**:
   - Tu código .NET (o enlace)
   - Lo que intentas lograr
   - Cualquier error que encuentres
3. **Espera respuesta**: La comunidad te ayudará

## 📞 Contacto

- **Issues**: Para reportar problemas o hacer preguntas
- **Pull Requests**: Para contribuir con mejoras
- **Discussions**: Para conversaciones generales

---

¿Listo para empezar? 🚀

```bash
# 1. Clona el repositorio
git clone https://github.com/kevinxp20/proyectoh.git

# 2. Ve al directorio
cd proyectoh

# 3. Analiza tu archivo
python dotnet_to_python_converter.py tu_archivo.cs --analyze

# 4. Convierte y revisa
python dotnet_to_python_converter.py tu_archivo.cs -o output.py
```
