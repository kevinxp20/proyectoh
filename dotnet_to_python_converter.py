#!/usr/bin/env python3
"""
Herramienta de ayuda para convertir código .NET a Python

Este script proporciona utilidades básicas para ayudar en la conversión
de código .NET/C# a Python. No es una conversión automática completa,
sino una herramienta de asistencia.
"""

import re
import sys
import argparse
from typing import List, Dict, Tuple


class DotNetToPythonConverter:
    """Conversor básico de sintaxis .NET a Python"""
    
    # Mapeo de tipos de datos
    TYPE_MAPPINGS = {
        'int': 'int',
        'long': 'int',
        'short': 'int',
        'byte': 'int',
        'float': 'float',
        'double': 'float',
        'decimal': 'Decimal',
        'string': 'str',
        'bool': 'bool',
        'void': 'None',
        'object': 'object',
        'var': '',  # Inferido en Python
    }
    
    # Mapeo de colecciones
    COLLECTION_MAPPINGS = {
        'List': 'List',
        'Dictionary': 'Dict',
        'HashSet': 'Set',
        'Queue': 'deque',
        'Stack': 'List',
        'IEnumerable': 'Iterable',
        'Array': 'List',
    }
    
    def __init__(self):
        self.imports = set()
        self.converted_lines = []
        
    def convert_type(self, csharp_type: str) -> str:
        """Convierte un tipo de C# a su equivalente en Python"""
        # Eliminar modificadores
        csharp_type = csharp_type.strip()
        
        # Tipos genéricos (List<T>, Dictionary<K,V>)
        if '<' in csharp_type:
            match = re.match(r'(\w+)<(.+)>', csharp_type)
            if match:
                container = match.group(1)
                inner_types = match.group(2)
                
                if container in self.COLLECTION_MAPPINGS:
                    python_container = self.COLLECTION_MAPPINGS[container]
                    # Convertir tipos internos
                    inner_python = ', '.join([
                        self.convert_type(t.strip()) 
                        for t in inner_types.split(',')
                    ])
                    # Solo agregar el import del tipo específico usado
                    self.imports.add(f'from typing import {python_container}')
                    return f"{python_container}[{inner_python}]"
        
        # Tipos simples
        if csharp_type in self.TYPE_MAPPINGS:
            result = self.TYPE_MAPPINGS[csharp_type]
            if result == 'Decimal':
                self.imports.add('from decimal import Decimal')
            return result
            
        # Si no se encuentra, devolver el tipo original
        return csharp_type
    
    def convert_property(self, line: str) -> List[str]:
        """Convierte una propiedad de C# a Python"""
        # public string Nombre { get; set; }
        match = re.match(r'\s*(public|private|protected)?\s+(\w+(?:<.+>)?)\s+(\w+)\s*\{\s*get;\s*set;\s*\}', line)
        if match:
            prop_type = match.group(2)
            prop_name = match.group(3)
            
            python_type = self.convert_type(prop_type)
            python_name = self.to_snake_case(prop_name)
            
            return [
                f"    @property",
                f"    def {python_name}(self) -> {python_type}:",
                f"        return self._{python_name}",
                f"",
                f"    @{python_name}.setter",
                f"    def {python_name}(self, value: {python_type}):",
                f"        self._{python_name} = value",
            ]
        return []
    
    def convert_method_signature(self, line: str) -> str:
        """Convierte la firma de un método de C# a Python"""
        # public ReturnType MethodName(Type1 param1, Type2 param2)
        match = re.match(
            r'\s*(public|private|protected|static)?\s*(async)?\s*(\w+(?:<.+>)?)\s+(\w+)\s*\((.*?)\)',
            line
        )
        if match:
            is_async = match.group(2) == 'async'
            return_type = match.group(3)
            method_name = match.group(4)
            params = match.group(5)
            
            # Convertir parámetros
            python_params = ['self']
            if params.strip():
                for param in params.split(','):
                    param = param.strip()
                    parts = param.split()
                    if len(parts) >= 2:
                        param_type = parts[0]
                        param_name = parts[1]
                        python_type = self.convert_type(param_type)
                        python_name = self.to_snake_case(param_name)
                        python_params.append(f"{python_name}: {python_type}")
            
            # Convertir tipo de retorno
            python_return = self.convert_type(return_type)
            
            # Convertir nombre del método
            python_method = self.to_snake_case(method_name)
            
            # Construir firma
            params_str = ', '.join(python_params)
            async_prefix = 'async ' if is_async else ''
            return f"    {async_prefix}def {python_method}({params_str}) -> {python_return}:"
        
        return line
    
    def convert_class_declaration(self, line: str) -> str:
        """Convierte la declaración de una clase de C# a Python"""
        # public class ClassName : BaseClass
        match = re.match(r'\s*(public|private|internal)?\s*class\s+(\w+)(?:\s*:\s*(\w+))?', line)
        if match:
            class_name = match.group(2)
            base_class = match.group(3)
            
            if base_class:
                return f"class {class_name}({base_class}):"
            else:
                return f"class {class_name}:"
        
        return line
    
    def to_snake_case(self, name: str) -> str:
        """Convierte PascalCase/camelCase a snake_case"""
        # Insertar guión bajo antes de letras mayúsculas
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
    
    def convert_string_interpolation(self, line: str) -> str:
        """Convierte interpolación de strings de C# a f-strings de Python"""
        # $"texto {variable}" -> f"texto {variable}"
        line = re.sub(r'\$"', 'f"', line)
        return line
    
    def convert_null_to_none(self, line: str) -> str:
        """Convierte null a None"""
        return re.sub(r'\bnull\b', 'None', line)
    
    def analyze_file(self, filename: str) -> Dict[str, any]:
        """Analiza un archivo .NET y proporciona un reporte"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
        except FileNotFoundError:
            print(f"Error: No se encuentra el archivo {filename}")
            return {}
        
        analysis = {
            'classes': [],
            'methods': [],
            'properties': [],
            'namespaces': [],
            'usings': [],
            'total_lines': len(content.splitlines()),
        }
        
        # Buscar clases
        analysis['classes'] = re.findall(r'class\s+(\w+)', content)
        
        # Buscar métodos
        analysis['methods'] = re.findall(r'(?:public|private|protected)\s+\w+\s+(\w+)\s*\(', content)
        
        # Buscar propiedades
        analysis['properties'] = re.findall(r'(?:public|private|protected)\s+\w+\s+(\w+)\s*\{\s*get;', content)
        
        # Buscar namespaces
        analysis['namespaces'] = re.findall(r'namespace\s+([\w.]+)', content)
        
        # Buscar using statements
        analysis['usings'] = re.findall(r'using\s+([\w.]+);', content)
        
        return analysis
    
    def convert_file(self, input_filename: str, output_filename: str = None):
        """Convierte un archivo .NET a Python (conversión básica)"""
        try:
            with open(input_filename, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except FileNotFoundError:
            print(f"Error: No se encuentra el archivo {input_filename}")
            return
        
        self.converted_lines = []
        self.imports = set()
        in_class = False
        indentation = 0
        
        for line in lines:
            stripped = line.strip()
            
            # Ignorar using statements (los manejaremos al final)
            if stripped.startswith('using ') and ';' in stripped:
                continue
            
            # Ignorar namespace (Python usa módulos)
            if stripped.startswith('namespace '):
                continue
            
            # Abrir llaves
            if '{' in stripped and not stripped.startswith('//'):
                in_class = True
                # Convertir declaración antes de la llave
                converted = self.convert_class_declaration(stripped.replace('{', '').strip())
                if converted:
                    self.converted_lines.append(converted)
                continue
            
            # Cerrar llaves
            if '}' in stripped and not stripped.startswith('//'):
                if indentation > 0:
                    indentation -= 1
                continue
            
            # Comentarios
            if stripped.startswith('//'):
                self.converted_lines.append(line.replace('//', '#'))
                continue
            
            # Líneas vacías
            if not stripped:
                self.converted_lines.append('')
                continue
            
            # Convertir propiedades
            if 'get;' in stripped and 'set;' in stripped:
                converted_props = self.convert_property(stripped)
                self.converted_lines.extend(converted_props)
                continue
            
            # Convertir métodos
            if re.search(r'\w+\s+\w+\s*\(.*\)', stripped):
                converted_method = self.convert_method_signature(stripped)
                self.converted_lines.append(converted_method)
                self.converted_lines.append('        pass  # TODO: Implementar')
                continue
            
            # Aplicar conversiones básicas
            converted = line
            converted = self.convert_string_interpolation(converted)
            converted = self.convert_null_to_none(converted)
            converted = converted.replace(';', '')  # Python no usa punto y coma
            
            self.converted_lines.append(converted.rstrip())
        
        # Construir salida
        output = []
        
        # Agregar imports de Python
        if self.imports:
            output.extend(sorted(self.imports))
            output.append('')
            output.append('')
        
        # Agregar código convertido
        output.extend(self.converted_lines)
        
        # Guardar o imprimir
        if output_filename:
            with open(output_filename, 'w', encoding='utf-8') as f:
                f.write('\n'.join(output))
            print(f"Conversión guardada en: {output_filename}")
        else:
            print('\n'.join(output))


def main():
    parser = argparse.ArgumentParser(
        description='Herramienta de ayuda para convertir código .NET a Python'
    )
    parser.add_argument(
        'input',
        help='Archivo .NET de entrada (.cs)'
    )
    parser.add_argument(
        '-o', '--output',
        help='Archivo Python de salida (.py). Si no se especifica, imprime en consola'
    )
    parser.add_argument(
        '-a', '--analyze',
        action='store_true',
        help='Solo analizar el archivo sin convertir'
    )
    
    args = parser.parse_args()
    
    converter = DotNetToPythonConverter()
    
    if args.analyze:
        analysis = converter.analyze_file(args.input)
        print("\n=== Análisis del archivo .NET ===\n")
        print(f"Total de líneas: {analysis.get('total_lines', 0)}")
        print(f"\nNamespaces encontrados: {len(analysis.get('namespaces', []))}")
        for ns in analysis.get('namespaces', []):
            print(f"  - {ns}")
        print(f"\nUsing statements: {len(analysis.get('usings', []))}")
        for u in analysis.get('usings', []):
            print(f"  - {u}")
        print(f"\nClases encontradas: {len(analysis.get('classes', []))}")
        for cls in analysis.get('classes', []):
            print(f"  - {cls}")
        print(f"\nMétodos encontrados: {len(analysis.get('methods', []))}")
        for method in analysis.get('methods', []):
            print(f"  - {method}")
        print(f"\nPropiedades encontradas: {len(analysis.get('properties', []))}")
        for prop in analysis.get('properties', []):
            print(f"  - {prop}")
    else:
        print("\n=== Conversión de .NET a Python ===\n")
        print("NOTA: Esta es una conversión básica. Revisa el código y ajusta según sea necesario.\n")
        converter.convert_file(args.input, args.output)
        print("\n=== Pasos siguientes ===")
        print("1. Revisa el código Python generado")
        print("2. Implementa los métodos marcados con 'pass'")
        print("3. Ajusta los imports según sea necesario")
        print("4. Prueba el código y realiza ajustes manuales")


if __name__ == '__main__':
    main()
