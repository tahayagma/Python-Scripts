from PyQt5 import QtWidgets,QtCore,QtGui
from selenium import webdriver

import sys
from selenium.webdriver.chrome.options import Options


class page(object):
	def home_page(self,sr):
		sr.setWindowTitle("Mobile Browser V1.0")
		sr.setFixedSize(300,200)
		sr.setStyleSheet("background-image: url(:/newPrefix/dexmon.png);\ncolor: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));")
		self.button =QtWidgets.QPushButton(sr)
		self.button.setText("Başlat")
		self.button.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.062, y1:0, x2:0.045, y2:0.954545, stop:0 rgba(203, 203, 203, 255), stop:0.316384 rgba(187, 187, 187, 255), stop:0.615819 rgba(137, 137, 137, 255), stop:0.694915 rgba(126, 126, 126, 255));")
		self.button.setGeometry(QtCore.QRect(120,150,65,25))
		font = QtGui.QFont()
		font.setBold(True)
		font.setPointSize(10)
		self.button.setFont(font)
		self.license = QtWidgets.QLabel(sr)
		self.license.setText("All Rights Reserved ©2019 deXmon.Inc")
		self.license.setGeometry(QtCore.QRect(5,180,195,17))
		self.dexmon= QtWidgets.QLabel(sr)
		self.dexmon.setStyleSheet("image: url(:/newPrefix/dexmon.png);")
		self.dexmon.setGeometry(QtCore.QRect(0,0,299,130))
		self.button.clicked.connect(self.open)

	def open(self):
		mobile_emulation = {"deviceName":"Galaxy S5"}

		chrome_options = webdriver.ChromeOptions()

		chrome_options.add_experimental_option("mobileEmulation",mobile_emulation)
		driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=chrome_options)
		driver.set_window_size(360,640)
		driver.get("http://www.google.com")



import dex


if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	Page = page()
	wind = QtWidgets.QWidget()
	Page.home_page(wind)
	wind.show()
	sys.exit(app.exec_())

