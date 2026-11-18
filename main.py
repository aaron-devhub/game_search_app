import shutil
import sys
import uuid
import hashlib
import database

from pathlib import Path
from PySide6.QtCore import QDate, Qt, QFile, QSettings
from PySide6.QtGui import QIcon, QPixmap, QActionGroup, QPainter, QColor
from PySide6.QtWidgets import (QApplication, QDialog, QDialogButtonBox, QFileDialog, QMainWindow, QMessageBox)
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent / "resources"))
from ui.ui_main_window import Ui_MainWindow
from ui.ui_game_form import Ui_vistaJuego
from components.game_card import GameCard, ruta_imagen

BASE_DIR = Path(__file__).resolve().parent
CARPETA_IMAGENES = BASE_DIR / "resources" / "images"
CARPETA_ESTILOS = BASE_DIR / "resources" / "styles"
CARPETA_ICONOS = BASE_DIR / "resources" / "icons"
COLOR_ICONOS = {"dark": "#e8e8ea", "light": "#1b1c20"}

def icono_tintado(icono, color, tam=32):
    pix = icono.pixmap(tam, tam)
    if pix.isNull():
        return icono
    pintor = QPainter(pix)
    pintor.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceIn)
    pintor.fillRect(pix.rect(), QColor(color))
    pintor.end()
    return QIcon(pix)

def aplicar_tema(nombre):
    ruta = CARPETA_ESTILOS / f"{nombre}.qss"
    try:
        css = ruta.read_text(encoding="utf-8")
    except OSError:
        QMessageBox.warning(None, "Tema no disponible",
                            f"No se pudo cargar el archivo de estilos «{ruta.name}».")
        return
    css = css.replace("@ICONOS@", CARPETA_ICONOS.as_posix())
    QApplication.instance().setStyleSheet(css)

def huella_imagen(ruta):
    ruta = ruta_imagen(ruta)
    if ruta.startswith(":"):
        archivo = QFile(ruta)
        if not archivo.open(QFile.OpenModeFlag.ReadOnly):
            return None
        datos = bytes(archivo.readAll())
        archivo.close()
    else:
        try:
            datos = Path(ruta).read_bytes()
        except OSError:
            return None
    return hashlib.sha1(datos).hexdigest()

def copiar_imagen(ruta):
    """Copia la foto elegida a ./images y devuelve la ruta relativa para la BD."""
    if not ruta:
        return None
    origen = Path(ruta)
    if not origen.is_absolute():  
        return ruta
    CARPETA_IMAGENES.mkdir(exist_ok=True)
    destino = CARPETA_IMAGENES / f"{uuid.uuid4().hex}{origen.suffix.lower()}"
    shutil.copy(origen, destino)
    return f"resources/images/{destino.name}"

