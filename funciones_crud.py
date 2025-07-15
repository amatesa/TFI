import sqlite3
from colorama import Fore, Style, init

init(autoreset=True)

def conectar():
    return sqlite3.connect('inventario.db')

def registrar_producto():
    
    '''Solicita lo datos de un nuevo producto y lo guarda en la base de datos.'''
    
    print(Fore.CYAN + "\n=== Registrar Nuevo Producto ===")
    print(Style.DIM + "-" * 50)
    nombre = input("Nombre: ").strip().lower()
    descripcion = input("Descripción: ").strip().lower()
    cantidad_input = input("Cantidad: ").strip().lower()
    precio_input = input("Precio: ").strip().lower()
    categoria = input("Categoría: ").strip().lower()
    
    #Validar los datos ingresados
    if not nombre:
        print(Fore.RED + "El nombre no puede estar vacío.")
        return
    try:
        cantidad = int(cantidad_input)
        if cantidad < 0:
            raise ValueError
    except ValueError:
        print(Fore.RED + "Cantidad debe ser un número entero no negativo.")
        return
    try:
        precio = float(precio_input)
        if precio <= 0:
            raise ValueError
    except ValueError:
        print(Fore.RED + "Precio debe ser un número positivo.")
        return
    
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute('''
        INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
        VALUES (?, ?, ?, ?, ?)
        ''', (nombre, descripcion, cantidad, precio, categoria))
        conexion.commit()
        print(Fore.GREEN + f"Producto {nombre} registrado correctamente.")
        print(Style.DIM + "-" * 50)
    except sqlite3.Error as e:
        print(Fore.RED + f"Error al registrar el producto: {e}")
    finally:
        conexion.close()

def mostrar_productos():
    
    '''Muestra todos los productos registrados en la base de datos.'''
    
    print(Fore.CYAN + "\n=== Mostrar Productos ===")
    print(Style.DIM + "-" * 50)
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM productos')
        productos = cursor.fetchall()
        
        if not productos:
            print(Fore.YELLOW + "No hay productos registrados.")
            print(Style.DIM + "-" * 50)
            return
        for producto in productos:
            print(Fore.WHITE + f"ID: {producto[0]} | Nombre: {producto[1].capitalize()} | Descripción: {producto[2]} | "
                               f"Cantidad: {producto[3]} | Precio: $ {producto[4]:.2f} | Categoría: {producto[5].capitalize()}")
            print(Style.DIM + "-" * 50)
    finally:
        conexion.close()

def actualizar_producto():
    '''Actualiza los datos de un producto existente.'''
    
    print(Fore.CYAN + "\n=== Actualizar Producto ===")
    print(Style.DIM + "-" * 50)
    id_input = input("Ingrese el ID del producto a actualizar: ").strip().lower()
    
    if not id_input.isdigit():
        print(Fore.RED + "ID inválido.")
        print(Style.DIM + "-" * 50)
        return

    id_producto = int(id_input)
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos WHERE id = ?", (id_producto,))
        producto = cursor.fetchone()

        if not producto:
            print(Fore.YELLOW + "Producto no encontrado.")
            print(Style.DIM + "-" * 50)
            return

        print(f"Producto actual: {producto}")
        nombre = input("Nuevo nombre (dejar vacío para mantener): ").strip().lower() or producto[1]
        descripcion = input("Nueva descripción: ").strip().lower() or producto[2]
        cantidad = input("Nueva cantidad: ").strip().lower()
        precio = input("Nuevo precio: ").strip().lower()
        categoria = input("Nueva categoría: ").strip().lower() or producto[5]

        cantidad = int(cantidad) if cantidad else producto[3]
        precio = float(precio) if precio else producto[4]

        cursor.execute('''
        UPDATE productos
        SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ?
        WHERE id = ?
        ''', (nombre, descripcion, cantidad, precio, categoria, id_producto))
        conexion.commit()
        print(Fore.GREEN + "Producto actualizado correctamente.")
        print(Style.DIM + "-" * 50)
    except Exception as e:
        print(Fore.RED + f"Error: {e}")
    finally:
        conexion.close()
        
def eliminar_producto():
  
    '''Elimina un producto de la base de datos por ID.'''
   
    print(Fore.CYAN + "\n=== Eliminar Producto ===")
    print(Style.DIM + "-" * 50)
    id_input = input("ID del producto: ").strip()
    if not id_input.isdigit():
        print(Fore.RED + "ID inválido.")
        print(Style.DIM + "-" * 50)
        return

    id_producto = int(id_input)
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT nombre FROM productos WHERE id = ?", (id_producto,))
        producto = cursor.fetchone()
        if not producto:
            print(Fore.YELLOW + "Producto no encontrado.")
            print(Style.DIM + "-" * 50)
            return

        confirmacion = input(f"¿Eliminar '{producto[0]}'? (S/N): ").strip().lower()
        if confirmacion != "s":
            print(Fore.YELLOW + "Eliminación cancelada.")
            print(Style.DIM + "-" * 50)
            return

        cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
        conexion.commit()
        print(Fore.GREEN + "Producto eliminado correctamente.")
        print(Style.DIM + "-" * 50)
    finally:
        conexion.close()
        
def buscar_producto():
   
    '''Busca un producto por su ID.'''
   
    print(Fore.CYAN + "\n=== Buscar Producto por ID ===")
    print(Style.DIM + "-" * 50)
    id_input = input("ID del producto: ").strip()
    if not id_input.isdigit():
        print(Fore.RED + "ID inválido.")
        print(Style.DIM + "-" * 50)
        return

    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos WHERE id = ?", (int(id_input),))
        producto = cursor.fetchone()
        if not producto:
            print(Fore.YELLOW + "Producto no encontrado.")
            print(Style.DIM + "-" * 50)
        else:
            print(Fore.GREEN + f"ID: {producto[0]} | Nombre: {producto[1]} | Descripción: {producto[2]} | "
                               f"Cantidad: {producto[3]} | Precio: ${producto[4]:.2f} | Categoría: {producto[5]}")
            print(Style.DIM + "-" * 50)
    finally:
        conexion.close()


def reporte_bajo_stock():
    
    '''Muestra los productos con cantidad menor o igual al límite ingresado.'''
  
    print(Fore.CYAN + "\n=== Reporte de Bajo Stock ===")
    print(Style.DIM + "-" * 50)
    limite_input = input("Límite de cantidad: ").strip()
    if not limite_input.isdigit():
        print(Fore.RED + "Límite inválido.")
        print(Style.DIM + "-" * 50)
        return

    try:
        limite = int(limite_input)
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (limite,))
        productos = cursor.fetchall()

        if not productos:
            print(Fore.YELLOW + "No hay productos con bajo stock.")
            print(Style.DIM + "-" * 50)
            return

        for producto in productos:
            print(Fore.WHITE + f"ID: {producto[0]} | Nombre: {producto[1]} | Cantidad: {producto[3]}")
    finally:
        conexion.close()