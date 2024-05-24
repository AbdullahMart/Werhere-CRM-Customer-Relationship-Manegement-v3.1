import sys
import os
import pickle
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QLineEdit,
                             QPushButton, QTableWidget, QTableWidgetItem, QLabel, QGridLayout, QHeaderView)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import subprocess
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

# Google Sheets API erişim kapsamı ve sayfa bilgileri
SCOPES = ['https://www.googleapis.com/auth/gmail.send', 'https://www.googleapis.com/auth/calendar','https://www.googleapis.com/auth/calendar.readonly']
SPREADSHEET_ID = '1Ak9sLDxCEGy092Pa7lXFahpJcG0xLUxpNHhTwOzE-_c'
RANGE_NAME = 'Sayfa1!A1:K40'

class MentorMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.creds = self.authenticate()  # Google Sheets API için kimlik doğrulama
        self.full_data = []  # Veriler için boş bir liste başlat
        self.setup_ui()  # UI bileşenlerini kurma

    def setup_ui(self):
        self.setWindowTitle('Mentor Menu')
        self.setGeometry(100, 100, 800, 600)
        main_layout = QVBoxLayout(self)

        # Resim etiketi
        self.image_label = QLabel(self)
        pixmap = QPixmap('images/werhere_image.png')  # Resmin yolu
        scaled_pixmap = pixmap.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio)  # Resmi ölçeklendir
        self.image_label.setPixmap(scaled_pixmap)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.image_label)

        # Arama çubuğu ve buton düzeni
        search_layout = QHBoxLayout()
        self.search_input = QLineEdit(self)
        self.search_input.setPlaceholderText('Name/Surname')
        self.search_input.setFixedHeight(40)
        self.search_input.setStyleSheet("font-size: 18px;")
        self.search_button = QPushButton('Search', self)
        self.search_button.setFixedHeight(40)
        self.search_button.setStyleSheet(self.button_style())
        self.search_button.clicked.connect(self.perform_search)
        self.search_input.returnPressed.connect(self.perform_search)
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(self.search_button)
        main_layout.addLayout(search_layout)

        # ComboBox ve diğer butonlar için düzen
        grid_layout = QGridLayout()
        self.combo_box = QComboBox(self)
        self.combo_box.addItems([
            'Please choose from here',
            'VIT projesinin tamamına katılması uygun olur',
            'VIT projesi ilk IT eğitimi alıp ITPH a yönlendirilmesi uygun olur',
            'VIT projesi ingilizce eğitimi alıp ITPH a yönlendirilmesi uygun olur',
            'VIT projesi kapsamında direkt ITPH a yönlendirilmesi uygun olur',
            'Direkt bireysel koçluk ile işe yönlendirilmesi uygun olur',
            'Bir sonraki VIT projesine katılması daha uygun olur',
            'Başka bir sektöre yönlendirilmeli',
            'Diğer'
        ])
        self.combo_box.setFixedHeight(40)
        self.combo_box.setStyleSheet("font-size: 18px;")
        self.combo_box.currentIndexChanged.connect(self.filter_by_status)
        grid_layout.addWidget(self.combo_box, 0, 0, 1, 2)

        # "All Interviews" butonu
        all_interviews_button = QPushButton('All Interviews', self)
        all_interviews_button.clicked.connect(self.load_all_data)
        all_interviews_button.setFixedHeight(40)
        all_interviews_button.setStyleSheet(self.button_style())
        grid_layout.addWidget(all_interviews_button, 1, 0, 1, 2)

        # "Preferences" butonu
        preferences_button = QPushButton('Preferences', self)
        preferences_button.setFixedHeight(40)
        preferences_button.setStyleSheet(self.button_style())
        preferences_button.clicked.connect(self.open_preferences)
        grid_layout.addWidget(preferences_button, 2, 0, 1, 2)

        # "Exit" butonu
        exit_button = QPushButton('Exit', self)
        exit_button.setFixedHeight(40)
        exit_button.setStyleSheet(self.button_style())
        exit_button.clicked.connect(self.open_login)
        grid_layout.addWidget(exit_button, 3, 0, 1, 2)

        main_layout.addLayout(grid_layout)

        # Tablo widget'ı
        self.table_widget = QTableWidget(self)
        self.table_widget.setRowCount(0)
        self.table_widget.setColumnCount(0)
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table_widget.horizontalHeader().sectionClicked.connect(self.sort_table_data)
        main_layout.addWidget(self.table_widget)

        self.setLayout(main_layout)

    def button_style(self):
        # Butonlar için stil
        return """
            QPushButton {
                border-radius: 15px;
                background-color: gray;
                color: green;
                font-size: 18px;
            }
            QPushButton:hover {
                background-color: orange;
            }
        """

    def authenticate(self):
        # Google Sheets API kimlik doğrulama
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

    def perform_search(self):
        # Arama işlemi
        search_text = self.search_input.text().lower()
        self.load_data(filter_text=search_text)

    def load_all_data(self):
        # Tüm verileri yükle
        self.load_data()

    def load_data(self, filter_text=None):
        # Google Sheets'ten verileri çek
        service = build('sheets', 'v4', credentials=self.creds)
        result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
        data = result.get('values', [])
        self.full_data = data

        if filter_text:
            # Arama filtresi uygula
            headers = data[0]
            filtered_data = [row for row in data if filter_text in row[1].lower() or filter_text in row[2].lower()]
            data = [headers] + filtered_data

        self.populate_table(data)

    def filter_by_status(self):
        # Duruma göre filtrele
        if not self.full_data:
            return  # Eğer full_data boşsa, filtreleme yapma

        selected_status = self.combo_box.currentText()
        headers = self.full_data[0]
        if selected_status == 'Please choose from here':
            self.populate_table(self.full_data)
        elif selected_status == 'Diğer':
            filtered_data = [row for row in self.full_data[1:] if row[4] not in [
                'VIT projesinin tamamına katılması uygun olur',
                'VIT projesi ilk IT eğitimi alıp ITPH a yönlendirilmesi uygun olur',
                'VIT projesi ingilizce eğitimi alıp ITPH a yönlendirilmesi uygun olur',
                'VIT projesi kapsamında direkt ITPH a yönlendirilmesi uygun olur',
                'Direkt bireysel koçluk ile işe yönlendirilmesi uygun olur',
                'Bir sonraki VIT projesine katılması daha uygun olur',
                'Başka bir sektöre yönlendirilmeli'
            ]]
            self.populate_table([headers] + filtered_data)
        else:
            filtered_data = [row for row in self.full_data[1:] if selected_status in row[4]]  # E sütununda filtrele
            self.populate_table([headers] + filtered_data)

    def populate_table(self, data):
        # Tabloyu doldur
        if data:
            headers = data[0]
            rows = data[1:]
            self.table_widget.setColumnCount(len(headers))
            self.table_widget.setRowCount(len(rows))
            self.table_widget.setHorizontalHeaderLabels(headers)
            for row_index, row in enumerate(rows):
                for column_index, item in enumerate(row):
                    self.table_widget.setItem(row_index, column_index, QTableWidgetItem(item))
        else:
            self.table_widget.setColumnCount(0)
            self.table_widget.setRowCount(0)

    def sort_table_data(self, column_index):
        # Tabloyu sütun başlıklarına göre sırala
        row_count = self.table_widget.rowCount()
        column_count = self.table_widget.columnCount()
        data = [[self.table_widget.item(row, col).text() if self.table_widget.item(row, col) else '' for col in range(column_count)] for row in range(row_count)]
        data.sort(key=lambda x: x[column_index])
        headers = [self.table_widget.horizontalHeaderItem(i).text() for i in range(column_count)]
        self.populate_table([headers] + data)

    def open_preferences(self):
        # Preferences butonuna basıldığında yeni bir pencere aç
        current_file = os.path.abspath(__file__)
        current_dir = os.path.dirname(current_file)
        preferences_file = os.path.join(current_dir, 'preference_admin_menu.py')
        subprocess.Popen([sys.executable, preferences_file])
        self.close()

    def open_login(self):
        # Exit butonuna basıldığında login penceresi aç
        current_file = os.path.abspath(__file__)
        current_dir = os.path.dirname(current_file)
        login_file = os.path.join(current_dir, 'login_window.py')
        subprocess.Popen([sys.executable, login_file])
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MentorMenu()
    form.show()
    sys.exit(app.exec())

