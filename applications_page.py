import os
import pickle
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from PyQt6 import QtCore, QtGui, QtWidgets

# Hangi kapsamları (scopes) kullanacağınızı belirtin
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# Kimlik doğrulama işlemi
def authenticate():
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

# Google Sheets'ten verileri çeken fonksiyon
def list_column_values(service, spreadsheet_id, range_name):
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
    values = result.get('values', [])
    return values

class Ui_applications_page_MainWindow(object):
    def setupUi(self, applications_page_MainWindow):
        applications_page_MainWindow.setObjectName("applications_page_MainWindow")
        applications_page_MainWindow.resize(1220, 735)
        applications_page_MainWindow.setMinimumSize(QtCore.QSize(1220, 735))
        applications_page_MainWindow.setMaximumSize(QtCore.QSize(1220, 735))
        self.centralwidget = QtWidgets.QWidget(parent=applications_page_MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1200, 700))
        self.frame.setMinimumSize(QtCore.QSize(1200, 700))
        self.frame.setMaximumSize(QtCore.QSize(1200, 700))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.Search_pushButton = QtWidgets.QPushButton(parent=self.frame)
        self.Search_pushButton.setGeometry(QtCore.QRect(9, 164, 111, 41))
        self.Search_pushButton.setStyleSheet("QPushButton:hover {\n"
"                  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0,157, 255, 255), stop:1 rgba(30, 206, 255, 255));\n"
"                  color: rgb(255, 255, 255);\n"
"                  }")
        self.Search_pushButton.setObjectName("Search_pushButton")
        self.Meetings_with_unassigned_mentor_pushButton = QtWidgets.QPushButton(parent=self.frame)
        self.Meetings_with_unassigned_mentor_pushButton.setGeometry(QtCore.QRect(9, 283, 311, 41))
        self.Meetings_with_unassigned_mentor_pushButton.setStyleSheet("QPushButton:hover {\n"
"                  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0,157, 255, 255), stop:1 rgba(30, 206, 255, 255));\n"
"                  color: rgb(255, 255, 255);\n"
"                  }")
        self.Meetings_with_unassigned_mentor_pushButton.setObjectName("Meetings_with_unassigned_mentor_pushButton")
        self.Meetings_with_assigned_mentor_pushButton = QtWidgets.QPushButton(parent=self.frame)
        self.Meetings_with_assigned_mentor_pushButton.setGeometry(QtCore.QRect(9, 223, 231, 41))
        self.Meetings_with_assigned_mentor_pushButton.setStyleSheet("QPushButton:hover {\n"
"                  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0,157, 255, 255), stop:1 rgba(30, 206, 255, 255));\n"
"                  color: rgb(255, 255, 255);\n"
"                  }")
        self.Meetings_with_assigned_mentor_pushButton.setObjectName("Meetings_with_assigned_mentor_pushButton")
        self.Different_records_pushButton = QtWidgets.QPushButton(parent=self.frame)
        self.Different_records_pushButton.setGeometry(QtCore.QRect(700, 280, 221, 41))
        self.Different_records_pushButton.setStyleSheet("QPushButton:hover {\n"
"                  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0,157, 255, 255), stop:1 rgba(30, 206, 255, 255));\n"
"                  color: rgb(255, 255, 255);\n"
"                  }")
        self.Different_records_pushButton.setObjectName("Different_records_pushButton")
        self.All_applications_pushButton = QtWidgets.QPushButton(parent=self.frame)
        self.All_applications_pushButton.setGeometry(QtCore.QRect(970, 220, 221, 101))
        self.All_applications_pushButton.setStyleSheet("QPushButton:hover {\n"
"                  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0,157, 255, 255), stop:1 rgba(30, 206, 255, 255));\n"
"                  color: rgb(255, 255, 255);\n"
"                  }")
        self.All_applications_pushButton.setObjectName("All_applications_pushButton")
        self.Filtered_Applications_pushButton = QtWidgets.QPushButton(parent=self.frame)
        self.Filtered_Applications_pushButton.setGeometry(QtCore.QRect(440, 280, 231, 41))
        self.Filtered_Applications_pushButton.setStyleSheet("QPushButton:hover {\n"
"                  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0,157, 255, 255), stop:1 rgba(30, 206, 255, 255));\n"
"                  color: rgb(255, 255, 255);\n"
"                  }")
        self.Filtered_Applications_pushButton.setObjectName("Filtered_Applications_pushButton")
        self.Former_VIT_Check_pushButton = QtWidgets.QPushButton(parent=self.frame)
        self.Former_VIT_Check_pushButton.setGeometry(QtCore.QRect(440, 220, 231, 41))
        self.Former_VIT_Check_pushButton.setStyleSheet("QPushButton:hover {\n"
"                  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0,157, 255, 255), stop:1 rgba(30, 206, 255, 255));\n"
"                  color: rgb(255, 255, 255);\n"
"                  }")
        self.Former_VIT_Check_pushButton.setObjectName("Former_VIT_Check_pushButton")
        self.Multiple_records_pushButton = QtWidgets.QPushButton(parent=self.frame)
        self.Multiple_records_pushButton.setGeometry(QtCore.QRect(700, 220, 221, 41))
        self.Multiple_records_pushButton.setStyleSheet("QPushButton:hover {\n"
"                  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0,157, 255, 255), stop:1 rgba(30, 206, 255, 255));\n"
"                  color: rgb(255, 255, 255);\n"
"                  }")
        self.Multiple_records_pushButton.setObjectName("Multiple_records_pushButton")
        self.Preferences_pushButton = QtWidgets.QPushButton(parent=self.frame)
        self.Preferences_pushButton.setGeometry(QtCore.QRect(440, 330, 171, 41))
        self.Preferences_pushButton.setStyleSheet("QPushButton:hover {\n"
"                  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0,157, 255, 255), stop:1 rgba(30, 206, 255, 255));\n"
"                  color: rgb(255, 255, 255);\n"
"                  }")
        self.Preferences_pushButton.setObjectName("Preferences_pushButton")
        self.Exit_pushButton = QtWidgets.QPushButton(parent=self.frame)
        self.Exit_pushButton.setGeometry(QtCore.QRect(1020, 330, 171, 41))
        self.Exit_pushButton.setStyleSheet("QPushButton:hover {\n"
"                  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0,157, 255, 255), stop:1 rgba(30, 206, 255, 255));\n"
"                  color: rgb(255, 255, 255);\n"
"                  }")
        self.Exit_pushButton.setObjectName("Exit_pushButton")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(440, 170, 751, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(520, 50, 161, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(10, 370, 1181, 321))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(160)
        self.Werhere = QtWidgets.QLabel(parent=self.frame)
        self.Werhere.setGeometry(QtCore.QRect(9, 3, 441, 131))
        self.Werhere.setText("")
        self.Werhere.setPixmap(QtGui.QPixmap("images/werhere_image.png"))
        self.Werhere.setObjectName("Werhere")
        self.Werhere_2 = QtWidgets.QLabel(parent=self.frame)
        self.Werhere_2.setGeometry(QtCore.QRect(750, 0, 441, 131))
        self.Werhere_2.setText("")
        self.Werhere_2.setPixmap(QtGui.QPixmap("werhere_image.png"))
        self.Werhere_2.setObjectName("Werhere_2")
        applications_page_MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=applications_page_MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1220, 43))
        self.menubar.setObjectName("menubar")
        applications_page_MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=applications_page_MainWindow)
        self.statusbar.setObjectName("statusbar")
        applications_page_MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(applications_page_MainWindow)
        QtCore.QMetaObject.connectSlotsByName(applications_page_MainWindow)


