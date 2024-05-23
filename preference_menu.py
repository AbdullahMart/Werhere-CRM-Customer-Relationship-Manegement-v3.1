import sys
import os
import subprocess
from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 500)
        MainWindow.setMinimumSize(QtCore.QSize(500, 500))
        MainWindow.setMaximumSize(QtCore.QSize(500, 500))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.preference_menu_frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.preference_menu_frame.setGeometry(QtCore.QRect(-10, -10, 510, 481))
        self.preference_menu_frame.setMaximumSize(QtCore.QSize(510, 500))
        self.preference_menu_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.489, y1:1, x2:0.494, y2:0, stop:0 rgba(71, 71, 71, 255), stop:1 rgba(255, 255, 255, 255));")
        self.preference_menu_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.preference_menu_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.preference_menu_frame.setObjectName("preference_menu_frame")
        self.werhere_logo_label = QtWidgets.QLabel(parent=self.preference_menu_frame)
        self.werhere_logo_label.setGeometry(QtCore.QRect(10, 20, 491, 101))
        self.werhere_logo_label.setStyleSheet("background-color: rgba(255, 255, 255, 0)")
        self.werhere_logo_label.setText("")
        self.werhere_logo_label.setPixmap(QtGui.QPixmap("images/werhere_image.png"))
        self.werhere_logo_label.setScaledContents(True)
        self.werhere_logo_label.setObjectName("werhere_logo_label")
        self.groupBox = QtWidgets.QGroupBox(parent=self.preference_menu_frame)
        self.groupBox.setGeometry(QtCore.QRect(50, 170, 401, 221))
        self.groupBox.setStyleSheet("\n"
"QGroupBox{\n"
"    border-radius : 15px;\n"
"background-color: qradialgradient(spread:pad, cx:0.488409, cy:0.557, radius:0.73, fx:0.482955, fy:0.568909, stop:0 rgba(89, 87, 87, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"}")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.bact_menu_pushButton = QtWidgets.QPushButton(parent=self.groupBox)
        self.bact_menu_pushButton.setGeometry(QtCore.QRect(40, 170, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        self.bact_menu_pushButton.setFont(font)
        self.bact_menu_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.bact_menu_pushButton.setStyleSheet("\n"
"QPushButton:hover{\n"
"   border-radius : 6px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color:  ;\n"
"    background-color: rgb(218, 30, 60);\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"                    background-color: rgb(255, 255, 255);\n"
"                    color: rgb(0, 0, 255);\n"
"                    }")
        self.bact_menu_pushButton.setObjectName("bact_menu_pushButton")
        self.exit_pushButton = QtWidgets.QPushButton(parent=self.groupBox)
        self.exit_pushButton.setGeometry(QtCore.QRect(280, 170, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        self.exit_pushButton.setFont(font)
        self.exit_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.exit_pushButton.setStyleSheet("\n"
"QPushButton:hover{\n"
"   border-radius : 6px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color:  ;\n"
"    background-color: rgb(218, 30, 60);\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"                    background-color: rgb(255, 255, 255);\n"
"                    color: rgb(0, 0, 255);\n"
"                    }")
        self.exit_pushButton.setObjectName("exit_pushButton")
        self.interviews_pushButton = QtWidgets.QPushButton(parent=self.groupBox)
        self.interviews_pushButton.setGeometry(QtCore.QRect(150, 100, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        self.interviews_pushButton.setFont(font)
        self.interviews_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.interviews_pushButton.setStyleSheet("\n"
"QPushButton:hover{\n"
"   border-radius : 6px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color:  ;\n"
"    background-color: rgb(218, 30, 60);\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"                    background-color: rgb(255, 255, 255);\n"
"                    color: rgb(0, 0, 255);\n"
"                    }")
        self.interviews_pushButton.setObjectName("interviews_pushButton")
        self.mentor_meeting_pushButton = QtWidgets.QPushButton(parent=self.groupBox)
        self.mentor_meeting_pushButton.setGeometry(QtCore.QRect(30, 30, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        self.mentor_meeting_pushButton.setFont(font)
        self.mentor_meeting_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.mentor_meeting_pushButton.setStyleSheet("\n"
"QPushButton:hover{\n"
"   border-radius : 6px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color:  ;\n"
"    background-color: rgb(218, 30, 60);\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"                    background-color: rgb(255, 255, 255);\n"
"                    color: rgb(0, 0, 255);\n"
"                    }")
        self.mentor_meeting_pushButton.setObjectName("mentor_meeting_pushButton")
        self.applications_pushButton = QtWidgets.QPushButton(parent=self.groupBox)
        self.applications_pushButton.setGeometry(QtCore.QRect(280, 40, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        self.applications_pushButton.setFont(font)
        self.applications_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.applications_pushButton.setStyleSheet("\n"
"QPushButton:hover{\n"
"   border-radius : 6px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color:  ;\n"
"    background-color: rgb(218, 30, 60);\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"                    background-color: rgb(255, 255, 255);\n"
"                    color: rgb(0, 0, 255);\n"
"                    }")
        self.applications_pushButton.setObjectName("applications_pushButton")
        self.label = QtWidgets.QLabel(parent=self.preference_menu_frame)
        self.label.setGeometry(QtCore.QRect(70, 160, 371, 21))
        self.label.setStyleSheet("background-color: qradialgradient(spread:reflect, cx:0.477, cy:0.568, radius:0.73, fx:0.46, fy:0.575, stop:0.602273 rgba(255, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Butonların Tanımlandığı yer
        self.applications_pushButton.clicked.connect(self.applications_clicked)
        self.interviews_pushButton.clicked.connect(self.interviews_clicked)
        self.mentor_meeting_pushButton.clicked.connect(self.mentor_meeting_clicked)
        self.bact_menu_pushButton.clicked.connect(self.back_menu_clicked)
        self.exit_pushButton.clicked.connect(self.exit_clicked)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Preference Menu"))
        self.bact_menu_pushButton.setText(_translate("MainWindow", "Main Menu"))
        self.exit_pushButton.setText(_translate("MainWindow", "Exit"))
        self.interviews_pushButton.setText(_translate("MainWindow", "Interviews"))
        self.mentor_meeting_pushButton.setText(_translate("MainWindow", "Mentor Meeting"))
        self.applications_pushButton.setText(_translate("MainWindow", "Applications"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'__Inter_46a1ea\',\'__Inter_Fallback_46a1ea\',\'system-ui\',\'arial\'; font-size:10pt; font-weight:600; color:#ffffff;\">CRM - Preference Menu</span></p></body></html>"))


    #Buton Fonksiyonlarının oluşturulduğu yer
    def applications_clicked(self):
        from  applications_page import Ui_applications_page_MainWindow
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_applications_page_MainWindow()
        self.ui.setupUi(self.MainWindow) 
        self.hide()
        self.MainWindow.show()

    def interviews_clicked(self):
        from interviews_page import Ui_interviews_page_MainWindow
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_interviews_page_MainWindow()
        self.ui.setupUi(self.MainWindow) 
        self.hide()
        self.MainWindow.show()
        

    def mentor_meeting_clicked(self):
        from mentor_interview_page import Ui_mentor_interviews_page_MainWindow
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_mentor_interviews_page_MainWindow()
        self.ui.setupUi(self.MainWindow) 
        self.hide()
        self.MainWindow.show()
            

    def back_menu_clicked(self):
        
        try:
            subprocess.Popen(["python", os.path.join(os.path.dirname(__file__), "login_window.py")])
        except FileNotFoundError:
            subprocess.Popen(["python3", os.path.join(os.path.dirname(__file__), "login_window.py")])

    def exit_clicked(self):
        self.close()
        

# Ui_MainWindow sınıfı, QMainWindow sınıfından türetilmemişti ve dolayısıyla close() metodunu doğrudan çağıramıyordu
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
