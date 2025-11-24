import csv
from turno import Turno

class GestorTurnos:
    def __init__(self):
        
        self.ruta_turnos = "./data/turnos.csv"

        self.turnos = []

        self.cargar_turnos()

    def menu_turnos(self):
        while True:
            print("\n GESTIÓN DE TURNOS ")
            print("1. Ver turnos existentes")
            print("2. Crear nuevo turno")
            print("3. Eliminar turno")
            print("4. Volver al menú principal")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.listar_turnos()
            elif opcion == "2":
                self.crear_turno()
            elif opcion == "3":
                self.eliminar_turno()
            elif opcion == "4":
                break
            else:
                print("\nOpción inválida.\n")