#Push Button
        # Connect header click event to sort column alphabetically
        self.tableWidget.horizontalHeader().sectionClicked.connect(self.sort_column_alphabetically)


        self.Exit_pushButton.clicked.connect(self.Exit_clicked)
        self.Preferences_pushButton.clicked.connect(self.Preferences_clicked)
        self.Former_VIT_Check_pushButton.clicked.connect(self.Former_VIT_Check_clicked)
        self.Filtered_Applications_pushButton.clicked.connect(self.Filtered_Applications_clicked)
        self.Multiple_records_pushButton.clicked.connect(self.Multiple_records_clicked)
        self.All_applications_pushButton.clicked.connect(self.load_all_applications)
        self.Meetings_with_assigned_mentor_pushButton.clicked.connect(self.Meetings_with_assigned_mentor_clicked)
        self.Meetings_with_unassigned_mentor_pushButton.clicked.connect(self.Meetings_with_unassigned_mentor_clicked)
        self.Search_pushButton.clicked.connect(self.Search_clicked)



    def retranslateUi(self, applications_page_MainWindow):
        _translate = QtCore.QCoreApplication.translate
        applications_page_MainWindow.setWindowTitle(_translate("applications_page_MainWindow", "Applications"))
        self.Search_pushButton.setText(_translate("applications_page_MainWindow", "Search"))
        self.Meetings_with_unassigned_mentor_pushButton.setText(_translate("applications_page_MainWindow", "Meetings with unassigned mentor"))
        self.Meetings_with_assigned_mentor_pushButton.setText(_translate("applications_page_MainWindow", "Meetings with assigned mentor"))
        self.Different_records_pushButton.setText(_translate("applications_page_MainWindow", "Different records"))
        self.All_applications_pushButton.setText(_translate("applications_page_MainWindow", "All applications"))
        self.Filtered_Applications_pushButton.setText(_translate("applications_page_MainWindow", "Filtered applications"))
        self.Former_VIT_Check_pushButton.setText(_translate("applications_page_MainWindow", "Former VIT Check"))
        self.Multiple_records_pushButton.setText(_translate("applications_page_MainWindow", "Multiple records"))
        self.Preferences_pushButton.setText(_translate("applications_page_MainWindow", "Preferences"))
        self.Exit_pushButton.setText(_translate("applications_page_MainWindow", "EXIT"))
        self.lineEdit_2.setText(_translate("applications_page_MainWindow", "          APPLICATIONS"))
        

        self.lineEdit.setPlaceholderText(_translate("applications_page_MainWindow", "      Name or Surname"))

     #Transitions and explainations

    def Exit_clicked(self):
        from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
        QApplication.instance().quit()   

    def Preferences_clicked(self):
        from preference_admin_menu import Ui_admin_pref_men_MainWindow
        self.MainWindow= QtWidgets.QMainWindow()
        self.ui =Ui_admin_pref_men_MainWindow()
        self.ui.setupUi(applications_page_MainWindow) 

    def Different_Records_clicked(self):
        
        # Burasi komple degisecek
        # self.filtering_list = self.applications    # I added it for filtering.
        self.worksheet = main.connection_hub('credentials/key.json', 'VIT1-2', 'Sayfa1')
        self.VIT1 = self.worksheet.get_all_values()
        self.worksheet = main.connection_hub('credentials/key.json', 'VIT2-2', 'Sayfa1')
        self.VIT2 = self.worksheet.get_all_values()

        differential_users = [self.VIT1[0]]
        for user1 in self.VIT1[1:]:
            found = False
            for user2 in self.VIT2[1:]:
                if user1[2] in user2[2]:
                    found = True
                    break
            if not found:
                differential_users.append(user1)

        for user2 in self.VIT2:
            found = False
            for user1 in self.VIT1:
                if user2[2] in user1[2]:
                    found = True
                    break
            if not found:
                differential_users.append(user2)

        if len(differential_users) > 1:  # If the searched_people variable is not empty!
            # The result obtained with the help of the method is printed into the comboBoxFilterOptions for filtering.
            # -3 row down-
            self.filtering_list = differential_users  # Assigned for filtering.
            self.form_applications.comboBoxFilterOptions.clear()
            self.form_applications.comboBoxFilterOptions.addItems(main.filter_active_options(self.filtering_list, self.filtering_column))
        else:
            no_application = ['There is no differential applicant!']
            [no_application.append('-') for i in range(len(self.applications[0]) - 1)]
            differential_users.append(no_application)
            # differential_users.append(['There is no differential applicant!', '-', '-', '-', '-', '-', '-', '-', ])
            # Above - one line - code works as same as active code. But active code is automated for cell amount
        return main.write2table(self.form_applications, differential_users)
        
    def Former_VIT_Check_clicked(self):

        print("-------Now you are looking at Former_VIT_Check")

    def Filtered_Applications_clicked(self):

        filtered_unique_applications = [self.applications[0]]
        unique_names = set()
        for application in self.applications[1:]:
            if application[2].strip().lower() not in unique_names:
                filtered_unique_applications.append(application)
                unique_names.add(application[2].strip().lower())

        if len(filtered_unique_applications) > 1:  # If the filtered_unique_applications variable is not empty!
            # The result obtained with the help of the method is printed into the comboBoxFilterOptions for filtering.
            # -3 row down-
            self.filtering_list = filtered_unique_applications  # Assigned for filtering.
            self.form_applications.comboBoxFilterOptions.clear()
            self.form_applications.comboBoxFilterOptions.addItems(main.filter_active_options(self.filtering_list, self.filtering_column))
        else:
            no_application = ['There is no application!']
            [no_application.append('-') for i in range(len(self.filtering_list[0]) - 1)]
            filtered_unique_applications.append(no_application)
            # filtered_unique_applications.append(['There is no application!', '-', '-', '-', '-', '-', '-', '-', ])
            # Above - one line - code works as same as active code. But active code is automated for cell amount
        return main.write2table(self.form_applications, filtered_unique_applications)

    def load_all_applications(self):
        # Kimlik doğrulaması yap
        creds = authenticate()
        service = build('sheets', 'v4', credentials=creds)

        # Google Sheets ID ve aralığını belirle
        spreadsheet_id = '1Ls6wq8vi_fKfVIqYiTpx3RrC4KZvPlT60D63sXboNbM'  # Google Sheets ID'nizi buraya girin
        range_name = 'Sayfa1!A1:Z1000'  # Aralığı ihtiyaçlarınıza göre ayarlayın

        # Verileri çek
        values = list_column_values(service, spreadsheet_id, range_name)

        if not values:
            print('No data found.')
            return

        # QTableWidget'e sütun başlıklarını ve verileri yükle
        self.tableWidget.setColumnCount(len(values[0]))
        self.tableWidget.setRowCount(len(values))

        # Set column headers from the first row of Google Sheets
        for col_idx, header in enumerate(values[0]):
            self.tableWidget.setHorizontalHeaderItem(col_idx, QtWidgets.QTableWidgetItem(header))

        # Load data excluding header row
        for row_idx, row_data in enumerate(values[1:]):
            for col_idx, cell_data in enumerate(row_data):
                self.tableWidget.setItem(row_idx, col_idx, QtWidgets.QTableWidgetItem(cell_data))

    # Function to sort column alphabetically when header is clicked
    def sort_column_alphabetically(self, logical_index):
        self.tableWidget.sortItems(logical_index, QtCore.Qt.SortOrder.AscendingOrder)

    def Multiple_records_clicked(self):
        print("-------Now you are looking at Multiple_records")
    def Meetings_with_assigned_mentor_clicked(self):
        print("-------Now you are looking at Meetings_with_assigned_mentor")
    def Meetings_with_unassigned_mentor_clicked(self):
        print("-------Now you are looking at Meetings_with_unassigned_mentor")
    def Search_clicked(self):

        searched_applications = [self.applications[0]]
        for application in self.applications[1:]:
            if (self.form_applications.lineEditSearch.text().strip().lower() in application[2].strip().lower()
                    and self.form_applications.lineEditSearch.text().strip().lower() != ''):
                searched_applications.append(application)

        # Make empty the search area
        self.form_applications.lineEditSearch.setText('')

        if len(searched_applications) > 1:  # If the searched_people variable is not empty!
            # The result obtained with the help of the method is printed into the comboBoxFilterOptions for filtering.
            # -3 row down-
            self.filtering_list = searched_applications  # Assigned for filtering.
            self.form_applications.comboBoxFilterOptions.clear()
            self.form_applications.comboBoxFilterOptions.addItems(main.filter_active_options(self.filtering_list, self.filtering_column))
        else:
            self.form_applications.comboBoxFilterOptions.clear()    # clears the combobox
            no_application = ['No User or Mentor Found!']
            [no_application.append('-') for i in range(len(self.applications[0]) - 1)]
            searched_applications.append(no_application)
            # searched_applications.append(['No User or Mentor Found!', '-', '-', '-', '-', '-', '-', '-', ])
            # Above - one line - code works as same as active code. But active code is automated for cell amount
        return main.write2table(self.form_applications, searched_applications)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    applications_page_MainWindow = QtWidgets.QMainWindow()
    ui = Ui_applications_page_MainWindow()
    ui.setupUi(applications_page_MainWindow)
    applications_page_MainWindow.show()
    sys.exit(app.exec())