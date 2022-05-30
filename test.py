import sqlite3 as sl
from PyQt5 import QtCore, QtWidgets
import sys
import os

# Variables
data_base_path = 'test.db'


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.showFullScreen()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 500, 100))
        self.label.setFrameShape(QtWidgets.QFrame.Panel)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setStyleSheet('background-color: white')
        # self.label.setPixmap(QtGui.QPixmap(source))
        self.label.setObjectName("label")

        # button 1
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(1800, 1000, 100, 50))
        self.pushButton_1.setText("Exit")

        # button 2
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 120, 100, 30))
        self.pushButton_2.setText("Создание БД")

        # button 3
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 160, 100, 30))
        self.pushButton_3.setText("Создание таблицы")

        # button 4
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(40, 200, 100, 30))
        self.pushButton_4.setText("Запись в таблицу")

        # button 5
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(40, 240, 100, 30))
        self.pushButton_5.setText("Вывод таблицы")

        # button 6
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(40, 280, 100, 30))
        self.pushButton_6.setText("Удаление таблицы")

        # button 7
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(40, 320, 100, 30))
        self.pushButton_7.setText("Удаление БД")

        # button 8
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(40, 360, 100, 30))
        self.pushButton_8.setText("Добавка строки")

        # qline
        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_1.setGeometry(QtCore.QRect(190, 120, 200, 40))
        self.lineEdit_1.setText("Variable1")
        self.lineEdit_1.setMaxLength(20)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

class mywindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_1.clicked.connect(self.exit_function)
        self.ui.pushButton_2.clicked.connect(self.create_db_function)
        self.ui.pushButton_3.clicked.connect(self.create_table_function)
        self.ui.pushButton_4.clicked.connect(self.create_data_function)
        self.ui.pushButton_5.clicked.connect(self.show_data_function)
        self.ui.pushButton_6.clicked.connect(self.erase_db_table_function)
        self.ui.pushButton_7.clicked.connect(self.erase_db_function)
        self.ui.lineEdit_1.editingFinished(self.lineEdit_1_event)
        # self.ui.pushButton_8.clicked.connect(self.add_data_to_table)
        # self.ui.pushButton_8.clicked.connect(self.add_data_to_table(4, 'M', 'market', 'buy', 800, 5, 'YNDX', 'time'))
        self.initUi()

    def lineEdit_1_event(self):
        self.


    def initUi(self):
        self.statusBar().showMessage('Ready')

    def exit_function(self):
        sys.exit()

    def create_db_function(self):
        con = sl.connect(data_base_path)
        self.statusBar().showMessage(str((con)) + 'path:' + data_base_path)
        con.close()

    def create_table_function(self):
        con = sl.connect(data_base_path)
        # cursor = con.cursor()
        try:
            con.execute("""CREATE TABLE TABLE_OF_ORDERS (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                id_client TEXT,
                order_type TEXT,
                buy_sell TEXT,
                price INTEGER,
                amount INTEGER,
                ticker TEXT,
                time INTEGER)""")
            self.statusBar().showMessage('Create executed succesful')
        except Exception as e:
            print(e)
            self.statusBar().showMessage(str(e))
        con.commit()
        con.close()

    def create_data_function(self):
        con = sl.connect(data_base_path)
        try:
            sql = 'INSERT INTO TABLE_OF_ORDERS (id, id_client, order_type, buy_sell, price, amount, ticker, time) values(?, ?, ?, ?, ?, ?, ?, ?)'
            data = [(1, 'Alice', 'market', 'buy', 900, 10, 'YNDX', 'time'),
                    (2, 'Bob', 'market', 'sell', 1100, 1, 'YNDX', 'time'),
                    (3, 'Mikle', 'market', 'buy', 800, 5, 'YNDX', 'time')]
            with con:
                con.executemany(sql, data)
            self.statusBar().showMessage('INSERT executed succesful')
        except Exception as e:
            print(e)
            self.statusBar().showMessage(str(e))
        con.close()

    def add_data_to_table(self, number_of_order, id_client, order_type, buy_sell, price, amount, ticker, time):

        con = sl.connect(data_base_path)
        try:
            sql = 'INSERT INTO TABLE_OF_ORDERS (id, id_client, order_type, buy_sell, price, amount, ticker, time) values(?, ?, ?, ?, ?, ?, ?, ?)'
            data = [(number_of_order, id_client, order_type, buy_sell, price, amount, ticker, time)]
            con.executemany(sql, data)
            self.statusBar().showMessage('INSERT of DATA succesful' + data)

        except Exception as e:
            print(e)
            self.statusBar().showMessage(str(e))
        con.close()


    def show_data_function(self):
        con = sl.connect(data_base_path)
        cursor = con.cursor()
        try:
            cursor.execute("SELECT * FROM TABLE_OF_ORDERS")
            product = cursor.fetchall()
            self.ui.label.setText(str(product))
            self.statusBar().showMessage('DATA IS SHOWED')
        except Exception as e:
            print(e)
            self.statusBar().showMessage(str(e))
        con.close()

    def erase_db_table_function(self):
        con = sl.connect(data_base_path)
        cur = con.cursor()
        try:
            cur.execute("DROP TABLE TABLE_OF_ORDERS")
            con.close()
            self.statusBar().showMessage('Table IS ERASED')
        except Exception as e:
            print(e)
            self.statusBar().showMessage(str(e))

    def erase_db_function(self):
        try:
            os.remove(data_base_path)
            self.statusBar().showMessage('DB IS ERASED' +" File: " + data_base_path)

        except Exception as e:
            print(e)
            self.statusBar().showMessage(str(e))


app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())







