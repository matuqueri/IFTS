import csv
from turno import Turno

class GestorTurnos:
    def __init__(self):
        
        self.ruta_turnos = "../data/turnos.csv"

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

    def cargar_turnos(self):
        self.turnos.clear()

        try:
            with open(self.ruta_turnos, mode="r", newline="") as archivo:
                lector = csv.DictReader(archivo)

                for fila in lector:
                    turno = Turno(
                        id=int(fila["id"]),
                        cliente_id=int(fila["cliente_id"]),
                        peluquero_id=int(fila["peluquero_id"]),
                        fecha=fila["fecha"],
                        hora=fila["hora"]
                    )
                    self.turnos.append(turno)

        except FileNotFoundError:
            print("Archivo de turnos no encontrado. Se creará uno nuevo al guardar.")
        except Exception as e:
            print(f"Error al cargar turnos: {e}")

    def guardar_turnos(self):
        try:
            with open(self.ruta_turnos, mode="w", newline="") as archivo:
                campos = ["id", "cliente_id", "peluquero_id", "fecha", "hora"]
                escritor = csv.DictWriter(archivo, fieldnames=campos)

                escritor.writeheader()

                for t in self.turnos:
                    escritor.writerow({
                        "id": t.id,
                        "cliente_id": t.cliente_id,
                        "peluquero_id": t.peluquero_id,
                        "fecha": t.fecha,
                        "hora": t.hora
                    })

            print("\nTurnos guardados exitosamente.\n")

        except Exception as e:
            print(f"Error al guardar turnos: {e}")

    def listar_turnos(self):
        print("\n LISTA DE TURNOS ")

        if len(self.turnos) == 0:
            print("No hay turnos cargados.\n")
            return

        for t in self.turnos:
            print(t)

        print()

    def crear_turno(self):
        print("\n CREAR NUEVO TURNO ")

        try:
            nuevo_id = len(self.turnos) + 1
            cliente_id = int(input("ID del cliente: "))
            peluquero_id = int(input("ID del peluquero: "))
            fecha = input("Fecha (AAAA-MM-DD): ")
            hora = input("Hora (HH:MM): ")

            turno = Turno(nuevo_id, cliente_id, peluquero_id, fecha, hora)
            self.turnos.append(turno)
            self.guardar_turnos()

        except ValueError:
            print("Error: Ingrese valores numéricos para IDs.\n")
        except Exception as e:
            print(f"Error al crear turno: {e}")

    def eliminar_turno(self):
        print("\n ELIMINAR TURNO ")

        try:
            id_borrar = int(input("ID del turno a eliminar: "))
            encontrado = False

            for t in self.turnos:
                if t.id == id_borrar:
                    self.turnos.remove(t)
                    encontrado = True
                    break

            if encontrado:
                self.guardar_turnos()
                print(f"Turno {id_borrar} eliminado.\n")
            else:
                print("No existe un turno con ese ID.\n")

        except ValueError:
            print("Ingrese un número válido.\n")
        except Exception as e:
            print(f"Error al eliminar turno: {e}")
