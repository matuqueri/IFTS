from gestor_turnos import GestorTurnos

def mostrar_menu_principal():
    print("\n SISTEMA DE TURNOS - PELUQUERÍA ")
    print("1. Gestión de Turnos")
    print("2. Gestión de Clientes (En desarrollo)")
    print("3. Gestión de Peluqueros (En desarrollo)")
    print("4. Guardar / Cargar Datos (En desarrollo)")
    print("5. Salir")

def menu_principal():
    gestor = GestorTurnos()

    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            gestor.menu_turnos()

        elif opcion == "2":
            print("\n>>> Esta sección está en desarrollo.\n")

        elif opcion == "3":
            print("\n>>> Esta sección está en desarrollo.\n")

        elif opcion == "4":
            print("\n>>> Funcionalidad en desarrollo.\n")

        elif opcion == "5":
            print("\nSaliendo del sistema...")
            break

        else:
            print("\nOpción inválida. Intente nuevamente.\n")

if __name__ == "__main__":
    menu_principal()
