from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import os
from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtWidgets import QMessageBox

# Google Sheets API kapsamları
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

def list_column_values(service, spreadsheet_id, range_name):
    """
    Belirli bir Google Sheets'deki belirli bir aralıktaki değerleri listeler.
    """
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
    values = result.get('values', [])
    if not values:
        return {}
    headers = values[0]
    data = {header: [] for header in headers}
    for row in values[1:]:
        for i, header in enumerate(headers):
            data[header].append(row[i] if i < len(row) else None)
    return data

def authenticate():
    """
    Google Sheets API'ına kimlik doğrulama yapar.
    """
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return creds

def authenticate_user(username, password):
    """
    Veritabanındaki kullanıcı adı ve şifreyi doğrular.
    """
    credentials = authenticate()
    if credentials is None:
        return None
    service = build('sheets', 'v4', credentials=credentials)
    spreadsheet_id = '1nyTJioGcvDyHV8ZryxdWmU3ziBe1Txs9mC0yuDhrVUg'  # "Kullanicilar" dosyasının kimliği
    range_name = 'Form Yanıtları 1!A:C'
    column_values = list_column_values(service, spreadsheet_id, range_name)
    for i in range(len(column_values['kullanici'])):
        if column_values['kullanici'][i] == username and column_values['parola'][i] == password:
            return column_values['yetki'][i]
    return None

