import sys

# Импортируем из PyQt5.QtWidgets классы для создания приложения и виджет
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sqlite3


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(645, 841)
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 0, 41, 31))
        self.pushButton_4.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 30, 645, 150))
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setGeometry(QtCore.QRect(0, 180, 645, 150))
        self.widget_2.setObjectName("widget_2")
        self.widget_3 = QtWidgets.QWidget(Form)
        self.widget_3.setGeometry(QtCore.QRect(0, 330, 645, 150))
        self.widget_3.setObjectName("widget_3")
        self.widget_4 = QtWidgets.QWidget(Form)
        self.widget_4.setGeometry(QtCore.QRect(0, 480, 645, 150))
        self.widget_4.setObjectName("widget_4")
        self.widget_5 = QtWidgets.QWidget(Form)
        self.widget_5.setGeometry(QtCore.QRect(0, 630, 645, 150))
        self.widget_5.setObjectName("widget_5")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 790, 100, 35))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(545, 790, 100, 35))
        self.pushButton_6.setObjectName("pushButton_6")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Справочник по лекарствам"))
        self.pushButton_4.setText(_translate("Form", "<--"))
        self.pushButton_5.setText(_translate("Form", "Назад<--"))
        self.pushButton_6.setText(_translate("Form", "Вперёд-->"))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(645, 369)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 20, 431, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 100, 131, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 190, 131, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 280, 131, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Справочник по лекарствам"))
        self.label.setText(_translate("MainWindow", "Справочник по лекарствам"))
        self.pushButton.setText(_translate("MainWindow", "Справочник"))
        self.pushButton_2.setText(_translate("MainWindow", "Добавить лекарство"))
        self.pushButton_3.setText(_translate("MainWindow", "Выход"))


# Отнаследуем наш класс от простейшего графического примитива QWidget
class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow,
        # остальное без изменений
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.exit)
        self.pushButton.clicked.connect(self.switch1)

    def exit(self):
        sys.exit(app.exec_())

    def switch1(self):
        self.sw = Second_Main()
        self.sw.show()
        self.hide()


