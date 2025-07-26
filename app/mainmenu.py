import os
import utils.corefiles as cf
import utils.screenControllers as sc
import utils.validateData as vd
import config as cfg
import app.submenus as sm

opcionesMenu = [ 'Gestión de Ligas', 'Gestión de Equipos', 'Gestión de Jugadores', 'Gestión de Cuerpo Técnico y Médico', 'Gestión de Torneos', 'Ver estadísticas', 'Salir']

def main_menu():
    while True: 
        sc.limpiar_pantalla()
        print("=========================================")
        print("       GESTOR DE TORNEOS DE FÚTBOL       ")
        print("=========================================")
        print("-> Bienvenido al Menú Principal")
        for i, opcion in enumerate(opcionesMenu, start=1):
            print(f"{i}. {opcion}")
        op = vd.validateInt("Seleccione una opción: ") - 1
        
        if op < 0 or op >= len(opcionesMenu): 
            print("Opción no válida. Intente de nuevo.")
            input("Presione Enter para continuar...")
            continue 
        
        match op:
            case 0:
                sm.subMenuGestionLiga()
            case 1:
                sm.subMenuGestionEquipo()
            case 2:
                sm.subMenuGestionJugador()
            case 3:
                sm.subMenuGestionCuerpoTecMed()
            case 4:
                sm.subMenuGestionTorneo()
            case 5:
                print("Funcionalidad de estadísticas aún no implementada.")
                input("Presione Enter para continuar...")
            case 6:
                print("Saliendo del programa...")
                input("Presione Enter para continuar...")
                return 
            case _:
                print("Opción no implementada aún.")
                input("Presione Enter para continuar...")
        