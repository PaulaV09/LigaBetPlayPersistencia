import os
import controllers.equipos as ec
import controllers.jugadores as jc
import controllers.tranferencias as tc
import controllers.ligas as lc
import controllers.cuerpoMedico as cm
import controllers.cuerpoTecnico as ct

opcionesMenu = ['Registrar liga', 'Listar ligas', 'Registrar equipo', 'Listar equipos', 'Registrar jugador', 'Listar jugadores', 'Transferencia de jugador', 'Registrar cuerpo tecnico', 'Listar cuerpo tecnico', 'Registrar cuerpo medico', 'Listar cuerpo medico','Registrar torneo', 'Listar torneos', 'Programar fechas', 'Registrar marcador', 'Ver estadísticas', 'Salir']

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
                lc.registrarLiga()
            case 1:
                lc.listarLigas()
            case 2:
                ec.registrarEquipo()
            case 3:
                ec.listarEquipos()
            case 4:
                jc.registrarJugador()
            case 5:
                jc.listarJugadores()
            case 6:
                tc.transferirJugador()
            case 7:
                ct.registrarCuerpoTecnico()
            case 8:
                ct.listarCuerpoTecnico()
            case 9:
                cm.registrarCuerpoMedico()
            case 10:
                cm.listarCuerpoMedico()
            case 11:
                print("Funcionalidad no implementada aún.")
                input("Presione Enter para continuar...")
            case 12:
                print("Funcionalidad no implementada aún.")
                input("Presione Enter para continuar...")
            case 13:
                print("Funcionalidad no implementada aún.")
                input("Presione Enter para continuar...")
            case 14:
                print("Funcionalidad no implementada aún.")
                input("Presione Enter para continuar...")
            case 15:    
                print("Funcionalidad no implementada aún.")
                input("Presione Enter para continuar...")
            case 16:
                print("Saliendo del programa...")
                input("Presione Enter para continuar...")
                return 
            case _:
                print("Opción no implementada aún.")
                input("Presione Enter para continuar...")
        