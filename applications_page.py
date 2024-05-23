import subprocess
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QTableWidget, QLabel, QTableWidgetItem, QComboBox
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt
import sys
import os
import pickle
from collections import Counter, defaultdict
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

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

class ApplicationWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Pencere başlığı ve boyutu
        self.setWindowTitle("Applications")
        self.setGeometry(100, 100, 1220, 735)

        # Merkezi widget ve ana layout
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.mainLayout = QVBoxLayout(self.centralWidget)

        # Arama çubuğu ve butonu yatay layout
        self.searchLayout = QHBoxLayout()

        # PNG için QLabel
        self.pngLabel = QLabel()
        self.pngLabel.setPixmap(QPixmap("images/werhere_image.png"))
        self.pngLabel.setFixedSize(250, 40)  # PNG boyutunu ayarlayın
        self.pngLabel.setScaledContents(True)

        # QLineEdit ve Search butonu
        self.searchLineEdit = QLineEdit()
        self.searchLineEdit.setMaximumWidth(540)  # Arama çubuğunun maksimum genişliğini ayarlayın
        self.searchLineEdit.setPlaceholderText("Name/Surname")  # Placeholder text
        self.searchLineEdit.returnPressed.connect(self.search_applications)  # Enter tuşuna basıldığında arama yap

        self.searchButton = QPushButton("Search")
        self.searchButton.setStyleSheet("""
        QPushButton {
            background-color: #696969; /* Koyu gri */
            border-radius: 10px;
            padding: 10px;
            color: white; /* Beyaz metin rengi */
        }
        QPushButton:hover {
            background-color: #40E0D0; /* Turkuaz */
        }
        """)
        self.searchButton.clicked.connect(self.search_applications)  # Butona tıklandığında arama yap

        # PNG ve arama elemanlarını layout'a ekle
        self.searchLayout.addWidget(self.pngLabel)
        self.searchLayout.addWidget(self.searchLineEdit)
        self.searchLayout.addWidget(self.searchButton)
        self.mainLayout.addLayout(self.searchLayout)

        # Diğer butonlar için layout
        self.buttonLayout = QHBoxLayout()

        self.leftButtonLayout = QVBoxLayout()
        self.middleButtonLayout = QVBoxLayout()
        self.rightButtonLayout = QVBoxLayout()

        # Buton stil sayfası (hover rengi turkuaz yapar, köşeleri yuvarlar)
        button_style = """
        QPushButton {
            background-color: #696969; /* Koyu gri */
            border-radius: 10px;
            padding: 10px;
            color: white; /* Beyaz metin rengi */
        }
        QPushButton:hover {
            background-color: #40E0D0; /* Turkuaz */
        }
        """

        # Buton isimleri ve sıralaması
        button_texts = [
            "All Applications", "Meetings with Assigned Mentor", "Filtered Applications",
            "Multiple Registrations", "Meetings with Unassigned Mentor", "Preferences",
            "Different Registrations", "Former VIT Check", "EXIT"
        ]

        # Butonları oluştur ve uygun layout'a ekle
        for i, text in enumerate(button_texts):
            button = QPushButton(text)
            button.setStyleSheet(button_style)
            button.setMinimumHeight(40)  # Minimum buton yüksekliği
            button.clicked.connect(self.handleButtonClick)  # Tıklama olayını bağla

            if i < 3:
                self.leftButtonLayout.addWidget(button)
            elif i < 6:
                self.middleButtonLayout.addWidget(button)
            else:
                self.rightButtonLayout.addWidget(button)

        self.buttonLayout.addLayout(self.leftButtonLayout)
        self.buttonLayout.addLayout(self.middleButtonLayout)
        self.buttonLayout.addLayout(self.rightButtonLayout)

        self.mainLayout.addLayout(self.buttonLayout)

        # ComboBox'u butonların altına ekle
        self.comboBox = QComboBox()
        self.comboBox.addItems([
            "Language level B1 and above [Ingilizce]",
            "Language level A2 and below [Ingilizce]",
            "Language level B1 and above [Nederlands]",
            "Language level A2 and below [Nederlands]",
            "At least one of English and Nederlands is at B1 level"
        ])
        self.comboBox.currentIndexChanged.connect(self.handleComboBoxChange)
        self.mainLayout.addWidget(self.comboBox)

        # QTableWidget
        self.tableWidget = QTableWidget()
        self.tableWidget.setFont(QFont("Arial", 11))
        self.tableWidget.setSortingEnabled(True)  # Sıralama etkinleştirildi
        self.tableWidget.setSizeAdjustPolicy(QTableWidget.SizeAdjustPolicy.AdjustToContents)
        self.mainLayout.addWidget(self.tableWidget)

    def handleButtonClick(self):
        sender = self.sender()
        if sender.text() == "All Applications":
            self.load_all_applications()
        elif sender.text() == "Multiple Registrations":
            self.find_multiple_registrations()
        elif sender.text() == "Meetings with Assigned Mentor":
            self.find_assigned_mentor_meetings()
        elif sender.text() == "Meetings with Unassigned Mentor":
            self.find_unassigned_mentor_meetings()
        elif sender.text() == "Filtered Applications":
            self.find_filtered_applications()
        elif sender.text() == "Preferences":
            self.open_preferences()
        elif sender.text() == "Different Registrations":
            self.find_different_registrations()
        elif sender.text() == "Former VIT Check":
            self.former_vit_check()
        elif sender.text() == "EXIT":
            self.exit_application()

    def handleComboBoxChange(self):
        index = self.comboBox.currentIndex()
        if index == 0:
            self.find_language_level("K", ["B1", "B2 ve üzeri", "C1", "C2"])
        elif index == 1:
            self.find_language_level("K", ["A0", "A1", "A2"])
        elif index == 2:
            self.find_language_level("L", ["B1", "B2 ve üzeri", "C1", "C2"])
        elif index == 3:
            self.find_language_level("L", ["A0", "A1", "A2"])
        elif index == 4:
            self.find_combined_language_level()

    def find_language_level(self, column_letter, levels):
        try:
            creds = authenticate()
            service = build('sheets', 'v4', credentials=creds)
            spreadsheet_id = '1Ls6wq8vi_fKfVIqYiTpx3RrC4KZvPlT60D63sXboNbM'  # Kendi Spreadsheet ID'nizi ekleyin
            range_name = 'Sayfa1!A1:V40'  # Kendi veri aralığınızı ekleyin
            data = list_column_values(service, spreadsheet_id, range_name)
            headers = data[0]

            # Sütun harfinden indeksi bul
            column_index = ord(column_letter) - ord('A')

            filtered_data = [row for row in data if len(row) > column_index and row[column_index] in levels]
            filtered_data.insert(0, headers)  # Başlıkları tekrar ekle

            self.load_data(filtered_data)
        except Exception as e:
            print(f"Error finding language level {column_letter}: {e}")

    def find_combined_language_level(self):
        try:
            creds = authenticate()
            service = build('sheets', 'v4', credentials=creds)
            spreadsheet_id = '1Ls6wq8vi_fKfVIqYiTpx3RrC4KZvPlT60D63sXboNbM'  # Kendi Spreadsheet ID'nizi ekleyin
            range_name = 'Sayfa1!A1:V40'  # Kendi veri aralığınızı ekleyin
            data = list_column_values(service, spreadsheet_id, range_name)
            headers = data[0]

            english_column_index = ord('K') - ord('A')
            dutch_column_index = ord('L') - ord('A')
            levels = ["B1", "B2 ve üzeri", "C1", "C2"]

            filtered_data = [row for row in data if (
                (len(row) > english_column_index and row[english_column_index] in levels) or 
                (len(row) > dutch_column_index and row[dutch_column_index] in levels)
            )]
            filtered_data.insert(0, headers)  # Başlıkları tekrar ekle

            self.load_data(filtered_data)
        except Exception as e:
            print(f"Error finding combined language levels: {e}")

    def load_all_applications(self):
        try:
            creds = authenticate()
            service = build('sheets', 'v4', credentials=creds)
            spreadsheet_id = '1Ls6wq8vi_fKfVIqYiTpx3RrC4KZvPlT60D63sXboNbM'  # Kendi Spreadsheet ID'nizi ekleyin
            range_name = 'Sayfa1!A1:V40'  # Kendi veri aralığınızı ekleyin
            data = list_column_values(service, spreadsheet_id, range_name)
            print("Data retrieved from Google Sheets:", data)  # Hata ayıklama için veriyi yazdırın
            self.load_data(data)
        except Exception as e:
            print(f"Error loading data: {e}")

    def find_multiple_registrations(self):
        try:
            creds = authenticate()
            service = build('sheets', 'v4', credentials=creds)
            spreadsheet_id = '1Ls6wq8vi_fKfVIqYiTpx3RrC4KZvPlT60D63sXboNbM'  # Kendi Spreadsheet ID'nizi ekleyin
            range_name = 'Sayfa1!A1:V40'  # Kendi veri aralığınızı ekleyin
            data = list_column_values(service, spreadsheet_id, range_name)
            headers = data[0]
            name_column = [row[1].strip().lower() for row in data[1:]]  # B sütunu (isimler) büyük/küçük harf duyarsız
            name_counts = Counter(name_column)

            # Birden fazla kayıt bulunan isimler
            multiple_names = {name for name, count in name_counts.items() if count > 1}

            # İlgili satırları filtrele
            filtered_data = [row for row in data if row[1].strip().lower() in multiple_names]
            filtered_data.insert(0, headers)  # Başlıkları tekrar ekle

            self.load_data(filtered_data)
        except Exception as e:
            print(f"Error finding multiple registrations: {e}")

    def find_assigned_mentor_meetings(self):
        try:
            creds = authenticate()
            service = build('sheets', 'v4', credentials=creds)
            spreadsheet_id = '1Ls6wq8vi_fKfVIqYiTpx3RrC4KZvPlT60D63sXboNbM'  # Kendi Spreadsheet ID'nizi ekleyin
            range_name = 'Sayfa1!A1:V40'  # Kendi veri aralığınızı ekleyin
            data = list_column_values(service, spreadsheet_id, range_name)
            headers = data[0]
            
            # "Mentor Görüşmesi" sütunu U (21. sütun) olduğu için kontrol edin
            filtered_data = [row for row in data if len(row) > 20 and row[20].strip().
                        strip().upper() == "OK"]
            filtered_data.insert(0, headers)  # Başlıkları tekrar ekle
            
            self.load_data(filtered_data)
        except Exception as e:
            print(f"Error finding assigned mentor meetings: {e}")

    def find_unassigned_mentor_meetings(self):
        try:
            creds = authenticate()
            service = build('sheets', 'v4', credentials=creds)
            spreadsheet_id = '1Ls6wq8vi_fKfVIqYiTpx3RrC4KZvPlT60D63sXboNbM'  # Kendi Spreadsheet ID'nizi ekleyin
            range_name = 'Sayfa1!A1:V40'  # Kendi veri aralığınızı ekleyin
            data = list_column_values(service, spreadsheet_id, range_name)
            headers = data[0]
            
            # "Mentor Görüşmesi" sütunu U (21. sütun) olduğu için kontrol edin
            filtered_data = [row for row in data if len(row) > 20 and row[20].strip().upper() != "OK"]
            filtered_data.insert(0, headers)  # Başlıkları tekrar ekle
            
            self.load_data(filtered_data)
        except Exception as e:
            print(f"Error finding unassigned mentor meetings: {e}")

    def find_filtered_applications(self):
        try:
            creds = authenticate()
            service = build('sheets', 'v4', credentials=creds)
            spreadsheet_id = '1Ls6wq8vi_fKfVIqYiTpx3RrC4KZvPlT60D63sXboNbM'  # Kendi Spreadsheet ID'nizi ekleyin
            range_name = 'Sayfa1!A1:V40'  # Kendi veri aralığınızı ekleyin
            data = list_column_values(service, spreadsheet_id, range_name)
            headers = data[0]
            
            seen_names = set()
            filtered_data = []
            
            for row in data[1:]:
                name = row[1].strip().lower()  # B sütunu (isim ve soyisim) büyük/küçük harf duyarsız
                if name not in seen_names:
                    seen_names.add(name)
                    filtered_data.append(row)
            
            filtered_data.insert(0, headers)  # Başlıkları tekrar ekle
            
            self.load_data(filtered_data)
        except Exception as e:
            print(f"Error finding filtered applications: {e}")

    def load_data(self, data):
        if not data:
            print("No data found.")
            return

        headers = data[0]  # İlk satır başlıkları içerir
        rows = len(data)
        cols = len(headers)

        self.tableWidget.setRowCount(rows - 1)
        self.tableWidget.setColumnCount(cols)

        # Sütun başlıklarını ayarla
        self.tableWidget.setHorizontalHeaderLabels(headers)

        # Verileri tabloya ekle
        for row in range(1, rows):
            for col in range(cols):
                item = QTableWidgetItem(data[row][col])
                self.tableWidget.setItem(row - 1, col, item)

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

    def search_applications(self):
        search_text = self.searchLineEdit.text().strip().lower()
        if not search_text:
            return
        
        try:
            creds = authenticate()
            service = build('sheets', 'v4', credentials=creds)
            spreadsheet_id = '1Ls6wq8vi_fKfVIqYiTpx3RrC4KZvPlT60D63sXboNbM'  # Kendi Spreadsheet ID'nizi ekleyin
            range_name = 'Sayfa1!A1:V40'  # Kendi veri aralığınızı ekleyin
            data = list_column_values(service, spreadsheet_id, range_name)
            headers = data[0]
            filtered_data = [row for row in data if search_text in row[1].lower()]
            filtered_data.insert(0, headers)  # Başlıkları tekrar ekle
            self.load_data(filtered_data)
        except Exception as e:
            print(f"Error searching data: {e}")

    def former_vit_check(self):
        try:
            creds = authenticate()
            service = build('sheets', 'v4', credentials=creds)

            # VIT1 dosyasından verileri çek
            vit1_spreadsheet_id = '1JKrqbqj6kmwE7jVgSScQbIVXu3QeEnDYZZ6cxl8nXbA'
            vit1_range_name = 'Sayfa1!A1:V40'
            vit1_data = list_column_values(service, vit1_spreadsheet_id, vit1_range_name)
            vit1_names = {row[1].strip().lower() for row in vit1_data[1:]}

            # VIT2 dosyasından verileri çek
            vit2_spreadsheet_id = '1NHQPJGHnyIwX1GCXE8nWDeVL5_GTEMJbRnaA2Vemmr0'
            vit2_range_name = 'Sayfa1!A1:V40'
            vit2_data = list_column_values(service, vit2_spreadsheet_id, vit2_range_name)
            vit2_names = {row[1].strip().lower() for row in vit2_data[1:]}

            # Başvurular dosyasından verileri çek
            basvurular_spreadsheet_id = '1Ls6wq8vi_fKfVIqYiTpx3RrC4KZvPlT60D63sXboNbM'
            basvurular_range_name = 'Sayfa1!A1:V40'
            basvurular_data = list_column_values(service, basvurular_spreadsheet_id, basvurular_range_name)
            headers = basvurular_data[0]

            # İsimlerin en az iki dosyada bulunduğunu kontrol et
            all_names = defaultdict(int)
            for name in vit1_names:
                all_names[name] += 1
            for name in vit2_names:
                all_names[name] += 1
            for row in basvurular_data[1:]:
                name = row[1].strip().lower()
                all_names[name] += 1

            # En az iki dosyada bulunan isimleri filtrele
            common_names = {name for name, count in all_names.items() if count > 1}

            # İlgili satırları filtrele ve aynı kişiyi sadece bir kez ekle
            added_names = set()
            filtered_data = []
            for row in basvurular_data[1:]:
                name = row[1].strip().lower()
                if name in common_names and name not in added_names:
                    filtered_data.append(row)
                    added_names.add(name)

            filtered_data.insert(0, headers)  # Başlıkları tekrar ekle

            self.load_data(filtered_data)
        except Exception as e:
            print(f"Error finding former VIT check: {e}")

    def find_different_registrations(self):
        try:
            creds = authenticate()
            service = build('sheets', 'v4', credentials=creds)

            # VIT1 dosyasından verileri çek
            vit1_spreadsheet_id = '1JKrqbqj6kmwE7jVgSScQbIVXu3QeEnDYZZ6cxl8nXbA'
            vit1_range_name = 'Sayfa1!A1:V40'
            vit1_data = list_column_values(service, vit1_spreadsheet_id, vit1_range_name)
            vit1_names = {row[1].strip().lower() for row in vit1_data[1:]}

            # VIT2 dosyasından verileri çek
            vit2_spreadsheet_id = '1NHQPJGHnyIwX1GCXE8nWDeVL5_GTEMJbRnaA2Vemmr0'
            vit2_range_name = 'Sayfa1!A1:V40'
            vit2_data = list_column_values(service, vit2_spreadsheet_id, vit2_range_name)
            vit2_names = {row[1].strip().lower() for row in vit2_data[1:]}

            # Başvurular dosyasından verileri çek
            basvurular_spreadsheet_id = '1Ls6wq8vi_fKfVIqYiTpx3RrC4KZvPlT60D63sXboNbM'
            basvurular_range_name = 'Sayfa1!A1:V40'
            basvurular_data = list_column_values(service, basvurular_spreadsheet_id, basvurular_range_name)
            headers = basvurular_data[0]

            # VIT1 ve VIT2 dosyalarında olmayan isimleri bul
            vit1_vit2_names = vit1_names.union(vit2_names)
            different_names = {row[1].strip().lower() for row in basvurular_data[1:] if row[1].strip().lower() not in vit1_vit2_names}

            # İlgili satırları filtrele ve aynı kişiyi sadece bir kez ekle
            filtered_data = [row for row in basvurular_data[1:] if row[1].strip().lower() in different_names]
            filtered_data.insert(0, headers)  # Başlıkları tekrar ekle

            self.load_data(filtered_data)
        except Exception as e:
            print(f"Error finding different registrations: {e}")

    def open_preferences(self):
        self.close()
        try:
            subprocess.Popen(["python3", os.path.join(os.path.dirname(__file__), "preference_admin_menu.py")])
        except FileNotFoundError:
            subprocess.Popen(["python", os.path.join(os.path.dirname(__file__), "preference_admin_menu.py")])

    def exit_application(self):
        self.close()
        try:
            subprocess.Popen(["python3", os.path.join(os.path.dirname(__file__), "login_window.py")])
        except FileNotFoundError:
            subprocess.Popen(["python", os.path.join(os.path.dirname(__file__), "login_window.py")])

if __name__ == "__main__":
    app = QApplication([])
    window = ApplicationWindow()
    window.show()
    app.exec()

