import sqlite3

def crear_base_de_datos():
    """Crea la base de datos 'inventario.db' y la tabla 'productos'."""
    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()
    
    # Usar CHECK para asegurar que los valores de cantidad y precio sean válidos.
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT,
        cantidad INTEGER NOT NULL CHECK(cantidad >= 0),
        precio REAL NOT NULL CHECK(precio > 0),
        categoria TEXT
    )
    ''')
    conexion.commit()
    conexion.close()
    print("Base de datos y tabla 'productos' creadas correctamente.")
    
    if __name__ == "__main__":
    #Uso el __name__ = "__main" para asegurarme de que la base de datos se crea solo al ejecutar este archivo directamente. De lo contrario, se crea al importar el módulo.
        crear_base_de_datos()