# GameDex

Gestión de biblioteca de videojuegos · Diseño de Interfaces · 2.º DAM

## 1. Equipo

Integrantes: Lizbeth y Aarón

## 2. Descripción

GameDex es una aplicación de escritorio para catalogar y gestionar una biblioteca personal de videojuegos. Se Muestra la colección de videojuegos en formato de tarjetas visuales, que permite buscar y filtrar en tiempo real, y ofrece alta, edición y borrado de juegos con imagen personalizada. Los datos se guardan en una base de datos SQLite local que la propia aplicación crea al arrancar.

**Tecnologías:** Python 3.10+, PySide6 (Qt6), Qt Designer, hojas de estilo QSS y SQLite 3.

## 3. Requisitos e instalación

- Python 3.10 o superior.
- Dependencias declaradas en `requirements.txt` (PySide6 ≥ 6.7).

Se recomienda usar un entorno virtual:

```bash
python -m venv .venv
# Windows:        .venv\Scripts\activate
# Linux / macOS:  source .venv/bin/activate
pip install -r requirements.txt
```

## 4. Ejecución

Desde la carpeta raíz del proyecto:

```bash
python main.py
```

No se necesita ninguna configuración adicional ni rutas absolutas: el fichero `database.db` se crea junto a `database.py` si no existe (RF09) y los datos se cargan al iniciar la interfaz (RF10).

**Datos de prueba.** En `MainWindow.__init__` (`main.py`) hay dos líneas alternativas: `database.initDatosPrueba()` rellena una BD vacía con 8 juegos de ejemplo con sus carátulas; `database.conectar()` arranca con la BD vacía. Se deja comentada la que no se use.

## 5. Funcionalidades

| Código | Requisito | Cómo se cubre |
|---|---|---|
| RF01 | Ventana principal | `MainWindow` con barra de menú «Datos», buscador, filtros y área con scroll. |
| RF02 | Catálogo | Tarjetas `GameCard` en cuadrícula de 3 columnas. |
| RF03 | Búsqueda en tiempo real | El campo de búsqueda filtra por título en cada pulsación (`textChanged`). |
| RF04 | Filtros | Combos de plataforma y género rellenados con los valores existentes en la BD; botón «Limpiar Filtro». |
| RF05 | Añadir juego | Botón «Crear» o menú Datos → Añadir Juegos; abre el formulario modal. |
| RF06 | Editar juego | Botón «Editar» de cada tarjeta; el formulario se precarga con los datos. |
| RF07 / RF08 | Eliminar con confirmación | Botón «Borrar» de la tarjeta y diálogo modal de confirmación. |
| RF09 / RF10 | BD automática y carga inicial | `CREATE TABLE IF NOT EXISTS` al conectar; el listado se carga al iniciar. |
| RF11 | Validación | Título obligatorio; puntuación limitada a 1–5 (`QSpinBox` y `CHECK` en SQLite); año con `QDateEdit`. |
| RF12 | Mensajes | Avisos de campos faltantes, imagen repetida, borrado y exportación completada. |

**Funcionalidades opcionales implementadas**

- **Modo claro / oscuro:** Menú Ver → Modo claro / Modo oscuro. Cada tema es una hoja de estilo QSS (resources/styles/light.qss y dark.qss) que se aplica a toda la aplicación, incluidos los diálogos y mensajes. Los iconos del menú y del botón «Limpiar Filtro» se recolorean según el tema. La elección se recuerda entre sesiones (QSettings).
- **Gestión de carátulas:** Se puede adjuntar una imagen (PNG, JPG, JPEG, WEBP, BMP). Se copia a `resources/images/` con un nombre único y se guarda su ruta relativa en la BD.
- **Detección de carátulas duplicadas:** Se compara el contenido (hash SHA-1) y se avisa si otro juego ya usa la misma imagen.
- **Exportación de datos:** Menú Datos → Exportar Datos genera `GameDexExportDDMMAAAA-HHMMSS.csv` con toda la colección, en la carpeta desde la que se ejecuta la aplicación.

## 6. Estructura del proyecto

