# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'notepad.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import os
import sys
import webbrowser # bu modül ile linklerimizi açabileceğiz


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(1300, 660)
        Form.setStyleSheet("background-color: rgb(0, 0, 0);")
        Form.setWindowOpacity(0.8) # burda pencerenin opaklığını ayarladık. siz zevkinize göre yaparsınız
        p_icon = QtGui.QIcon()
        p_icon.addPixmap(QtGui.QPixmap(":/newPrefix/not.ico"))
        Form.setWindowIcon(p_icon)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 280, 161, 161))
        self.label.setStyleSheet("image: url(:/newPrefix/logo.png);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(1130, 270, 161, 161))
        self.label_2.setStyleSheet("image: url(:/newPrefix/logo.png);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(160, 520, 961, 141))
        self.label_3.setStyleSheet("image: url(:/newPrefix/my.png);")
        self.label_3.setObjectName("label_3")
        self.lisans = QtWidgets.QLabel(Form)
        self.lisans.setEnabled(False)
        self.lisans.setGeometry(QtCore.QRect(4, 640, 251, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.lisans.setFont(font)
        self.lisans.setStyleSheet("color: rgb(170, 85, 0);")
        self.lisans.setObjectName("lisans")
        self.ayarlar = QtWidgets.QPushButton(Form)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/set.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.ayarlar.setIcon(icon)
        self.ayarlar.setIconSize(QtCore.QSize(53,47))
        self.ayarlar.setGeometry(QtCore.QRect(1230,600,40,41))
        self.ayarlar.clicked.connect(self.ayarlar_ac)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(190, 10, 911, 421))
        self.fontu = QtGui.QFont()
        self.fontu.setPointSize(15)
        self.fontu.setBold(True)
        self.fontu.setWeight(75)
        #self.fontu.setFamily("Consolas")
        self.plainTextEdit.setFont(self.fontu)
        self.plainTextEdit.setStyleSheet("color: rgb(255,0,0);")
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(405, 460, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(35, 40, 3, 255), stop:0.136364 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.335227 rgba(245, 236, 112, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.625 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.772727 rgba(187, 156, 51, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.840909 rgba(168, 142, 42, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.dosya_kaydet)
        self.pushButton_2 = QtWidgets.QPushButton(Form) # bu  buton temizleme butonu istedğiniz şekilde ad verebilirsiz
        self.pushButton_2.setGeometry(QtCore.QRect(565, 460, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(35, 40, 3, 255), stop:0.136364 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.335227 rgba(245, 236, 112, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.625 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.772727 rgba(187, 156, 51, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.840909 rgba(168, 142, 42, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.temizle)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(725, 460, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(35, 40, 3, 255), stop:0.136364 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.335227 rgba(245, 236, 112, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.625 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.772727 rgba(187, 156, 51, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.840909 rgba(168, 142, 42, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.dosya_ac) # burda butona bağlantı sağlamış olduk
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MY NOTEPAD")) # BURDA FORM YERE YAZAB YERE PENCEREMİZİN BAŞLIĞINI YAZCAĞIZ
        self.lisans.setText(_translate("Form", "All Rights Reserved ©2018 by Ubeyde"))
        self.pushButton.setText(_translate("Form", "KAYDET")) # Burdan buton adlarını değştirebilirsiniz
        self.pushButton_2.setText(_translate("Form", "TEMİZLE"))
        #self.pushButton_2.setShortcut(_translate("Form","Enter"))
        self.pushButton_3.setText(_translate("Form", "DOSYA AÇ"))

    def temizle(self):
        self.plainTextEdit.clear()
    def dosya_ac(self):
        dosya_yolu = QFileDialog.getOpenFileName(None, "Dosya Aç",os.getenv("HOME"))
        with open(dosya_yolu[0],"r") as dosyam:
            self.plainTextEdit.setPlainText(dosyam.read())

    def dosya_kaydet(self):
        dosya_yolu = QFileDialog.getSaveFileName(None,"Dosya Kaydet", os.getenv("HOME"))
        with open(dosya_yolu[0],"w") as dosyam:
            dosyam.write(self.plainTextEdit.toPlainText())
    def ayarlar_ac(self):
        yeni.show()



    def setting(self, settings):
        settings.setObjectName("Settings")
        settings.setFixedSize(410, 202)
        settings.setWindowTitle("AYARLAR")
        set_icon = QtGui.QIcon()
        set_icon.addPixmap(QtGui.QPixmap(":/newPrefix/not.ico"))
        settings.setWindowIcon(set_icon)
        self.y_t_stili = QtWidgets.QComboBox(settings)
        self.y_t_stili.setGeometry(QtCore.QRect(120, 70, 69, 22))
        self.y_t_stili.setObjectName("y_t_stili")
        self.y_t_stili.addItem("Kalın")
        self.y_t_stili.addItem("İtalik")
        self.y_t_stili.activated.connect(self.yazi_stili_degistir) # BUTONLARDAN TEK FARKLARI CLİCKED YERİNE ACTİVATED YAZIYORUZ.
        self.renk = QtWidgets.QComboBox(settings)
        self.renk.setGeometry(QtCore.QRect(320, 70, 69, 22))
        self.renk.setObjectName("renk")
        self.renk.addItem("Kırmızı")
        self.renk.addItem("Mavi")
        self.renk.addItem("Yeşil")
        self.renk.addItem("Beyaz")
        self.renk.addItem("Mor")
        self.renk.addItem("Sarı")
        self.renk.addItem("Gri")
        self.renk.activated.connect(self.yazi_rengini_degistir)
        self.y_tipi = QtWidgets.QComboBox(settings)
        self.y_tipi.setGeometry(QtCore.QRect(20, 70, 69, 22))
        self.y_tipi.setObjectName("comboBox_3")
        self.y_tipi.addItem("Consolas")
        self.y_tipi.addItem("MV Boli")
        self.y_tipi.addItem("Segoe UI")
        self.y_tipi.addItem("Playbill")
        self.y_tipi.activated.connect(self.yazi_tipini_degistir)
        self.boyut = QtWidgets.QComboBox(settings)
        self.boyut.setGeometry(QtCore.QRect(220, 70, 69, 22))
        self.boyut.setObjectName("boyut")
        self.boyut.addItem("8") # comboboxumuza burdan istediğimiz kadar değer ekleyebiliriz
        self.boyut.addItem("10")
        self.boyut.addItem("12")
        self.boyut.addItem("14")
        self.boyut.addItem("16")
        self.boyut.addItem("18")
        self.boyut.addItem("24")
        self.boyut.addItem("30")
        self.boyut.addItem("60")
        self.boyut.addItem("72")
        self.boyut.activated.connect(self.yazi_boyutunu_degistir)
        self.yazi_tipimiz = QtWidgets.QLabel(settings)
        self.yazi_tipimiz.setGeometry(QtCore.QRect(20, 40, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.yazi_tipimiz.setText("Yazı Tipi:")
        self.yazi_tipimiz.setFont(font)
        self.yazi_stili = QtWidgets.QLabel(settings)
        self.yazi_stili.setText("Yazi Tipi Stili:")
        self.yazi_stili.setGeometry(QtCore.QRect(120, 40, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.yazi_stili.setFont(font)
        self.yazi_boyutumuz = QtWidgets.QLabel(settings)
        self.yazi_boyutumuz.setGeometry(QtCore.QRect(220, 40, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.yazi_boyutumuz.setFont(font)
        self.yazi_boyutumuz.setText("Yazı Boyutu:")
        self.yazi_rengi = QtWidgets.QLabel(settings)
        self.yazi_rengi.setGeometry(QtCore.QRect(320, 40, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.yazi_rengi.setFont(font)
        self.yazi_rengi.setText("Yazı Rengi:")
        self.tamam_buton = QtWidgets.QPushButton(settings)
        self.tamam_buton.setGeometry(320, 150, 69, 22)
        self.tamam_buton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.062, y1:0, x2:0.045, y2:0.954545, stop:0 rgba(203, 203, 203, 255), stop:0.316384 rgba(187, 187, 187, 255), stop:0.615819 rgba(137, 137, 137, 255), stop:0.694915 rgba(126, 126, 126, 255));")
        self.tamam_buton.setText("Tamam")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tamam_buton.setFont(font)
        self.tamam_buton.clicked.connect(yeni.close) # butonlara fonksiyon bağlamyı gösterdik dahaönce  burda ise tamam butonuna tıklandığında ayarlar kapanacak
        self.git = QtWidgets.QPushButton(settings)
        self.git.setGeometry(QtCore.QRect(10,150,50,50))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/git.jpg"), QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.git.setIcon(icon)
        self.git.setIconSize(QtCore.QSize(50,50))
        self.git.clicked.connect(self.ac)
    def ac(self):
        webbrowser.open(r"https://github.com/ebuubeyde")

    def yazi_stili_degistir(self,stl): #burda fonksiyona stl diye bir değişken atadık ordan gelen verileri işleyebileceğiz.
        stl = self.y_t_stili.itemText(stl) # burda ise ayarlardan gelecek olan bilgiyi alıp stl değişkenine atadık
        fontu = QtGui.QFont() # font adında bir değer oluştu onu texteditimize atalım
        if stl == "Kalın":
            fontu.setBold(True) # burdan bold değerini yani kalınlık değerini true olarak ayarladık.
            ui.plainTextEdit.setFont(fontu)
        elif stl == "İtalik":
            fontu.setItalic(True)
            ui.plainTextEdit.setFont(fontu)  # burda fonksiyon bitti
    def yazi_tipini_degistir(self,tp):
        tp = self.y_tipi.itemText(tp)
        fn = QtGui.QFont()
        if tp == "Consolas": # tp değişkenini text değerini sorgulayıp şartlı durumu oluşturduk
            fn.setFamily("Consolas") # set family ile yazi ailesini değiştirebilirsiniz
            ui.plainTextEdit.setFont(fn) # daha sonra ise text editimize gerekn değişkenlei atadık
        elif tp == "Segoe UI":
            fn.setFamily("Segoe UI")
            ui.plainTextEdit.setFont(fn)
        elif tp == "MV Boli":
            fn.setFamily("MV Boli")
            ui.plainTextEdit.setFont(fn)
        elif tp == "Play Bill":
            fn.setFamily("Play Bill")
            ui.plainTextEdit.setFont(fn) # bu fonksiyonda tamam
    def yazi_boyutunu_degistir(self,boy):
        boy = self.boyut.itemText(boy)
        font = QtGui.QFont()
        if boy == "8":
            font.setPointSize(8) # setpointsize ile yazı boyutunu değiştirebilirsiniz
            ui.plainTextEdit.setFont(font)
        elif boy == "10":
            font.setPointSize(10)
            ui.plainTextEdit.setFont(font)
        elif boy == "12":
            font.setPointSize(12)
            ui.plainTextEdit.setFont(font)
        elif boy == "14":
            font.setPointSize(14)
            ui.plainTextEdit.setFont(font)
        elif boy == "16":
            font.setPointSize(16)
            ui.plainTextEdit.setFont(font)
        elif boy == "18":
            font.setPointSize(18)
            ui.plainTextEdit.setFont(font)
        elif boy == "20":
            font.setPointSize(20)
            ui.plainTextEdit.setFont(font)
        elif boy == "24":
            font.setPointSize(24)
            ui.plainTextEdit.setFont(font)
        elif boy == "30":
            font.setPointSize(30)
            ui.plainTextEdit.setFont(font)
        elif boy == "60":
            font.setPointSize(60)
            ui.plainTextEdit.setFont(font)
        elif boy == "72":
            font.setPointSize(72)
            ui.plainTextEdit.setFont(font) # bu fonskiyon tamam
    def yazi_rengini_degistir(self,ren):
        ren =self.renk.itemText(ren)
        fon = QtGui.QFont()
        if ren == "Kırmızı":
            ui.plainTextEdit.setStyleSheet("color: red;") # eğer istediğiniz renklerin tonlarını rgb kodlarını yazarak da yapabilirsiniz. ben direk adlarını yazdım
        elif ren == "Mavi":
            ui.plainTextEdit.setStyleSheet("color: blue;")
        elif ren == "Mor":
            ui.plainTextEdit.setStyleSheet("color: purple;")
        elif ren == "Yeşil":
            ui.plainTextEdit.setStyleSheet("color: rgb(0,255,0);") # örnek olarak burd istediğim ton renginin kodlarını yazdım.
        elif ren == "Sarı":
            ui.plainTextEdit.setStyleSheet("color: yellow;")
        elif ren == "Beyaz":
            ui.plainTextEdit.setStyleSheet("color: white;")
        elif ren == "Gri":
            ui.plainTextEdit.setStyleSheet("color: gray;") # bu fons-ksiyon da tamam



import image # görüntünün bulunduğu dosyayı içe aktardık. sonunda genellikle _rc olur. siz dosyasının ismiyle çağırın yani _rc kısmını silelir genellikle

if __name__ == "__main__": # bunun anlamı altta yazdığımız isimleri yukarıdaki ana classın içinde mi diye sormuş olduk.
    import sys # sys modülümüz içe aktardık
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    yeni = QtWidgets.QWidget()
    uo = Ui_Form()
    uo.setting(yeni)


    #ayarlarım = QtWidgets.QWidget() # burda ayarlarım adında br pencere oluşturduk.
    #ui_1 = Settings() # settings adında olan sınıfımızı ui_1 adında bir değişkene atamış olduk .
    #ui_1.setting(ayarlarım) # arayüzümüzün bulunduğu setupUİ fonskiyonumuza pencereyi ekledik ki arayüz gösterilsin
    Form.show() # bu ise başlagınçta göstermek istediğimiz  penceremizi show() fonksiyonu ile gösteriyoruz.
    sys.exit(app.exec_())# pencerenini biz kapatmayana kadar görünmesini sağladık

