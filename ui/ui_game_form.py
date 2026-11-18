# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'game_form.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDateEdit, QDialog,
    QDialogButtonBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpinBox, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_vistaJuego(object):
    def setupUi(self, vistaJuego):
        if not vistaJuego.objectName():
            vistaJuego.setObjectName(u"vistaJuego")
        vistaJuego.resize(330, 267)
        icon = QIcon()
        icon.addFile(u":/icons/icons/gamedex.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        vistaJuego.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(vistaJuego)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lblTitulo = QLabel(vistaJuego)
        self.lblTitulo.setObjectName(u"lblTitulo")

        self.horizontalLayout_6.addWidget(self.lblTitulo)

        self.txtTitulo = QLineEdit(vistaJuego)
        self.txtTitulo.setObjectName(u"txtTitulo")

        self.horizontalLayout_6.addWidget(self.txtTitulo)


        self.verticalLayout_7.addLayout(self.horizontalLayout_6)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lblImagen = QLabel(vistaJuego)
        self.lblImagen.setObjectName(u"lblImagen")

        self.horizontalLayout.addWidget(self.lblImagen)

        self.btnImagen = QPushButton(vistaJuego)
        self.btnImagen.setObjectName(u"btnImagen")

        self.horizontalLayout.addWidget(self.btnImagen)


        self.verticalLayout_7.addLayout(self.horizontalLayout)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lblAnio = QLabel(vistaJuego)
        self.lblAnio.setObjectName(u"lblAnio")

        self.horizontalLayout_7.addWidget(self.lblAnio)

        self.datAnio = QDateEdit(vistaJuego)
        self.datAnio.setObjectName(u"datAnio")

        self.horizontalLayout_7.addWidget(self.datAnio)


        self.verticalLayout_7.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lblGen = QLabel(vistaJuego)
        self.lblGen.setObjectName(u"lblGen")
        self.lblGen.setLocale(QLocale(QLocale.Spanish, QLocale.Spain))

        self.horizontalLayout_8.addWidget(self.lblGen)

        self.txtGen = QLineEdit(vistaJuego)
        self.txtGen.setObjectName(u"txtGen")

        self.horizontalLayout_8.addWidget(self.txtGen)


        self.verticalLayout_7.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lblPlat = QLabel(vistaJuego)
        self.lblPlat.setObjectName(u"lblPlat")

        self.horizontalLayout_10.addWidget(self.lblPlat)

        self.txtPlat = QLineEdit(vistaJuego)
        self.txtPlat.setObjectName(u"txtPlat")

        self.horizontalLayout_10.addWidget(self.txtPlat)


        self.verticalLayout_7.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lblPunt = QLabel(vistaJuego)
        self.lblPunt.setObjectName(u"lblPunt")

        self.horizontalLayout_9.addWidget(self.lblPunt)

        self.spinPunt = QSpinBox(vistaJuego)
        self.spinPunt.setObjectName(u"spinPunt")
        self.spinPunt.setMinimum(1)
        self.spinPunt.setMaximum(5)
        self.spinPunt.setValue(1)

        self.horizontalLayout_9.addWidget(self.spinPunt)


        self.verticalLayout_7.addLayout(self.horizontalLayout_9)


        self.verticalLayout.addLayout(self.verticalLayout_7)

        self.botones = QDialogButtonBox(vistaJuego)
        self.botones.setObjectName(u"botones")
        self.botones.setLocale(QLocale(QLocale.Spanish, QLocale.Spain))
        self.botones.setOrientation(Qt.Orientation.Horizontal)
        self.botones.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Save)
        self.botones.setCenterButtons(False)

        self.verticalLayout.addWidget(self.botones)


        self.retranslateUi(vistaJuego)
        self.botones.accepted.connect(vistaJuego.accept)
        self.botones.rejected.connect(vistaJuego.reject)

        QMetaObject.connectSlotsByName(vistaJuego)
    # setupUi

    def retranslateUi(self, vistaJuego):
        vistaJuego.setWindowTitle(QCoreApplication.translate("vistaJuego", u"GameInfo", None))
        self.lblTitulo.setText(QCoreApplication.translate("vistaJuego", u"Titulo:", None))
        self.txtTitulo.setPlaceholderText(QCoreApplication.translate("vistaJuego", u"Escribir aqu\u00ed...", None))
        self.lblImagen.setText(QCoreApplication.translate("vistaJuego", u"Ninguna imagen seleccionada", None))
        self.btnImagen.setText(QCoreApplication.translate("vistaJuego", u"Seleccionar imagen", None))
        self.lblAnio.setText(QCoreApplication.translate("vistaJuego", u"A\u00f1o:", None))
        self.datAnio.setDisplayFormat(QCoreApplication.translate("vistaJuego", u"yyyy", None))
        self.lblGen.setText(QCoreApplication.translate("vistaJuego", u"G\u00e9nero:", None))
        self.txtGen.setPlaceholderText(QCoreApplication.translate("vistaJuego", u"Ej. Acci\u00f3n", None))
        self.lblPlat.setText(QCoreApplication.translate("vistaJuego", u"Plataforma:", None))
        self.txtPlat.setPlaceholderText(QCoreApplication.translate("vistaJuego", u"Ej. PSX", None))
        self.lblPunt.setText(QCoreApplication.translate("vistaJuego", u"Puntuaci\u00f3n:", None))
        self.spinPunt.setSuffix(QCoreApplication.translate("vistaJuego", u"\u2605", None))
    # retranslateUi

