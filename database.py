import sqlite3

from pathlib import Path

NOMBRE_BD = str(Path(__file__).resolve().parent / "database.db")

#Métodos de referencia para así poder modificar el main y sus funciones, sin la BBDD no podía hacer mucho TwT

def conectar():
    """Abre la conexión y crea la tabla si no existe (RF09)."""
    conexion = sqlite3.connect(NOMBRE_BD)
    conexion.execute("""
        CREATE TABLE IF NOT EXISTS juegos (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            imagen      TEXT,
            titulo      TEXT NOT NULL,
            genero      TEXT,
            plataforma  TEXT,
            anio        INTEGER,
            puntuacion  REAL CHECK (puntuacion BETWEEN 1 AND 5)
        )
    """)
    conexion.commit()
    return conexion


def initDatosPrueba():
    """Crea la BD y, si está vacía, la rellena con juegos de ejemplo."""
    conexion = conectar()
    cuantos = conexion.execute("SELECT COUNT(*) FROM juegos").fetchone()[0]

    if cuantos == 0:
        juegos_demo = [
            ("The Legend of Zelda: Ocarina of Time", "Aventuras", "GameBoy", 1998, 5, ":/images/images/The_Legend_of_Zelda_Ocarina_of_Time.png"),
            ("Metal Gear Solid", "Acción", "PSX", 1998, 5, ":/images/images/Metal_Gear_Solid.png"),
            ("Final Fantasy VII", "RPG", "PSX", 1997, 5, ":/images/images/Final_Fantasy_vii.png"),
            ("God of War Ragnarök", "Acción", "PS5", 2022, 4.5, ":/images/images/God_of_War_Ragnarok.png"),
            ("Pokémon Esmeralda", "RPG", "GameBoy", 2004, 4, ":/images/images/Pokemon_Esmeralda.png"),
            ("Luigi's Mansion 3", "Casual", "Switch 1", 2019, 4, ":/images/images/Luigis_Mansion_3.png"),
            ("Metroid Prime 4", "FPS", "Switch 2", 2025, 4, ":/images/images/Metroid_Prime_4.png"),
            ("Patapon Remastered", "Ritmo", "PSP", 2023, 3.5, ":/images/images/Patapon_Remastered.png"),
        ]
        conexion.executemany(
            "INSERT INTO juegos (titulo, genero, plataforma, anio, puntuacion, imagen) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            juegos_demo,
        )
        conexion.commit()

    return conexion


# ---------- Consultas ----------

def listar(conexion, filtro="", genero="", plataforma=""):
    """
    Devuelve TODOS los juegos que cumplan los filtros.
    Vacío en un filtro = no filtrar por él.
    """
    sql = ("SELECT id, titulo, genero, plataforma, anio, puntuacion, imagen "
           "FROM juegos WHERE 1=1")
    parametros = []

    if filtro:
        sql += " AND titulo LIKE ?"
        parametros.append(f"%{filtro}%")
    if genero:
        sql += " AND genero = ?"
        parametros.append(genero)
    if plataforma:
        sql += " AND plataforma = ?"
        parametros.append(plataforma)

    sql += " ORDER BY titulo"
    return conexion.execute(sql, parametros).fetchall()


def plataformas_existentes(conexion):
    """Lista de plataformas guardadas, para rellenar los combos."""
    filas = conexion.execute(
        "SELECT DISTINCT plataforma FROM juegos "
        "WHERE plataforma IS NOT NULL AND plataforma != '' "
        "ORDER BY plataforma"
    ).fetchall()
    return [fila[0] for fila in filas]


def generos_existentes(conexion):
    filas = conexion.execute(
        "SELECT DISTINCT genero FROM juegos "
        "WHERE genero IS NOT NULL AND genero != '' "
        "ORDER BY genero"
    ).fetchall()
    return [fila[0] for fila in filas]


# ---------- Altas / bajas / modificaciones ----------

def insertar(conexion, titulo, genero, plataforma, anio, puntuacion, imagen=None):
    conexion.execute(
        "INSERT INTO juegos (titulo, genero, plataforma, anio, puntuacion, imagen) "
        "VALUES (?, ?, ?, ?, ?, ?)",
        (titulo, genero, plataforma, anio, puntuacion, imagen),
    )
    conexion.commit()


def actualizar(conexion, id_juego, titulo, genero, plataforma, anio, puntuacion, imagen=None):
    conexion.execute(
        "UPDATE juegos SET titulo=?, genero=?, plataforma=?, anio=?, puntuacion=?, imagen=? "
        "WHERE id=?",
        (titulo, genero, plataforma, anio, puntuacion, imagen, id_juego),
    )
    conexion.commit()


def borrar(conexion, id_juego):
    conexion.execute("DELETE FROM juegos WHERE id = ?", (id_juego,))
    conexion.commit()


def obtener_por_id(conexion, id_juego):
    return conexion.execute(
        "SELECT id, titulo, genero, plataforma, anio, puntuacion, imagen "
        "FROM juegos WHERE id = ?",
        (id_juego,),
    ).fetchone()


