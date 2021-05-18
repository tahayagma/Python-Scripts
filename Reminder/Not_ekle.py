from PyQt5 import QtCore,QtWidgets,QtGui
import sys,os
import time
import datetime
import winreg
#os.system("copy C:\Program Files\system.exe")
#key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r"Software\\Microsoft\\Windows\\CurrentVersion\\Run",0,winreg.KEY_ALL_ACCESS)
#winreg.SetValueEx(key,"sys",0,w,winreg.REG_SZ,r"C:\Users\USER\Desktop\python\completed_project_new\system.exe")
#key.Close()



class home_page(object):
    def interface(self,pp):
        pp.setWindowTitle("NOTUNUZ v.0.1")
        pp.setFixedSize(400,200)
        pp.setStyleSheet("background-color: rgb(176,176,176)")
        pp.move(961,507)
        pp.setWindowIcon(QtGui.QIcon("Note.ico"))
        self.check = QtWidgets.QCheckBox(pp)
        self.check.setGeometry(QtCore.QRect(25,130,100,30))
        self.check.stateChanged.connect(self.checki)
        self.check.setText("Okudum,Anladım")
        self.label_2 = QtWidgets.QLabel(pp)
        self.label_2.setGeometry(QtCore.QRect(25,151,93,17))
        self.label_2.setText("Mesajınız Kaldırılır !!")
        self.label_2.setStyleSheet("color: red;")
        self.label_2.setEnabled(False)
        self.label_3 = QtWidgets.QLabel(pp)
        self.label_3.setGeometry(QtCore.QRect(308,130,60,17))
        self.textedit = QtWidgets.QTextEdit(pp)
        self.textedit.setGeometry(QtCore.QRect(20,10,350,120))
        self.textedit.setStyleSheet("background-color: White;")
        self.textedit.setEnabled(False)
        self.button = QtWidgets.QPushButton(pp)
        self.button.setGeometry(QtCore.QRect(306,155,60,20))
        self.button.setText("Ekle")
        self.button.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.062, y1:0, x2:0.045, y2:0.954545, stop:0 rgba(203, 203, 203, 255), stop:0.316384 rgba(187, 187, 187, 255), stop:0.615819 rgba(137, 137, 137, 255), stop:0.694915 rgba(126, 126, 126, 255));")
        self.button.clicked.connect(self.show)
        self.lisence  = QtWidgets.QLabel(pp)
        self.lisence.setText("All Rights Reserved ©2019 deXmon.Inc")
        self.lisence.setGeometry(QtCore.QRect(5,180,220,15))
        self.lisence.setEnabled(False)
        self.lisence.setStyleSheet("color: rgb(64,64,64);")
        self.zaman = datetime.datetime.now()
        self.date = datetime.datetime.strftime(self.zaman, "%d.%m.%Y")
        self.label_3.setText(self.date)

    def insert(self,ek):
        ek.setWindowTitle("Not Ekle")
        ek.setFixedSize(400,220)
        ek.setStyleSheet("background-color :rgb(176,176,176);")
        ek.setWindowIcon(QtGui.QIcon("Note.ico"))
        self.edit = QtWidgets.QTextEdit(ek)
        self.edit.setGeometry(QtCore.QRect(20,10,350,120))
        self.edit.setStyleSheet("background-color: white;")
        self.change_date = QtWidgets.QLabel(ek)
        self.change_date.setText("Saat:")
        self.change_date.setGeometry(QtCore.QRect(24,135,100,20))
        self.change_time_line = QtWidgets.QTimeEdit(ek)
        self.change_time_line.setGeometry(QtCore.QRect(24,160,50,20))
        self.warn = QtWidgets.QLabel(ek)
        self.warn.setGeometry(QtCore.QRect(15,180,220,17))
        self.warn.setStyleSheet("color:red;")
        self.button_2 = QtWidgets.QPushButton(ek)
        self.button_2.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.062, y1:0, x2:0.045, y2:0.954545, stop:0 rgba(203, 203, 203, 255), stop:0.316384 rgba(187, 187, 187, 255), stop:0.615819 rgba(137, 137, 137, 255), stop:0.694915 rgba(126, 126, 126, 255));")
        self.button_2.setText("Tamam")
        self.button_2.setGeometry(QtCore.QRect(310,150,60,20))
        self.button_2.clicked.connect(self.function)
        #self.important = QtWidgets.QCheckBox(ek)
        #self.important.setText("Önemli")
        #self.important.setGeometry(QtCore.QRect(100,160,60,17))
        #self.important.stateChanged.connect(self.color_red)

        self.lisence_2 = QtWidgets.QLabel(ek)
        self.lisence_2.setGeometry(QtCore.QRect(5,200,220,15))
        self.lisence_2.setText("All Rights Reserved ©2019 deXmon.Inc")
        self.lisence_2.setEnabled(False)
        self.lisence_2.setStyleSheet("color: rg(64,64,64);")
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(12)
        self.textedit.setFont(font)
        try:
            try:
                with open("log.qr","r+",encoding="utf-8") as dosya:
                    self.deger = dosya.readlines()
                    self.textedit.setText(self.deger[0])
            except IndexError:
                with open("log.qr","w") as dosya:
                    dosya.write("Not ekle..")


        except FileNotFoundError:
            with open("log.qr","w",encoding="utf-8") as log:
                log.write("Not ekle..")


    def function(self):
        try:
            with open("log.qr", "r+",encoding="utf-8") as file:
                if bool(self.edit.toPlainText()) == True:
                    self.values = self.edit.toPlainText() + "\n"
                    file.write(self.values)

                else:
                    pass


        except FileNotFoundError:
            with open("log.qr","w",encoding="utf-8") as fuel:
                fuel.write(self.edit.toPlainText() + "\n")




        #if bool(self.values) == True:
            #self.textedit.setText(self.values)
        #else:pass
        if self.change_time_line.text() != "00:00":
            while True:
                self.change = datetime.datetime.now()

                self.clock = datetime.datetime.strftime(self.change, "%H:%M")
                wind.close()
                pen.close()
                time.sleep(20)
                if self.clock == self.change_time_line.text():
                    wind.show()
                    wind.move(961, 507)
                    break
                else:
                    pass
        else:pass
        pen.close()

    #def color_red(self):
        #if self.important.isChecked() == True:
            #with open("log.qr","w",encoding="utf-8") as dos:
                #text = self.textedit.setText().setStyleSheet("color:red;")
                #dos.write(text)
            #self.textedit.setStyleSheet("""QTextEdit{
                                        #background-color:white;
                                        #color:red;}""")
        #else:pass


    def checki(self):
        if self.check.isChecked() == True:
            self.textedit.clear()
            os.system("log.qr")

        else:pass


    def show(self):
        pen.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    wind = QtWidgets.QWidget()
    new = home_page()
    new.interface(wind)
    pen = QtWidgets.QWidget()
    new.insert(pen)
    wind.show()
    sys.exit(app.exec_())




