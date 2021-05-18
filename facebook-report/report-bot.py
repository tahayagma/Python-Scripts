#-*-coding:UTF-8-*-
from selenium import webdriver
import webbrowser
import time
import pyautogui
import sys
from PyQt5 import QtWidgets,QtGui
import logging # yaptığımız işlemler için log tutuyoruz.
logging.basicConfig(filename = "kayitlar.log",level = logging.DEBUG)

class Pencere(QtWidgets.QWidget):
    def __init__(self):

        super().__init__()

        self.init_ui()


    def init_ui(self):

        self.link = QtWidgets.QLineEdit()
        self.lingir = QtWidgets.QLabel("Link       :")
        self.sifre = QtWidgets.QLineEdit()
        self.sifregir = QtWidgets.QLabel("Parola   :")
        self.sifre.setEchoMode(QtWidgets.QLineEdit.Password)
        self.eposta = QtWidgets.QLineEdit()
        self.mailgir = QtWidgets.QLabel("E-posta :")
        self.al = QtWidgets.QPushButton("Sayfa Şikayet Et")
        self.sahıs = QtWidgets.QPushButton("Hesap Şikayet Et")
        self.yazi = QtWidgets.QLabel("Deneme sürümüdür. Powered by Ubeyde\n© Coded 2017")
        self.fullyap = QtWidgets.QCommandLinkButton("Premium")


        self.setWindowTitle("Facebook Report V1.0")
        self.setGeometry(100,100,420,220)
        #self. setStyleSheet('background-color :green') burası pencerenin arka plan rengini ayarlar

        h_box1 = QtWidgets.QHBoxLayout()
        h_box1.addWidget(self.mailgir)
        h_box1.addWidget(self.eposta)
        h_box1.addStretch()

        h_box2 = QtWidgets.QHBoxLayout()
        h_box2.addWidget(self.sifregir)
        h_box2.addWidget(self.sifre)
        h_box2.addStretch()


        h_box3 = QtWidgets.QHBoxLayout()
        h_box3.addWidget(self.lingir)
        h_box3.addWidget(self.link)
        h_box3.addStretch()



        v_box = QtWidgets.QVBoxLayout()
        v_box.addLayout(h_box1)
        v_box.addLayout(h_box2)
        v_box.addLayout(h_box3)
        v_box.addWidget(self.yazi)
        v_box.addStretch()
        v_box.addWidget(self.fullyap)
        v_box.addStretch()
        v_box.addWidget(self.sahıs)
        v_box.addWidget(self.al)
        v_box.addStretch()

        self.setLayout(v_box)
        self.sahıs.clicked.connect(self.facebok)
        self.al.clicked.connect(self.sayfa)
        self.fullyap.clicked.connect(self.warning)
        self.show()



    def warning(self):
        yeni.show()


    def sayfa(self):
        browser = webdriver.Chrome()
        browser.maximize_window()

        browser.get('https://www.facebook.com/')

        username = browser.find_element_by_xpath('//*[@id="email"]')
        password = browser.find_element_by_xpath('//*[@id="pass"]')

        username.send_keys(self.eposta.text())
        password.send_keys(self.sifre.text())

        login = browser.find_element_by_xpath('//*[@id="loginbutton"]')
        login.click()
        liste = []
        liste.append(self.link.text())
        link2 = self.link.text().replace("www", "mbasic")
        browser.get(link2)
        ucnoktatıkla = browser.find_element_by_link_text('Diğer')
        ucnoktatıkla.click()
        sikayetet = browser.find_element_by_xpath('//*[@id="root"]/table/tbody/tr/td/div[2]/div/div/div[2]/table/tbody/tr/td[2]/a')
        sikayetet.click()
        facedeolmasın = browser.find_element_by_xpath('//*[@id="question-form"]/div[1]/fieldset/label[3]/div/table/tbody/tr/td[2]/div/div')
        facedeolmasın.click()
        devam = browser.find_element_by_xpath('//*[@id="question-form"]/div[2]/input')
        devam.click()
        nefret = browser.find_element_by_xpath('//*[@id="question-form"]/div[1]/fieldset/label[2]/div/table/tbody/tr/td[2]/div/div')
        nefret.click()
        devam2 = browser.find_element_by_xpath('//*[@id="question-form"]/div[2]/input')
        devam2.click()
        ırkaetnik = browser.find_element_by_xpath('//*[@id="question-form"]/div[1]/fieldset/label[1]/div/table/tbody/tr/td[2]/div/div')
        ırkaetnik.click()
        devam3 = browser.find_element_by_xpath('//*[@id="question-form"]/div[2]/input')
        devam3.click()
        faceyegonder = browser.find_element_by_xpath('//*[@id="actions-form"]/div[1]/fieldset/label[1]/div/table/tbody/tr/td[2]/div/div/span')
        faceyegonder.click()
        time.sleep(2)
        pyautogui.click(x=419, y=321, clicks=1500, interval=0.40)
        pyautogui.press("space",interval=0.25,presses=1500)

        time.sleep(3)
        bitti = browser.find_element_by_link_text('Bitti')
        bitti.click()
        time.sleep(1)
        browser.close()


    def facebok(self):
        browser = webdriver.Chrome()
        browser.maximize_window()

        browser.get('https://www.facebook.com/')

        username = browser.find_element_by_xpath('//*[@id="email"]')
        password = browser.find_element_by_xpath('//*[@id="pass"]')

        username.send_keys(self.eposta.text())
        password.send_keys(self.sifre.text())

        login = browser.find_element_by_xpath('//*[@id="loginbutton"]')
        login.click()
        time.sleep(5)
        liste = []
        liste.append(self.link.text())
        link1 = self.link.text().replace("www", "mbasic")
        browser.get(link1)
        sikayetet = browser.find_element_by_link_text('Diğer')
        sikayetet.click()
        buprofil = browser.find_element_by_link_text('Bu Profili Şikayet Et')
        buprofil.click()
        profildevam = browser.find_element_by_xpath('//*[@id="question-form"]/div[1]/fieldset/label[2]/div/table/tbody/tr/td[2]/div/div')
        profildevam.click()
        devam = browser.find_element_by_xpath('//*[@id="question-form"]/div[2]/input')
        devam.click()
        sahtehesap = browser.find_element_by_xpath('//*[@id="question-form"]/div[1]/fieldset/label[3]/div/table/tbody/tr/td[2]/div/div')
        sahtehesap.click()
        sahtedevam = browser.find_element_by_xpath('//*[@id="question-form"]/div[2]/input')
        sahtedevam.click()
        faceyegonder = browser.find_element_by_xpath('//*[@id="actions-form"]/div[1]/fieldset/label[1]/div/table/tbody/tr/td[2]/div/div/span')
        faceyegonder.click()
        time.sleep(2)
        pyautogui.click(x=412, y=306, clicks=1500, interval=0.40)
        pyautogui.press("space",interval=0.25,presses=1500)

        time.sleep(3)
        bitti = browser.find_element_by_link_text('Bitti')
        bitti.click()
        time.sleep(1)
        browser.close()


class uyari(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.gorsel()
    def gorsel(self):
        self.labeli = QtWidgets.QLabel("""
        Full sürüm V2.0 -->
         
        [*]-->   Arka planda çalışma 
        [*]-->   Block engelinden kaçma
        [*]-->   Daha fazla şikayet
        """)
        self.labeli.move(0,10)
        self.ilet = QtWidgets.QCommandLinkButton("İletişim")
        self.ilet.setFixedSize(100,40)
        self.setGeometry(150, 200, 300, 200)
        self. setStyleSheet('background-color :lightblue') #burası pencerenin arka plan rengini ayarlar
        self.setWindowTitle("   HAKKINDA   ")
        h_box = QtWidgets.QHBoxLayout()
        h_box.addWidget(self.labeli)
        h_box.addStretch()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addLayout(h_box)
        v_box.addWidget(self.ilet)
        self.setLayout(v_box)

        self.ilet.clicked.connect(self.site)
    def site(self):
        webbrowser.open("https://github.com/ebuubeyde")




app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
yeni = uyari()
sys.exit(app.exec_())
