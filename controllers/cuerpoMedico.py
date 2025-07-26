import os
import utils.corefiles as cf
import utils.screenControllers as sc
import utils.validateData as vd
import config as cfg

def registrarCuerpoMedico():
    sc.limpiar_pantalla()
    print("--- Registrar Cuerpo Médico ---")
    cuerpo_medico_data = cf.readJson(cfg.DB_CUERPO_MEDICO)
    equipos_data = cf.readJson(cfg.DB_EQUIPOS)
    if not isinstance(cuerpo_medico_data, dict) or 'cuerpo_medico' not in cuerpo_medico_data:
        cuerpo_medico_data = {"cuerpo_medico": {}}    
    nombre = vd.validatetext("Ingrese el nombre del miembro del cuerpo médico: ").title()
    cargo = vd.validatetext("Ingrese el cargo del miembro del cuerpo médico: ").title()
    print("---------------------------")
    print("\nEquipos registrados:")
    for equipo in equipos_data.get("equipos", {}).values():
        print(f"ID: {equipo.get('id', 'N/A')} - Nombre: {equipo.get('nombre', 'N/A')}")
    
    while True:
        idEquipo = vd.validateInt("Ingrese el ID del equipo al que pertenece el miembro del cuerpo médico: ")
        if str(idEquipo) in equipos_data.get("equipos", {}):
            break
        else:
            print(f"Error: No se encontró un equipo con ID {idEquipo}.")
            sc.pausar_pantalla()
            return
        
    if not cuerpo_medico_data.get("cuerpo_médico"):
        id_cuerpo_medico = "1"
    else:
        max_id = max(int(k) for k in cuerpo_medico_data["cuerpo_medico"].keys())
        id_cuerpo_medico = str(max_id + 1)
    
    miembro = {
        "id": id_cuerpo_medico,
        "nombre": nombre,
        "cargo": cargo,
        "id_equipo": idEquipo,
    }

    cuerpo_medico_data["cuerpo_medico"][id_cuerpo_medico] = miembro
    cf.writeJson(cfg.DB_CUERPO_MEDICO, cuerpo_medico_data)

    print(f"\nEl miembro del cuerpo médico '{nombre}' registrado con éxito con el ID: {id_cuerpo_medico}")
    sc.pausar_pantalla()

def listarCuerpoMedico():
    sc.limpiar_pantalla()
    print("--- Listar Cuerpo Médico ---")
    cuerpo_medico_data = cf.readJson(cfg.DB_CUERPO_MEDICO)
    equipos_data = cf.readJson(cfg.DB_EQUIPOS)
    cuerpo_medico = cuerpo_medico_data.get("cuerpo_medico", {})
    equipos = equipos_data.get("equipos", {})

    if not cuerpo_medico:
        print("No hay miembros del cuerpo médico registrados.")
        sc.pausar_pantalla()
        return  
    for id_miembro, miembro in cuerpo_medico.items():
        id_equipo = str(miembro.get('id_equipo', ''))
        nombre_equipo = equipos.get(id_equipo, {}).get('nombre', 'Equipo no encontrado')
        print('--------------------------')
        print(f"ID: {id_miembro}\nNombre: {miembro.get('nombre', 'N/A')}\nCargo: {miembro.get('cargo', 'N/A')}\nEquipo: {nombre_equipo} (ID: {id_equipo})")
    sc.pausar_pantalla()
