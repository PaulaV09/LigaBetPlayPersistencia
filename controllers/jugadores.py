import os
import utils.corefiles as cf
import utils.screenControllers as sc
import utils.validateData as vd
import config as cfg

def registrarJugador():
    sc.limpiar_pantalla()
    equipos_data = cf.readJson(cfg.DB_EQUIPOS)
    if not isinstance(equipos_data, dict) or 'equipos' not in equipos_data:
        print("No hay equipos registrados. Registre un equipo primero.")
        sc.pausar_pantalla()
        return
    print("--- Registrar Jugador ---")
    jugadores_data = cf.readJson(cfg.DB_JUGADORES)
    if not isinstance(jugadores_data, dict) or 'jugadores' not in jugadores_data:
        jugadores_data = {"jugadores": {}}

    nombre = vd.validatetext("Ingrese el nombre del jugador: ").title()
    posicion = vd.validatetext("Ingrese la posición del jugador: ").title()
    print("---------------------------")
    print("\nEquipos registrados:")
    for equipo in equipos_data.get("equipos", {}).values():
        print(f"ID: {equipo.get('id', 'N/A')} - Nombre: {equipo.get('nombre', 'N/A')}")
    print("---------------------------")
    idEquipo = vd.validateInt("Ingrese el ID del equipo al que pertenece el jugador: ")
    dorsal = vd.validateInt("Ingrese la dorsal del jugador: ")
    for jugador in jugadores_data.get("jugadores", {}).values():
        if jugador.get("dorsal", "") == dorsal and jugador.get("id_equipo", "") == idEquipo:
            print(f"Error: La dorsal '{dorsal}' ya está registrada en el equipo '{idEquipo}'.")
            sc.pausar_pantalla()
            return
        
    if not jugadores_data.get("jugadores"):
        id_jugador = "1"
    else:
        max_id = max(int(k) for k in jugadores_data["jugadores"].keys())
        id_jugador = str(max_id + 1)

    jugador = {
        "id": id_jugador,
        "nombre": nombre,
        "posicion": posicion,
        "id_equipo": idEquipo,
        "dorsal": dorsal,
        "isPrestamo": False 
    }

    jugadores_data["jugadores"][id_jugador] = jugador
    cf.writeJson(cfg.DB_JUGADORES, jugadores_data)

    print(f"\nEl jugador '{nombre}' registrado con éxito con el ID: {id_jugador}")
    sc.pausar_pantalla()

def listarJugadores():
    sc.limpiar_pantalla()
    print("--- Listar Jugadores ---")
    jugadores_data = cf.readJson(cfg.DB_JUGADORES)
    equipos_data = cf.readJson(cfg.DB_EQUIPOS)
    jugadores = jugadores_data.get("jugadores", {})
    equipos = equipos_data.get("equipos", {})

    if not jugadores:
        print("No hay jugadores registrados.")
        sc.pausar_pantalla()
        return

    for id_jugador, jugador in jugadores.items():
        id_equipo = str(jugador.get('id_equipo', ''))
        nombre_equipo = equipos.get(id_equipo, {}).get('nombre', 'Equipo no encontrado')

        print('--------------------------')
        print(f"ID: {id_jugador}\nNombre: {jugador.get('nombre', 'N/A')}\nPosición: {jugador.get('posicion', 'N/A')}\nEquipo: {nombre_equipo} (ID: {id_equipo})\nDorsal: {jugador.get('dorsal', 'N/A')}")
    sc.pausar_pantalla()