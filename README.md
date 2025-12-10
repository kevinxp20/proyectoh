# Marvel Comics Character Search - Python Version

Este proyecto ha sido convertido de JavaScript/HTML a Python. Ahora incluye dos formas de usar la aplicación:

## Descripción

Aplicación para buscar comics de Marvel por ID de personaje usando la API de Marvel Comics.

## Versiones Disponibles

### 1. Versión de Línea de Comandos (CLI)

Script Python simple que se ejecuta desde la terminal.

**Uso:**
```bash
python marvel_comics.py <character_id>
```

**Ejemplo:**
```bash
python marvel_comics.py 1009368  # Iron Man
```

O ejecutar sin parámetros para ingresar el ID interactivamente:
```bash
python marvel_comics.py
```

### 2. Versión Web (Flask)

Aplicación web usando Flask que replica la funcionalidad original del HTML/JavaScript.

**Instalación:**
```bash
pip install -r requirements.txt
```

**Ejecutar:**
```bash
python app.py
```

Luego abrir en el navegador: `http://localhost:5000`

## Características

- ✅ Autenticación con Marvel API usando MD5 hash
- ✅ Búsqueda de comics por ID de personaje
- ✅ Muestra títulos, descripciones e imágenes
- ✅ Versión CLI para uso rápido en terminal
- ✅ Versión web con interfaz gráfica usando Flask

## IDs de Personajes Populares

- 1009368 - Iron Man
- 1009610 - Spider-Man  
- 1009220 - Captain America
- 1009664 - Thor
- 1009351 - Hulk
- 1009189 - Black Widow
- 1009262 - Daredevil
- 1009282 - Doctor Strange

## Requisitos

- Python 3.6+
- requests
- Flask (solo para la versión web)

## Estructura del Proyecto

```
proyectoh/
├── marvel_comics.py      # Versión CLI
├── app.py                # Aplicación web Flask
├── templates/
│   └── index.html        # Interfaz web
├── requirements.txt      # Dependencias Python
├── index.html           # Versión original JavaScript (mantener como referencia)
└── README.md            # Este archivo
```

## Conversión de JavaScript a Python

Esta aplicación fue convertida del código JavaScript original que usaba:
- HTML/JavaScript con jQuery
- Llamadas AJAX directas a la API de Marvel
- Bootstrap para la interfaz

La versión Python incluye:
- **CLI**: Script Python puro con `requests`
- **Web**: Backend Flask con frontend HTML similar al original
- Mismas credenciales y lógica de autenticación de la API
- Formato de salida mejorado para la terminal

## Notas de Seguridad

⚠️ Las claves de API están incluidas en el código por defecto (las mismas que estaban en el JavaScript original). 

**Para usar tus propias claves de API**, puedes configurar variables de entorno:

```bash
export MARVEL_PUBLIC_KEY="tu_clave_publica"
export MARVEL_PRIVATE_KEY="tu_clave_privada"
```

O en Windows:
```cmd
set MARVEL_PUBLIC_KEY=tu_clave_publica
set MARVEL_PRIVATE_KEY=tu_clave_privada
```

**Obtener claves de Marvel API:**
1. Regístrate en https://developer.marvel.com/
2. Crea una cuenta y obtén tus claves
3. Usa las variables de entorno mencionadas arriba

## Licencia

Este es un proyecto educativo para demostrar la conversión de JavaScript a Python.
