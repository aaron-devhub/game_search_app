from pathlib import Path

from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QLabel, QPushButton, QVBoxLayout)

BASE_DIR = Path(__file__).resolve().parent.parent   # carpeta del proyecto (gamedex)


def ruta_imagen(ruta):
    if ruta.startswith(":"):
        return ruta
    return str(BASE_DIR / ruta)


class GameCard(QFrame):
    """
    Tarjeta de un videojuego para el catálogo.

    Recibe los datos por parámetro y avisa a main.py mediante señales
    cuando el usuario quiere editar o eliminar ese juego concreto.
    """

    # Señales personalizadas: llevan el id del juego clicado
    editar = Signal(int)
    eliminar = Signal(int)

    def __init__(self, id_juego, titulo, genero, plataforma, anio, puntuacion, imagen=None):
        super().__init__()

        self.id_juego = id_juego

        # Aspecto de tarjeta (funciona con el modo claro/oscuro por QSS)
        self.setObjectName("tarjetaJuego")

        # Columnas: portada, texto, botones
        fila_principal = QVBoxLayout(self)
        fila_principal.setContentsMargins(10, 10, 10, 10)
        fila_principal.setSpacing(4)

        linea_titulo = QHBoxLayout()

        # Portada
        portada = QLabel()
        portada.setObjectName("portadaCard")
        portada.setFixedSize(80, 100)
        portada.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pix = QPixmap(ruta_imagen(imagen)) if imagen else QPixmap()
        if pix.isNull():
            portada.setText("🎮")   # sin foto, o no se encuentra el archivo
        else:
            portada.setPixmap(pix.scaled(
                80, 100,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation))

        texto = QVBoxLayout()
        texto.addWidget(self._etiqueta(titulo, "tituloCard"))
        texto.addWidget(self._etiqueta(
            f"{genero or '-'} - {plataforma or '-'} - {anio or '-'}",
            "detalleCard"))
        texto.addWidget(self._etiqueta(self._estrellas(puntuacion), "puntosCard"))

        boton_editar = QPushButton("Editar")
        boton_editar.setObjectName("btnEditarCard")
        boton_editar.setToolTip("Editar este juego")

        boton_borrar = QPushButton("Borrar")
        boton_borrar.setObjectName("btnBorrarCard")
        boton_borrar.setToolTip("Eliminar este juego")

        boton_editar.clicked.connect(lambda: self.editar.emit(self.id_juego))
        boton_borrar.clicked.connect(lambda: self.eliminar.emit(self.id_juego))

        linea_titulo.addWidget(portada)      # <- nuevo, a la izquierda del texto
        linea_titulo.addLayout(texto)
        linea_titulo.addStretch()   # empuja los botones a la derecha que si no queda raro
        linea_titulo.addWidget(boton_editar)
        linea_titulo.addWidget(boton_borrar)

        fila_principal.addLayout(linea_titulo)

    # ---------- helpers internos ----------

    def _etiqueta(self, texto, nombre):
        etiqueta = QLabel(texto)
        etiqueta.setObjectName(nombre)
        etiqueta.setWordWrap(True)
        return etiqueta

    @staticmethod
    def _estrellas(puntuacion):
        if puntuacion is None:
            return "-"
        return "★" * int(puntuacion) + "☆" * (5 - int(puntuacion)) #Las estrellas solo muestran enteros
