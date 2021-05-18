from PyQt5 import QtWidgets, QtCore,QtGui
import time
import os
import sys
import webbrowser
import subprocess



class interface(object):
    def arayüz(self,ar):
        ar.setWindowTitle("PC KAPAT V0.1")
        ar.setFixedSize(320,208)
        window_icon = QtGui.QIcon()
        window_icon.addPixmap(QtGui.QPixmap(":/newPrefix/win.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        ar.setWindowIcon(window_icon)
        self.saat_ayarla = QtWidgets.QLabel(ar)
        self.saat_ayarla.setText("Zaman ayarla:")
        self.saat_ayarla.setGeometry(QtCore.QRect(10,130,92,20))
        fon = QtGui.QFont()
        fon.setBold(True)
        fon.setPixelSize(13)
        self.saat_ayarla.setFont(fon)
        self.bilgi = QtWidgets.QLabel(ar)
        self.bilgi.setGeometry(QtCore.QRect(10,165,245,16))
        self.bilgi.setStyleSheet("color: red;")
        self.saat_gir = QtWidgets.QComboBox(ar)
        self.saat_gir.setGeometry(QtCore.QRect(120,130,80,20))
        self.saat_gir.addItem("None")
        self.saat_gir.addItem("1 saat")
        self.saat_gir.addItem("2 saat")
        self.saat_gir.addItem("3 saat")
        self.saat_gir.addItem("4 saat")
        self.saat_gir.addItem("5 saat")
        self.saat_gir.addItem("6 saat")
        self.saat_gir.activated.connect(self.saat_fonksiyonu)
        self.yatay_cizgi = QtWidgets.QFrame(ar)
        self.yatay_cizgi.setFrameShape(QtWidgets.QFrame.HLine)
        self.yatay_cizgi.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.yatay_cizgi.setGeometry(QtCore.QRect(5,187,310,7))
        self.yatay_cizgi_2 = QtWidgets.QFrame(ar)
        self.yatay_cizgi_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.yatay_cizgi_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.yatay_cizgi_2.setGeometry(QtCore.QRect(5,5,310,7))
        self.dikey_cizgi = QtWidgets.QFrame(ar)
        self.dikey_cizgi.setFrameShape(QtWidgets.QFrame.VLine)
        self.dikey_cizgi.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.dikey_cizgi.setGeometry(QtCore.QRect(5, 8, 5, 180))
        self.dikey_cizgi_2 = QtWidgets.QFrame(ar)
        self.dikey_cizgi_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.dikey_cizgi_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.dikey_cizgi_2.setGeometry(QtCore.QRect(313, 8, 5, 180))
        self.kapat_yazi = QtWidgets.QLabel(ar)
        self.kapat_yazi.setText("Kapat")
        self.kapat_yazi.setGeometry(QtCore.QRect(30,70,40,20))
        self.kapat_yazi.setFont(fon)
        self.restart = QtWidgets.QLabel(ar)
        self.restart.setText("Yeniden Başlat")
        self.restart.setGeometry(QtCore.QRect(110,70,100,20))
        self.restart.setFont(fon)
        self.lisans = QtWidgets.QLabel(ar)
        self.lisans.setText("All Rights Reserved ©2018 by Ubeyde")
        self.lisans.setGeometry(QtCore.QRect(6,190,217,14))
        self.lisans.setEnabled(False)
        self.lisans.setStyleSheet("color: rgb(252,127,36)")
        font = QtGui.QFont()
        font.setBold(True)
        self.lisans.setFont(font)
        self.time = QtWidgets.QPushButton(ar)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/time.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.time.setIcon(icon)
        self.time.setGeometry(QtCore.QRect(220,125,30,30))
        self.time.setIconSize(QtCore.QSize(35,35))
        self.time.clicked.connect(self.goster)

        self.kapat_iconu = QtWidgets.QPushButton(ar)
        self.kapat_iconu.setGeometry(QtCore.QRect(30,30,34,34))
        iconu = QtGui.QIcon()
        iconu.addPixmap(QtGui.QPixmap(":/newPrefix/off.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.kapat_iconu.setIconSize(QtCore.QSize(40,40))
        self.kapat_iconu.setIcon(iconu)
        self.kapat_iconu.clicked.connect(self.kapat_fonskiyonu)


        self.restart_iconu = QtWidgets.QPushButton(ar)
        self.restart_iconu.setGeometry(QtCore.QRect(140, 30, 36, 36))
        iconum = QtGui.QIcon()
        iconum.addPixmap(QtGui.QPixmap(":/newPrefix/restart.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.restart_iconu.setIconSize(QtCore.QSize(40, 40))
        self.restart_iconu.setIcon(iconum)
        self.restart_iconu.clicked.connect(self.yeniden_baslat)

        self.github = QtWidgets.QPushButton(ar)
        self.github.setGeometry(QtCore.QRect(295,190,20,20))
        git_icon = QtGui.QIcon()
        git_icon.addPixmap(QtGui.QPixmap(":/newPrefix/git.jpg"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.github.setIconSize(QtCore.QSize(20,20))
        self.github.setIcon(git_icon)
        self.github.clicked.connect(self.git)

        self.iptal_et = QtWidgets.QPushButton(ar)
        self.iptal_et.setGeometry(QtCore.QRect(230,30,32,32))
        iptal_iconu = QtGui.QIcon()
        iptal_iconu.addPixmap(QtGui.QPixmap(":/newPrefix/icon3.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.iptal_et.setIcon(iptal_iconu)
        self.iptal_et.setIconSize(QtCore.QSize(50,50))
        self.iptal_yazi = QtWidgets.QLabel(ar)
        self.iptal_yazi.setGeometry(QtCore.QRect(230,70,48,14))
        self.iptal_yazi.setText("İptal Et")
        self.iptal_yazi.setFont(fon)
        self.iptal_et.clicked.connect(self.iptal_fonksiyonu)



    def git(self):
        webbrowser.open("https://github.com/ebuubeyde")
    def saat_fonksiyonu(self,sat):
        saati = self.saat_gir.itemText(sat)
        si = subprocces.STARTUPINFO()
        si.dwFlags = subprocces.STARTF_USESHOWWINDOW
        if saati == "1 saat":
            subprocess.Popen("shutdown -s -t 3600",startupinfo = si)
        elif saati == "2 saat":
            subprocess.Popen("shutdown -s -t 7200",startupinfo = si)
        elif saati == "3 saat":
            subprocess.Popen("shutdown -s -t 10800",startupinfo = si)
        elif saati == "4 saat":
            subprocess.Popen("shutdown -s -t 14400",startupinfo = si)
        elif saati == "5 saat":
            subprocess.Popen("shutdown -s -t 18000",startupinfo = si)
        elif saati == "6 saat":
            subprocess.Popen("shutdown -s -t 21600",startupinfo = si)
        else:pass
    def iptal_fonksiyonu(self):
        si = subprocces.STARTUPINFO()
        si.dwFlags = subprocces.STARTF_USESHOWWINDOW
        subprocess.Popen("shutdown -a",startupinfo = si)
    def kapat_fonskiyonu(self):
        si = subprocces.STARTUPINFO()
        si.dwFlags = subprocces.STARTF_USESHOWWINDOW
        subprocess.Popen("shutdown -p",startupinfo = si)
    def yeniden_baslat(self):
        si = subprocces.STARTUPINFO()
        si.dwFlags = subprocces.STARTF_USESHOWWINDOW
        subprocess.Popen("shutdown -r",startupinfo = si)

    def goster(self):
        self.bilgi.setText("Belirtilen saat sonra bilgisayarın kapanmasını sağlar.")

import icons
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()
    guı = interface()
    guı.arayüz(pencere)
    pencere.show()
    sys.exit(app.exec_())
