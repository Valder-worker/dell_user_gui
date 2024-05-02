from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(200, 110)
        MainWindow.setMinimumSize(QtCore.QSize(200, 110))
        MainWindow.setMaximumSize(QtCore.QSize(200, 110))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(20, 75, 75, 23))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 75, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_1 = QtWidgets.QCheckBox(self.centralwidget)
        #self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(10, 10, 181, 16))
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 181, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 181, 16))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.i = 0

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_function()

    #def del_user(self):

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Удаление абонентов"))
        self.pushButton_1.setText(_translate("MainWindow", "Запустить"))
        self.pushButton_2.setText(_translate("MainWindow", "Остановить"))
        self.label_1.setText(_translate("MainWindow", "Циклировать"))
        self.label_2.setText(_translate("MainWindow", "TextLabel_2"))
        self.label_3.setText(_translate("MainWindow", "TextLabel_3"))
    def add_function(self):
        self.pushButton_1.clicked.connect(self.del_user)

    def del_user(self):
        self.i += 1
        self.label_2.setText("Нажали "+ str(self.i) + " раз")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
