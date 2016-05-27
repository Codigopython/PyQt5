# -*- coding: utf-8 -*-

import sys, re
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from firebird import *


    # Con esta forma de crear el programa me da error al tratar de implementar 
    # un QMessageBox.information(self, buttons=QMessageBox.Ok)
    # y de validar los campos usando expresiones regulares


class log(object):

    def inicio(self, main):
        main.setObjectName('main')
        main.setWindowTitle('Sinergia !!!!')
        main.setWindowModality(Qt.ApplicationModal)
        main.setWindowIcon(QIcon('img/gato.jpg'))
        main.resize(540, 339)
        main.setFixedSize(540, 339)

        tpg = QFont()
        tpg.setFamily("Georgia")
        tpg.setPointSize(18)
        tpg.setItalic(True)
        main.setFont(tpg)

        # ********************************************

        self.grilla = QWidget(main)
        self.grilla.setObjectName('grilla')
        self.hmain = QHBoxLayout(self.grilla)
        self.hmain.setObjectName('hmain')
        self.grupo = QGroupBox(self.grilla)
        self.grupo.setObjectName('grupo')
        self.grupo.setAlignment(Qt.AlignCenter)
        self.grupo.setTitle('Ingreso al sistema')
        # *******************************************

        self.lbd = QLabel(self.grupo)
        self.lbd.setGeometry(QRect(20, 40, 471, 31))
        self.lbd.setAlignment(Qt.AlignCenter)
        self.lbd.setObjectName("lbd")
        self.lbd.setText('')

        self.lbc = QLabel(self.grupo)
        self.lbc.setObjectName('lbc')
        self.lbc.setGeometry(QRect(170, 170, 171, 31))
        self.lbc.setAlignment(Qt.AlignCenter)
        self.lbc.setText('Contraseña :')

        self.txa = QLineEdit(self.grupo)
        self.txa.setGeometry(QRect(90, 120, 331, 31))
        self.txa.setObjectName("txa")
        self.txa.setPlaceholderText('Escribe aqui tu correo')

        self.lba = QLabel(self.grupo)
        self.lba.setObjectName('lba')
        self.lba.setGeometry(QRect(180, 80, 131, 31))
        self.lba.setAlignment(Qt.AlignCenter)
        self.lba.setText('Correo')

        self.txb = QLineEdit(self.grupo)
        self.txb.setGeometry(QRect(90, 210, 331, 31))
        self.txb.setObjectName("txb")
        self.txb.setPlaceholderText('Escribe aqui tu contraseña')

        self.btn = QPushButton(self.grupo)
        self.btn.setGeometry(QRect(140, 260, 231, 41))
        self.btn.setObjectName("btn")
        self.btn.setCursor(Qt.OpenHandCursor)
        self.btn.setText('Entrar')

        self.btn.clicked.connect(self.principal)
        

        self.hmain.addWidget(self.grupo)
        main.setCentralWidget(self.grilla)
# *****************************************************************************

    # def validar(self):
    #     correo = self.txa.setText('')
    #     val = re.match('[A-Za-z]+((.+|_+)([a-z]+|(\d+)))?@[A-Za-z]+.com$', correo, re.I)



    def principal(self):

        cx = con.cursor()
        cx.execute("SELECT * FROM usuarios WHERE correo = ? AND contra = ?",(self.txa.text(), self.txb.text()))
        datos = cx.fetchone()
        if datos is None:
            self.lbd.setText('Datos incorrectos o vacios')
            correo = self.txa.setText('')
            val = re.match('[A-Za-z]+((.+|_+)([a-z]+|(\d+)))?@[A-Za-z]+.com$', correo)
            self.lbd.setText('Ingresa un correo valido')
            # QMessageBox.information(self, buttons=QMessageBox.Ok)
            # print('Datos incorrectos')
        else:
            print('Bienvenido : ', datos[1], datos[2])
            main.close()
            con.commit()
            con.close()


if __name__ == '__main__':
    ap = QApplication(sys.argv)
    main = QMainWindow()
    with open('temas/estilos.qss', 'r') as e:
        estilo = e.read()
    ap.setStyleSheet(estilo)
    an = log()
    an.inicio(main)
    main.show()
    sys.exit(ap.exec_())
