#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from PyQt5 import QtWidgets,QtGui,QtCore
import sys
from subprocess import PIPE, Popen # KOMUT SATIRINA KOMUT GÖNDERMEK İÇİN MODÜLÜMÜZ İÇE AKTARDIK
import webbrowser # LİNK AÇMAK İÇİN İÇE AKTARDIK

class main_window(object):
    def second_window(self,sc): # BURDAKİ SC DEĞİŞKENE BİR ÇOK YERDE BİZE KOLAYLIK SAĞLAR
        sc.setWindowTitle("Ağ Anahtarı Göster")
        sc.setFixedSize(400,345)
        sc.setStyleSheet("background-color: rgb(205,205,193);")#122,139,139);")
        self.info_label = QtWidgets.QLabel(sc) # BUNUNLA BİR ETİKET OLUŞTURMUŞ OLDUK
        self.info_label.setGeometry(QtCore.QRect(10,10,100,15)) # ETİKETİN KONUMU AYARLADIK
        #İLK İKİ DEĞER SAĞDAN ÜSTTEN BOŞLUK DİĞER İKİSİ İSE ETİKETİN UZUNLUĞUNU VE GENİŞLİĞİNİ İFADE EDER
        self.info_label.setText("Bir ağ adı girin:") # LABELİN YAZISINI BELİRLEMİŞ OLDUK.
        font = QtGui.QFont()
        font.setPointSize(9) # YAZININ BOYUTUNU AYARLADIK
        font.setBold(True) # YAZININ KALIN OLMASINI SAĞLADIK
        self.info_label.setFont(font)
        background ="background-color: qlineargradient(spread:pad, x1:0.062, y1:0, x2:0.045, y2:0.954545, stop:0 rgba(203, 203, 203, 255), stop:0.316384 rgba(187, 187, 187, 255), stop:0.615819 rgba(137, 137, 137, 255), stop:0.694915 rgba(126, 126, 126, 255));"
        # BACKGROUND ADLI DEĞİŞKENE BUTON ARKA PLAN ÖZELLİKLERİNİ AKTARDIK
        self.query_buton = QtWidgets.QPushButton(sc) # BUTON OLUŞTURDUK
        self.query_buton.setGeometry(QtCore.QRect(10,80,80,25)) #BUTONUN BOYUTUNU AYARLADIK
        self.query_buton.setText("Sorgula") #BUTON ÜZERİNDE SORULA YAZISINI YAZDIRDIK
        self.query_buton.setFont(font) # OLUŞTURDUĞUMUZ FONT ÖZELLİKLERİNİ BUTONA AKTARDIK
        self.query_buton.setStyleSheet(background) # BUTONUN ARKA PLAN RENGİNİ BUTONA AKTARDIK
        self.query_buton.clicked.connect(self.query) # ALT KISIMDA OLUŞTURDUĞUMUZ query ADLI FONKSİYONU BU BUTONA BAĞLADIK
        self.lineEdit = QtWidgets.QLineEdit(sc) # LİNE EDİT OLUŞTURDUK
        self.lineEdit.setGeometry(QtCore.QRect(120,10,90,25))
        self.lineEdit.setStyleSheet("background-color: white;") # LİNEEDİT ARKA PLAN RENGİNİ AYALADIK
        self.all_show_buton_2 = QtWidgets.QPushButton(sc)
        self.all_show_buton_2.setGeometry(QtCore.QRect(110,80,100,25))
        self.all_show_buton_2.setText("Tümünü Göster")
        self.all_show_buton_2.setStyleSheet(background)
        self.all_show_buton_2.setFont(font)
        self.all_show_buton_2.clicked.connect(self.all_show)
        self.my_wifi_buton = QtWidgets.QPushButton(sc)
        self.my_wifi_buton.setGeometry(QtCore.QRect(350,7,30,30))
        ıcon = QtGui.QIcon() # BUTONA ICON EKLEMEK İCON ICIN DEĞİŞKENİNİ OLUŞTURDUK
        ıcon.addPixmap(QtGui.QPixmap(":/newPrefix/network.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off) # ICON DEĞİŞKENİMİZİ BELİRTTİK
        self.my_wifi_buton.setIcon(ıcon) # İCON BUTONA YAZDIRDIK
        self.my_wifi_buton.setIconSize(QtCore.QSize(40,40)) # BUTON ÜZERİNDE İCONUN BOYUTUNU AYARLADIK
        self.my_wifi_buton.clicked.connect(self.my_wifi)
        self.info_label_2 = QtWidgets.QLabel(sc)
        self.info_label_2.setText("Bağlı Olan\nAğ şifresini Göster")
        self.info_label_2.setGeometry(QtCore.QRect(240,7,92,28))
        self.info_label_2.setEnabled(False) # BUNUN YAZININ SÖNÜK OLMASINI SAĞLADIK
        self.text_browser = QtWidgets.QTextBrowser(sc) # TEXT BROWSERİ OLUŞTURDUK
        self.text_browser.setGeometry(QtCore.QRect(7,125,385,195))
        self.text_browser.setStyleSheet("background-color: white;")# ARKA PLAN RENGİNİ AYARLADIK
        self.out_label = QtWidgets.QLabel(sc)
        self.out_label.setGeometry(QtCore.QRect(10,35,320,40))
        self.out_label.setFont(font)
        self.face_buton = QtWidgets.QPushButton(sc)
        self.face_buton.setGeometry(QtCore.QRect(372,323,20,20))
        self.git_buton = QtWidgets.QPushButton(sc)
        self.git_buton.setGeometry(QtCore.QRect(345,323,20,20))
        git_icon = QtGui.QIcon()
        git_icon.addPixmap(QtGui.QPixmap(":/newPrefix/git.jpg"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.git_buton.setIcon(git_icon)
        self.git_buton.setIconSize(QtCore.QSize(25,25))
        face_icon = QtGui.QIcon()
        face_icon.addPixmap(QtGui.QPixmap(":/newPrefix/face.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.face_buton.setIcon(face_icon)
        self.face_buton.setIconSize(QtCore.QSize(25, 25))
        self.git_buton.clicked.connect(self.git_open)
        self.face_buton.clicked.connect(self.face_open)
        self.license = QtWidgets.QLabel(sc)
        self.license.setGeometry(QtCore.QRect(5,323,200,15))
        self.license.setText("All Rights Reserved © 2018 by Ubeyde")
        self.license.setEnabled(False)
    def git_open(self):
        webbrowser.open("https://github.com/ebuubeyde") # WEB BROWSER İLE LİNKİMİZİN AÇILMASINI SAĞLADIK
    def face_open(self):
        webbrowser.open("https://www.facebook.com/ubeyde1200")


    def all_show(self):
        komut_1 = "netsh wlan show profile"
        p = Popen(komut_1, shell=True, stderr=PIPE, stdout=PIPE)
        (out_1, err) = p.communicate()
        son = str(out_1)
        yeni = son[175:]
        sonu = yeni.split(r"\r\n")
        tp = sonu[0:10]
        out = "\r\n".join(tp)
        self.text_browser.setText(out)


    def my_wifi(self):
        try:
            komut = 'NETSH WLAN SHOW INTERFACE | findstr /r "^....SSID"'
            p = Popen(komut, shell=True, stderr=PIPE, stdout=PIPE)
            (out, err) = p.communicate()

            out = str(out)
            wifi_name = out[31:-5]
            print(wifi_name)
            komut_2 = 'netsh wlan show profile {} key = clear'.format(wifi_name)
            pel = Popen(komut_2, shell=True, stderr=PIPE, stdout=PIPE)
            (outu, erri) = pel.communicate()

            out = str(outu)
            new = out.split(r"\r\n")
            liste = list(new)
            password = liste[32]
            tp = tuple(password)
            son = tp[29:]
            cv = "".join(son)
            self.out_label.setStyleSheet("color: green;")
            self.out_label.setText("{}'nın ağ anahtarı:\n {}".format(wifi_name, cv))
        except:
            self.out_label.setStyleSheet("color: red;")
            self.out_label.setText("Beklenmeyen bir hata oluştu.")
    def query(self):
        try:
            komut_2 = 'netsh wlan show profile {} key = clear'.format(self.lineEdit.text())
            pel = Popen(komut_2, shell=True, stderr=PIPE, stdout=PIPE)
            (outu, erri) = pel.communicate()

            out = str(outu)
            new = out.split(r"\r\n")
            liste = list(new)
            password = liste[32]
            tp =tuple(password)
            son = tp[29:]
            cv = "".join(son)
            self.out_label.setStyleSheet("color: green;")
            self.out_label.setText("{}'nın ağ anahtarı:\n {}".format(self.lineEdit.text(),cv))
        except:
            self.out_label.setStyleSheet("color: red;")
            self.out_label.setText("Lütfen ağ adını kontrol edin")


import ıcon # ICONLARIN BULUNDUĞU PY DOSYASINI İÇE AKTARDIK

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    wind = QtWidgets.QWidget()
    new_variable = main_window()
    new_variable.second_window(wind)
    wind.show()
    sys.exit(app.exec_())
