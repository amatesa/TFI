from colorama import Fore, Style, init
from funciones_crud import (registrar_producto, mostrar_productos, actualizar_producto, eliminar_producto, buscar_producto, reporte_bajo_stock)

from db import crear_base_de_datos

#Uso de autoreset para que los colores se reinicien automáticamente luego de cada impresión.
init(autoreset=True)

def menu():
    crear_base_de_datos()
    while True:
        print(Style.BRIGHT + Fore.BLUE + "\n╔══════════════════════════════╗")
        print(Style.BRIGHT + Fore.BLUE + "║      GESTOR DE INVENTARIO    ║")
        print(Style.BRIGHT + Fore.BLUE + "╠══════════════════════════════╣")
        print(Style.BRIGHT + Fore.BLUE + "║ 1. Registrar producto        ║")
        print(Style.BRIGHT + Fore.BLUE + "║ 2. Ver productos             ║")
        print(Style.BRIGHT + Fore.BLUE + "║ 3. Actualizar producto       ║")
        print(Style.BRIGHT + Fore.BLUE + "║ 4. Eliminar producto         ║")
        print(Style.BRIGHT + Fore.BLUE + "║ 5. Buscar producto por ID    ║")
        print(Style.BRIGHT + Fore.BLUE + "║ 6. Reporte de bajo stock     ║")
        print(Style.BRIGHT + Fore.BLUE + "║ 7. Salir                     ║")
        print(Style.BRIGHT + Fore.BLUE + "╚══════════════════════════════╝")

        opcion = input("Seleccioná una opción: ").strip()

        match opcion:
            case "1":
                registrar_producto()
                input(Fore.MAGENTA + "\nPresioná Enter para continuar...")
            case "2":
                mostrar_productos()
                input(Fore.MAGENTA + "\nPresioná Enter para continuar...")
            case "3":
                actualizar_producto()
                input(Fore.MAGENTA + "\nPresioná Enter para continuar...")
            case "4":
                eliminar_producto()
                input(Fore.MAGENTA + "\nPresioná Enter para continuar...")
            case "5":
                buscar_producto()
                input(Fore.MAGENTA + "\nPresioná Enter para continuar...")
            case "6":
                reporte_bajo_stock()
                input(Fore.MAGENTA + "\nPresioná Enter para continuar...")
            case "7":
                print(Fore.GREEN + "Gracias por usar el sistema.")
                break
            case _:
                print(Fore.RED + "Opción inválida. Intentá nuevamente.")

# Utilizar el bloque if __name__ == "__main__" para ejecutar el menú al iniciar el script.
if __name__ == "__main__":
    menu()