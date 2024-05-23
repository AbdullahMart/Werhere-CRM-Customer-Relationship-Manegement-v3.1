from PyQt6 import QtCore, QtGui, QtWidgets,QtCore
import os
import subprocess


class Ui_admin_pref_men_MainWindow(object):
    def setupUi(self, admin_pref_men_MainWindow):
        admin_pref_men_MainWindow.setObjectName("admin_pref_men_MainWindow")
        admin_pref_men_MainWindow.resize(500, 500)
        admin_pref_men_MainWindow.setMinimumSize(QtCore.QSize(500, 500))
        admin_pref_men_MainWindow.setMaximumSize(QtCore.QSize(500, 500))
        admin_pref_men_MainWindow.setAcceptDrops(False)
        admin_pref_men_MainWindow.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        admin_pref_men_MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(parent=admin_pref_men_MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.admin_preference_menu_frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.admin_preference_menu_frame.setGeometry(QtCore.QRect(-150, -100, 721, 661))
        self.admin_preference_menu_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.489, y1:1, x2:0.494, y2:0, stop:0 rgba(71, 71, 71, 255), stop:1 rgba(255, 255, 255, 255));")
        self.admin_preference_menu_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.admin_preference_menu_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.admin_preference_menu_frame.setObjectName("admin_preference_menu_frame")
        self.werhere_image_label = QtWidgets.QLabel(parent=self.admin_preference_menu_frame)
        self.werhere_image_label.setGeometry(QtCore.QRect(160, 110, 481, 101))
        self.werhere_image_label.setStyleSheet("background-color: rgba(255, 255, 255, 5);")
        self.werhere_image_label.setText("")
        self.werhere_image_label.setPixmap(QtGui.QPixmap("images/werhere_image.png"))
        self.werhere_image_label.setScaledContents(True)
        self.werhere_image_label.setObjectName("werhere_image_label")
        self.label = QtWidgets.QLabel(parent=self.admin_preference_menu_frame)
        self.label.setGeometry(QtCore.QRect(220, 250, 371, 21))
        self.label.setStyleSheet("background-color: qradialgradient(spread:reflect, cx:0.477, cy:0.568, radius:0.73, fx:0.46, fy:0.575, stop:0.602273 rgba(255, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(parent=self.admin_preference_menu_frame)
        self.groupBox.setGeometry(QtCore.QRect(210, 260, 391, 221))
        self.groupBox.setStyleSheet("\n"
"QGroupBox{\n"
"    border-radius : 15px;\n"
"background-color: qradialgradient(spread:pad, cx:0.488409, cy:0.557, radius:0.73, fx:0.482955, fy:0.568909, stop:0 rgba(89, 87, 87, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"}")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.interviews_pushButton = QtWidgets.QPushButton(parent=self.groupBox)
        self.interviews_pushButton.setGeometry(QtCore.QRect(150, 120, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.interviews_pushButton.setFont(font)
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
        self.mentor_interview_pushButton = QtWidgets.QPushButton(parent=self.groupBox)
        self.mentor_interview_pushButton.setGeometry(QtCore.QRect(240, 40, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.mentor_interview_pushButton.setFont(font)
        self.mentor_interview_pushButton.setStyleSheet("\n"
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
        self.mentor_interview_pushButton.setObjectName("mentor_interview_pushButton")
        self.back_menu_pushButton = QtWidgets.QPushButton(parent=self.groupBox)
        self.back_menu_pushButton.setGeometry(QtCore.QRect(40, 180, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.back_menu_pushButton.setFont(font)
        self.back_menu_pushButton.setStyleSheet("\n"
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
        self.back_menu_pushButton.setObjectName("back_menu_pushButton")
        self.Exit_pushButton = QtWidgets.QPushButton(parent=self.groupBox)
        self.Exit_pushButton.setGeometry(QtCore.QRect(230, 180, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.Exit_pushButton.setFont(font)
        self.Exit_pushButton.setStyleSheet("\n"
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
        self.Exit_pushButton.setObjectName("Exit_pushButton")
        self.application_page_pushButton = QtWidgets.QPushButton(parent=self.groupBox)
        self.application_page_pushButton.setGeometry(QtCore.QRect(40, 40, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.application_page_pushButton.setFont(font)
        self.application_page_pushButton.setStyleSheet("\n"
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
        self.application_page_pushButton.setObjectName("application_page_pushButton")
        self.werhere_image_label.raise_()
        self.groupBox.raise_()
        self.label.raise_()
        admin_pref_men_MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=admin_pref_men_MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 22))
        self.menubar.setObjectName("menubar")
        admin_pref_men_MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=admin_pref_men_MainWindow)
        self.statusbar.setObjectName("statusbar")
        admin_pref_men_MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(admin_pref_men_MainWindow)
        QtCore.QMetaObject.connectSlotsByName(admin_pref_men_MainWindow)
     
        #Butonlara fonksiyonlar burada atanıyor.
        self.application_page_pushButton.clicked.connect(self.application_page_clicked)
      
        self.mentor_interview_pushButton.clicked.connect(self.mentor_interview_clicked)
       
        self.interviews_pushButton.clicked.connect(self.interviews_clicked)
      
        self.back_menu_pushButton.clicked.connect(self.back_menu_clicked)
       
        self.Exit_pushButton.clicked.connect(self.Exit_clicked)

    #Qt Dizayner fonksiyonu.
    def retranslateUi(self, admin_pref_men_MainWindow):
        _translate = QtCore.QCoreApplication.translate
        admin_pref_men_MainWindow.setWindowTitle(_translate("admin_pref_men_MainWindow", "                                                          Admin Preference Menu "))
        self.label.setText(_translate("admin_pref_men_MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'__Inter_46a1ea\',\'__Inter_Fallback_46a1ea\',\'system-ui\',\'arial\'; font-size:10pt; font-weight:600; color:#ffffff;\">CRM - Admin Preference Menu</span></p></body></html>"))
        self.interviews_pushButton.setText(_translate("admin_pref_men_MainWindow", "Interviews"))
        self.mentor_interview_pushButton.setText(_translate("admin_pref_men_MainWindow", "Mentor Interview"))
        self.back_menu_pushButton.setText(_translate("admin_pref_men_MainWindow", "Main Menu"))
        self.Exit_pushButton.setText(_translate("admin_pref_men_MainWindow", "Exit"))
        self.application_page_pushButton.setText(_translate("admin_pref_men_MainWindow", "Applications"))
  
    #Buton fonksiyonları burada bulunuyor.
    def application_page_clicked(self):
      
        from applications_page import Ui_applications_page_MainWindow
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_applications_page_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.close()
        self.MainWindow.show()
       

    def mentor_interview_clicked(self):
       
        from mentor_interview_page import Ui_mentor_interviews_page_MainWindow
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_mentor_interviews_page_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.close()
        self.MainWindow.show()
      

    def interviews_clicked(self):
        
        from interviews_page import Ui_interviews_page_MainWindow
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_interviews_page_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.close()
        self.MainWindow.show()
        
    def back_menu_clicked(self):
        self.close()
        try:
            subprocess.Popen(["python", os.path.join(os.path.dirname(__file__), "login_window.py")])
        except FileNotFoundError:
            subprocess.Popen(["python3", os.path.join(os.path.dirname(__file__), "login_window.py")])
        

    def Exit_clicked(self):
        self.close()


# Ui_MainWindow sınıfı, QMainWindow sınıfından türetilmemişti ve dolayısıyla close() metodunu doğrudan çağıramıyordu
class MainWindow(QtWidgets.QMainWindow, Ui_admin_pref_men_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
