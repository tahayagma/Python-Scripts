from  PyQt5 import QtCore,QtWidgets
import sys

class window(object):
    pass
    def pencil(self,pc):
        pc.setFixedSize(400,200)
        pc.setWindowTitle("Text link")
        link = QtWidgets.QLabel(pc)
        link.setText("<a href = 'https://facebook.com/ubeyde1200'>Author</a>")
        link.setOpenExternalLinks(True)
        link.setGeometry(QtCore.QRect(100,100,40,20))



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    wind = QtWidgets.QWidget()
    Window = window()
    Window.pencil(wind)
    wind.show()
    sys.exit(app.exec_())

