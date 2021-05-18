# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets #gerekli modülleri içe aktardık

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(410, 202) # resize ile penceremizin boyutu belirlediğimiz boyutta kalacak herhangi bir değişiklik yapılamayacak
        self.comboBox = QtWidgets.QComboBox(Form) # combobox oluşturduk
        self.comboBox.setGeometry(QtCore.QRect(120, 70, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(320, 70, 69, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(Form)
        self.comboBox_3.setGeometry(QtCore.QRect(20, 70, 69, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_4 = QtWidgets.QComboBox(Form)
        self.comboBox_4.setGeometry(QtCore.QRect(220, 70, 69, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 40, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(120, 40, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(220, 40, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(320, 40, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.comboBox.setItemText(0, _translate("Form", "Kalın"))
        self.comboBox.setItemText(1, _translate("Form", "İtalik"))
        self.comboBox.setItemText(2, _translate("Form", "Normal"))
        self.comboBox_2.setItemText(0, _translate("Form", "Kırmızı"))
        self.comboBox_2.setItemText(1, _translate("Form", "Mavi"))
        self.comboBox_2.setItemText(2, _translate("Form", "Yeşil"))
        self.comboBox_2.setItemText(3, _translate("Form", "Sarı"))
        self.comboBox_2.setItemText(4, _translate("Form", "Beyaz"))
        self.comboBox_2.setItemText(5, _translate("Form", "Mor"))
        self.comboBox_3.setItemText(0, _translate("Form", "Arial"))
        self.comboBox_3.setItemText(1, _translate("Form", "Black"))
        self.comboBox_3.setItemText(2, _translate("Form", "New Item"))
        self.comboBox_3.setItemText(3, _translate("Form", "New Item"))
        self.comboBox_4.setItemText(0, _translate("Form", "9"))
        self.comboBox_4.setItemText(1, _translate("Form", "10"))
        self.comboBox_4.setItemText(2, _translate("Form", "11"))
        self.comboBox_4.setItemText(3, _translate("Form", "12"))
        self.comboBox_4.setItemText(4, _translate("Form", "13"))
        self.label.setText(_translate("Form", "Yazı Tipi:"))
        self.label_2.setText(_translate("Form", "Yazı Tipi Stili:"))
        self.label_3.setText(_translate("Form", "Yazı Boyutu:"))
        self.label_4.setText(_translate("Form", "Yazı Rengi:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