class Second_Main(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_4.clicked.connect(self.back)
        _translate = QtCore.QCoreApplication.translate
        page = 0
        con = sqlite3.connect("medicine.db")
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM Main""").fetchall()
        if len(result) <= 5:
            self.pushButton_5.setEnabled(False)
            self.pushButton_6.setEnabled(False)
            for i in range(len(result)):
                photo = 'C:/Users/User/PycharmProjects/konkurs/medicine_photo/' + str(result[i][0]) + '.png'
                name = result[i][1]
                type = result[i][2]
                kolvo = result[i][3]
                if i == 0:
                    label = QLabel(self.widget)
                    pixmap = QtGui.QPixmap(photo)
                    label.setPixmap(pixmap)
                    self.label_1 = QtWidgets.QLabel(self.widget)
                    self.label_1.setGeometry(QtCore.QRect(180, 0, 431, 51))
                    self.label_1.setText(_translate("Widget", name))
                    font = QtGui.QFont()
                    font.setPointSize(12)
                    self.label_1.setFont(font)
                    self.label_2 = QtWidgets.QLabel(self.widget)
                    self.label_2.setGeometry(QtCore.QRect(180, 80, 431, 51))
                    self.label_2.setText(_translate("Widget", 'Тип: ' + type))
                    font = QtGui.QFont()
                    font.setPointSize(12)
                    self.label_2.setFont(font)
                    self.label_3 = QtWidgets.QLabel(self.widget)
                    self.label_3.setGeometry(QtCore.QRect(450, 80, 431, 51))
                    self.label_3.setText(_translate("Widget", 'Количество: ' + kolvo))
                    font = QtGui.QFont()
                    font.setPointSize(12)
                    self.label_3.setFont(font)
                elif i == 1:
                    label = QLabel(self.widget_2)
                    pixmap = QtGui.QPixmap(photo)
                    label.setPixmap(pixmap)
                    self.label_1 = QtWidgets.QLabel(self.widget_2)
                    self.label_1.setGeometry(QtCore.QRect(180, 0, 431, 51))
                    self.label_1.setText(_translate("Widget", name))
                    font = QtGui.QFont()
                    font.setPointSize(12)
                    self.label_1.setFont(font)
                    self.label_2 = QtWidgets.QLabel(self.widget_2)
                    self.label_2.setGeometry(QtCore.QRect(180, 80, 431, 51))
                    self.label_2.setText(_translate("Widget", 'Тип: ' + type))
                    font = QtGui.QFont()
                    font.setPointSize(12)
                    self.label_2.setFont(font)
                    self.label_3 = QtWidgets.QLabel(self.widget_2)
                    self.label_3.setGeometry(QtCore.QRect(450, 80, 431, 51))
                    self.label_3.setText(_translate("Widget", 'Количество: ' + kolvo))
                    font = QtGui.QFont()
                    font.setPointSize(12)
                    self.label_3.setFont(font)
                elif i == 2:
                    label = QLabel(self.widget_3)
                    pixmap = QtGui.QPixmap(photo)
                    label.setPixmap(pixmap)
                    self.label_1 = QtWidgets.QLabel(self.widget_3)
                    self.label_1.setGeometry(QtCore.QRect(180, 0, 431, 51))
                    self.label_1.setText(_translate("Widget", name))
                    font = QtGui.QFont()
                    font.setPointSize(12)
                    self.label_1.setFont(font)
                    self.label_2 = QtWidgets.QLabel(self.widget_3)
                    self.label_2.setGeometry(QtCore.QRect(180, 80, 431, 51))
                    self.label_2.setText(_translate("Widget", 'Тип: ' + type))
                    font = QtGui.QFont()
                    font.setPointSize(12)
                    self.label_2.setFont(font)
                    self.label_3 = QtWidgets.QLabel(self.widget_3)
                    self.label_3.setGeometry(QtCore.QRect(450, 80, 431, 51))
                    self.label_3.setText(_translate("Widget", 'Количество: ' + kolvo))
                    font = QtGui.QFont()
                    font.setPointSize(12)
                    self.label_3.setFont(font)
                elif i == 3:
                    label = QLabel(self.widget_4)
                    pixmap = QtGui.QPixmap(photo)
                    label.setPixmap(pixmap)
                    self.label_1 = QtWidgets.QLabel(self.widget_4)
                    self.label_1.setGeometry(QtCore.QRect(180, 0, 431, 51))
                    self.label_1.setText(_translate("Widget", name))
                    font = QtGui.QFont()
                    font.setPointSize(12)
                    self.label_1.setFont(font)
                    self.label_2 = QtWidgets.QLabel(self.widget_4)
                    self.label_2.setGeometry(QtCore.QRect(180, 80, 431, 51))
                    self.label_2.setText(_translate("Widget", 'Тип: ' + type))
                    font = QtGui.QFont()
                    font.setPointSize(12)
                    self.label_2.setFont(font)
                    self.label_3 = QtWidgets.QLabel(self.widget_4)
                    self.label_3.setGeometry(QtCore.QRect(450, 80, 431, 51))
                    self.label_3.setText(_translate("Widget", 'Количество: ' + kolvo))
                    font = QtGui.QFont()
                    font.setPointSize(12)
                    self.label_3.setFont(font)
                elif i == 4:
                    label = QLabel(self.widget_5)
                    pixmap = QtGui.QPixmap(photo)
                    label.setPixmap(pixmap)
                    self.label_1 = QtWidgets.QLabel(self.widget_5)
                    self.label_1.setGeometry(QtCore.QRect(180, 0, 431, 51))
                    self.label_1.setText(_translate("Widget", name))
                    font = QtGui.QFont()
                    font.setPointSize(12)
                    self.label_1.setFont(font)
                    self.label_2 = QtWidgets.QLabel(self.widget_5)
                    self.label_2.setGeometry(QtCore.QRect(180, 80, 431, 51))
                    self.label_2.setText(_translate("Widget", 'Тип: ' + type))
                    font = QtGui.QFont()
                    font.setPointSize(12)
                    self.label_2.setFont(font)
                    self.label_3 = QtWidgets.QLabel(self.widget_5)
                    self.label_3.setGeometry(QtCore.QRect(450, 80, 431, 51))
                    self.label_3.setText(_translate("Widget", 'Количество: ' + kolvo))
                    font = QtGui.QFont()
                    font.setPointSize(12)
                    self.label_3.setFont(font)


    def back(self):
        self.mm = Main()
        self.mm.show()
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec_())