class Ui_LoginMainWindow(object):
    def setupUi(self, LoginMainWindow):
        self.main_window= LoginMainWindow
        LoginMainWindow.setObjectName("LoginMainWindow")
        LoginMainWindow.resize(500, 385)
        LoginMainWindow.setMinimumSize(QtCore.QSize(500, 385))
        LoginMainWindow.setMaximumSize(QtCore.QSize(500, 385))
        self.centralwidget = QtWidgets.QWidget(parent=LoginMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_login_main = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_login_main.setGeometry(QtCore.QRect(0, -30, 600, 415))
        self.frame_login_main.setMinimumSize(QtCore.QSize(600, 415))
        self.frame_login_main.setMaximumSize(QtCore.QSize(600, 415))
        self.frame_login_main.setAutoFillBackground(False)
        self.frame_login_main.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.489, y1:1, x2:0.494, y2:0, stop:0 rgba(71, 71, 71, 255), stop:1 rgba(255, 255, 255, 255));")
        self.frame_login_main.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.frame_login_main.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_login_main.setObjectName("frame_login_main")
        self.werhere_image_label = QtWidgets.QLabel(parent=self.frame_login_main)
        self.werhere_image_label.setGeometry(QtCore.QRect(10, 50, 471, 71))
        self.werhere_image_label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.werhere_image_label.setText("")
        self.werhere_image_label.setPixmap(QtGui.QPixmap("images/werhere_image.png"))
        self.werhere_image_label.setScaledContents(True)
        self.werhere_image_label.setObjectName("werhere_image_label")
        self.welkomTextEdit_2 = QtWidgets.QTextEdit(parent=self.frame_login_main)
        self.welkomTextEdit_2.setGeometry(QtCore.QRect(0, 340, 501, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.welkomTextEdit_2.setFont(font)
        self.welkomTextEdit_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.welkomTextEdit_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.welkomTextEdit_2.setObjectName("welkomTextEdit_2")
        self.welkomTextEdit = QtWidgets.QTextEdit(parent=self.frame_login_main)
        self.welkomTextEdit.setGeometry(QtCore.QRect(30, 30, 461, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.welkomTextEdit.setFont(font)
        self.welkomTextEdit.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.welkomTextEdit.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.welkomTextEdit.setObjectName("welkomTextEdit")
        self.admin_login_groupBox = QtWidgets.QGroupBox(parent=self.frame_login_main)
        self.admin_login_groupBox.setGeometry(QtCore.QRect(60, 140, 388, 183))
        self.admin_login_groupBox.setMinimumSize(QtCore.QSize(388, 181))
        self.admin_login_groupBox.setMaximumSize(QtCore.QSize(388, 183))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        self.admin_login_groupBox.setFont(font)
        self.admin_login_groupBox.setStyleSheet("\n"
"QGroupBox{\n"
"    border-radius : 15px;\n"
"background-color: qradialgradient(spread:pad, cx:0.488409, cy:0.557, radius:0.73, fx:0.482955, fy:0.568909, stop:0 rgba(89, 87, 87, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"}")
        self.admin_login_groupBox.setTitle("")
        self.admin_login_groupBox.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.admin_login_groupBox.setObjectName("admin_login_groupBox")
        self.admin_login_pushButton = QtWidgets.QPushButton(parent=self.admin_login_groupBox)
        self.admin_login_pushButton.setGeometry(QtCore.QRect(150, 140, 75, 24))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.admin_login_pushButton.setFont(font)
        self.admin_login_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.admin_login_pushButton.setStyleSheet("\n"
"QPushButton:hover{\n"
"   border-radius : 6px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color:  ;\n"
"    background-color: rgb(218, 30, 60);\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"\n"
"}")
        self.admin_login_pushButton.setObjectName("admin_login_pushButton")
        self.admin_password_lineEdit_4 = QtWidgets.QLineEdit(parent=self.admin_login_groupBox)
        self.admin_password_lineEdit_4.setGeometry(QtCore.QRect(160, 80, 161, 31))
        self.admin_password_lineEdit_4.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius : 10px ;")
        self.admin_password_lineEdit_4.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.admin_password_lineEdit_4.setObjectName("admin_password_lineEdit_4")
        self.admin_user_name_label = QtWidgets.QLabel(parent=self.admin_login_groupBox)
        self.admin_user_name_label.setGeometry(QtCore.QRect(50, 50, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.admin_user_name_label.setFont(font)
        self.admin_user_name_label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.admin_user_name_label.setObjectName("admin_user_name_label")
        self.admin_password_label = QtWidgets.QLabel(parent=self.admin_login_groupBox)
        self.admin_password_label.setGeometry(QtCore.QRect(50, 90, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.admin_password_label.setFont(font)
        self.admin_password_label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.admin_password_label.setObjectName("admin_password_label")
        self.admin_username_lineEdit_3 = QtWidgets.QLineEdit(parent=self.admin_login_groupBox)
        self.admin_username_lineEdit_3.setGeometry(QtCore.QRect(160, 40, 161, 31))
        self.admin_username_lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius : 10px ;")
        self.admin_username_lineEdit_3.setObjectName("admin_username_lineEdit_3")
        self.admin_exit_pushButton = QtWidgets.QPushButton(parent=self.admin_login_groupBox)
        self.admin_exit_pushButton.setGeometry(QtCore.QRect(240, 140, 75, 24))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.admin_exit_pushButton.setFont(font)
        self.admin_exit_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.admin_exit_pushButton.setStyleSheet("\n"
"QPushButton:hover{\n"
"   border-radius : 6px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color:  ;\n"
"    background-color: rgb(218, 30, 60);\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"\n"
"}")
        self.admin_exit_pushButton.setObjectName("admin_exit_pushButton")
        self.label = QtWidgets.QLabel(parent=self.frame_login_main)
        self.label.setGeometry(QtCore.QRect(70, 130, 371, 21))
        self.label.setStyleSheet("background-color: qradialgradient(spread:reflect, cx:0.477, cy:0.568, radius:0.73, fx:0.46, fy:0.575, stop:0.602273 rgba(255, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.label.setObjectName("label")
        LoginMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=LoginMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 22))
        self.menubar.setObjectName("menubar")
        LoginMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=LoginMainWindow)
        self.statusbar.setObjectName("statusbar")
        LoginMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginMainWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginMainWindow)

        #Butunların tanımladığı yer

        self.admin_login_pushButton.clicked.connect(self.admin_login_clicked)
        self.admin_exit_pushButton.clicked.connect(self.admin_exit_clicked)


    def retranslateUi(self, LoginMainWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginMainWindow.setWindowTitle(_translate("LoginMainWindow", "MainWindow"))
        self.welkomTextEdit_2.setHtml(_translate("LoginMainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:10pt; font-weight:700; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:400; color:#ffffff;\">copyright@WearehereAcademy-2024</span></p></body></html>"))
        self.welkomTextEdit.setHtml(_translate("LoginMainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:700; color:#47555a;\">Welcome to</span></p></body></html>"))
        self.admin_login_pushButton.setText(_translate("LoginMainWindow", "Login"))
        self.admin_password_lineEdit_4.setPlaceholderText(_translate("LoginMainWindow", "Password"))
        self.admin_user_name_label.setText(_translate("LoginMainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:400; color:#ffffff;\">Username</span></p></body></html>"))
        self.admin_password_label.setText(_translate("LoginMainWindow", "<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">Password</span></p></body></html>"))
        self.admin_username_lineEdit_3.setPlaceholderText(_translate("LoginMainWindow", "Username"))
        self.admin_exit_pushButton.setText(_translate("LoginMainWindow", "Exit"))
        self.label.setText(_translate("LoginMainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'__Inter_46a1ea\',\'__Inter_Fallback_46a1ea\',\'system-ui\',\'arial\'; font-size:10pt; font-weight:600; color:#ffffff;\">CRM (Customer Relationship Management)</span></p></body></html>"))


        #Buton fonksiyonlarının tanımlandığı yer
    
    def admin_login_clicked(self):
        username = self.admin_username_lineEdit_3.text()
        password = self.admin_password_lineEdit_4.text()
        result = authenticate_user(username, password)
        
        
        if result == "admin":
            QMessageBox.information(self.centralwidget, "Başarılı", "Admin girişi başarılı!")
            from preference_admin_menu import Ui_admin_pref_men_MainWindow
            self.adminWindow = QtWidgets.QMainWindow()
            self.adminUi = Ui_admin_pref_men_MainWindow()
            self.adminUi.setupUi(self.adminWindow)
            self.adminWindow.show()
            self.main_window.close()
            
            
        elif result == "user":
            QMessageBox.information(self.centralwidget, "Başarılı", "User girişi başarılı!")
            from preference_menu import  Ui_MainWindow
            self.userWindow = QtWidgets.QMainWindow()
            self.userUi =  Ui_MainWindow()
            self.userUi.setupUi(self.userWindow)
            self.userWindow.show()
            self.main_window.close()
        else:
            QMessageBox.warning(self, "Hata", "Kullanıcı adı veya şifre hatalı!")
            self.admin_username_lineEdit_3.clear()
            self.admin_password_lineEdit_4.clear()

    def admin_exit_clicked(self):
        QtWidgets.QApplication.instance().quit()
 
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
