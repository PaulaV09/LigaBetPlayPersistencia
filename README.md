# 🏆 Proyecto: **Gestión de Torneos Internacionales de Fútbol (Python + JSON)**

------

## 📘 **Descripción General**

Este proyecto es una aplicación de consola desarrollada en Python para la gestión integral de torneos de fútbol. Permite administrar ligas, equipos, jugadores y personal, así como llevar un registro detallado de los torneos, desde la programación de partidos hasta la actualización automática de estadísticas. Toda la información se almacena de forma persistente en archivos JSON.

## 📂 **Estructura del Proyecto**

La estructura del proyecto es la siguiente: 

```
LigaBetPlayPersistencia/
│
├── app/						
│   └── mainmenu.py 			# Menú principal del programa (7 opciones de menú)
│	└── submenus.py 			# Submenús de cada opción del menú principal
│
├── controllers/                # Lógica funcional por módulo
│   ├── cuerpoMedico.py 		# Registro y listado de cuerpo médico
│   ├── cuerpoTecnico.py 		# Registro y listado de cuerpo técnico
│   ├── equipos.py 				# Registro y listado de equipos
│   ├── estadisticas.py 		# Ver tabla general y estadísticas de equipos
│   ├── fechas.py 				# Programar fecha y partidos de la fecha
│   ├── jugadores.py 			# Registro y listado de jugadores
│   ├── ligas.py              	# Registro y listado de ligas
│   ├── marcadores.py           # Registro de marcadores de partidos
│   ├── torneos.py       		# Registro y listado de torneos
│   └── transferencias.py       # Transferencias de jugadores (venta/préstamo)
│
├── utils/
│   └── corefiles.py         	# Funciones comunes de lectura/escritura JSON
│   └── screenControllers.py	# Funciones de control de pantalla (limpiar/pausar)
│   └── validateData.py			# Funciones para validar el tipo de input
│
├── data/                       # Archivos JSON persistentes
│   ├── equipos.json
│   ├── jugadores.json
│   ├── ligas.json
│   ├── torneos.json
│   ├── fechas.json
│   ├── marcadores.json
│   ├── estadisticas.json
│   ├── cuerpoTecnico.json
│   ├── cuerpoMedico.json
│   └── transferencias.json
│								
├── main.py						# Punto de entrada del programa
├── config.py					# Archivo de configuración con las rutas de JSON
├── .gitignore					# Archivo para evitar que se suba al repo las carpetas __pycache__
│
└── README.md                   # Documentación del proyecto
```

## 🚀 Funcionalidades Principales

El sistema está organizado en módulos que cubren todas las áreas de la gestión de una liga:

### 1. Gestión de Entidades

- **Ligas:** Registrar y listar las diferentes ligas, cada una asociada a un país.
- **Equipos:** Crear equipos, asignarlos a una liga y registrar sus estadísticas iniciales (Partidos Jugados, Ganados, Puntos, etc.).
- **Jugadores:** Registrar jugadores, asignarlos a un equipo y validar que no se repitan dorsales en un mismo club.
- **Personal (Cuerpo Técnico y Médico):** Registrar miembros del cuerpo técnico y médico, asociándolos a su equipo correspondiente.

### 2. Gestión de Competición

- **Torneos:** Crear torneos que pueden ser **nacionales** (vinculados a una liga específica) o **internacionales** (abiertos a equipos de cualquier país). El sistema permite seleccionar los equipos participantes de una lista dinámica.
- **Programación de Fechas:** Para un torneo existente, se pueden programar las fechas de los partidos. El sistema valida que haya un número par de equipos y permite emparejarlos hasta que todos tengan un partido asignado para esa fecha.
- **Registro de Marcadores:** Ingresar los resultados de los partidos jugados. Esta acción es clave, ya que actualiza automáticamente los siguientes datos:
  - El marcador en el archivo `fechas.json`.
  - Las estadísticas de ambos equipos en `equipos.json` (PJ, PG, PE, PP, GF, GC y Puntos).
  - Un historial de marcadores en `marcadores.json`.

### 3. Transferencias y Préstamos

- **Movimiento de Jugadores:** Transferir un jugador de un equipo a otro o registrar un préstamo.
- **Historial de Transferencias:** Cada movimiento se guarda en `transferencias.json`, registrando el tipo de operación (transferencia o préstamo), las fechas y, en caso de préstamo, si incluye opción de compra.

### 4. Estadísticas y Reportes

- **Tabla General de Posiciones:** Muestra una tabla con las estadísticas completas de todos los equipos.
- **Reportes de Rendimiento:** Genera reportes para identificar rápidamente
  - Equipo con más goles a favor.
  - Equipo con más goles en contra.
  - Equipo con más puntos.
  - Equipos con más partidos ganados, empatados o perdidos.

## 🛠️ Tecnologías Utilizadas

- **Lenguaje:** Python 3
- **Manejo de Datos:** Módulo `json` para la serialización y deserialización de datos.
- **Sistema de Archivos:** Módulo `os` para la gestión de rutas y la limpieza de la consola.
- **Manejo de Rutas:** Módulo `sys` para la configuración del `path` del proyecto, permitiendo una estructura de módulos organizada y escalable.

## ⚙️ Cómo se Ejecuta

No se requiere la instalación de ninguna librería externa, solo tener Python 3 instalado en tu sistema.

1. Clona o descarga el repositorio en tu máquina local.

2. Abre una terminal o línea de comandos.

3. Navega hasta la carpeta raíz del proyecto (`LigaBetPlayPersistencia`).

4. Ejecuta el punto de entrada de la aplicación con el siguiente comando:

   ```python
   python main.py
   ```

5. El programa se iniciará y podrás interactuar con él a través de los menús en la consola.