#Dialogo
class DialogoJuego(QDialog):
    def __init__(self, parent=None, datos=None, titulo_inicial=""):
        super().__init__(parent)
        self.ui = Ui_vistaJuego()
        self.ui.setupUi(self)
        for rol, nombre in ((QDialogButtonBox.StandardButton.Save, "btnGuardar"),
                            (QDialogButtonBox.StandardButton.Cancel, "btnCancelar")):
            boton = self.ui.botones.button(rol)
            boton.setObjectName(nombre)
            boton.style().unpolish(boton)
            boton.style().polish(boton)
        self.imagen = None
        self.id_juego = None
        self.ui.btnImagen.clicked.connect(self.elegir_imagen)
        
        if titulo_inicial:                      
            self.ui.txtTitulo.setText(titulo_inicial)

        if datos:  # rellenamos los campos con lo que había en la BBDD
            self.id_juego = datos[0] 
            _, titulo, genero, plataforma, anio, puntuacion, imagen = datos
            self.ui.txtTitulo.setText(titulo)
            self.ui.txtGen.setText(genero or "") #Permite nulos
            self.ui.txtPlat.setText(plataforma or "")
            if anio:
                self.ui.datAnio.setDate(QDate(anio, 1, 1))
            self.ui.spinPunt.setValue(int(puntuacion or 1))
            self.imagen = imagen
            self.mostrar_imagen()

    def elegir_imagen(self):
        ruta, _ = QFileDialog.getOpenFileName(
            self, "Seleccionar imagen", "",
            "Imágenes (*.png *.jpg *.jpeg *.webp *.bmp)")
        if not ruta:
            return
        usada_por = self.parent().juego_con_imagen(ruta, self.id_juego)
        if usada_por:
            QMessageBox.warning(self, "Imagen repetida", f"Esa imagen ya la usa «{usada_por}». Elige otra.")
            return
        self.imagen = ruta
        self.mostrar_imagen()

    def mostrar_imagen(self):
        pix = QPixmap(str(BASE_DIR / self.imagen)) if self.imagen else QPixmap()
        if pix.isNull():
            self.ui.lblImagen.setText("Ninguna imagen seleccionada")
        else:
            self.ui.lblImagen.setPixmap(
                pix.scaled(80, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def obtener_datos(self): #Devuelve los datos de la BBDD, si existen o se ponen Defaults
        return (
            self.ui.txtTitulo.text().strip(),
            self.ui.txtGen.text().strip(),
            self.ui.txtPlat.text().strip(),
            self.ui.datAnio.date().year(),
            self.ui.spinPunt.value(),
            self.imagen,
        )
        
# Ventana principal
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Descomentar según se necesite
        # Base de datos (con datos de prueba, solo para debugging)
        self.bd = database.initDatosPrueba()
        # Cargar BBDD sin datos de prueba
        #self.bd = database.conectar()
        self.id_editando = None   # id del juego a editar, si lo hay

        # Conexiones slots
        self.ui.busqueda.textChanged.connect(self.refrescar)
        self.ui.comboPlat.activated.connect(self.refrescar)
        self.ui.comboGen.activated.connect(self.refrescar)
        self.ui.limpiaFiltro.clicked.connect(self.limpiar_filtros)

        self.ui.btnCrear.clicked.connect(self.anadir)
        self.ui.actionAnadir.triggered.connect(self.anadir)
        self.ui.actionEditar.triggered.connect(self.editar_sin_seleccion)
        self.ui.actionEliminar.triggered.connect(self.eliminar_sin_seleccion)
        self.ui.actionExportar.triggered.connect(self.exportar)

        # ---- Tema claro / oscuro ----
        menu_ver = self.ui.menuBar.addMenu("Ver")
        menu_ver.addAction(self.ui.actionLight)
        menu_ver.addAction(self.ui.actionDark)

        grupo_tema = QActionGroup(self)
        grupo_tema.setExclusive(True)
        for accion in (self.ui.actionLight, self.ui.actionDark):
            accion.setCheckable(True)
            grupo_tema.addAction(accion)

        self.ui.actionLight.triggered.connect(lambda: self.cambiar_tema("light"))
        self.ui.actionDark.triggered.connect(lambda: self.cambiar_tema("dark"))

        tema = QSettings("GameDex", "GameDex").value("tema", "light")
        (self.ui.actionDark if tema == "dark" else self.ui.actionLight).setChecked(True)

        # Guardamos los iconos originales para poder recolorearlos en cada tema
        self.iconos_base = [(w, w.icon()) for w in (
            self.ui.actionExportar, self.ui.actionAnadir,
            self.ui.actionEliminar, self.ui.actionEditar,
            self.ui.limpiaFiltro)]
        self.aplicar_tema_completo(tema)

        self.rellenar_combos()
        self.refrescar()

    # ---------------------- Game Cards ----------------------
    # Así no hay problema de nuevas consolas o géneros
    def rellenar_combos(self):
        """Las opciones de los filtros salen de la propia BD."""
        self.ui.comboPlat.clear()
        self.ui.comboPlat.addItem("")   # vacío = sin filtro
        for nombre in database.plataformas_existentes(self.bd):
            self.ui.comboPlat.addItem(nombre)
        self.ui.comboPlat.setCurrentIndex(-1) # Inicializa en ninguno, para que así no aparezcan filtros al iniciar

        self.ui.comboGen.clear()
        self.ui.comboGen.addItem("")
        for nombre in database.generos_existentes(self.bd):
            self.ui.comboGen.addItem(nombre)
        self.ui.comboGen.setCurrentIndex(-1)

    def refrescar(self):
        """Redibuja todas las tarjetas."""
        filtro = self.ui.busqueda.text()
        genero = self.ui.comboGen.currentText()
        plataforma = self.ui.comboPlat.currentText()

        juegos = database.listar(self.bd, filtro, genero, plataforma)

        # Limpiar las tarjetas anteriores
        while self.ui.gridLayout.count():
            item = self.ui.gridLayout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        # Una tarjeta por juego, 3 por fila
        for indice, juego in enumerate(juegos):
            tarjeta = GameCard(*juego)
            tarjeta.editar.connect(self.editar)
            tarjeta.eliminar.connect(self.confirmar_borrado)
            self.ui.gridLayout.addWidget(tarjeta, indice // 3, indice % 3)

    def limpiar_filtros(self):
        self.ui.busqueda.clear()
        self.ui.comboPlat.setCurrentIndex(-1)
        self.ui.comboGen.setCurrentIndex(-1)
        self.refrescar()

    # ---------------------- Cambiar tema ----------------------------
    
    def aplicar_tema_completo(self, nombre):
        aplicar_tema(nombre)                       
        color = COLOR_ICONOS[nombre]
        for destino, original in self.iconos_base:  
            destino.setIcon(icono_tintado(original, color))

    def cambiar_tema(self, nombre):
        self.aplicar_tema_completo(nombre)
        QSettings("GameDex", "GameDex").setValue("tema", nombre)

    # ---------------------- imágenes repetidas ----------------------

    def juego_con_imagen(self, ruta, id_excluir=None):
        """Devuelve el título del OTRO juego que ya usa esa imagen, o None."""
        huella = huella_imagen(ruta)
        if huella is None:
            return None
        for id_, titulo, *_, imagen in database.listar(self.bd):
            if id_ == id_excluir or not imagen:
                continue
            if huella_imagen(imagen) == huella:
                return titulo
        return None

    # ---------------------- añadir y/o editar ----------------------

    def anadir(self):
        dialogo = DialogoJuego(self, titulo_inicial=self.ui.busqueda.text().strip())
        if dialogo.exec() == QDialog.Accepted:
            titulo, genero, plataforma, anio, puntuacion, imagen = dialogo.obtener_datos()
            if not titulo:   # validación RF11
                QMessageBox.warning(self, "¡Faltan campos!", "El título es obligatorio.")
                return
            database.insertar(self.bd, titulo, genero, plataforma, anio, puntuacion, copiar_imagen(imagen))
            self.rellenar_combos()   # puede haber nueva plataforma/género
            self.refrescar()

    def editar(self, id_juego):
        datos = database.obtener_por_id(self.bd, id_juego)
        if not datos:
            return
        dialogo = DialogoJuego(self, datos)
        if dialogo.exec() == QDialog.Accepted:
            titulo, genero, plataforma, anio, puntuacion, imagen = dialogo.obtener_datos()
            if not titulo:
                QMessageBox.warning(self, "¡Faltan Campos!", "El título es obligatorio.")
                return
            database.actualizar(self.bd, id_juego, titulo, genero, plataforma, anio, puntuacion, copiar_imagen(imagen))
            self.rellenar_combos()
            self.refrescar()

    def editar_sin_seleccion(self):
        QMessageBox.information(self, "Info - Editar juego",
                                "Pulsa el botón 'Editar' de la tarjeta del juego que quieras modificar.")

    # ---------------------- borrado ----------------------

    def confirmar_borrado(self, id_juego):
        datos = database.obtener_por_id(self.bd, id_juego)
        titulo = datos[1] if datos else "este juego"
        respuesta = QMessageBox.question(
            self, "Confirmar borrado",
            f"¿Seguro que quieres eliminar {titulo}?",
        )
        if respuesta == QMessageBox.Yes:
            database.borrar(self.bd, id_juego)
            self.rellenar_combos()
            self.refrescar()

    def eliminar_sin_seleccion(self):
        QMessageBox.information(self, "Info - Eliminar juego",
                                "Pulsa el botón 'Borrar' de la tarjeta del juego que quieras eliminar.")

    # ---------------------- exportar ----------------------
    def exportar(self):
        import csv
        from datetime import datetime
        fcha = datetime.now().strftime("%d%m%Y-%H%M%S")     #Tener la fecha evita duplicados :D
        archivo = f"GameDexExport{fcha}.csv"
        with open(f"{archivo}", "w", newline="", encoding="utf-8") as fichero:
            escritor = csv.writer(fichero)
            escritor.writerow(["id", "titulo", "genero", "plataforma", "anio", "puntuacion", "imagen"])
            escritor.writerows(database.listar(self.bd))
        QMessageBox.information(self, "Exportación completada", f"Colección exportada a {archivo}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    ventana = MainWindow()
    ventana.show()
    sys.exit(app.exec())
