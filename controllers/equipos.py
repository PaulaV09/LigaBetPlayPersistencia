import os
import utils.corefiles as cf
import utils.screenControllers as sc
import utils.validateData as vd
import config as cfg

def registrarEquipo():
    sc.limpiar_pantalla()
    print("--- Registrar Equipo ---")
    equipos_data = cf.readJson(cfg.DB_EQUIPOS)
    ligas_data = cf.readJson(cfg.DB_LIGAS)
    if not isinstance(ligas_data, dict) or 'ligas' not in ligas_data:
        print("No hay ligas registradas. Registre una liga primero.")
        sc.pausar_pantalla()
        return
    if not isinstance(equipos_data, dict) or 'equipos' not in equipos_data:
        equipos_data = {"equipos": {}}

    nombre = vd.validatetext("Ingrese el nombre del equipo: ").title()

    for equipo in equipos_data.get("equipos", {}).values():
        if equipo.get("nombre", "").lower() == nombre.lower():
            print(f"Error: El equipo '{nombre}' ya está registrado.")
            sc.pausar_pantalla()
            return

    fecha = vd.validate_string("Ingrese la fecha de fundación del equipo (DD-MM-AAAA): ")
    pais = vd.validatetext("Ingrese el país del equipo: ").title()
    for liga in ligas_data.get("ligas", {}).values():
        print('--------------------------')
        print(f"ID: {liga.get('id', 'N/A')} - Nombre: {liga.get('nombre', 'N/A')}")
    
    while True:
        idLiga = vd.validateInt("Ingrese el ID de la liga a la que pertenece el equipo: ")
        if str(idLiga) in ligas_data.get("ligas", {}):
            break
        else:
            print(f"Error: No se encontró una liga con ID {idLiga}.")
            sc.pausar_pantalla()
            return

    if not equipos_data.get("equipos"):
        id_equipo = "1"
    else:
        max_id = max(int(k) for k in equipos_data["equipos"].keys())
        id_equipo = str(max_id + 1)
    equipo = {
        "id": id_equipo,
        "nombre": nombre,
        "fecha_fundacion": fecha,
        "pais": pais,
        "id_liga": idLiga,
        "pj": 0,
        "pg": 0,
        "pe": 0,
        "pp": 0,
        "gf": 0,
        "gc": 0,
        "pt": 0
    }

    equipos_data["equipos"][id_equipo] = equipo
    cf.writeJson(cfg.DB_EQUIPOS, equipos_data)

    print(f"\nEquipo '{nombre}' registrado con éxito con el ID: {id_equipo}")
    sc.pausar_pantalla()

def listarEquipos():
    sc.limpiar_pantalla()
    print("--- Listar Equipos ---")
    equipos_data = cf.readJson(cfg.DB_EQUIPOS)
    if not isinstance(equipos_data, dict) or 'equipos' not in equipos_data:
        print("No hay equipos registrados.")
        sc.pausar_pantalla()
        return
    equipos = equipos_data.get("equipos", {})
    if not equipos:
        print("No hay equipos registrados.")
        sc.pausar_pantalla()
        return
    for id_equipo, equipo in equipos.items():
        print('--------------------------')
        print(f"ID: {id_equipo}\nNombre: {equipo.get('nombre', 'N/A')}\nFecha de Fundación: {equipo.get('fecha_fundacion', 'N/A')}\nPaís: {equipo.get('pais', 'N/A')}\nLiga ID: {equipo.get('id_liga', 'N/A')}")
    sc.pausar_pantalla()