from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QTableWidget, QLabel, QTableWidgetItem, QComboBox
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
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
        self.mainLayout.addWidget(self.comboBox)

        # QTableWidget
        self.tableWidget = QTableWidget()
        self.tableWidget.setFont(QFont("Arial", 11))
        self.tableWidget.setSortingEnabled(True)  # Sıralama etkinleştirildi
        self.mainLayout.addWidget(self.tableWidget)

        # Örnek veri
        self.load_data([
            ["Alice", "Engineering", "A"],
            ["Bob", "Science", "B"],
            ["Charlie", "Arts", "C"]
        ])

    def load_data(self, data):
        rows = len(data)
        cols = len(data[0]) if rows > 0 else 0

        self.tableWidget.setRowCount(rows)
        self.tableWidget.setColumnCount(cols)

        for row in range(rows):
            for col in range(cols):
                item = QTableWidgetItem(data[row][col])
                self.tableWidget.setItem(row, col, item)

        self.tableWidget.setHorizontalHeaderLabels(["Name", "Department", "Grade"])
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
