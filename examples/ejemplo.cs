using System;
using System.Collections.Generic;
using System.Linq;

namespace EjemploConversion
{
    // Clase de modelo de datos
    public class Producto
    {
        public int Id { get; set; }
        public string Nombre { get; set; }
        public decimal Precio { get; set; }
        public bool Disponible { get; set; }
        public List<string> Categorias { get; set; }

        public Producto()
        {
            Categorias = new List<string>();
        }

        public string ObtenerEtiqueta()
        {
            return $"{Nombre} - ${Precio:F2}";
        }

        public bool EstaEnCategoria(string categoria)
        {
            return Categorias.Contains(categoria);
        }
    }

    // Servicio de negocio
    public class ProductoService
    {
        private List<Producto> _productos;

        public ProductoService()
        {
            _productos = new List<Producto>();
        }

        public void AgregarProducto(Producto producto)
        {
            if (producto == null)
            {
                throw new ArgumentNullException(nameof(producto));
            }
            _productos.Add(producto);
        }

        public List<Producto> ObtenerTodos()
        {
            return _productos;
        }

        public List<Producto> ObtenerDisponibles()
        {
            return _productos.Where(p => p.Disponible).ToList();
        }

        public List<Producto> BuscarPorCategoria(string categoria)
        {
            return _productos
                .Where(p => p.EstaEnCategoria(categoria))
                .OrderBy(p => p.Nombre)
                .ToList();
        }

        public decimal CalcularTotal()
        {
            return _productos.Sum(p => p.Precio);
        }
    }

    // Clase de utilidades
    public static class Utilidades
    {
        public static string FormatearPrecio(decimal precio)
        {
            return $"${precio:F2}";
        }

        public static bool ValidarNombre(string nombre)
        {
            return !string.IsNullOrWhiteSpace(nombre) && nombre.Length >= 3;
        }
    }
}
