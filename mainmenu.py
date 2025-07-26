import os
import controllers.equipos as ec

opcionesMenu = ['Registrar equipo', 'Listar equipos', 'Registrar jugador', 'Listar jugadores', 'Transferencia de jugador', 'Ver estadísticas', 'Salir']

def main_menu():
    while True: 
        os.system('cls' if os.name == 'nt' else 'clear')
        print("====================================")
        print("       GESTOR DE LIGA BETPLAY       ")
        print("====================================")
        print("-> Bienvenido al Menú Principal")
        for i, opcion in enumerate(opcionesMenu, start=1):
            print(f"{i}. {opcion}")
        try:
            op = int(input("Seleccione una opción: ")) - 1 
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
            input("Presione Enter para continuar...")
            continue
        
        if op < 0 or op >= len(opcionesMenu): 
            print("Opción no válida. Intente de nuevo.")
            input("Presione Enter para continuar...")
            continue 
        
        match op:
            case 0: 
                ec.registrarEquipo()
            case 1: 
                ec.listarEquipos()
            case 2:  
                pass
            case 3:  
                pass
            case 4:     
                pass
            case 5:
                pass
            case 6:
                print("Saliendo del programa...")
                input("Presione Enter para continuar...")
                return 
            case _:
                print("Opción no implementada aún.")
                input("Presione Enter para continuar...")
        