import os
import utils.corefiles as cf
import utils.screenControllers as sc
import utils.validateData as vd
import config as cfg

def registrarMarcador():
    sc.limpiar_pantalla()
    print("--- Registrar Marcador ---")
    fechas_data = cf.readJson(cfg.DB_FECHAS)
    equipos_data = cf.readJson(cfg.DB_EQUIPOS)
    torneos_data = cf.readJson(cfg.DB_TORNEOS)
    marcadores_data = cf.readJson(cfg.DB_MARCADORES)
    equipos = equipos_data.get("equipos", {})
    torneos = torneos_data.get("torneos", {})

    if not isinstance(marcadores_data, dict) or 'marcadores' not in marcadores_data:
        marcadores_data = {"marcadores": {}}

    if not fechas_data:
        print("No hay fechas programadas en ningún torneo.")
        sc.pausar_pantalla()
        return

    print("\nTorneos con fechas programadas:")
    torneos_disponibles_mostrados = [] 
    contador_torneos = 1
    for id_torneo_key in fechas_data.keys():
        id_torneo_solo = id_torneo_key.split('_')[1]
        nombre_torneo = torneos.get(id_torneo_solo, {}).get('nombre', 'Nombre no encontrado')
        print(f"{contador_torneos}. {nombre_torneo} (ID Interno: {id_torneo_key})")
        torneos_disponibles_mostrados.append(id_torneo_key) 
        contador_torneos += 1

    opcion_torneo_str = vd.validate_string("Ingrese el número del torneo para registrar un marcador: ")
    opcion_torneo_int = 0
    try:
        opcion_torneo_int = int(opcion_torneo_str)
    except ValueError:
        print("Error: Ingrese un número válido para el torneo.")
        sc.pausar_pantalla()
        return

    if 1 <= opcion_torneo_int <= len(torneos_disponibles_mostrados):
        key_torneo = torneos_disponibles_mostrados[opcion_torneo_int - 1]
        id_torneo_seleccionado = key_torneo.split('_')[1]
    else:
        print("Error: Opción de torneo no válida.")
        sc.pausar_pantalla()
        return

    print("\nFechas disponibles en este torneo:")
    fechas_del_torneo = fechas_data[key_torneo]
    fechas_disponibles_mostradas = [] 
    contador_fechas = 1
    for key_fecha in fechas_del_torneo.keys():
        numero_fecha = key_fecha.split('_')[1]
        print(f"{contador_fechas}. Fecha Nro: {numero_fecha} (ID Interno: {key_fecha})")
        fechas_disponibles_mostradas.append(key_fecha)
        contador_fechas += 1

    opcion_fecha_str = vd.validate_string("Ingrese el número de la fecha para registrar un marcador: ")
    opcion_fecha_int = 0
    try:
        opcion_fecha_int = int(opcion_fecha_str)
    except ValueError:
        print("Error: Ingrese un número válido para la fecha.")
        sc.pausar_pantalla()
        return

    if 1 <= opcion_fecha_int <= len(fechas_disponibles_mostradas):
        key_fecha = fechas_disponibles_mostradas[opcion_fecha_int - 1]
        numero_fecha_seleccionada = key_fecha.split('_')[1] 
    else:
        print("Error: Opción de fecha no válida.")
        sc.pausar_pantalla()
        return

    partidos_de_la_fecha = fechas_data[key_torneo][key_fecha].get("partidos", [])

    partidos_pendientes = []
    for p in partidos_de_la_fecha:
        if p.get("marcador_local") is None:
            partidos_pendientes.append(p)

    if not partidos_pendientes:
        print("Todos los partidos de esta fecha ya tienen un marcador registrado.")
        sc.pausar_pantalla()
        return

    print("\nPartidos pendientes de esta fecha:")
    partidos_disponibles_mostrados = []
    contador_partidos = 1
    for partido in partidos_pendientes:
        id_local = partido.get("equipo_local")
        id_visitante = partido.get("equipo_visitante")
        nombre_local = equipos.get(id_local, {}).get("nombre", "N/A")
        nombre_visitante = equipos.get(id_visitante, {}).get("nombre", "N/A")
        print(f"{contador_partidos}. {nombre_local} vs {nombre_visitante} (ID Interno: {partido.get('id_partido')})")
        partidos_disponibles_mostrados.append(partido) 
        contador_partidos += 1

    opcion_partido_str = vd.validate_string("Ingrese el número del partido para registrar el marcador: ")
    opcion_partido_int = 0
    try:
        opcion_partido_int = int(opcion_partido_str)
    except ValueError:
        print("Error: Ingrese un número válido para el partido.")
        sc.pausar_pantalla()
        return

    if 1 <= opcion_partido_int <= len(partidos_disponibles_mostrados):
        partido_seleccionado = partidos_disponibles_mostrados[opcion_partido_int - 1]
        id_partido_seleccionado = partido_seleccionado.get('id_partido', '')
    else:
        print("Error: Opción de partido no válida.")
        sc.pausar_pantalla()
        return
    id_local = partido_seleccionado["equipo_local"]
    id_visitante = partido_seleccionado["equipo_visitante"]
    nombre_local = equipos.get(id_local, {}).get("nombre", "N/A")
    nombre_visitante = equipos.get(id_visitante, {}).get("nombre", "N/A")

    print(f"\nRegistrando marcador para: {nombre_local} vs {nombre_visitante}")
    goles_local = vd.validateInt("Ingrese el número de goles del equipo local: ")
    goles_visitante = vd.validateInt("Ingrese el número de goles del equipo visitante: ")

    partido_seleccionado["marcador_local"] = goles_local
    partido_seleccionado["marcador_visitante"] = goles_visitante

    for equipo_id in [id_local, id_visitante]:
        if equipo_id in equipos:
            if "pj" not in equipos[equipo_id]: equipos[equipo_id]["pj"] = 0
            if "pg" not in equipos[equipo_id]: equipos[equipo_id]["pg"] = 0
            if "pe" not in equipos[equipo_id]: equipos[equipo_id]["pe"] = 0
            if "pp" not in equipos[equipo_id]: equipos[equipo_id]["pp"] = 0
            if "gf" not in equipos[equipo_id]: equipos[equipo_id]["gf"] = 0
            if "gc" not in equipos[equipo_id]: equipos[equipo_id]["gc"] = 0
            if "pt" not in equipos[equipo_id]: equipos[equipo_id]["pt"] = 0

    equipos[id_local]["pj"] += 1
    equipos[id_visitante]["pj"] += 1
    equipos[id_local]["gf"] += goles_local
    equipos[id_visitante]["gf"] += goles_visitante
    equipos[id_local]["gc"] += goles_visitante
    equipos[id_visitante]["gc"] += goles_local

    if goles_local > goles_visitante:
        equipos[id_local]["pg"] += 1
        equipos[id_visitante]["pp"] += 1
        equipos[id_local]["pt"] += 3
        equipos[id_visitante]["pt"] += 0
    elif goles_local < goles_visitante:
        equipos[id_visitante]["pg"] += 1
        equipos[id_local]["pp"] += 1
        equipos[id_visitante]["pt"] += 3
        equipos[id_local]["pt"] += 0
    else:
        equipos[id_local]["pe"] += 1
        equipos[id_visitante]["pe"] += 1
        equipos[id_local]["pt"] += 1
        equipos[id_visitante]["pt"] += 1

    if "marcadores" not in marcadores_data:
        marcadores_data["marcadores"] = {}
    
    marcadores_data["marcadores"][id_partido_seleccionado] = {
        "id_partido": id_partido_seleccionado,
        "goles_local": goles_local,
        "goles_visitante": goles_visitante
    }
    cf.writeJson(cfg.DB_FECHAS, fechas_data)
    cf.writeJson(cfg.DB_EQUIPOS, equipos_data)
    cf.writeJson(cfg.DB_MARCADORES, marcadores_data)

    print(f"\nMarcador registrado con éxito para el partido {id_partido_seleccionado}.")
    sc.pausar_pantalla()