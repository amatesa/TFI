GESTOR DE INVENTARIO - Proyecto Final Python
============================================

Descripción:
Sistema de gestión de inventario que permite registrar, consultar, actualizar, buscar y eliminar productos, además de generar reportes de bajo stock.

Estructura del proyecto:
- db.py : Crea la base de datos y tabla 'productos'.
- funciones_crud.py : Lógica de gestión de productos (CRUD).
- menu.py : Interfaz en terminal para interactuar con el sistema.
- inventario.db : Base de datos generada automáticamente.

Tecnologías usadas:
- Python 3.x
- SQLite3 (base de datos)
- colorama (mejora visual en terminal)

Ejecución:
1. Asegurate de tener `colorama` instalado:
   `pip install colorama`
2. Ejecutá el archivo `menu.py`:
   `python menu.py`

Funcionalidades:
- Registrar nuevos productos.
- Visualizar todos los productos.
- Actualizar productos por ID.
- Eliminar productos por ID.
- Buscar producto por ID.
- Reporte de productos con stock bajo (por cantidad).