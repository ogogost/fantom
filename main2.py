import sqlite3 as sl
import sys
import os
import logging

from datetime import datetime
from PyQt5 import QtCore, QtWidgets

# Variables
data_base_path = 'test.db'

data_combobox = (['111', '222'])

logging.basicConfig(
    level=logging.DEBUG,
    filename="mylog.log",
    format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
    datefmt='%H:%M:%S',
)

logging.info('Start script')


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.showFullScreen()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 40, 400, 400))
        self.label.setFrameShape(QtWidgets.QFrame.Panel)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setStyleSheet('background-color: white')
        self.label.setObjectName("label")

        self.status_monitor = QtWidgets.QLabel(self.centralwidget)
        self.status_monitor.setGeometry(20, 600, 500, 400)
        self.status_monitor.setFrameShape(QtWidgets.QFrame.Panel)
        self.status_monitor.setFrameShadow(QtWidgets.QFrame.Plain)

        # button 1
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(1700, 950, 200, 100))
        self.pushButton_1.setStyleSheet("background-color: pink")
        self.pushButton_1.setText("Exit")

        # button 2
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 40, 130, 30))
        self.pushButton_2.setStyleSheet("background-color: cyan")
        self.pushButton_2.setText("Создание БД")

        # button 3
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 80, 130, 30))
        self.pushButton_3.setStyleSheet("background-color: cyan")
        self.pushButton_3.setText("Создание таблицы \n ордеров")

        # button 4
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(700, 40, 130, 30))
        self.pushButton_4.setText("Запись в таблицу \n заявок пресета")

        # button 5
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(700, 80, 130, 30))
        self.pushButton_5.setText("Вывод таблицы \n ордеров")

        # button 6
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(40, 280, 130, 30))
        self.pushButton_6.setStyleSheet("background-color: pink")
        self.pushButton_6.setText("Удаление таблицы \n ордеров")

        # button 7
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(40, 320, 130, 30))
        self.pushButton_7.setStyleSheet("background-color: pink")
        self.pushButton_7.setText("Удаление БД")

        # button 8
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(700, 430, 130, 30))
        self.pushButton_8.setText("Добавка строки")

        # button 9
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(340, 460, 130, 30))
        self.pushButton_9.setText("Сортировка")

        # button 10
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(340, 500, 130, 30))
        self.pushButton_10.setText("Транзакция")

        # qline1
        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_1.setGeometry(QtCore.QRect(750, 130, 150, 30))
        self.lineEdit_1.setText("John")
        self.lineEdit_1.setMaxLength(100)
        self.label_of_lineEdit_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_of_lineEdit_1.setText("Name_of_client")
        self.label_of_lineEdit_1.setGeometry(QtCore.QRect(660, 130, 80, 20))
        self.label_of_lineEdit_1.setStyleSheet('border-style: solid; border-width: 1px; border-color: black;')

        # # combobox
        # self.combo = QtWidgets.QComboBox(self.centralwidget)
        # self.combo.setGeometry(750, 130, 150, 30)
        # self.combo.setEditable(True)
        # self.combo.addItems(data_combobox)
        # self.combo.setStyleSheet('QCombobox {background-color: white; color: black}')

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
        self.lineEdit_6.setGeometry(QtCore.QRect(750, 360, 150, 30))
        self.lineEdit_6.setText("YNDX")
        self.lineEdit_6.setMaxLength(100)
        self.label_of_lineEdit_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_of_lineEdit_6.setText("Ticker")
        self.label_of_lineEdit_6.setGeometry(QtCore.QRect(660, 360, 80, 20))
        self.label_of_lineEdit_6.setStyleSheet('border-style: solid; border-width: 1px; border-color: black;')

        # раздел с таблицей клиентов

        # кнопка создания таблицы клиентов
        self.pushButton_create_clients = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_create_clients.setGeometry(1000, 40, 130, 40)
        self.pushButton_create_clients.setStyleSheet("background-color: cyan")
        self.pushButton_create_clients.setText('Создание таблицы \n клиентов')

        # экран таблицы клиентов

        self.label_CLIENTS = QtWidgets.QLabel(self.centralwidget)
        self.label_CLIENTS.setGeometry(QtCore.QRect(1150, 40, 400, 300))
        self.label_CLIENTS.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_CLIENTS.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_CLIENTS.setStyleSheet('background-color: white')
        # self.label.setPixmap(QtGui.QPixmap(source))

        # кнопка вывода данных таблицы клиентов
        self.pushButton_show_CLIENTS = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_show_CLIENTS.setGeometry(1000, 90, 130, 40)
        self.pushButton_show_CLIENTS.setText('Вывод данных \n таблицы клиентов')

        # insert preset data to table of clients button
        self.pushButton_add_preset_CLIENTS = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add_preset_CLIENTS.setGeometry(1000, 140, 130, 40)
        self.pushButton_add_preset_CLIENTS.setText('Ввод данных \n preset')

        # delete table of clients
        self.pushButton_delete_CLIENTS = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_delete_CLIENTS.setGeometry(1000, 190, 130, 40)
        self.pushButton_delete_CLIENTS.setStyleSheet("background-color: pink")
        self.pushButton_delete_CLIENTS.setText('Удаление таблицы \n клиентов')

        # qline name of client
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(1700, 40, 150, 30))
        self.lineEdit_7.setText("Name")
        self.lineEdit_7.setMaxLength(100)
        self.label_of_lineEdit_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_of_lineEdit_7.setText("Name of client")
        self.label_of_lineEdit_7.setGeometry(QtCore.QRect(1600, 40, 80, 20))
        self.label_of_lineEdit_7.setStyleSheet('border-style: solid; border-width: 1px; border-color: black;')

        # qline cash
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(1700, 80, 150, 30))
        self.lineEdit_8.setText("0")
        self.lineEdit_8.setMaxLength(100)
        self.label_of_lineEdit_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_of_lineEdit_8.setText("Cash")
        self.label_of_lineEdit_8.setGeometry(QtCore.QRect(1600, 80, 80, 20))
        self.label_of_lineEdit_8.setStyleSheet('border-style: solid; border-width: 1px; border-color: black;')

        # qline amount
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(1700, 120, 150, 30))
        self.lineEdit_9.setText("0")
        self.lineEdit_9.setMaxLength(100)
        self.label_of_lineEdit_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_of_lineEdit_9.setText("Amount")
        self.label_of_lineEdit_9.setGeometry(QtCore.QRect(1600, 120, 80, 20))
        self.label_of_lineEdit_9.setStyleSheet('border-style: solid; border-width: 1px; border-color: black;')

        # qline ticker
        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setGeometry(QtCore.QRect(1700, 160, 150, 30))
        self.lineEdit_10.setText("YNDX")
        self.lineEdit_10.setMaxLength(100)
        self.label_of_lineEdit_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_of_lineEdit_10.setText("Ticker")
        self.label_of_lineEdit_10.setGeometry(QtCore.QRect(1600, 160, 80, 20))
        self.label_of_lineEdit_10.setStyleSheet('border-style: solid; border-width: 1px; border-color: black;')

        # кнопка добавки строки
        self.pushButton_add_string_CLIENTS = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add_string_CLIENTS.setGeometry(1620, 210, 200, 30)
        self.pushButton_add_string_CLIENTS.setText('Добавка строки')

        # раздел с таблицей сделок

        self.label_TRADES = QtWidgets.QLabel(self.centralwidget)
        self.label_TRADES.setGeometry(700, 600, 500, 400)
        self.label_TRADES.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_TRADES.setFrameShadow(QtWidgets.QFrame.Plain)

        # кнопка создания таблицы
        self.pushButton_create_TRADES = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_create_TRADES.setGeometry(550, 600, 130, 40)
        self.pushButton_create_TRADES.setText('Создание таблицы \n сделок')
        self.pushButton_create_TRADES.setStyleSheet("background-color: cyan")

        # кнопка вывода таблицы
        self.pushButton_show_TRADES = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_show_TRADES.setGeometry(550, 650, 130, 40)
        self.pushButton_show_TRADES.setText('Вывод таблицы \n сделок')

        # button 11
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(550, 700, 130, 40))
        self.pushButton_11.setStyleSheet("background-color: pink")
        self.pushButton_11.setText("Удаление таблицы \n сделок")

        # кнопка показа всех данных таблиц
        self.pushButton_show_all = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_show_all.setGeometry(1700, 800, 200, 100)
        self.pushButton_show_all.setText('Показать все данные')

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
        self.ui.pushButton_4.clicked.connect(self.create_ORDERS)
        self.ui.pushButton_5.clicked.connect(self.show_ORDERS)
        self.ui.pushButton_6.clicked.connect(self.erase_db_table_function)
        self.ui.pushButton_7.clicked.connect(self.erase_db_function)
        self.ui.lineEdit_1.editingFinished.connect(self.lineEdit_1_event)
        self.ui.pushButton_8.clicked.connect(self.add_data_to_table)
        self.ui.pushButton_9.clicked.connect(self.sort_ORDERS)
        self.ui.pushButton_10.clicked.connect(self.transaction)
        self.ui.pushButton_create_clients.clicked.connect(self.create_CLIENTS_function)
        self.ui.pushButton_show_CLIENTS.clicked.connect(self.show_CLIENTS_func)
        self.ui.pushButton_add_preset_CLIENTS.clicked.connect(self.add_preset_CLIENTS)
        self.ui.pushButton_delete_CLIENTS.clicked.connect(self.del_CLIENTS)
        self.ui.pushButton_add_string_CLIENTS.clicked.connect(self.add_string_CLIENTS)
        self.ui.pushButton_create_TRADES.clicked.connect(self.create_TRADES)
        self.ui.pushButton_show_TRADES.clicked.connect(self.show_TRADES_func)
        self.ui.pushButton_show_all.clicked.connect(self.show_all)
        self.ui.pushButton_11.clicked.connect(self.del_TRADES)

        self.ui.radiobutton_ML_1.toggled.connect(self.rb_ml_1)
        self.ui.radiobutton_ML_2.toggled.connect(self.rb_ml_2)
        self.ui.radiobutton_BS_1.toggled.connect(self.rb_bs_1)
        self.ui.radiobutton_BS_2.toggled.connect(self.rb_bs_2)

        # self.ui.combo.activated.connect(self.onActivated)

        self.initUi()

    def del_TRADES(self):
        con = sl.connect(data_base_path)
        cur = con.cursor()
        try:
            cur.execute("DROP TABLE TRADES")
            con.close()
            self.statusBar().showMessage('Table of TRADES deleted')
        except Exception as e:
            print(e)
            self.statusBar().showMessage(str(e))

    def onActivated(self):
        global data_combobox
        data_combobox = ('dddd', 'ssss', 'vvvv')
        self.ui.status_monitor.setText('combobox activated')

    def show_TRADES_func(self):
        con = sl.connect(data_base_path)
        cursor = con.cursor()
        try:
            cursor.execute("SELECT * FROM TRADES")
            product = cursor.fetchall()  # вытаскиваем содержимое бд в виде списка
            a = '\n'.join(map(str, product))  # разбиваем список переносом строки
            self.ui.label_TRADES.setText(a)
            self.statusBar().showMessage('DATA IS SHOWED')
        except Exception as e:
            print(e)
            self.statusBar().showMessage(str(e))
        con.close()

    def create_TRADES(self):
        con = sl.connect(data_base_path)
        try:
            con.execute("""CREATE TABLE TRADES (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                seller_name_client TEXT,
                buyer_name_client TEXT,
                price INTEGER,
                amount INTEGER,
                ticker TEXT,
                datetime timestamp)""")
            self.statusBar().showMessage('Create TRADES executed succesful')
        except Exception as e:
            print(e)
            self.statusBar().showMessage(str(e))
        con.commit()
        con.close()

    def transaction(self):
        buy_list_sorted = ()
        sell_list_sorted = ()

        con = sl.connect(data_base_path)
        cursor = con.cursor()
        try:
            cursor.execute("SELECT * FROM ORDERS")
            product = cursor.fetchall()  # вытаскиваем содержимое таблицы ордеров в виде списка
            buy_list = []  # создаём пустые списки
            sell_list = []  # создаём пустые списки
            for i in product:  # цикл добавляет строки из бд по наличию слова BUY в списке
                if i[3] == 'BUY':
                    buy_list.append(i)
                else:
                    sell_list.append(i)
            # сортируем каждый список по величине цены
            buy_list_sorted = sorted(buy_list, key=lambda buy_list: buy_list[4], reverse=True)
            sell_list_sorted = sorted(sell_list, key=lambda sell_list: sell_list[4])

            def fun(v):  # вспомогательная функция для сортировки заявок по времени
                return (v[4], v[7])

            # сортируем по функции, в случае одинаковой цены, приоритет по времени заявки
            buy_list_sorted.sort(key=fun)
            sell_list_sorted.sort(key=fun)
            a = '\n'.join(map(str, buy_list_sorted))
            b = '\n'.join(map(str, sell_list_sorted))
            self.ui.status_monitor.setText(str(a) + '\n' + '\n' + str(b))
            con.commit()
            con.close()
            self.statusBar().showMessage('ORDERS is sorted')

        except Exception as error:
            print(error)
            self.statusBar().showMessage(str(error))
        # con.close()

        if len(buy_list_sorted) > 0 and len(sell_list_sorted) > 0:
            buyer = buy_list_sorted[-1]
            buyer_name = buyer[1]
            seller = sell_list_sorted[0]
            seller_name = seller[1]
            delta_price = int(buyer[4] - int(seller[4]))
            delta_amount = int(buyer[5]) - int(seller[5])
            trade_amount = min(buyer[5], seller[5])
            sell_price = seller[4]
            trade_money = trade_amount * sell_price

            self.ui.label_TRADES.setText(str(buyer) + "\n" + str(seller)
                                         + "\n" + str(buyer[0]) + "\n" + str(seller[0]))

            if int(buyer[4]) >= int(seller[4]):

                con = sl.connect(data_base_path)
                cursor = con.cursor()

                # вносим изменения в таблице клиентов, по каждому клиенту
                def update_CLIENTS(money, amnt, name):
                    try:
                        sql_query = 'UPDATE CLIENTS SET cash = cash + ?, amount = amount + ? where name_client = ?'
                        data = (money, amnt, name)
                        con.execute(sql_query, data)
                        con.commit()
                    except Exception as error:
                        print(error)
                        self.statusBar().showMessage(str(error))

                update_CLIENTS(-trade_money, trade_amount, buyer_name)
                update_CLIENTS(trade_money, -trade_amount, seller_name)

                # создаем запись в таблице сделок
                try:
                    sql = 'INSERT INTO TRADES (seller_name_client, buyer_name_client, price, amount, ticker, datetime) values (?, ?, ?, ?, ?, ?)'
                    data = (seller_name, buyer_name, sell_price, trade_amount, seller[6], datetime.today())
                    con.executemany(sql, (data,))
                    cursor.execute('SELECT * FROM TRADES')
                    trades = cursor.fetchall()
                    a = '\n'.join(map(str, trades))  # разбиваем список переносом строки
                    self.ui.label_TRADES.setText(a)
                    self.statusBar().showMessage('Insert to TRADES executed succesful')
                except Exception as error:
                    print(error)
                    self.statusBar().showMessage(str(error))
                con.commit()
                # con.close()
                self.statusBar().showMessage(
                    'OK' + "    delta_price = " + str(delta_price) + '  delta_amount = ' + str(delta_amount))

                # определяем минорный и мажорный ордер
                if int(buyer[5]) < int(seller[5]):
                    minor_id_order = buyer[0]
                    major_id_order = seller[0]
                else:
                    minor_id_order = seller[0]
                    major_id_order = buyer[0]

                # удаляем минорный ордер
                def delete_ORDER_id(id_order):
                    try:
                        sql_query = 'DELETE FROM ORDERS WHERE id = ?'
                        con.execute(sql_query, (id_order,))
                        con.commit()
                    except Exception as error:
                        print(error)
                        self.statusBar().showMessage(str(error))

                delete_ORDER_id(minor_id_order)

                # редактируем мажорный ордер
                def update_order(amount, id_order):
                    try:
                        sql_query = 'UPDATE ORDERS set amount = amount - ? where id = ?'
                        data = (amount, id_order)
                        con.execute(sql_query, data)
                        con.commit()
                    except Exception as error:
                        print(error)
                        self.statusBar().showMessage(str(error))

                update_order(trade_amount, major_id_order)
            else:
                self.statusBar().showMessage('Error of comparision')
        else:
            self.statusBar().showMessage('Orders have not pair')

    def add_string_CLIENTS(self):
        name_client = self.ui.lineEdit_7.text()
        cash = self.ui.lineEdit_8.text()
        amount = self.ui.lineEdit_9.text()
        ticker = self.ui.lineEdit_10.text()
        con = sl.connect(data_base_path)
        cursor = con.cursor()
        try:
            sql = 'INSERT INTO CLIENTS (id, name_client, cash, amount, ticker, datetime) values(null, ?, ?, ?, ?, ?)'
            data = [(name_client, cash, amount, ticker, datetime.today())]
            con.executemany(sql, data)
            cursor.execute("SELECT * FROM CLIENTS")
            product = cursor.fetchall()  # вытаскиваем содержимое бд в виде списка
            a = '\n'.join(map(str, product))  # разбиваем список переносом строки
            self.ui.label_CLIENTS.setText(a)
            con.commit()
            con.close()
            # show_ORDERS(self)
            self.statusBar().showMessage('INSERT of DATA succesful' + str(data))
        except Exception as error:
            print(error)
            self.statusBar().showMessage(str(error))
        con.close()

    def del_CLIENTS(self):
        con = sl.connect(data_base_path)
        cur = con.cursor()
        try:
            cur.execute("DROP TABLE CLIENTS")
            con.close()
            self.statusBar().showMessage('Table of CLIENTS IS ERASED')
        except Exception as e:
            print(e)
            self.statusBar().showMessage(str(e))

    def add_preset_CLIENTS(self):
        con = sl.connect(data_base_path)
        cursor = con.cursor()

        try:
            sql = 'INSERT INTO CLIENTS (id, name_client, cash, amount, ticker, datetime) values(null, ?, ?, ?, ?, ?)'
            data = [('Alice', 1000000, 1000, 'YNDX', datetime.today()),
                    ('Bob', 2000000, 1100, 'YNDX', datetime.today()),
                    ('Mikle', 9000000, 800, 'YNDX', datetime.today()),
                    ('Nick', 7830000, 200, 'YNDX', datetime.today()),
                    ('George', 3806000, 250, 'YNDX', datetime.today()),
                    ('Oleg', 7820000, 800, 'YNDX', datetime.today()),
                    ('Alex', 7430000, 2000, 'YNDX', datetime.today())]
            with con:
                con.executemany(sql, data)
            self.statusBar().showMessage('INSERT executed succesful')
        except Exception as error:
            print(error)
            self.statusBar().showMessage(str(error))

        try:
            cursor.execute("SELECT * FROM CLIENTS")
            product = cursor.fetchall()  # вытаскиваем содержимое бд в виде списка
            a = '\n'.join(map(str, product))  # разбиваем список переносом строки
            self.ui.label_CLIENTS.setText(a)
            # self.statusBar().showMessage('DATA IS SHOWED')
        except Exception as error:
            print(error)
            self.statusBar().showMessage(str(error))

        con.close()

    def show_CLIENTS_func(self):
        con = sl.connect(data_base_path)
        cursor = con.cursor()
        try:
            cursor.execute("SELECT * FROM CLIENTS")
            product = cursor.fetchall()  # вытаскиваем содержимое бд в виде списка
            a = '\n'.join(map(str, product))  # разбиваем список переносом строки
            self.ui.label_CLIENTS.setText(a)
            self.statusBar().showMessage('DATA from CLIENTS is showed')
            logging.info('DATA from CLIENTS is showed')
        except Exception as Error:
            print(Error)
            self.statusBar().showMessage(str(Error))
        con.close()

    def create_CLIENTS_function(self):
        con = sl.connect(data_base_path)
        # cursor = con.cursor()
        try:
            con.execute("""CREATE TABLE CLIENTS (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                name_client TEXT,
                cash INTEGER,
                amount INTEGER,
                ticker TEXT,
                datetime timestamp)""")
            # следующая запись делает колонку name_client в таблице клиентов уникальной,
            # то есть в нее нельзя записать дубль!
            con.execute("""CREATE UNIQUE INDEX name_client ON CLIENTS(name_client)""")
            self.statusBar().showMessage('Create CLIENTS executed succesful')
        except Exception as error:
            print(error)
            self.statusBar().showMessage(str(error))
        con.commit()
        con.close()

    def sort_ORDERS(self):

        global buy_list_sorted
        global sell_list_sorted
        con = sl.connect(data_base_path)
        cursor = con.cursor()
        try:
            cursor.execute("SELECT * FROM ORDERS")
            product = cursor.fetchall()  # вытаскиваем содержимое таблицы ордеров в виде списка
            buy_list = []  # создаём пустые списки
            sell_list = []  # создаём пустые списки
            for i in product:  # цикл добавляет строки из бд по наличию слова BUY в списке
                if i[3] == 'BUY':
                    buy_list.append(i)
                else:
                    sell_list.append(i)
            # сортируем каждый список по величине цены
            buy_list_sorted = sorted(buy_list, key=lambda buy_list: buy_list[4], reverse=True)
            sell_list_sorted = sorted(sell_list, key=lambda sell_list: sell_list[4])

            def fun(v):  # вспомогательная функция для сортировки заявок
                return (v[4], v[7])

            # сортируем по функции, в случае одинаковой цены, приоритет по времени заявки
            buy_list_sorted.sort(key=fun)
            sell_list_sorted.sort(key=fun)
            a = '\n'.join(map(str, buy_list_sorted))
            b = '\n'.join(map(str, sell_list_sorted))
            self.ui.status_monitor.setText(str(a) + '\n' + '\n' + str(b))
            con.commit()
            con.close()
            self.statusBar().showMessage('ORDERS is sorted')

        except Exception as error:
            print(error)
            self.statusBar().showMessage(str(error))
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
            con.execute("""CREATE TABLE ORDERS (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
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

    def create_ORDERS(self):
        con = sl.connect(data_base_path)
        try:
            sql = 'INSERT INTO ORDERS (id, name_client, order_type, buy_sell, price, amount, ticker, datetime)' \
                  ' values(null, ?, ?, ?, ?, ?, ?, ?)'
            data = [('Alice', 'Limit', 'BUY', 900, 10, 'YNDX', datetime.today()),
                    ('Bob', 'Limit', 'SELL', 700, 1, 'YNDX', datetime.today()),
                    ('Mikle', 'Limit', 'BUY', 800, 5, 'YNDX', datetime.today()),
                    ('George', 'Limit', 'BUY', 850, 2, 'YNDX', datetime.today()),
                    ('Alex', 'Limit', 'Sell', 800, 200, 'YNDX', datetime.today()),
                    ('Nick', 'Limit', 'BUY', 820, 5, 'YNDX', datetime.today()),
                    ('Oleg', 'Limit', 'BUY', 820, 15, 'YNDX', datetime.today())]
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
        buy_sell = self.ui.lineEdit_3.text()
        price = self.ui.lineEdit_4.text()
        amount = self.ui.lineEdit_5.text()
        ticker = self.ui.lineEdit_6.text()
        con = sl.connect(data_base_path)
        cursor = con.cursor()
        try:
            sql = 'INSERT INTO ORDERS (id, name_client, order_type, buy_sell, price, amount, ticker, datetime)' \
                  ' values(null, ?, ?, ?, ?, ?, ?, ?)'
            data = [(name_client, order_type, buy_sell, price, amount, ticker, datetime.today())]
            con.executemany(sql, data)
            cursor.execute("SELECT * FROM ORDERS")
            product = cursor.fetchall()  # вытаскиваем содержимое бд в виде списка
            a = '\n'.join(map(str, product))  # разбиваем список переносом строки
            self.ui.label.setText(a)
            con.commit()
            con.close()
            # show_ORDERS(self)
            self.statusBar().showMessage('INSERT of DATA succesful' + str(data))
        except Exception as error:
            print(error)
            self.statusBar().showMessage(str(error))
        con.close()

    def show_ORDERS(self):
        con = sl.connect(data_base_path)
        cursor = con.cursor()
        try:
            cursor.execute("SELECT * FROM ORDERS")
            product = cursor.fetchall()  # вытаскиваем содержимое бд в виде списка
            a = '\n'.join(map(str, product))  # разбиваем список переносом строки
            self.ui.label.setText(a)
            self.statusBar().showMessage('DATA IS SHOWED')
        except Exception as error:
            print(error)
            self.statusBar().showMessage(str(error))
        con.close()

    def erase_db_table_function(self):
        con = sl.connect(data_base_path)
        cur = con.cursor()
        try:
            cur.execute("DROP TABLE ORDERS")
            con.close()
            self.statusBar().showMessage('Table IS ERASED')
        except Exception as error:
            print(error)
            self.statusBar().showMessage(str(error))

    def erase_db_function(self):
        try:
            os.remove(data_base_path)
            self.statusBar().showMessage('DB IS ERASED' + " File: " + data_base_path)
        except Exception as error:
            print(error)
            self.statusBar().showMessage(str(error))

    def status_monitor(self):
        try:
            log_file = open('mylog.log')
            log = []
            for line in log_file.readlines():
                log.append(line)
            log_file.close()
            self.ui.status_monitor.setText(str(log))
        except Exception as error:
            print(error)
            self.statusBar().showMessage(str(error))

    def show_all(self):
        self.show_ORDERS()
        self.show_CLIENTS_func()
        self.show_TRADES_func()
        self.status_monitor()


app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())
