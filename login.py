#Created by Vincent Munyalo

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QMovie
import sys, os
from home import *
from client import Client

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 550)
        Form.setFixedSize(400, 550)
        Form.setStyleSheet("background-image: assets/background.png;")

        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 420, 580))
        self.widget.setStyleSheet(
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
                "    background-color:rgba(105, 118, 132, 200);\n"
                "}\n"
                "\n"
                "QPushButton#pushButton_2, #pushButton_3, #pushButton_4, #pushButton_5{    \n"
                "    background-color: rgba(0, 0, 0, 0);\n"
                "    color:rgba(85, 98, 112, 255);\n"
                "}\n"
                "QPushButton#pushButton_2:hover, #pushButton_3:hover, #pushButton_4:hover, #pushButton_5:hover{    \n"
                "    color:rgba(155, 168, 182, 220);\n"
                "}\n"
                "QPushButton#pushButton_2:pressed, #pushButton_3:pressed, #pushButton_4:pressed, #pushButton_5:pressed{    \n"
                "    padding-left:5px;\n"
                "    padding-top:5px;\n"
                "    color:rgba(115, 128, 142, 255);\n"
                "    border-radius:20px;"
                "}\n"
                "Qlabel#label{  \n"
                "     border: 20px;"
                "}")

        
        self.widget.setObjectName("widget")

        #frame
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setGeometry(QtCore.QRect(20, 30, 460, 480))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        radius = 20
        self.frame.setStyleSheet(
        """
            background-color: blue;
            border-top-left-radius:{0}px;
            border-bottom-left-radius:{0}px;
            border-top-right-radius:{0}px;
            border-bottom-right-radius:{0}px;
            """.format(radius))

        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 420, 550))
        self.label.setStyleSheet(
                "border-image: url(:assets/background.png);\n"
                "border-radius:20px;"
                )
        self.label.setStyleSheet(
                    "border-top-left-radius :20px;"
                    "border-top-right-radius : 20px; "
                    "border-bottom-left-radius : 20px; "
                    "border-bottom-right-radius : 20px")
        
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.setPixmap(QtGui.QPixmap("assets/background.png"))

        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 340, 490))
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0.715909, stop:0 rgba(0, 0, 0, 9), stop:0.375 rgba(0, 0, 0, 50), stop:0.835227 rgba(0, 0, 0, 75));\n"
                "border-radius:20px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")


        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 600, 520))
        self.label_3.setStyleSheet("background-color:rgba(0, 0, 0, 100);\n")
        #        "border-radius:15px;")
        
        self.label_3.setStyleSheet("border-radius:15px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(155, 115, 90, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(255, 255, 255, 210);")
        self.label_4.setObjectName("label_4")

        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 185, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                "border:none;\n"
                "border-bottom:2px solid rgba(105, 118, 132, 255);\n"
                "color:rgba(255, 255, 255, 230);\n"
                "padding-bottom:7px;")
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 250, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                "border:none;\n"
                "border-bottom:2px solid rgba(105, 118, 132, 255);\n"
                "color:rgba(255, 255, 255, 230);\n"
                "padding-bottom:7px;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(100, 330, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.authenticate)

        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(310, 480, 260, 20))
        self.label_7.setObjectName("label_7")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setText("©2022")
        self.label_7.setStyleSheet("color: white")
        self.label_7.setScaledContents(True)

        myFont=QtGui.QFont()
        myFont.setBold(True)
        myFont.setPointSize(10)
        self.label_7.setFont(myFont)

        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(111, 378, 191, 21))
        self.label_5.setStyleSheet("color:rgba(255, 255, 255, 140);")
        self.label_5.setObjectName("label_5")

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(105, 399, 141, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")


        '''self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0, color=QtGui.QColor(234, 221, 186, 100)))'''
        self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0, color=QtGui.QColor(105, 118, 132, 100)))
        self.label_3.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0, color=QtGui.QColor(105, 118, 132, 100)))
        self.pushButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3, color=QtGui.QColor(105, 118, 132, 100)))
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Zerys"))
        self.label_4.setText(_translate("Form", "Log In"))
        self.lineEdit.setPlaceholderText(_translate("Form", "  Username"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "  Password"))
        self.pushButton.setText(_translate("Form", "L o g  I n"))
        self.pushButton.setShortcut(_translate("Form", "Return"))
        self.label_5.setText(_translate("Form", "Forgot your User Name or Password? "))
        

    def go_home(self):
        self.home = QtWidgets.QWidget()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.home)
        self.home.show()

    def authenticate(self):
        self.loading = Loading()
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        try:
            os.makedirs('bin')
            print('Directory created!')
        except:
            print('Directory seems to exist')

        try:
            client = Client()
        except:
            print('Unable to access server')
            QtWidgets.QMessageBox.critical(None, 'Login Failed', 'Server inaccessible. Try again later or contact support')
        else:
            if username != '' and password !='':
                if client.run(username, password) == 'exists':
                        print('Logging in... ')
                        Form.close()
                        self.go_home()

                elif client.run(username, password) == 'incorrect_pwd':
                    print('Incorrect Password')
                    QtWidgets.QMessageBox.critical(None, 'Login Failed', 'Incorrect Password')

                elif client.run(username, password) == 'null':
                    print('User doesn\'t exist')
                    QtWidgets.QMessageBox.critical(None, 'Login Failed', 'User doesn\'t exist!')
                else:
                    print('Unknown issue')
                    QtWidgets.QMessageBox.critical(None, 'Login Failed', 'Username or Password incorrect!')


            elif username == '':
                QtWidgets.QMessageBox.critical(None, 'Login Failed', 'Username can\'t be blank!')
                return 'fail'

            elif password == '':
                QtWidgets.QMessageBox.critical(None, 'Login Failed', 'Password can\'t be blank!')
                return 'fail'
                                
                                   
stylesheet = """
        Ui_Form {
        background-image: url("assets/background.png");
        background-repeat: no-repeat; 
        background-position: center;
        }
        """

class Loading(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(50, 50)
        self.setGeometry(650, 330, 100, 100)
        self.setStyleSheet('background-color : lightgrey;')

        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)

        self.label_animation = QtWidgets.QLabel(self)

        self.movie = QMovie('./assets/load.gif')
        self.label_animation.setMovie(self.movie)

        timer = QTimer(self)
        self.animate()
        timer.singleShot(1000, self.end)
        try:
            os.makedirs('bin')
            print('Directory created!')
        except:
            print('Directory seems to exist')

    def animate(self):
        self.movie.start()
    
    def end(self):
        self.movie.stop()
        self.close()

     

if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = Ui_Form()
        ui.setupUi(Form)
        Form.show()
        sys.exit(app.exec_())
