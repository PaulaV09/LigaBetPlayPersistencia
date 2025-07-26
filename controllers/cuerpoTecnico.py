import os
import utils.corefiles as cf
import utils.screenControllers as sc
import utils.validateData as vd
import config as cfg

def registrarCuerpoTecnico():
    sc.limpiar_pantalla()
    print("--- Registrar Cuerpo Técnico ---")
    cuerpo_tecnico_data = cf.readJson(cfg.DB_CUERPO_MEDICO)
    equipos_data = cf.readJson(cfg.DB_EQUIPOS)
    if not isinstance(cuerpo_tecnico_data, dict) or 'cuerpo_tecnico' not in cuerpo_tecnico_data:
        cuerpo_tecnico_data = {"cuerpo_tecnico": {}}    
    nombre = vd.validatetext("Ingrese el nombre del miembro del cuerpo técnico: ").title()
    cargo = vd.validatetext("Ingrese el cargo del miembro del cuerpo técnico: ").title()
    print("---------------------------")
    print("\nEquipos registrados:")
    for equipo in equipos_data.get("equipos", {}).values():
        print(f"ID: {equipo.get('id', 'N/A')} - Nombre: {equipo.get('nombre', 'N/A')}")
    
    while True:
        idEquipo = vd.validateInt("Ingrese el ID del equipo al que pertenece el miembro del cuerpo técnico: ")
        if str(idEquipo) in equipos_data.get("equipos", {}):
            break
        else:
            print(f"Error: No se encontró un equipo con ID {idEquipo}.")
            sc.pausar_pantalla()
            return
        
    if not cuerpo_tecnico_data.get("cuerpo_tecnico"):
        id_cuerpo_tecnico = "1"
    else:
        max_id = max(int(k) for k in cuerpo_tecnico_data["cuerpo_tecnico"].keys())
        id_cuerpo_tecnico = str(max_id + 1)
    
    miembro = {
        "id": id_cuerpo_tecnico,
        "nombre": nombre,
        "cargo": cargo,
        "id_equipo": idEquipo,
    }

    cuerpo_tecnico_data["cuerpo_tecnico"][id_cuerpo_tecnico] = miembro
    cf.writeJson(cfg.DB_CUERPO_MEDICO, cuerpo_tecnico_data)

    print(f"\nEl miembro del cuerpo técnico '{nombre}' registrado con éxito con el ID: {id_cuerpo_tecnico}")
    sc.pausar_pantalla()

def listarCuerpoTecnico():
    sc.limpiar_pantalla()
    print("--- Listar Cuerpo Técnico ---")
    cuerpo_tecnico_data = cf.readJson(cfg.DB_CUERPO_MEDICO)
    equipos_data = cf.readJson(cfg.DB_EQUIPOS)
    cuerpo_tecnico = cuerpo_tecnico_data.get("cuerpo_tecnico", {})
    equipos = equipos_data.get("equipos", {})

    if not cuerpo_tecnico:
        print("No hay miembros del cuerpo técnico registrados.")
        sc.pausar_pantalla()
        return  
    for id_miembro, miembro in cuerpo_tecnico.items():
        id_equipo = str(miembro.get('id_equipo', ''))
        nombre_equipo = equipos.get(id_equipo, {}).get('nombre', 'Equipo no encontrado')
        print('--------------------------')
        print(f"ID: {id_miembro}\nNombre: {miembro.get('nombre', 'N/A')}\nCargo: {miembro.get('cargo', 'N/A')}\nEquipo: {nombre_equipo} (ID: {id_equipo})")
    sc.pausar_pantalla()
