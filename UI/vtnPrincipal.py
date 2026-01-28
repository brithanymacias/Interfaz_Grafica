# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vtnPrincipal.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QMainWindow,
                               QMenuBar, QPushButton, QSizePolicy, QStatusBar,
                               QTextEdit, QWidget, QLineEdit)

class Ui_vtnPrincipal(object):
    def setupUi(self, vtnPrincipal):
        if not vtnPrincipal.objectName():
            vtnPrincipal.setObjectName(u"vtnPrincipal")
        vtnPrincipal.resize(441, 515)
        self.centralwidget = QWidget(vtnPrincipal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lblNombre = QLabel(self.centralwidget)
        self.lblNombre.setObjectName(u"lblNombre")
        self.lblNombre.setGeometry(QRect(36, 70, 81, 20))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.lblNombre.setFont(font)
        self.lblApellido = QLabel(self.centralwidget)
        self.lblApellido.setObjectName(u"lblApellido")
        self.lblApellido.setGeometry(QRect(30, 140, 91, 20))
        self.lblApellido.setFont(font)
        self.txtNombre = QLineEdit(self.centralwidget)
        self.txtNombre.setObjectName(u"txtNombre")
        self.txtNombre.setGeometry(QRect(132, 70, 241, 20))
        self.txtNombre.setMaxLength(20)
        self.txtApellido = QLineEdit(self.centralwidget)
        self.txtApellido.setObjectName(u"txtApellido")
        self.txtApellido.setGeometry(QRect(130, 140, 241, 20))
        self.txtApellido.setMaxLength(20)
        self.btnGuardar = QPushButton(self.centralwidget)
        self.btnGuardar.setObjectName(u"btnGuardar")
        self.btnGuardar.setGeometry(QRect(90, 410, 81, 31))
        self.lblCedula = QLabel(self.centralwidget)
        self.lblCedula.setObjectName(u"lblCedula")
        self.lblCedula.setGeometry(QRect(30, 200, 91, 21))
        self.lblCedula.setFont(font)
        self.txtCedula = QLineEdit(self.centralwidget)
        self.txtCedula.setObjectName(u"txtCedula")
        self.txtCedula.setGeometry(QRect(130, 200, 141, 21))
        self.txtCedula.setMaxLength(10)
        self.btnLimpiar = QPushButton(self.centralwidget)
        self.btnLimpiar.setObjectName(u"btnLimpiar")
        self.btnLimpiar.setGeometry(QRect(240, 410, 91, 31))
        self.lblSexo = QLabel(self.centralwidget)
        self.lblSexo.setObjectName(u"lblSexo")
        self.lblSexo.setGeometry(QRect(30, 330, 91, 20))
        self.lblSexo.setFont(font)
        self.CbSexo = QComboBox(self.centralwidget)
        self.CbSexo.addItem("")
        self.CbSexo.addItem("")
        self.CbSexo.addItem("")
        self.CbSexo.addItem("")
        self.CbSexo.setObjectName(u"CbSexo")
        self.CbSexo.setGeometry(QRect(130, 330, 131, 31))
        self.lblEmail = QLabel(self.centralwidget)
        self.lblEmail.setObjectName(u"lblEmail")
        self.lblEmail.setGeometry(QRect(30, 270, 91, 20))
        self.lblEmail.setFont(font)
        self.txtEmail = QLineEdit(self.centralwidget)
        self.txtEmail.setObjectName(u"txtEmail")
        self.txtEmail.setGeometry(QRect(130, 270, 241, 21))
        self.txtEmail.setMaxLength(40)
        vtnPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(vtnPrincipal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 441, 21))
        vtnPrincipal.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(vtnPrincipal)
        self.statusbar.setObjectName(u"statusbar")
        vtnPrincipal.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.txtNombre, self.txtApellido)
        QWidget.setTabOrder(self.txtApellido, self.txtCedula)
        QWidget.setTabOrder(self.txtCedula, self.txtEmail)
        QWidget.setTabOrder(self.txtEmail, self.CbSexo)
        QWidget.setTabOrder(self.CbSexo, self.btnGuardar)
        QWidget.setTabOrder(self.btnGuardar, self.btnLimpiar)

        self.retranslateUi(vtnPrincipal)

        QMetaObject.connectSlotsByName(vtnPrincipal)
    # setupUi

    def retranslateUi(self, vtnPrincipal):
        vtnPrincipal.setWindowTitle(QCoreApplication.translate("vtnPrincipal", u"MainWindow", None))
        self.lblNombre.setText(QCoreApplication.translate("vtnPrincipal", u"Nombre:", None))
        self.lblApellido.setText(QCoreApplication.translate("vtnPrincipal", u"Apellido:", None))
        self.btnGuardar.setText(QCoreApplication.translate("vtnPrincipal", u"Guardar", None))
        self.lblCedula.setText(QCoreApplication.translate("vtnPrincipal", u"C\u00e9dula:", None))
        self.btnLimpiar.setText(QCoreApplication.translate("vtnPrincipal", u"Limpiar", None))
        self.lblSexo.setText(QCoreApplication.translate("vtnPrincipal", u"Sexo:", None))
        self.CbSexo.setItemText(0, QCoreApplication.translate("vtnPrincipal", u"Seleccionar", None))
        self.CbSexo.setItemText(1, QCoreApplication.translate("vtnPrincipal", u"Masculino", None))
        self.CbSexo.setItemText(2, QCoreApplication.translate("vtnPrincipal", u"Femenino", None))
        self.CbSexo.setItemText(3, QCoreApplication.translate("vtnPrincipal", u"Prefiero no decirlo", None))

        self.lblEmail.setText(QCoreApplication.translate("vtnPrincipal", u"E-mail:", None))
    # retranslateUi

