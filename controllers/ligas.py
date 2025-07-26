import os
import utils.corefiles as cf
import utils.screenControllers as sc
import utils.validateData as vd
import config as cfg

def registrarLiga():
    sc.limpiar_pantalla()
    print("--- Registrar Liga ---")
    ligas_data = cf.readJson(cfg.DB_LIGAS)
    if not isinstance(ligas_data, dict) or 'ligas' not in ligas_data:
        ligas_data = {"ligas": {}}

    nombre = vd.validatetext("Ingrese el nombre de la liga: ").title()
    for liga in ligas_data.get("ligas", {}).values():
        if liga.get("nombre", "").lower() == nombre.lower():
            print(f"Error: La liga '{nombre}' ya está registrada.")
            sc.pausar_pantalla()
            return
    pais = vd.validatetext("Ingrese el país de la liga: ").title()
    if not ligas_data.get("ligas"):
        id_liga = "1"
    else:
        max_id = max(int(k) for k in ligas_data["ligas"].keys())
        id_liga = str(max_id + 1)
    liga = {
        "id": id_liga,
        "nombre": nombre,
        "pais": pais,
    }

    ligas_data["ligas"][id_liga] = liga
    cf.writeJson(cfg.DB_LIGAS, ligas_data)

    print(f"\nLiga '{nombre}' registrada con éxito con el ID: {id_liga}")
    sc.pausar_pantalla

def listarLigas():
    sc.limpiar_pantalla()
    print("--- Listar Ligas ---")
    ligas_data = cf.readJson(cfg.DB_LIGAS)
    if not isinstance(ligas_data, dict) or 'ligas' not in ligas_data:
        print("No hay ligas registradas.")
        sc.pausar_pantalla()
        return
    ligas = ligas_data.get("ligas", {})
    if not ligas:
        print("No hay ligas registradas.")
        sc.pausar_pantalla()
        return
    for id_liga, liga in ligas.items():
        print('--------------------------')
        print(f"ID: {id_liga}\nNombre: {liga.get('nombre', 'N/A')}\nPaís: {liga.get('pais', 'N/A')}")
    sc.pausar_pantalla()