import os
import utils.corefiles as cf
import utils.screenControllers as sc
import utils.validateData as vd
import config as cfg

def registrarTorneo():
    sc.limpiar_pantalla()
    print("--- Registrar Torneo ---")

    torneos_data = cf.readJson(cfg.DB_TORNEOS)
    equipos_data = cf.readJson(cfg.DB_EQUIPOS)
    ligas_data = cf.readJson(cfg.DB_LIGAS)

    equipos = equipos_data.get("equipos", {})
    ligas = ligas_data.get("ligas", {})

    if not equipos:
        print("No hay equipos registrados. Registre un equipo primero.")
        sc.pausar_pantalla()
        return

    if not isinstance(torneos_data, dict) or 'torneos' not in torneos_data:
        torneos_data = {"torneos": {}}

    nombre = vd.validatetext("Ingrese el nombre del torneo: ").title()
    for torneo in torneos_data.get("torneos", {}).values():
        if torneo.get("nombre", "").lower() == nombre.lower():
            print(f"Error: El torneo '{nombre}' ya está registrado.")
            sc.pausar_pantalla()
            return

    fecha_inicio = vd.validate_string("Ingrese la fecha de inicio del torneo (DD-MM-AAAA): ")
    fecha_fin = vd.validate_string("Ingrese la fecha de fin del torneo (DD-MM-AAAA): ")
    isInternacional = vd.validateBoolean("¿El torneo es internacional? (S/N): ")

    equipos_participantes = []
    id_liga_torneo = None

    if isInternacional:
        print("\n--- Selección de equipos para Torneo Internacional ---")
        equipos_disponibles = equipos.copy()
    else:
        print("\n--- Selección de Liga para Torneo Nacional ---")
        if not ligas:
            print("No hay ligas registradas. Registre una liga primero.")
            sc.pausar_pantalla()
            return

        for id_liga, liga in ligas.items():
            print(f"ID: {id_liga} - Nombre: {liga.get('nombre', 'N/A')}")

        while True:
            id_liga_input = vd.validate_string("Ingrese el ID de la liga del torneo: ")
            if id_liga_input in ligas:
                id_liga_torneo = int(id_liga_input)
                break
            else:
                print(f"Error: No se encontró una liga con ID {id_liga_input}.")

        equipos_disponibles = {} 
        for id_equipo, equipo in equipos.items(): 
            if str(equipo.get("id_liga")) == str(id_liga_torneo):
                equipos_disponibles[id_equipo] = equipo
                if not equipos_disponibles:
                    print(f"No hay equipos registrados en la liga seleccionada.")
                    sc.pausar_pantalla()
                    return

    print("\n--- Seleccione los equipos participantes ---")
    while True:
        if not equipos_disponibles:
            print("No hay más equipos disponibles para seleccionar.")
            break

        print("Equipos disponibles:")
        for id_equipo, equipo in equipos_disponibles.items():
            print(f"ID: {id_equipo} - Nombre: {equipo.get('nombre', 'N/A')} - País: {equipo.get('pais', 'N/A')}")

        id_equipo_input = vd.validate_string("\nIngrese el ID del equipo a añadir (o escriba 'fin' para terminar): ").lower()

        if id_equipo_input == 'fin':
            break

        if id_equipo_input in equipos_disponibles:
            equipos_participantes.append(id_equipo_input)
            equipo_seleccionado = equipos_disponibles.pop(id_equipo_input)
            print(f"Equipo '{equipo_seleccionado.get('nombre')}' añadido al torneo.")
        else:
            print("Error: ID de equipo no válido o ya seleccionado.")

        sc.pausar_pantalla()
        sc.limpiar_pantalla()

    if not equipos_participantes:
        print("No se seleccionó ningún equipo. Operación cancelada.")
        sc.pausar_pantalla()
        return


    if not torneos_data.get("torneos"):
        id_torneo = "1"
    else:
        max_id = max(int(k) for k in torneos_data["torneos"].keys())
        id_torneo = str(max_id + 1)

    torneo = {
        "id": id_torneo,
        "nombre": nombre,
        "fecha_inicio": fecha_inicio,
        "fecha_fin": fecha_fin,
        "isInternacional": isInternacional,
        "id_liga": id_liga_torneo,
        "equipos_participantes": equipos_participantes
    }

    torneos_data["torneos"][id_torneo] = torneo
    cf.writeJson(cfg.DB_TORNEOS, torneos_data)

    print(f"\nTorneo '{nombre}' registrado con éxito con el ID: {id_torneo}")
    print(f"Equipos participantes: {len(equipos_participantes)}")
    sc.pausar_pantalla()

def listarTorneos():
    sc.limpiar_pantalla()
    print("--- Listar Torneos ---")
    torneos_data = cf.readJson(cfg.DB_TORNEOS)
    equipos_data = cf.readJson(cfg.DB_EQUIPOS)
    ligas_data = cf.readJson(cfg.DB_LIGAS)

    torneos = torneos_data.get("torneos", {})
    equipos = equipos_data.get("equipos", {})
    ligas = ligas_data.get("ligas", {})

    if not torneos:
        print("No hay torneos registrados.")
        sc.pausar_pantalla()
        return

    for id_torneo, torneo in torneos.items():
        print('---------------------------------')
        print(f"ID: {id_torneo} - Nombre: {torneo.get('nombre', 'N/A')}")
        print(f"Fechas: {torneo.get('fecha_inicio', 'N/A')} a {torneo.get('fecha_fin', 'N/A')}")

        if torneo.get('isInternacional'):
            print("Tipo: Internacional")
        else:
            id_liga = str(torneo.get('id_liga', ''))
            nombre_liga = ligas.get(id_liga, {}).get('nombre', 'Liga no encontrada')
            print(f"Tipo: Nacional (Liga: {nombre_liga})")

        print("Equipos Participantes:")
        equipos_participantes_ids = torneo.get('equipos_participantes', [])
        if not equipos_participantes_ids:
            print("  - Ninguno")
        else:
            for id_equipo in equipos_participantes_ids:
                nombre_equipo = equipos.get(str(id_equipo), {}).get('nombre', 'Equipo no encontrado')
                print(f"  - {nombre_equipo} (ID: {id_equipo})")

    sc.pausar_pantalla()