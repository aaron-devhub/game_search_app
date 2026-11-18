# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(935, 581)
        icon = QIcon()
        icon.addFile(u":/icons/icons/gamedex.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.actionExportar = QAction(MainWindow)
        self.actionExportar.setObjectName(u"actionExportar")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentSave))
        self.actionExportar.setIcon(icon1)
        self.actionExportar.setIconVisibleInMenu(True)
        self.actionLight = QAction(MainWindow)
        self.actionLight.setObjectName(u"actionLight")
        self.actionAnadir = QAction(MainWindow)
        self.actionAnadir.setObjectName(u"actionAnadir")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.actionAnadir.setIcon(icon2)
        self.actionAnadir.setIconVisibleInMenu(True)
        self.actionDark = QAction(MainWindow)
        self.actionDark.setObjectName(u"actionDark")
        self.actionEliminar = QAction(MainWindow)
        self.actionEliminar.setObjectName(u"actionEliminar")
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditDelete))
        self.actionEliminar.setIcon(icon3)
        self.actionEliminar.setIconVisibleInMenu(True)
        self.actionEditar = QAction(MainWindow)
        self.actionEditar.setObjectName(u"actionEditar")
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditSelectAll))
        self.actionEditar.setIcon(icon4)
        self.actionEditar.setIconVisibleInMenu(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.busqueda = QLineEdit(self.centralwidget)
        self.busqueda.setObjectName(u"busqueda")
        self.busqueda.setToolTipDuration(-1)

        self.horizontalLayout_3.addWidget(self.busqueda)

        self.btnCrear = QPushButton(self.centralwidget)
        self.btnCrear.setObjectName(u"btnCrear")

        self.horizontalLayout_3.addWidget(self.btnCrear)

        self.espacio = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.espacio)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lblPlatFiltro = QLabel(self.centralwidget)
        self.lblPlatFiltro.setObjectName(u"lblPlatFiltro")

        self.horizontalLayout.addWidget(self.lblPlatFiltro)

        self.comboPlat = QComboBox(self.centralwidget)
        self.comboPlat.setObjectName(u"comboPlat")
        self.comboPlat.setEditable(True)

        self.horizontalLayout.addWidget(self.comboPlat)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lblGenFiltro = QLabel(self.centralwidget)
        self.lblGenFiltro.setObjectName(u"lblGenFiltro")

        self.horizontalLayout_2.addWidget(self.lblGenFiltro)

        self.comboGen = QComboBox(self.centralwidget)
        self.comboGen.setObjectName(u"comboGen")
        self.comboGen.setEditable(True)

        self.horizontalLayout_2.addWidget(self.comboGen)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.limpiaFiltro = QPushButton(self.centralwidget)
        self.limpiaFiltro.setObjectName(u"limpiaFiltro")
        icon5 = QIcon(QIcon.fromTheme(u"edit-clear"))
        self.limpiaFiltro.setIcon(icon5)

        self.verticalLayout_3.addWidget(self.limpiaFiltro)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 913, 445))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 935, 22))
        self.menuDatos = QMenu(self.menuBar)
        self.menuDatos.setObjectName(u"menuDatos")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuDatos.menuAction())
        self.menuDatos.addAction(self.actionExportar)
        self.menuDatos.addAction(self.actionAnadir)
        self.menuDatos.addAction(self.actionEliminar)
        self.menuDatos.addAction(self.actionEditar)

        self.retranslateUi(MainWindow)

        self.comboGen.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"GameDex", None))
        self.actionExportar.setText(QCoreApplication.translate("MainWindow", u"Exportar Datos", None))
        self.actionLight.setText(QCoreApplication.translate("MainWindow", u"Modo claro", None))
        self.actionAnadir.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir Juegos", None))
        self.actionDark.setText(QCoreApplication.translate("MainWindow", u"Modo oscuro", None))
        self.actionEliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar Juego", None))
        self.actionEditar.setText(QCoreApplication.translate("MainWindow", u"Editar Juego", None))
#if QT_CONFIG(tooltip)
        self.busqueda.setToolTip(QCoreApplication.translate("MainWindow", u"Buscar videojuegos", None))
#endif // QT_CONFIG(tooltip)
        self.busqueda.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar...", None))
        self.btnCrear.setText(QCoreApplication.translate("MainWindow", u"Crear", None))
        self.lblPlatFiltro.setText(QCoreApplication.translate("MainWindow", u"Plataforma:", None))
#if QT_CONFIG(tooltip)
        self.comboPlat.setToolTip(QCoreApplication.translate("MainWindow", u"Filtrar por plataforma", None))
#endif // QT_CONFIG(tooltip)
        self.comboPlat.setCurrentText("")
        self.comboPlat.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Plataforma", None))
        self.lblGenFiltro.setText(QCoreApplication.translate("MainWindow", u"G\u00e9nero:", None))
#if QT_CONFIG(tooltip)
        self.comboGen.setToolTip(QCoreApplication.translate("MainWindow", u"Filtrar por g\u00e9nero", None))
#endif // QT_CONFIG(tooltip)
        self.comboGen.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Genero", None))
        self.limpiaFiltro.setText(QCoreApplication.translate("MainWindow", u"Limpiar Filtro", None))
        self.menuDatos.setTitle(QCoreApplication.translate("MainWindow", u"Datos", None))
    # retranslateUi

