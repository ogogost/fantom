import sqlite3 as sl
from PyQt5 import QtCore, QtWidgets
import sys
import os
from datetime import datetime, date, time

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
        # self.label = QtWidgets.QTableWidget(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 40, 400, 400))
        self.label.setFrameShape(QtWidgets.QFrame.Panel)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setStyleSheet('background-color: white')
        # self.label.setPixmap(QtGui.QPixmap(source))
        self.label.setObjectName("label")


        self.status_monitor = QtWidgets.QLabel(self.centralwidget)
        self.status_monitor.setGeometry(200, 600, 500, 400)
        self.status_monitor.setFrameShape(QtWidgets.QFrame.Panel)
        self.status_monitor.setFrameShadow(QtWidgets.QFrame.Plain)


        # button 1
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(1500, 800, 200, 100))
        self.pushButton_1.setText("Exit")

        # button 2
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 40, 200, 30))
        self.pushButton_2.setText("Создание БД")

        # button 3
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 80, 200, 30))
        self.pushButton_3.setText("Создание таблицы ордеров")

        # button 4
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(700, 40, 200, 30))
        self.pushButton_4.setText("Запись в таблицу заявок пресета")

        # button 5
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(700, 80, 200, 30))
        self.pushButton_5.setText("Вывод таблицы ордеров")

        # button 6
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(40, 280, 200, 30))
        self.pushButton_6.setText("Удаление таблицы ордеров")

        # button 7
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(40, 320, 200, 30))
        self.pushButton_7.setText("Удаление БД")

        # button 8
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(700, 430, 200, 30))
        self.pushButton_8.setText("Добавка строки")

        # button 9
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(340, 460, 200, 30))
        self.pushButton_9.setText("Сортировка")

        # qline1
        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_1.setGeometry(QtCore.QRect(750, 130, 150, 30))
        self.lineEdit_1.setText("John")
        # self.lineEdit_1.setInputMask('HHH:HHH')
        self.lineEdit_1.setMaxLength(100)
        self.label_of_lineEdit_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_of_lineEdit_1.setText("Name_of_client")
        self.label_of_lineEdit_1.setGeometry(QtCore.QRect(660,130,80,20))
        self.label_of_lineEdit_1.setStyleSheet('border-style: solid; border-width: 1px; border-color: black;')

        # qline2
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(750, 170, 150, 30))
        self.lineEdit_2.setText("Market")
        self.lineEdit_2.setMaxLength(100)
        self.label_of_lineEdit_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_of_lineEdit_2.setText("Order_type")
        self.label_of_lineEdit_2.setGeometry(QtCore.QRect(660, 170, 80, 20))
        self.label_of_lineEdit_2.setStyleSheet('border-style: solid; border-width: 1px; border-color: black;')

        # radiobuttons for 'Market/Limit'
        self.label_for_radiobutton_ML_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_for_radiobutton_ML_1.setGeometry(760, 200, 100, 20)
        self.label_for_radiobutton_ML_1.setText('Market')
        self.radiobutton_ML_1 = QtWidgets.QRadioButton(self.centralwidget)
        self.radiobutton_ML_1.setGeometry(800, 200, 20, 20)
        self.label_for_radiobutton_ML_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_for_radiobutton_ML_2.setGeometry(840, 200, 100, 20)
        self.label_for_radiobutton_ML_2.setText('Limit')
        self.radiobutton_ML_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radiobutton_ML_2.setGeometry(870, 200, 20, 20)

        # qline3
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(750, 230, 150, 30))
        self.lineEdit_3.setText("BUY")
        self.lineEdit_3.setMaxLength(100)
        self.label_of_lineEdit_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_of_lineEdit_3.setText("BUY_SELL")
        self.label_of_lineEdit_3.setGeometry(QtCore.QRect(660, 230, 80, 20))
        self.label_of_lineEdit_3.setStyleSheet('border-style: solid; border-width: 1px; border-color: black;')

        # radiobuttons for 'Buy/Sell'
        self.label_for_radiobutton_BS_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_for_radiobutton_BS_1.setGeometry(770, 260, 100, 20)
        self.label_for_radiobutton_BS_1.setText('BUY')
        self.radiobutton_BS_1 = QtWidgets.QRadioButton(self.centralwidget)
        self.radiobutton_BS_1.setGeometry(800, 260, 20, 20)
        self.label_for_radiobutton_BS_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_for_radiobutton_BS_2.setGeometry(840, 260, 100, 20)
        self.label_for_radiobutton_BS_2.setText('SELL')
        self.radiobutton_BS_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radiobutton_BS_2.setGeometry(870, 260, 20, 20)

        # qline4
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(750, 280, 150, 30))
        self.lineEdit_4.setText("1000")
        self.lineEdit_4.setMaxLength(100)
        self.label_of_lineEdit_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_of_lineEdit_4.setText("Price")
        self.label_of_lineEdit_4.setGeometry(QtCore.QRect(660, 280, 80, 20))
        self.label_of_lineEdit_4.setStyleSheet('border-style: solid; border-width: 1px; border-color: black;')


        # qline5
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(750, 320, 150, 30))
        self.lineEdit_5.setText("6")
        self.lineEdit_5.setMaxLength(100)
        self.label_of_lineEdit_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_of_lineEdit_5.setText("Amount")
        self.label_of_lineEdit_5.setGeometry(QtCore.QRect(660, 320, 80, 20))
        self.label_of_lineEdit_5.setStyleSheet('border-style: solid; border-width: 1px; border-color: black;')


        # qline6
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(750, 360, 150, 40))
        self.lineEdit_6.setText("YANDEX")
        self.lineEdit_6.setMaxLength(100)
        self.label_of_lineEdit_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_of_lineEdit_6.setText("Ticker")
        self.label_of_lineEdit_6.setGeometry(QtCore.QRect(660, 360, 80, 20))
        self.label_of_lineEdit_6.setStyleSheet('border-style: solid; border-width: 1px; border-color: black;')


        # раздел с таблицей клиентов

        # кнопка создания таблицы клиентов
        self.pushButton_create_t_o_c = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_create_t_o_c.setGeometry(1000, 40, 130, 40)
        self.pushButton_create_t_o_c.setText('Создание таблицы \n клиентов')

        # экран таблицы клиентов

        self.label_toc = QtWidgets.QLabel(self.centralwidget)
        self.label_toc.setGeometry(QtCore.QRect(1150,40, 400, 300))
        self.label_toc.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_toc.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_toc.setStyleSheet('background-color: white')
        # self.label.setPixmap(QtGui.QPixmap(source))

        # кнопка вывода данных таблицы клиентов
        self.pushButton_show_toc = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_show_toc.setGeometry(1000, 90, 130, 40)
        self.pushButton_show_toc.setText('Вывод данных \n таблицы клиентов')

        # insert preset data to table of clients button
        self.pushButton_add_preset_toc = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add_preset_toc.setGeometry(1000, 140, 130, 40)
        self.pushButton_add_preset_toc.setText('Ввод данных \n preset')

        # delete table of clients
        self.pushButton_delete_toc = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_delete_toc.setGeometry(1000, 190, 130, 40)
        self.pushButton_delete_toc.setText('Удаление таблицы \n клиентов')


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
        self.ui.lineEdit_1.editingFinished.connect(self.lineEdit_1_event)
        self.ui.pushButton_8.clicked.connect(self.add_data_to_table)
        # self.ui.pushButton_8.clicked.connect(self.lineEdit_1_event)
        # self.ui.pushButton_8.clicked.connect(self.add_data_to_table(4, 'M', 'market', 'buy', 800, 5, 'YNDX', 'time'))
        self.ui.pushButton_9.clicked.connect(self.sort_too)
        self.ui.pushButton_create_t_o_c.clicked.connect(self.create_table_of_clients_function)
        self.ui.pushButton_show_toc.clicked.connect(self.show_toc_func)
        self.ui.pushButton_add_preset_toc.clicked.connect(self.add_preset_toc)
        self.ui.pushButton_delete_toc.clicked.connect(self.del_toc)


        self.ui.radiobutton_ML_1.toggled.connect(self.rb_ml_1)
        self.ui.radiobutton_ML_2.toggled.connect(self.rb_ml_2)
        self.ui.radiobutton_BS_1.toggled.connect(self.rb_bs_1)
        self.ui.radiobutton_BS_2.toggled.connect(self.rb_bs_2)

        self.initUi()

    def del_toc(self):
        con = sl.connect(data_base_path)
        cur = con.cursor()
        try:
            cur.execute("DROP TABLE TABLE_OF_CLIENTS")
            con.close()
            self.statusBar().showMessage('Table of clients IS ERASED')
        except Exception as e:
            print(e)
            self.statusBar().showMessage(str(e))

    def add_preset_toc(self):
        con = sl.connect(data_base_path)
        cursor = con.cursor()

        try:
            sql = 'INSERT INTO TABLE_OF_CLIENTS (id, name_client, cash, amount, ticker, datetime) values(null, ?, ?, ?, ?, ?)'
            data = [('Alice', 1000000000, 1000, 'YNDX', datetime.today()),
                    ('Bob', 2000000, 1100, 'YNDX', datetime.today()),
                    ('Mikle', 9000000, 800, 'YNDX', datetime.today())]
            with con:
                con.executemany(sql, data)
            self.statusBar().showMessage('INSERT executed succesful')
        except Exception as e:
            print(e)
            self.statusBar().showMessage(str(e))

        try:
            cursor.execute("SELECT * FROM TABLE_OF_CLIENTS")
            product = cursor.fetchall()  # вытаскиваем содержимое бд в виде списка
            a = '\n'.join(map(str, product))  # разбиваем список переносом строки
            self.ui.label_toc.setText(a)
            self.statusBar().showMessage('DATA IS SHOWED')
        except Exception as e:
            print(e)
            self.statusBar().showMessage(str(e))

        con.close()


    def show_toc_func(self):
        con = sl.connect(data_base_path)
        cursor = con.cursor()
        try:
            cursor.execute("SELECT * FROM TABLE_OF_CLIENTS")
            product = cursor.fetchall()  # вытаскиваем содержимое бд в виде списка
            a = '\n'.join(map(str, product))  # разбиваем список переносом строки
            self.ui.label_toc.setText(a)
            self.statusBar().showMessage('DATA IS SHOWED')
        except Exception as e:
            print(e)
            self.statusBar().showMessage(str(e))
        con.close()



    def create_table_of_clients_function(self):
        con = sl.connect(data_base_path)
        # cursor = con.cursor()
        try:
            con.execute("""CREATE TABLE TABLE_OF_CLIENTS (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                name_client TEXT,
                cash INTEGER,
                amount INTEGER,
                ticker TEXT,
                datetime timestamp)""")
            self.statusBar().showMessage('Create table_of_clients executed succesful')
        except Exception as e:
            print(e)
            self.statusBar().showMessage(str(e))
        con.commit()
        con.close()

    def sort_too(self):
        con = sl.connect(data_base_path)
        cursor = con.cursor()
        try:
            cursor.execute("SELECT * FROM TABLE_OF_ORDERS")
            product = cursor.fetchall()  # вытаскиваем содержимое бд в виде списка
            buy_list = [] # создаём пустые списки
            sell_list = [] # создаём пустые списки
            for i in product: # цикл добавляет строки из бд по наличию слова BUY в списке
                if i[3] == 'BUY':
                    buy_list.append(i)
                else:
                    sell_list.append(i)

            # сортируем каждый список по величине цены
            buy_list_sorted = sorted(buy_list, key=lambda buy_list:buy_list[4], reverse=True)
            sell_list_sorted = sorted(sell_list, key=lambda sell_list:sell_list[4])

            def fun(v):  # вспомогательная функция для сортировки заявок
                return (v[4], v[7])
            buy_list_sorted.sort(key=fun)
            sell_list_sorted.sort(key=fun)

            a = '\n'.join(map(str, buy_list_sorted))
            b = '\n'.join(map(str, sell_list_sorted))

            self.ui.status_monitor.setText(str(a) + '\n' + str(b))
            # self.ui.status_monitor.setText(str(product))
            con.commit()
            con.close()

            self.statusBar().showMessage('table_of_orders is sorted')

        except Exception as e:
            print(e)
            self.statusBar().showMessage(str(e))
        con.close()
    def rb_ml_1(self):
        self.ui.lineEdit_2.setText('Market')
    def rb_ml_2(self):
        self.ui.lineEdit_2.setText('Limit')

    def rb_bs_1(self):
        self.ui.lineEdit_3.setText('BUY')
    def rb_bs_2(self):
        self.ui.lineEdit_3.setText('SELL')


    def lineEdit_1_event(self):
        self.statusBar().showMessage(str(self.ui.lineEdit_1.text()))


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
                name_client TEXT,
                order_type TEXT,
                buy_sell TEXT,
                price INTEGER,
                amount INTEGER,
                ticker TEXT,
                datetime timestamp)""")
            self.statusBar().showMessage('Create executed succesful')
        except Exception as e:
            print(e)
            self.statusBar().showMessage(str(e))
        con.commit()
        con.close()

    def create_data_function(self):
        con = sl.connect(data_base_path)
        try:
            sql = 'INSERT INTO TABLE_OF_ORDERS (id, name_client, order_type, buy_sell, price, amount, ticker, datetime) values(null, ?, ?, ?, ?, ?, ?, ?)'
            data = [('Alice', 'market', 'BUY', 900, 10, 'YNDX', datetime.today()),
                    ('Bob', 'market', 'SELL', 1100, 1, 'YNDX', datetime.today()),
                    ('Mikle', 'market', 'BUY', 800, 5, 'YNDX', datetime.today())]
            with con:
                con.executemany(sql, data)
            self.statusBar().showMessage('INSERT executed succesful')
        except Exception as e:
            print(e)
            self.statusBar().showMessage(str(e))
        con.close()

    def add_data_to_table(self):
        name_client = self.ui.lineEdit_1.text()
        order_type = self.ui.lineEdit_2.text()
        buy_sell =self.ui.lineEdit_3.text()
        price = self.ui.lineEdit_4.text()
        amount = self.ui.lineEdit_5.text()
        ticker = self.ui.lineEdit_6.text()

        con = sl.connect(data_base_path)
        cursor = con.cursor()

        try:
            sql = 'INSERT INTO TABLE_OF_ORDERS (id, name_client, order_type, buy_sell, price, amount, ticker, datetime) values(null, ?, ?, ?, ?, ?, ?, ?)'
            data = [(name_client, order_type, buy_sell, price, amount, ticker, datetime.today())]
            con.executemany(sql, data)
            cursor.execute("SELECT * FROM TABLE_OF_ORDERS")
            product = cursor.fetchall()  # вытаскиваем содержимое бд в виде списка
            a = '\n'.join(map(str, product))  # разбиваем список переносом строки
            self.ui.label.setText(a)
            con.commit()
            con.close()
            # show_data_function(self)

            self.statusBar().showMessage('INSERT of DATA succesful' + str(data))

        except Exception as e:
            print(e)
            self.statusBar().showMessage(str(e))
        con.close()


    def show_data_function(self):
        con = sl.connect(data_base_path)
        cursor = con.cursor()
        try:
            cursor.execute("SELECT * FROM TABLE_OF_ORDERS")
            product = cursor.fetchall() # вытаскиваем содержимое бд в виде списка
            a = '\n'.join(map(str, product)) # разбиваем список переносом строки
            self.ui.label.setText(a)
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


    def status_monitor(self):
        con = sl.connect(data_base_path)
        cursor = con.cursor()
        try:
            cursor.execute("SELECT * FROM TABLE_OF_ORDERS")
            product = cursor.fetchall()
            self.ui.status_monitor.setText(str(product))
            # self.statusBar().showMessage('DATA IS SHOWED')
        except Exception as e:
            print(e)
            # self.statusBar().showMessage(str(e))
        con.close()




app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())







