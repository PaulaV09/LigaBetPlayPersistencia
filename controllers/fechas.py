import os
import utils.corefiles as cf
import utils.screenControllers as sc
import utils.validateData as vd
import config as cfg

def programarFechas():
    sc.limpiar_pantalla()
    print("--- Programar Fechas de Torneo ---")

    torneos_data = cf.readJson(cfg.DB_TORNEOS)
    equipos_data = cf.readJson(cfg.DB_EQUIPOS)
    fechas_data = cf.readJson(cfg.DB_FECHAS)

    torneos = torneos_data.get("torneos", {})
    equipos = equipos_data.get("equipos", {})

    if not torneos:
        print("No hay torneos registrados.")
        sc.pausar_pantalla()
        return

    print("Torneos registrados:")
    for id_torneo, torneo in torneos.items():
        print(f"ID: {id_torneo} - Nombre: {torneo.get('nombre', 'N/A')}")

    id_torneo_seleccionado = vd.validate_string("\nIngrese el ID del torneo para programar fechas: ")
    if id_torneo_seleccionado not in torneos:
        print("Error: ID de torneo no válido.")
        sc.pausar_pantalla()
        return

    torneo_seleccionado = torneos[id_torneo_seleccionado]
    nombre_torneo = torneo_seleccionado.get('nombre')
    equipos_participantes_ids = torneo_seleccionado.get('equipos_participantes', [])

    if len(equipos_participantes_ids) % 2 != 0:
        print("\nError: El número de equipos en este torneo es impar. No se pueden programar partidos.")
        sc.pausar_pantalla()
        return
    
    numero_fecha = vd.validateInt("Ingrese el número de la fecha a programar (ej: 1, 2, 3...): ")
    
    key_torneo = f"torneo_{id_torneo_seleccionado}"
    key_fecha = f"fecha_{numero_fecha}"

    if key_torneo in fechas_data and key_fecha in fechas_data[key_torneo]:
        print(f"\nError: La fecha {numero_fecha} para el torneo '{nombre_torneo}' ya ha sido programada.")
        sc.pausar_pantalla()
        return

    print(f"\n--- Programando partidos para la Fecha {numero_fecha} del torneo '{nombre_torneo}' ---")
    
    equipos_disponibles = {} 
    for equipo_id in equipos_participantes_ids: 
        equipo_info = equipos.get(equipo_id, {})
        equipos_disponibles[equipo_id] = equipo_info
    partidos_programados = []
    
    num_partido = 1
    while equipos_disponibles:
        sc.limpiar_pantalla()
        print(f"--- Creando Partido {num_partido} de la Fecha {numero_fecha} ---")
        
        fecha_calendario = vd.validate_string("Ingrese la fecha del partido (DD-MM-AAAA): ")

        print("\nEquipos disponibles para este partido:")
        for id_equipo, equipo_info in equipos_disponibles.items():
            print(f"ID: {id_equipo} - Nombre: {equipo_info.get('nombre', 'N/A')}")

        while True:
            id_local = vd.validate_string("\nSeleccione el ID del equipo LOCAL: ")
            if id_local in equipos_disponibles:
                break
            print("Error: ID de equipo no válido o ya seleccionado.")
        
        equipos_disponibles.pop(id_local)

        print("\nEquipos restantes:")
        for id_equipo, equipo_info in equipos_disponibles.items():
            print(f"ID: {id_equipo} - Nombre: {equipo_info.get('nombre', 'N/A')}")

        while True:
            id_visitante = vd.validate_string("\nSeleccione el ID del equipo VISITANTE: ")
            if id_visitante in equipos_disponibles:
                break
            print("Error: ID de equipo no válido o ya seleccionado.")

        equipos_disponibles.pop(id_visitante)

        partido = {
            "id_partido": f"t{id_torneo_seleccionado}f{numero_fecha}p{num_partido}",
            "fecha_calendario": fecha_calendario,
            "equipo_local": id_local,
            "equipo_visitante": id_visitante,
            "marcador_local": None,
            "marcador_visitante": None
        }
        partidos_programados.append(partido)
        num_partido += 1
        print("\nPartido programado. Presione Enter para continuar...")
        sc.pausar_pantalla()

    if key_torneo not in fechas_data:
        fechas_data[key_torneo] = {}
    fechas_data[key_torneo][key_fecha] = {"partidos": partidos_programados}
    cf.writeJson(cfg.DB_FECHAS, fechas_data)

    print(f"\nFecha {numero_fecha} del torneo '{nombre_torneo}' programada con éxito.")
    sc.pausar_pantalla()
