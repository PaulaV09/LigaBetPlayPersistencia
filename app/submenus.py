import os
import controllers.equipos as ec
import controllers.jugadores as jc
import controllers.tranferencias as tc
import controllers.ligas as lc
import controllers.cuerpoMedico as cm
import controllers.cuerpoTecnico as ct
import controllers.torneos as tr
import controllers.fechas as fc
import utils.corefiles as cf
import utils.screenControllers as sc
import utils.validateData as vd
import config as cfg

opcionesSubMenuGestionLiga = ['Registrar Liga', 'Listar Ligas', 'Volver al Menú Principal']
opcionesSubMenuGestionEquipo = ['Registrar Equipo', 'Listar Equipos', 'Volver al Menú Principal']
opcionesSubMenuGestionJugador = ['Registrar Jugador', 'Listar Jugadores', 'Transferir Jugador', 'Volver al Menú Principal']
opcionesSubMenuGestionCuerpoTecMed = ['Registrar Cuerpo Técnico', 'Listar Cuerpo Técnico', 'Registrar Cuerpo Médico', 'Listar Cuerpo Médico', 'Volver al Menú Principal']
opcionesSubMenuGestionTorneo = ['Registrar Torneo', 'Listar Torneos', 'Programar Fechas', 'Registrar Marcador', 'Volver al Menú Principal']

def subMenuGestionLiga():
    sc.limpiar_pantalla()
    print("--- Gestión de Ligas ---")
    while True:
        print("Seleccione una opción:")
        for i, opcion in enumerate(opcionesSubMenuGestionLiga, start=1):
            print(f"{i}. {opcion}")
        op = vd.validateInt("Ingrese su opción: ") - 1
        
        if op < 0 or op >= len(opcionesSubMenuGestionLiga):
            print("Opción no válida. Intente de nuevo.")
            sc.pausar_pantalla()
            continue
        
        match op:
            case 0:
                lc.registrarLiga()
            case 1:
                lc.listarLigas()
            case 2:
                return
            case _:
                print("Opción no implementada aún.")
                sc.pausar_pantalla()

def subMenuGestionEquipo():
    sc.limpiar_pantalla()
    print("--- Gestión de Equipos ---")
    while True:
        print("Seleccione una opción:")
        for i, opcion in enumerate(opcionesSubMenuGestionEquipo, start=1):
            print(f"{i}. {opcion}")
        op = vd.validateInt("Ingrese su opción: ") - 1
        
        if op < 0 or op >= len(opcionesSubMenuGestionEquipo):
            print("Opción no válida. Intente de nuevo.")
            sc.pausar_pantalla()
            continue
        
        match op:
            case 0:
                ec.registrarEquipo()
            case 1:
                ec.listarEquipos()
            case 2:
                return
            case _:
                print("Opción no implementada aún.")
                sc.pausar_pantalla()

def subMenuGestionJugador():
    sc.limpiar_pantalla()
    print("--- Gestión de Jugadores ---")
    while True:
        print("Seleccione una opción:")
        for i, opcion in enumerate(opcionesSubMenuGestionJugador, start=1):
            print(f"{i}. {opcion}")
        op = vd.validateInt("Ingrese su opción: ") - 1
        
        if op < 0 or op >= len(opcionesSubMenuGestionJugador):
            print("Opción no válida. Intente de nuevo.")
            sc.pausar_pantalla()
            continue
        
        match op:
            case 0:
                jc.registrarJugador()
            case 1:
                jc.listarJugadores()
            case 2:
                tc.transferirJugador()
            case 3:
                return
            case _:
                print("Opción no implementada aún.")
                sc.pausar_pantalla()

def subMenuGestionCuerpoTecMed():
    sc.limpiar_pantalla()
    print("--- Gestión de Cuerpo Técnico y Médico ---")
    while True:
        print("Seleccione una opción:")
        for i, opcion in enumerate(opcionesSubMenuGestionCuerpoTecMed, start=1):
            print(f"{i}. {opcion}")
        op = vd.validateInt("Ingrese su opción: ") - 1
        
        if op < 0 or op >= len(opcionesSubMenuGestionCuerpoTecMed):
            print("Opción no válida. Intente de nuevo.")
            sc.pausar_pantalla()
            continue
        
        match op:
            case 0:
                ct.registrarCuerpoTecnico()
            case 1:
                ct.listarCuerpoTecnico()
            case 2:
                cm.registrarCuerpoMedico()
            case 3:
                cm.listarCuerpoMedico()
            case 4:
                return
            case _:
                print("Opción no implementada aún.")
                sc.pausar_pantalla()

def subMenuGestionTorneo():
    sc.limpiar_pantalla()
    print("--- Gestión de Torneos ---")
    while True:
        print("Seleccione una opción:")
        for i, opcion in enumerate(opcionesSubMenuGestionTorneo, start=1):
            print(f"{i}. {opcion}")
        op = vd.validateInt("Ingrese su opción: ") - 1
        
        if op < 0 or op >= len(opcionesSubMenuGestionTorneo):
            print("Opción no válida. Intente de nuevo.")
            sc.pausar_pantalla()
            continue
        
        match op:
            case 0:
                tr.registrarTorneo()
            case 1:
                tr.listarTorneos()
            case 2:
                fc.programarFechas()
            case 3:
                tr.registrarMarcador()
            case 4:
                return
            case _:
                print("Opción no implementada aún.")
                sc.pausar_pantalla()