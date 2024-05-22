from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import os
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtWidgets import QMessageBox
from Ui.login_window_ui import Ui_LoginMainWindow  # login_window_ui dosyasından Ui_LoginMainWindow sınıfını içe aktarıyoruz

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

class Ui_MainWindow(QtWidgets.QMainWindow, Ui_LoginMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


        #Butunların tanımladığı yer

        self.admin_login_pushButton.clicked.connect(self.admin_login_clicked)
        self.admin_exit_pushButton.clicked.connect(self.admin_exit_clicked)

        #Buton fonksiyonlarının tanımlandığı yer
    
    def admin_login_clicked(self):
        username = self.admin_username_lineEdit_3.text()
        password = self.admin_password_lineEdit_4.text()
        result = authenticate_user(username, password)
        if result == "admin":
            QMessageBox.information(self, "Başarılı", "Admin girişi başarılı!")
            from preference_admin_menu import Ui_admin_pref_men_MainWindow
            self.adminWindow = QtWidgets.QMainWindow()
            self.adminUi = Ui_admin_pref_men_MainWindow()
            self.adminUi.setupUi(self.adminWindow)
            self.adminWindow.show()
            self.close()
        elif result == "user":
            QMessageBox.information(self, "Başarılı", "User girişi başarılı!")
            from preference_menu import Ui_MainWindow
            self.userWindow = QtWidgets.QMainWindow()
            self.userUi = Ui_MainWindow()
            self.userUi.setupUi(self.userWindow)
            self.userWindow.show()
            self.close()
        else:
            QMessageBox.warning(self, "Hata", "Kullanıcı adı veya şifre hatalı!")
            self.admin_username_lineEdit_3.clear()
            self.admin_password_lineEdit_4.clear()

    def admin_exit_clicked(self):
        QtWidgets.QApplication.instance().quit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec())
