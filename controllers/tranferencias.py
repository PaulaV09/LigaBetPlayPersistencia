import os
import controllers.equipos as ec
import datetime
import controllers.jugadores as jc
import utils.corefiles as cf
import utils.screenControllers as sc
import utils.validateData as vd
import config as cfg

def transferirJugador():
    sc.limpiar_pantalla()
    print("--- Transferencia de Jugador ---")

    jugadores_data = cf.readJson(cfg.DB_JUGADORES)
    equipos_data = cf.readJson(cfg.DB_EQUIPOS)
    transferencias_data = cf.readJson(cfg.DB_TRANFERENCIAS)
    jugadores = jugadores_data.get("jugadores", {})
    equipos = equipos_data.get("equipos", {})

    if not isinstance(transferencias_data, dict) or 'transferencias' not in transferencias_data:
        transferencias_data = {"transferencias": {}}

    if not jugadores:
        print("No hay jugadores registrados.")
        sc.pausar_pantalla()
        return

    print("Jugadores registrados:")
    for id_jugador, jugador_info in jugadores.items():
        id_equipo = str(jugador_info.get('id_equipo', ''))
        nombre_equipo = equipos.get(id_equipo, {}).get('nombre', 'Equipo no encontrado')
        print('--------------------------')
        print(f"ID: {id_jugador}\nNombre: {jugador_info.get('nombre', 'N/A')}\nEquipo: {nombre_equipo} (ID: {id_equipo})")

    idJugador_str = vd.validate_string("Ingrese el ID del jugador a transferir: ")
    jugador = jugadores.get(idJugador_str)
    if not jugador:
        print(f"Error: No se encontró un jugador con ID {idJugador_str}.")
        sc.pausar_pantalla()
        return
    print("Equipos registrados:")
    for id_equipo, equipo in equipos.items():
        print('--------------------------')
        print(f"ID: {id_equipo}\nNombre: {equipo.get('nombre', 'N/A')}")

    nuevoEquipoId_str = vd.validate_string("Ingrese el ID del nuevo equipo: ")
    if nuevoEquipoId_str not in equipos:
        print(f"Error: No se encontró un equipo con ID {nuevoEquipoId_str}.")
        sc.pausar_pantalla()
        return
    
    if nuevoEquipoId_str == str(jugador.get('id_equipo')):
        print("Error: El jugador ya pertenece a este equipo.")
        sc.pausar_pantalla()
        return

    while True:
        tipo_operacion_input = vd.validateInt("¿Desea transferir o dar a prestamo? (1: Transferir, 2: Préstamo): ")
        if tipo_operacion_input in [1, 2]:
            break
        print("Opción no válida. Debe ser 1 o 2.")

    tipo_operacion_str = "transferir" if tipo_operacion_input == 1 else "dar a préstamo"
    while True:
        confirmacion = vd.validateInt(f"¿Está seguro de que desea {tipo_operacion_str} al jugador? (1: Sí, 2: No): ")
        if confirmacion in [1, 2]:
            break
        print("Opción no válida. Debe ser 1 o 2.")

    if confirmacion == 2:
        print("Operación cancelada.")
        sc.pausar_pantalla()
        return

    id_equipo_anterior = jugador.get('id_equipo')
    nombre_equipo_anterior = equipos.get(str(id_equipo_anterior), {}).get('nombre', 'Desconocido')
    nombre_equipo_nuevo = equipos.get(nuevoEquipoId_str, {}).get('nombre', 'Desconocido')

    historial_entry = {
        "id_jugador": idJugador_str,
        "nombre_jugador": jugador.get('nombre'),
        "id_equipo_anterior": str(id_equipo_anterior),
        "nombre_equipo_anterior": nombre_equipo_anterior,
        "id_equipo_nuevo": nuevoEquipoId_str,
        "nombre_equipo_nuevo": nombre_equipo_nuevo,
    }

    if tipo_operacion_input == 1: 
        historial_entry["tipo"] = "Transferencia"
        historial_entry["fecha_transferencia"] = datetime.date.today().strftime("%d-%m-%Y")
        jugador["isPrestamo"] = False
        mensaje_exito = f"Jugador '{jugador['nombre']}' transferido a '{nombre_equipo_nuevo}' exitosamente."
    else: 
        fecha_inicio = vd.validate_string("Ingrese la fecha de inicio del préstamo (DD-MM-AAAA): ")
        fecha_fin = vd.validate_string("Ingrese la fecha de fin del préstamo (DD-MM-AAAA): ")
        while True:
            opcion_compra_input = vd.validateInt("¿El préstamo incluye opción de compra? (1: Sí, 2: No): ")
            if opcion_compra_input in [1, 2]:
                break
            print("Opción no válida. Debe ser 1 o 2.")
        historial_entry["tipo"] = "Préstamo"
        historial_entry["fecha_inicio_prestamo"] = fecha_inicio
        historial_entry["fecha_fin_prestamo"] = fecha_fin
        historial_entry["opcion_compra"] = True if opcion_compra_input == 1 else False
        jugador["isPrestamo"] = True
        mensaje_exito = f"Jugador '{jugador['nombre']}' dado a préstamo a '{nombre_equipo_nuevo}' exitosamente."

    jugador["id_equipo"] = int(nuevoEquipoId_str)

    max_id = max([int(k) for k in transferencias_data.get("transferencias", {}).keys()] or [0])
    id_transfer = str(max_id + 1)
    transferencias_data["transferencias"][id_transfer] = historial_entry
    cf.writeJson(cfg.DB_JUGADORES, jugadores_data)
    cf.writeJson(cfg.DB_TRANFERENCIAS, transferencias_data)

    print(mensaje_exito)
    sc.pausar_pantalla()
    