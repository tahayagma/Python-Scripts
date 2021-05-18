from PyQt5 import QtWidgets,QtGui,QtCore
import sys
import time
import os
# NOT: KESİNLİKLE TÜRKÇE KARAKTER KULLANMAYIN HER NE KADAR PYTHON 3 UYUMLU DESELERDE.  :)


class AnaPencere(object):

    def pencere(self,small):
        small.setWindowTitle("BASİC CALCULATOR") # penceremizin başlığını ayarladık
        small.setFixedSize(480,300) # pencere boyutunu ayarladık setFixedsize ile değişiklik yapılmasını engelledik
        small.setStyleSheet("background-color: rgb(198,226,255);") # 198,226,255
        iconum = QtGui.QIcon()
        iconum.addPixmap(QtGui.QPixmap(":/icon/icons.ico"))
        small.setWindowIcon(iconum) # belirlemiş olduğumuz iconu setWindowIcon diye penceremizin iconu haline getirmiş olduk
        fontlar = QtGui.QFont()#fontları ayrı ayrı yazmak yerine tek bir değişkene atayıp ordan istediğimiz şekilde kısa bir şekilde yazabiliriz..
        fontlar.setPointSize(10) # buton üzerine yazdığımız yazının boyutunu ayarlamış olduk
        fontlar.setBold(True) # buton üzerindeki yazının kalın olmasını sağladık italik gibi değerleri de bu yolla ayarlayabliriz
        buton_arka_plan = "background-color: qlineargradient(spread:pad, x1:0.062, y1:0, x2:0.045, y2:0.954545, stop:0 rgba(203, 203, 203, 255), stop:0.316384 rgba(187, 187, 187, 255), stop:0.615819 rgba(137, 137, 137, 255), stop:0.694915 rgba(126, 126, 126, 255));"
        # butonların arka plan özelliklerini kod kalabalığı olmasın diye tek bir değişkene atayıp rahat  ve sade bir şekiilde kullanabildik

        self.topla = QtWidgets.QPushButton(small) # pushbutoon diyerek bir tane buton oluşturduk.
        self.topla.setText("Topla ( + )") # buton üzerindeki yazıyı ayarladık
        self.topla.setStyleSheet(buton_arka_plan) # belirttiğimiz arka planı butonumuza aktarmış olduk.
        self.topla.setGeometry(QtCore.QRect(30,250,90,30)) # butonumuzun yerini ve boyutunu ayarlamış olduk.
        self.topla.setFont(fontlar) # butonlar için belirtilen font değerlerinii butonlara aktardık
        self.topla.clicked.connect(self.toplama) # butona istediğimiz fonksiyonu bağlamış olduk

        self.sayi = QtWidgets.QPushButton(small)
        self.sayi.setText("Çıkart ( - )")
        self.sayi.setStyleSheet(buton_arka_plan)
        self.sayi.setGeometry(QtCore.QRect(140, 250, 90, 30))
        self.sayi.setFont(fontlar)
        self.sayi.clicked.connect(self.decal)

        self.to_strike = QtWidgets.QPushButton(small)
        self.to_strike.setText(" Çarp ( x )")
        self.to_strike.setStyleSheet(buton_arka_plan)
        self.to_strike.setGeometry(QtCore.QRect(250, 250, 90, 30))
        self.to_strike.setFont(fontlar)
        self.to_strike.clicked.connect(self.to_strikes)

        self.division = QtWidgets.QPushButton(small)
        self.division.setText("Böl ( / )")
        self.division.setStyleSheet(buton_arka_plan)
        self.division.setGeometry(QtCore.QRect(360, 250, 90, 30))
        self.division.setFont(fontlar)
        self.division.clicked.connect(self.divisions)

        self.lisans =QtWidgets.QLabel(small)
        self.lisans.setText("All Rights Reserved ©2018 by Ubeyde")
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        self.lisans.setFont(font)
        self.lisans.setStyleSheet("color : rgb(252,127,36)")
        self.lisans.setGeometry(QtCore.QRect(0,285,200,15))

        self.one_number = QtWidgets.QLineEdit(small)
        self.one_number.setGeometry(QtCore.QRect(30,50,90,25))
        dene = QtGui.QFont()
        dene.setPointSize(15)
        self.one_number.setFont(dene)

        self.two_number = QtWidgets.QLineEdit(small)
        self.two_number.setGeometry(QtCore.QRect(180,50,90,25))
        self.two_number.setFont(dene)

        self.output = QtWidgets.QLineEdit(small)
        self.output.setGeometry(QtCore.QRect(330,50,90,25))
        self.output.setFont(dene)

        self.isaretler = QtWidgets.QLabel(small)
        self.isaretler.setGeometry(QtCore.QRect(135,48,30,30))
        self.isaretler.setText("")
        isaretler_fontu = QtGui.QFont()
        isaretler_fontu.setBold(True)
        isaretler_fontu.setPointSize(25)
        self.isaretler.setFont(isaretler_fontu)

        self.esittir_isareti = QtWidgets.QLabel(small)
        self.esittir_isareti.setGeometry(QtCore.QRect(290, 48, 30, 30))
        self.esittir_isareti.setText("=")
        self.esittir_isareti.setFont(isaretler_fontu)

        self.resim = QtWidgets.QLabel(small)
        self.resim.setGeometry(QtCore.QRect(0,80,460,170))
        self.resim.setStyleSheet("image: url(:/icon/mat.png);")

        self.dikey = QtWidgets.QFrame(small)
        self.dikey.setFrameShape(QtWidgets.QFrame.VLine)
        self.dikey.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.dikey.setGeometry(QtCore.QRect(7,13,3,272))
        self.dikey_2 = QtWidgets.QFrame(small)
        self.dikey_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.dikey_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.dikey_2.setGeometry(QtCore.QRect(470, 11, 3, 277))

        self.yatay = QtWidgets.QFrame(small)
        self.yatay.setFrameShape(QtWidgets.QFrame.HLine)
        self.yatay.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.yatay.setGeometry(QtCore.QRect(8,283,464,5))
        self.yatay_2 = QtWidgets.QFrame(small)
        self.yatay_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.yatay_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.yatay_2.setGeometry(QtCore.QRect(8, 9, 464, 5))

    def hata(self,error):
        error.setWindowTitle("HATA !!")
        error.setFixedSize(370,100)
        self.message= QtWidgets.QLabel(error)
        self.message.setText("Beklenmeyen bir hata oluştu. Sayı değerli ifadeler girin !!")
        fn = QtGui.QFont()
        fn.setPointSize(10)
        self.message.setStyleSheet("color: rgb(100,0,0);")
        self.message.setFont(fn)
        self.message.setGeometry(QtCore.QRect(10,20,350,50))

    def toplama(self):
        self.isaretler.setText("+")
        try:
            one = int(self.one_number.text())
            two = int(self.two_number.text())
            out = str(one+two)
            self.output.setText(out)
        except:uyari.show()
    def decal(self):
        self.isaretler.setText("-")
        try:
            one = int(self.one_number.text())
            two = int(self.two_number.text())
            out = str(one-two)
            self.output.setText(out)
        except:uyari.show()

    def to_strikes(self):
        self.isaretler.setText("x")
        try:
            one = int(self.one_number.text())
            two = int(self.two_number.text())
            out = str(one*two)
            self.output.setText(out)
        except:uyari.show()
    def divisions(self):
        try:
            one = int(self.one_number.text())
            two = int(self.two_number.text())
            out = str(one/two)
            self.output.setText(out)
        except:uyari.show()
        self.isaretler.setText("/")

import icon

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    small =QtWidgets.QWidget()
    goster = AnaPencere()
    goster.pencere(small)
    uyari = QtWidgets.QWidget()
    warnıng = AnaPencere()
    warnıng.hata(uyari)
    small.show()
    sys.exit(app.exec_())