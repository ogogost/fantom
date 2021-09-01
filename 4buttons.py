import sqlite3 as sl
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import sys, os
import bot
from threading import Thread
import my_sql_module
import sqlite3


# Variables
data_base_path = '4buttons.db'
flag_of_bot = True
con = sqlite3.connect(data_base_path)
sqlite3.connect(data_base_path, check_same_thread=False)

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 900)
        # MainWindow.showFullScreen()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(400, 20, 800, 600))
        self.label.setFrameShape(QtWidgets.QFrame.Panel)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setStyleSheet('background-color: white')
        # self.label.setPixmap(QtGui.QPixmap(source))
        self.label.setObjectName("label")

        # button 1
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(400, 650, 200, 80))
        self.pushButton_1.setText("Thread 1")

        # button 2
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(800, 650, 200, 80))
        self.pushButton_2.setText("Thread 2")

        # button 3
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(400, 750, 200, 80))
        self.pushButton_3.setText("Thread 3")

        # button 4
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(800, 750, 200, 80))
        self.pushButton_4.setText("Thread 4")

        # button 5
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(1000, 750, 200, 80))
        self.pushButton_5.setText("STOP")


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
        self.ui.pushButton_1.clicked.connect(self.Thread_1)
        # self.ui.pushButton_2.clicked.connect(self.Thread_2)
        # self.ui.pushButton_3.clicked.connect(self.Thread_3)
        # self.ui.pushButton_4.clicked.connect(self.Thread_4)
        self.ui.pushButton_5.clicked.connect(self.stop_function)


        self.initUi()


    def initUi(self):
        self.statusBar().showMessage('Ready')


    def Thread_1(self):
        my_thread1 = Mythread()
        my_thread1.start()

    def stop_function(self):
        global flag_of_bot
        flag_of_bot = False


class Mythread(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        print('Thread is started')
        Text = bot.generator_of_shit(con)
        self.ui.label.setText(Text)


app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())







