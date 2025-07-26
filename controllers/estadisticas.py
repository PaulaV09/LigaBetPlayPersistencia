import os
import utils.corefiles as cf
import utils.screenControllers as sc
import utils.validateData as vd
import config as cfg

def tablaGeneral():
    sc.limpiar_pantalla()
    print("--- Tabla General ---")
    ligas_data = cf.readJson(cfg.DB_LIGAS)
    equipos_data = cf.readJson(cfg.DB_EQUIPOS)
    if not isinstance(ligas_data, dict) or 'ligas' not in ligas_data:
        print("No hay ligas registradas. Registre una liga primero.")
        sc.pausar_pantalla()
        return
    if not isinstance(equipos_data, dict) or 'equipos' not in equipos_data:
        print("No hay equipos registrados. Registre un equipo primero.")
        sc.pausar_pantalla()
        return
    equipos = equipos_data.get("equipos", {})
    if not equipos:
        print("No hay equipos registrados.")
        sc.pausar_pantalla()
        return
    print(f"{'ID':<5} {'Nombre':<20} {'PJ':<3} {'PG':<3} {'PE':<3} {'PP':<3} {'GF':<3} {'GC':<3} {'Puntos':<6}")
    for equipo in equipos.values():
        id_equipo = equipo.get('id', '')
        nombre = equipo.get('nombre', 'N/A')
        pj = equipo.get('pj', 0)
        pg = equipo.get('pg', 0)
        pe = equipo.get('pe', 0)
        pp = equipo.get('pp', 0)
        gf = equipo.get('gf', 0)
        gc = equipo.get('gc', 0)
        puntos = equipo.get('pt', 0)
        print(f"{id_equipo:<5} {nombre:<20} {pj:<3} {pg:<3} {pe:<3} {pp:<3} {gf:<3} {gc:<3} {puntos:<6}")
    sc.pausar_pantalla()

def equipoMasGolesAFavor():
    sc.limpiar_pantalla()
    print("--- Equipo con Más Goles a Favor ---")
    equipos_data = cf.readJson(cfg.DB_EQUIPOS)
    if not isinstance(equipos_data, dict) or 'equipos' not in equipos_data:
        print("No hay equipos registrados. Registre un equipo primero.")
        sc.pausar_pantalla()
        return
    equipos = equipos_data.get("equipos", {})
    if not equipos:
        print("No hay equipos registrados.")
        sc.pausar_pantalla()
        return
    max_goles = -1
    equipo_max_goles = None
    for equipo in equipos.values():
        if equipo.get('gf', 0) > max_goles:
            max_goles = equipo['gf']
            equipo_max_goles = equipo
    if equipo_max_goles:
        print(f"Equipo: {equipo_max_goles['nombre']}, Goles a Favor: {max_goles}")
    else:
        print("No se encontró ningún equipo con goles a favor.")
    sc.pausar_pantalla()

def equipoMasGolesEnContra():
    sc.limpiar_pantalla()
    print("--- Equipo con Más Goles en Contra ---")
    equipos_data = cf.readJson(cfg.DB_EQUIPOS)
    if not isinstance(equipos_data, dict) or 'equipos' not in equipos_data:
        print("No hay equipos registrados. Registre un equipo primero.")
        sc.pausar_pantalla()
        return
    equipos = equipos_data.get("equipos", {})
    if not equipos:
        print("No hay equipos registrados.")
        sc.pausar_pantalla()
        return
    max_goles_contra = -1
    equipo_max_goles_contra = None
    for equipo in equipos.values():
        if equipo.get('gc', 0) > max_goles_contra:
            max_goles_contra = equipo['gc']
            equipo_max_goles_contra = equipo
    if equipo_max_goles_contra:
        print(f"Equipo: {equipo_max_goles_contra['nombre']}, Goles en Contra: {max_goles_contra}")
    else:
        print("No se encontró ningún equipo con goles en contra.")
    sc.pausar_pantalla()