```
GameDex/
├── main.py               # Punto de entrada: MainWindow, DialogoJuego y gestión de temas
├── database.py           # Conexión y consultas a SQLite (CRUD, filtros)
├── requirements.txt      # Dependencias de Python
├── README.md             # Esta documentación
├── database.db           # Se genera automáticamente al ejecutar
│
├── ui/
│   ├── main_window.ui    # Diseño de la ventana principal (Qt Designer)
│   ├── game_form.ui      # Diseño del formulario de alta/edición
│   ├── ui_main_window.py # Generado con pyside6-uic
│   └── ui_game_form.py   # Generado con pyside6-uic
│
├── components/
│   └── game_card.py      # Componente propio GameCard (hereda de QFrame)
│
└── resources/
    ├── resources.qrc     # Recursos de Qt (iconos e imágenes de ejemplo)
    ├── resources_rc.py   # Generado con pyside6-rcc
    ├── images/           # Carátulas (de ejemplo y las añadidas por el usuario)
    ├── icons/            # Icono de la aplicación y flechas SVG de cada tema
    └── styles/
        ├── light.qss     # Tema claro
        └── dark.qss      # Tema oscuro

```

## 7. Arquitectura

- **Diseño (`ui/`):** Las ventanas se diseñan en Qt Designer y se convierten a Python con `pyside6-uic`. La lógica nunca se escribe en los archivos generados.
- **Lógica (`main.py`):** `MainWindow` conecta señales y refresca el catálogo; `DialogoJuego` gestiona el formulario modal.
- **Componente reutilizable (`components/game_card.py`):** `GameCard` hereda de `QFrame`, muestra carátula, título, género · plataforma · año y puntuación en estrellas, y emite las señales `editar(id)` y `eliminar(id)`. Se instancia dinámicamente por cada juego.
- **Persistencia (`database.py`):** Tabla `juegos` con id, imagen, título (obligatorio), género, plataforma, año y puntuación (1–5). Todas las consultas usan parámetros (`?`).
- **Temas (resources/styles/):** Los widgets propios exponen objectName (tarjetaJuego, tituloCard, btnEditarCard…) para que el QSS pueda estilarlos sin tocar el código del componente. Los .qss usan el marcador @ICONOS@, que aplicar_tema() sustituye en tiempo de ejecución por la ruta de resources/icons/ calculada a partir de la ubicación de main.py, de modo que no hay rutas absolutas.

**Rutas relativas.** Las carátulas de ejemplo se cargan desde el sistema de recursos de Qt (`:/images/…`) y las añadidas por el usuario se guardan como `resources/images/<id>.ext` y se resuelven respecto a la carpeta del proyecto, de modo que funciona en cualquier equipo.

## 8. Regenerar archivos de Qt Designer y recursos

Solo es necesario si se modifican los `.ui` o el `.qrc`. Desde la raíz del proyecto:

```bash
pyside6-uic ui/main_window.ui -o ui/ui_main_window.py
pyside6-uic ui/game_form.ui -o ui/ui_game_form.py
pyside6-rcc resources/resources.qrc -o resources/resources_rc.py
```

Para editar las interfaces, abrir los .ui con pyside6-designer (incluido con PySide6). Los archivos .qss se cargan al ejecutar, por lo que no requieren recompilar nada

## 9. Usabilidad y accesibilidad

- Diseño con layouts (VBox, HBox, Grid) y área con scroll: los elementos se adaptan al redimensionar la ventana.
- Colores con contraste alto en ambos temas; la información de error o éxito va siempre en texto dentro de diálogos, sin depender solo del color. Los botones «Guardar» y «Cancelar» se distinguen por color y por texto.
- Borde resaltado en el control que tiene el foco del teclado.
- Tooltips en el buscador, los filtros y los botones de cada tarjeta.
- Acciones duplicadas en menú y botones; confirmación explícita antes de borrar.

## 10. Limitaciones conocidas

- Las estrellas de la tarjeta muestran solo la parte entera de la puntuación.
- Los iconos del menú «Datos» proceden del tema de iconos del sistema; en equipos sin tema de iconos pueden no mostrarse