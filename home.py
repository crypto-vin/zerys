# Created by Vincent |Munyalo

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QTextCursor
import sys
from zerys import Zerys
import threading
import time
import csv


class Ui_MainWindow(object):
    def __init__(self):
        self.levels = ['All', 'High', 'Premium']
        self.stop_event = False
        self.apply_count = 0
        f = open("bin/params.csv", "r", newline="")
        with f as csv_file:
            csv_reader = csv.reader(csv_file)
            row1 = next(csv_reader)
            row2 = next(csv_reader)
            row3 = next(csv_reader)
            acc_owner = row1
            usernames = row2
            phones = row3

        self.stop_threads = False
        self.texts = False
        self.launched = False
        self.acc_owner, self.usernames, self.phones = acc_owner[0], usernames, phones

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("Zerys")
        MainWindow.resize(400, 550)
        MainWindow.setFixedSize(400, 550)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet(
                "QPushButton#pushButton{    \n"
                "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
                "    color:rgba(255, 255, 255, 210);\n"
                "    border-radius:5px;\n"
                "}\n"

                "QPushButton#pushButton:hover{    \n"
                "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
                "}\n"
                
                "QPushButton#pushButton:pressed{    \n"
                "    padding-left:5px;\n"
                "    padding-top:5px;\n"
                "    font:15px;\n"
                "    background-color:rgba(105, 118, 132, 200);\n"
                "}\n"

                "QPushButton#stopButton{    \n"
                "    background-color:rgba(255, 0, 0, 1);\n"
                "    border-radius:5px;\n"
                "    font:13px;\n"
                "}\n"

                "QPushButton#stopButton:hover{    \n"
                "    background-color: rgba(237, 146, 57, 0.81);"
                "}\n"

                "QPushButton#stopButton:pressed{    \n"
                "    padding-left:5px;\n"
                "    padding-top:5px;\n"
                "    font:14px;\n"
                "    background-color:rgba(237, 146, 57, 0.81);\n"
                "}\n"

                "QPushButton#refreshButton{    \n"
                "    background-color:rgba(6, 6, 6, 0.91);\n"
                "    border-radius:5px;\n"
                "    font:13px;\n"
                "}\n"

                "QPushButton#refreshButton:hover{    \n"
                "    background-color: green;"
                "}\n"

                "QPushButton#refreshButton:pressed{    \n"
                "    padding-left:5px;\n"
                "    padding-top:5px;\n"
                "    font:14px;\n"
                "    background-color:light-green;\n"
                "}\n"


                "QFrame#frame{  \n"
                "    border: 10px;\n"
                "    background-color:rgba(6, 6, 6, 0.91);\n"
                "}\n"
                
                "QComboBox#comboBox{  \n"
                "    border: 10px;\n"
                "    border-radius:10px;\n"
                "    font:13px;\n"
                "}\n"

                "QSpinBox#spinBox{  \n"
                "    border: 10px;\n"
                "    border-radius:7px;\n"
                "    font:13px;\n"
                "}\n"
                
                "QLineEdit#lineEdit_2{  \n"
                "    border: 10px;\n"
                "    border-radius:10px;\n"
                "    font:13px;\n"
                "}\n"

                "QLabel#label_2, #label_3, #label_4, #label_5{  \n"
                "    color:rgba(255, 255, 255, 1);\n"
                "    font:13px;\n"
                "}"

                "QLabel#balance_label{  \n"
                "    color:green;\n"
                "    font:13px;\n"
                "}")


        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 20, 400, 550))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(120, 430, 161, 31))
        self.pushButton.setCheckable(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.launch)

        #stop button
        self.stopButton = QtWidgets.QPushButton(self.frame)
        self.stopButton.setGeometry(QtCore.QRect(180, 470, 40, 31))
        self.stopButton.setCheckable(True)
        self.stopButton.setObjectName("stopButton")
        self.stopButton.clicked.connect(self.terminate)

        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(130, 130, 141, 21))
        self.checkBox.setObjectName("checkBox")
        self.checkBox.setStyleSheet('color : green;')
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setItalic(True)
        self.checkBox.setFont(font)
        self.checkBox.stateChanged.connect(self.toggleVisibility)

        # phone label
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(40, 10, 61, 21))
        self.label_4.setObjectName("label_4")

        # interval label
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(310, 60, 81, 21))
        self.label_5.setObjectName("label_5")

        # password label
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 61, 20))
        self.label_3.setObjectName("label_3")

        # email label
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 50, 41, 21))
        self.label_2.setObjectName("label_2")

        # phone to receive sms
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setGeometry(QtCore.QRect(100, 10, 191, 25))
        self.comboBox_2.setStyleSheet("background-color: white ")
        self.comboBox_2.setObjectName("comboBox")
        self.comboBox_2.clear()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_2.setFont(font)
        self.comboBox_2.addItems(self.phones)

        # account username
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(100, 50, 191, 25))
        self.comboBox.setStyleSheet("background-color: white ")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.clear()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.addItems(self.usernames)

        # password line edit
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 90, 191, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(20, 155, 362, 265))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.textEdit.setFont(font)

        # refresh interval spin box
        self.spinBox = QtWidgets.QSpinBox(self.frame)
        self.spinBox.setGeometry(QtCore.QRect(325, 90, 40, 21))
        self.spinBox.setStyleSheet("background-color: white ")
        self.spinBox.setObjectName("spinBox")
        interval = 5
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox.setFont(font)
        self.spinBox.setValue(interval)

        # refresh button
        self.refreshButton = QtWidgets.QPushButton(self.frame)
        self.refreshButton.setGeometry(QtCore.QRect(352, 130, 30, 21))
        self.refreshButton.setCheckable(True)
        self.refreshButton.setObjectName("refreshButton")
        self.refreshButton.setIcon(QIcon('assets/refresh.gif'))
        self.refreshButton.clicked.connect(self.show_logs)

        # balance label
        self.balance_label = QtWidgets.QLabel(self.frame)
        self.balance_label.setGeometry(QtCore.QRect(275, 10, 150, 21))
        self.balance_label.setObjectName("balance_label")
        font = QtGui.QFont()
        font.setPointSize(8)
        self.balance_label.setFont(font)
        

       # MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 406, 21))
        self.menubar.setObjectName("menubar")

        self.menuHome = QtWidgets.QMenu(self.menubar)
        self.menuHome.setObjectName("menuHome")

        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")

        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")

        #MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        #MainWindow.setStatusBar(self.statusbar)

        self.actionGeneral = QtWidgets.QAction(MainWindow)
        self.actionGeneral.setObjectName("actionGeneral")

        self.actionAvatar = QtWidgets.QAction(MainWindow)
        self.actionAvatar.setObjectName("actionAvatar")

        self.actionPrivacy = QtWidgets.QAction(MainWindow)
        self.actionPrivacy.setObjectName("actionPrivacy")

        self.menuSettings.addAction(self.actionGeneral)
        self.menuSettings.addAction(self.actionAvatar)
        self.menuSettings.addAction(self.actionPrivacy)
        
        self.menubar.addAction(self.menuHome.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):    
        _translate = QtCore.QCoreApplication.translate
        self._translate = _translate
        self.pushButton.setText(_translate("MainWindow", "L a u n c h"))
        self.pushButton.setShortcut(_translate("MainWindow", "Return"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))
        self.refreshButton.setShortcut(_translate("MainWindow", "F5"))
        self.checkBox.setText(_translate("MainWindow", "Show Password"))
        self.textEdit.setPlaceholderText(_translate("Form", "Logs will appear here. Click on the refresh button above to the right."))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "  Password"))
        self.label_3.setText(_translate("MainWindow", "Password:"))
        self.label_2.setText(_translate("MainWindow", " Email:"))
        self.label_4.setText(_translate("MainWindow", " Phone:"))
        self.label_5.setText(_translate("MainWindow", " Interval (s)"))
        self.menuHome.setTitle(_translate("MainWindow", "Home"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionGeneral.setText(_translate("MainWindow", "General"))
        self.actionAvatar.setText(_translate("MainWindow", "Avatar"))
        self.actionPrivacy.setText(_translate("MainWindow", "Privacy"))
    
    def toggleVisibility(self):
        if self.lineEdit_2.echoMode()== QLineEdit.Normal:
            self.lineEdit_2.setEchoMode(QLineEdit.Password)
            self.checkBox.setText(self._translate("Form", "Show Password"))
        else:
            self.lineEdit_2.setEchoMode(QLineEdit.Normal)
            self.checkBox.setText(self._translate("Form", "Hide Password"))

    def launch(self):
        if not self.launched:
            email = str(self.comboBox.currentText())
            password = str(self.lineEdit_2.text())
            phone = str(self.comboBox_2.currentText())
            loop_duration = int(self.spinBox.value())
            if email == '':
                QtWidgets.QMessageBox.critical(None, 'Launch Failed', 'Email can\'t be blank!')
            elif password == '':
                QtWidgets.QMessageBox.critical(None, 'Launch Failed', 'Password can\'t be blank!')
            else:
                self.zerys = Zerys(email, password, phone, loop_duration)
                f_thread = threading.Thread(target = self.zerys.run)
                f_thread.start()
                print('Zerys is starting...')
                f = open('bin/logs.txt', 'w')
                with f:
                    f.write('\n Zerys v1.0.0 has launched successfully')
                self.zerys.running = True
                self.launched = True 
        else:
            QtWidgets.QMessageBox.critical(None, 'Failed', 'Zerys is running!')

    # display latest logs
    def show_logs(self):
        try:
            log_file = open('bin/logs.txt', 'a+')
        except:
            print('Log file exists')

        f = open('bin/logs.txt', 'r')
        with f:
            data = f.read()
            self.textEdit.setText(data)
            self.textEdit.moveCursor(QTextCursor.End)
    
    # kill process
    def terminate(self):
        try:
            if self.zerys.running:
                self.launched = False
                self.zerys.terminate()
                
            else:
                print('Wait for the program to start!')
                QtWidgets.QMessageBox.critical(None, 'Failed', 'Wait for the program to run!')
        except:
            pass


if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = Ui_MainWindow()
        ui.setupUi(Form)
        Form.show()
        sys.exit(app.exec_())