def equipoMasPuntos():
    sc.limpiar_pantalla()
    print("--- Equipo con Más Puntos ---")
    equipos_data = cf.readJson(cfg.DB_EQUIPOS)
    if not isinstance(equipos_data, dict) or 'equipos' not in equipos_data:
        print("No hay equipos registrados. Registre un equipo primero.")
        sc.pausar_pantalla()
        return
    equipos = equipos_data.get("equipos", {})
    if not equipos:
        print("No hay equipos registrados.")
        sc.pausar_pantalla()
        return
    max_puntos = -1
    equipo_max_puntos = None
    for equipo in equipos.values():
        if equipo.get('pt', 0) > max_puntos:
            max_puntos = equipo['pt']
            equipo_max_puntos = equipo
    if equipo_max_puntos:
        print(f"Equipo: {equipo_max_puntos['nombre']}, Puntos: {max_puntos}")
    else:
        print("No se encontró ningún equipo con puntos.")
    sc.pausar_pantalla()

def equipoMasPartidosGanados():
    sc.limpiar_pantalla()
    print("--- Equipo con Más Partidos Ganados ---")
    equipos_data = cf.readJson(cfg.DB_EQUIPOS)
    if not isinstance(equipos_data, dict) or 'equipos' not in equipos_data:
        print("No hay equipos registrados. Registre un equipo primero.")
        sc.pausar_pantalla()
        return
    equipos = equipos_data.get("equipos", {})
    if not equipos:
        print("No hay equipos registrados.")
        sc.pausar_pantalla()
        return
    max_partidos_ganados = -1
    equipo_max_partidos_ganados = None
    for equipo in equipos.values():
        if equipo.get('pg', 0) > max_partidos_ganados:
            max_partidos_ganados = equipo['pg']
            equipo_max_partidos_ganados = equipo
    if equipo_max_partidos_ganados:
        print(f"Equipo: {equipo_max_partidos_ganados['nombre']}, Partidos Ganados: {max_partidos_ganados}")
    else:
        print("No se encontró ningún equipo con partidos ganados.")
    sc.pausar_pantalla()

def equipoMasPartidosEmpatados():
    sc.limpiar_pantalla()
    print("--- Equipo con Más Partidos Empatados ---")
    equipos_data = cf.readJson(cfg.DB_EQUIPOS)
    if not isinstance(equipos_data, dict) or 'equipos' not in equipos_data:
        print("No hay equipos registrados. Registre un equipo primero.")
        sc.pausar_pantalla()
        return
    equipos = equipos_data.get("equipos", {})
    if not equipos:
        print("No hay equipos registrados.")
        sc.pausar_pantalla()
        return
    max_partidos_empatados = -1
    equipo_max_partidos_empatados = None
    for equipo in equipos.values():
        if equipo.get('pe', 0) > max_partidos_empatados:
            max_partidos_empatados = equipo['pe']
            equipo_max_partidos_empatados = equipo
    if equipo_max_partidos_empatados:
        print(f"Equipo: {equipo_max_partidos_empatados['nombre']}, Partidos Empatados: {max_partidos_empatados}")
    else:
        print("No se encontró ningún equipo con partidos empatados.")
    sc.pausar_pantalla()

def equipoMasPartidosPerdidos():
    sc.limpiar_pantalla()
    print("--- Equipo con Más Partidos Perdidos ---")
    equipos_data = cf.readJson(cfg.DB_EQUIPOS)
    if not isinstance(equipos_data, dict) or 'equipos' not in equipos_data:
        print("No hay equipos registrados. Registre un equipo primero.")
        sc.pausar_pantalla()
        return
    equipos = equipos_data.get("equipos", {})
    if not equipos:
        print("No hay equipos registrados.")
        sc.pausar_pantalla()
        return
    max_partidos_perdidos = -1
    equipo_max_partidos_perdidos = None
    for equipo in equipos.values():
        if equipo.get('pp', 0) > max_partidos_perdidos:
            max_partidos_perdidos = equipo['pp']
            equipo_max_partidos_perdidos = equipo
    if equipo_max_partidos_perdidos:
        print(f"Equipo: {equipo_max_partidos_perdidos['nombre']}, Partidos Perdidos: {max_partidos_perdidos}")
    else:
        print("No se encontró ningún equipo con partidos perdidos.")
    sc.pausar_pantalla()
    