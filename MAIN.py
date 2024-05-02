import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt
import logging
from time import strftime, localtime, sleep
import keyboard
import pyautogui
from python_imagesearch.imagesearch import imagesearch_numLoop
import resources
from win10toast import ToastNotifier
import configparser, os

logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(200, 140)
        MainWindow.setMinimumSize(QtCore.QSize(200, 140))
        MainWindow.setMaximumSize(QtCore.QSize(200, 140))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/112.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(20, 110, 75, 23))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 110, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.ch_label_1 = QtWidgets.QCheckBox(self.centralwidget)
        self.ch_label_1.setGeometry(QtCore.QRect(10, 85, 181, 16))
        self.ch_label_1.setObjectName("chbox_1")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(10, 0, 181, 16))
        self.label_1.setObjectName("label_1")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 60, 181, 16))
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 181, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 181, 16))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.centralwidget.window().setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowSystemMenuHint)


        keyboard.add_hotkey('alt+z',self.del_user)

        self.i = 0
        self.j = 0
        self.i1 =0
        self.x = self.centralwidget.window().pos().x()
        self.y = self.centralwidget.window().pos().y()

        self.config = configparser.ConfigParser()


        if not os.path.exists('settings.ini'):
            self.config['General'] = {'i': '0', 'j': '0'}
            with open('settings.ini', 'w') as configfile:
                self.config.write(configfile)
        else:
            self.config.read('settings.ini')
            self.i = int(self.config['General']['i'])
            self.j = int(self.config['General']['j'])
            self.x = int(self.config['General']['x'])
            self.y = int(self.config['General']['y'])
            self.centralwidget.window().move(self.x,self.y)

        self.retranslateUi(MainWindow)
        self.pushButton_1.clicked.connect(self.hide_to_tray)  # type: ignore
        self.pushButton_2.clicked.connect(self.stop)
        self.ch_label_1.clicked.connect((self.top))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Удаление абонентов"))
        self.pushButton_1.setText(_translate("MainWindow", "В трей"))
        self.pushButton_2.setText(_translate("MainWindow", "Выход"))
        self.label_1.setText(_translate("MainWindow", "Запуск по клавишам ALT+Z"))
        self.label_2.setText(_translate("MainWindow", "Сколько раз запустили: " + str(self.i)))
        self.label_3.setText(_translate("MainWindow", "Успешных удалений: " + str(self.j)))
        self.label_4.setText(_translate("MainWindow", "Удалено сегодня: " + str(self.i1)))
        self.ch_label_1.setText(_translate("MaimWindow", "Поверх всех окон"))

    def top(self):
        if self.ch_label_1.isChecked():
            self.centralwidget.window().setWindowFlags(self.centralwidget.window().windowFlags() | Qt.WindowStaysOnTopHint)
        else:
            self.centralwidget.window().setWindowFlags(self.centralwidget.window().windowFlags() & ~Qt.WindowStaysOnTopHint)
        self.centralwidget.window().show()
    def stop(self):
        self.config['General']['i'] = str(self.i)
        self.config['General']['j'] = str(self.j)
        self.config['General']['x'] = str(self.centralwidget.window().pos().x())
        self.config['General']['y'] = str(self.centralwidget.window().pos().y())
        with open('settings.ini', 'w') as configfile:
            self.config.write(configfile)
        QtWidgets.QApplication.quit()

    def hide_to_tray(self):
        self.centralwidget.window().hide()
        self.tray_icon.show()

    def show_from_tray(self):
        self.centralwidget.window().show()
        self.tray_icon.hide()

    def del_user(self):
        print("push start")
        self.i += 1
        self.label_2.setText("Сколько раз запустили: " + str(self.i))
        def locate_and_click(image_path):
            pos = imagesearch_numLoop(image_path, 0.2, 7)
            if pos[0] != -1:
                print("position: ", pos[0], pos[1])
                logging.info("position: %s, %s", pos[0], pos[1])
                pyautogui.click(pos[0] + 5, pos[1] + 5)
                sleep(0.5)
                return True
            else:
                print(" Изображение не найдено")
                logging.warning("Изображение не найдено")
                sleep(0.5)
                return False
        #while True:
        print("Начало цикла, для запуска использовать ALT+Z")
        #keyboard.wait('Alt + Z')
        sleep(0.5)
        logging.info("--------Начало цикла--------")
        # sleep(1)
        if locate_and_click("pict/is1.png"):
            # print("Найдена картинка Изменить свойства, кликаем на него")
            logging.info("Найдена картинка Изменить свойства, кликаем на него")
            if locate_and_click("pict/zpp1.png"):
                # print("Нашли запрет приема платежей без галочки, кликаем по нему")
                logging.info("Нашли запрет приема платежей без галочки, кликаем по нему")
                pyautogui.scroll(-400)
                sleep(0.5)
                # print("Скролим вниз страницы")
                logging.info("Скролим вниз страницы")
                if locate_and_click("pict/save.png"):
                    # print("Нашли сохранить и кликнули по ней")
                    logging.info("Нашли сохранить и кликнули по ней")
                    if locate_and_click("pict/is1.png"):
                        # print("Нашли свойства 2")
                        logging.info("Нашли свойства 2")
                        if locate_and_click("pict/ik1.png"):
                            # print("Нашли изменение класса и кликнули по нему")
                            logging.info("Нашли изменение класса и кликнули по нему")
                            if locate_and_click("pict/del.png"):
                                # print("Нашли кнопку удаление и кликаем по ней")
                                logging.info("Нашли кнопку удаление и кликаем по ней")
                                if locate_and_click("pict/oi1.png"):
                                    # print("Нашли основную информацию, кликаем на нее")
                                    logging.info("Нашли основную информацию, кликаем на нее")
                                    logging.info("Скриншот удаленной учетки")
                                    sleep(0.5)
                                    pyautogui.screenshot(
                                        'screen/' + strftime('%Y-%m-%d_%H.%M.%S', localtime()) + '.jpg')
                                    self.j += 1
                                    self.label_3.setText("Успешных удалений: " + str(self.j))
                                    self.i1 += 1
                                    self.label_4.setText("Удалений за сеанс: " + str(self.i1))
                                    self.toast = ToastNotifier()
                                    self.toast.show_toast("Удаление абонента", "Удаление абонента прошло успешно",
                                                     duration=3, icon_path="113.ico")
                                    #self.i += 1
                                    #self.label_2.setText("Удалили абонентов: " + str(self.i) + " раз")
                                else:
                                    # print("Не найдена основная информация")
                                    logging.error("Не найдена основная информация")
                                    pyautogui.screenshot(
                                        'screen/' + "Ошибка 6 _ " + strftime('%Y-%m-%d_%H.%M.%S',
                                                                             localtime()) + '.jpg')
                            else:
                                # print("Не найдена кнопка удаления")
                                logging.error("Не найдена кнопка удаления")
                                pyautogui.screenshot(
                                    'screen/' + "Ошибка 6 _ " + strftime('%Y-%m-%d_%H.%M.%S',
                                                                         localtime()) + '.jpg')
                        else:
                            # print("Не найдено изменение класса")
                            logging.error("Не найдено изменение класса")
                            pyautogui.screenshot(
                                'screen/' + "Ошибка 5 _ " + strftime('%Y-%m-%d_%H.%M.%S', localtime()) + '.jpg')
                    else:
                        # print("Не нашли свойства 2")
                        logging.error("Не нашли свойства 2")
                        pyautogui.screenshot(
                            'screen/' + "Ошибка 4 _ " + strftime('%Y-%m-%d_%H.%M.%S', localtime()) + '.jpg')
                else:
                    # print("Не нашли кнопку сохранить")
                    logging.error("Не нашли кнопку сохранить")
                    pyautogui.screenshot(
                        'screen/' + "Ошибка 3 _ " + strftime('%Y-%m-%d_%H.%M.%S', localtime()) + '.jpg')
            else:
                # print("не найдена картинка пустой запрет платежей")
                logging.error("не найдена картинка пустой запрет платежей")
                pyautogui.screenshot(
                    'screen/' + "Ошибка 2 _ " + strftime('%Y-%m-%d_%H.%M.%S', localtime()) + '.jpg')
        else:
            # print("не найдена картинка изменить свойства")
            logging.error("не найдена картинка изменить свойства")
            pyautogui.screenshot(
                'screen/' + "Ошибка 1 _ " + strftime('%Y-%m-%d_%H.%M.%S', localtime()) + '.jpg')

def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.tray_icon = QtWidgets.QSystemTrayIcon(MainWindow)  # Создаем иконку в трее
    ui.tray_icon.setIcon(QtGui.QIcon(":/icons/112.png"))  # Укажите путь к вашей иконке
    ui.tray_icon.setVisible(False)
    ui.tray_icon.activated.connect(ui.show_from_tray)  # Подключаем иконку в трей к функции отображения окна
    MainWindow.show()
    #Ui_MainWindow.stop
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()