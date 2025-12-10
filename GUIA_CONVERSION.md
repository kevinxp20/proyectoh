# Guía de Conversión: JavaScript a Python

## ¿Qué se convirtió?

La aplicación original en **JavaScript/HTML** que buscaba comics de Marvel se ha convertido completamente a **Python**.

## Archivos Creados

### 1. `marvel_comics.py` - Versión de Línea de Comandos
Script Python que puedes ejecutar directamente desde la terminal.

**Ejemplo de uso:**
```bash
python marvel_comics.py 1009368
```

Este comando buscará todos los comics de Iron Man (ID: 1009368).

### 2. `app.py` + `templates/index.html` - Versión Web
Aplicación web usando Flask que funciona igual que la versión original HTML/JavaScript.

**Cómo ejecutar:**
```bash
pip install -r requirements.txt
python app.py
```

Luego abre tu navegador en: http://localhost:5000

### 3. `requirements.txt`
Lista de dependencias Python necesarias:
- `requests` - Para llamar a la API de Marvel
- `Flask` - Para la aplicación web

### 4. `test_marvel.py`
Pruebas automatizadas que verifican que el código funciona correctamente.

**Ejecutar tests:**
```bash
python test_marvel.py
```

### 5. `README.md`
Documentación completa en español con:
- Instrucciones de instalación
- Ejemplos de uso
- IDs de personajes populares
- Notas de seguridad

### 6. `.gitignore`
Configuración para que Git ignore archivos temporales de Python.

## Diferencias Clave: JavaScript vs Python

| Aspecto | JavaScript Original | Python Nuevo |
|---------|-------------------|--------------|
| **Ejecución** | Navegador web | Terminal o servidor web |
| **Autenticación API** | MD5 con crypto-js | MD5 con hashlib |
| **Peticiones HTTP** | jQuery $.getJSON | requests library |
| **Interfaz** | Solo HTML/JavaScript | CLI + Flask web app |
| **Configuración** | Código hardcoded | Variables de entorno |

## ¿Qué funcionalidad se mantuvo?

✅ Buscar comics por ID de personaje
✅ Autenticación con Marvel API (timestamp + hash MD5)
✅ Mostrar títulos, descripciones e imágenes
✅ Mismo formato de presentación de datos
✅ Mismas credenciales de API (pueden cambiarse)

## ¿Qué se mejoró?

✅ **Dos modos de uso**: línea de comandos y web
✅ **Variables de entorno**: credenciales configurables
✅ **Mejor manejo de errores**: mensajes claros en español
✅ **Accesibilidad mejorada**: ARIA labels, textos descriptivos
✅ **Seguridad**: Debug mode controlado, sin vulnerabilidades
✅ **Tests automatizados**: verificación de funcionalidad
✅ **Documentación completa**: en español con ejemplos

## Próximos Pasos Recomendados

1. **Probar la versión CLI:**
   ```bash
   python marvel_comics.py 1009610  # Spider-Man
   ```

2. **Probar la versión web:**
   ```bash
   pip install -r requirements.txt
   python app.py
   # Abrir http://localhost:5000 en el navegador
   ```

3. **Personalizar con tus propias claves:**
   ```bash
   export MARVEL_PUBLIC_KEY="tu_clave"
   export MARVEL_PRIVATE_KEY="tu_clave_privada"
   ```

4. **Desplegar en producción:**
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:8000 app:app
   ```

## Preguntas Frecuentes

**P: ¿Puedo seguir usando el archivo HTML original?**
R: Sí, está preservado como `index.html` para referencia.

**P: ¿Necesito Python 3?**
R: Sí, se requiere Python 3.6 o superior.

**P: ¿Funciona offline?**
R: No, necesita conexión a internet para llamar a la API de Marvel.

**P: ¿Cómo obtengo mis propias claves de Marvel API?**
R: Regístrate en https://developer.marvel.com/

**P: ¿Dónde están los ejemplos de IDs de personajes?**
R: En el README.md o ejecuta el script sin parámetros para ver ejemplos.

## Soporte

Si tienes dudas sobre cómo usar la conversión:
1. Lee el README.md completo
2. Ejecuta los tests: `python test_marvel.py`
3. Revisa los ejemplos en este documento
