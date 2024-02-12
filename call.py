from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class ContactGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Contact Details - LICET")
        self.setFixedSize(500, 800)

        # Create a heading label
        self.heading_label = QLabel(self)
        self.heading_label.setText("WELCOME TO LICET\n\n Contact Us")
        self.heading_label.setStyleSheet("font: 16pt Helvetica; background-color: #0072C6; color: white")
        self.heading_label.setAlignment(Qt.AlignCenter)
        self.heading_label.setGeometry(50, 50, 400, 100)

        # Create a label for email
        self.email_label = QLabel(self)
        self.email_label.setText("Email:")
        self.email_label.setStyleSheet("font: 12pt Helvetica Bold; background-color: #C2B280")
        self.email_label.setGeometry(50, 200, 400, 30)

        # Create a label for email address
        self.email_address_label = QLabel(self)
        self.email_address_label.setText("licet@licet.ac.in")
        self.email_address_label.setStyleSheet("font: 12pt Helvetica; background-color: #E6E6E6")
        self.email_address_label.setGeometry(50, 240, 400, 30)

        # Create a label for phone number
        self.phone_label = QLabel(self)
        self.phone_label.setText("Phone:")
        self.phone_label.setStyleSheet("font: 12pt Helvetica Bold; background-color: #C2B280")
        self.phone_label.setGeometry(50, 280, 400, 30)

        # Create a label for phone number
        self.phone_number_label = QLabel(self)
        self.phone_number_label.setText("+91 – 44 – 28178490")
        self.phone_number_label.setStyleSheet("font: 12pt Helvetica; background-color: #E6E6E6")
        self.phone_number_label.setGeometry(50, 320, 400, 30)

        # Create a label for admission queries
        self.admission_label = QLabel(self)
        self.admission_label.setText("Admission Queries:")
        self.admission_label.setStyleSheet("font: 12pt Helvetica Bold; background-color: #C2B280")
        self.admission_label.setGeometry(50, 360, 400, 30)

        # Create a label for admission query phone number
        self.admission_phone_label = QLabel(self)
        self.admission_phone_label.setText("9003813339")
        self.admission_phone_label.setStyleSheet("font: 12pt Helvetica; background-color: #E6E6E6")
        self.admission_phone_label.setGeometry(50, 400, 400, 30)

        # Create a label for address
        self.address_label = QLabel(self)
        self.address_label.setText("Address:")
        self.address_label.setStyleSheet("font: 12pt Helvetica Bold; background-color: #C2B280")
        self.address_label.setGeometry(50, 440, 400, 30)

        # Create a label for address details
        self.address_details_label = QLabel(self)
        self.address_details_label.setText("LICET Loyola Campus\n Nungambakkam, Chennai – 600034.")
        self.address_details_label.setStyleSheet("font: 12pt Helvetica; background-color: #E6E6E6")
        self.address_details_label.setGeometry(50, 480, 400, 60)

        # Create a close button
        self.close_button = QPushButton(self)
        self.close_button.setText("Close")
        self.close_button.setGeometry(200, 600, 100, 30)
        self.close_button.clicked.connect(self.close)

if __name__ == "__main__":
    app = QApplication([])
    window = ContactGUI()
    window.show()
    app.exec_()
