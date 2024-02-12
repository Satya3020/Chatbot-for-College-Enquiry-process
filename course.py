import csv
import sys, re
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QComboBox, QMessageBox
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout,QGroupBox
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QToolButton
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QGridLayout
from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QVBoxLayout
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QToolButton
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QRect

class CourseSuggestionForm(QWidget):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("Student details Form")
        self.setFixedSize(500, 800)
        
        layout = QVBoxLayout()
        group_box = QGroupBox()
        group_box.setStyleSheet("QGroupBox { border-radius: 10px; border: 2px solid gray;}")
        
        # Create labels
        self.label = QLabel(self)
        self.label2 = QLabel(self)
        self.label2.setText("\nHey! Glad to see you! \nAre you interested in Holistic Formation, Professionalism and willing to form a just society? \n\nCongrats, LICET is the right choice for you. \nFill out the course preference form. \nWe will reach you soon. Best wishes to your future..")
        self.label2.setWordWrap(True)
        group_box_layout = QVBoxLayout()
        group_box_layout.addWidget(self.label2)
        group_box.setLayout(group_box_layout)
        self.label.setStyleSheet("font-size: 30px; padding:10px; padding-bottom: 10px;")
        self.label2.setStyleSheet("font-size: 15px; padding:10px; padding-bottom: 10px; border: 2px solid black;")
        self.label2.move(50, 500)
        
        layout.addWidget(group_box)
        self.setLayout(layout)

        self.name_label = QLabel(self)
        self.name_label.setText("Name:")
        self.name_label.move(40, 80)

        self.email_label = QLabel(self)
        self.email_label.setText("Email:")
        self.email_label.move(40, 130)

        self.phone_label = QLabel(self)
        self.phone_label.setText("Phone:\nWith countryCode")
        self.phone_label.move(38, 190)

        self.course1_label = QLabel(self)
        self.course1_label.setText("Course\nPreference 1:")
        self.course1_label.move(40, 230)

        self.course2_label = QLabel(self)
        self.course2_label.setText("Course\nPreference 2:")
        self.course2_label.move(40, 280)

        # Create line edits
        self.name_edit = QLineEdit(self)
        self.name_edit.setGeometry(200, 80, 200, 25)

        self.email_edit = QLineEdit(self)
        self.email_edit.setGeometry(200, 130, 200, 25)

        self.phone_edit = QLineEdit(self)
        self.phone_edit.setGeometry(200, 180, 200, 25)

        # Create combo boxes
        self.course1_combo = QComboBox(self)
        self.course1_combo.setGeometry(200, 230, 200, 25)
        self.course1_combo.addItem("Select Course Preference 1")
        self.course1_combo.addItem("CSE")
        self.course1_combo.addItem("IT")
        self.course1_combo.addItem("ECE")
        self.course1_combo.addItem("EEE")
        self.course1_combo.addItem("MECH")

        self.course2_combo = QComboBox(self)
        self.course2_combo.setGeometry(200, 280, 200, 25)
        self.course2_combo.addItem("Select Course Preference 2")
        self.course2_combo.addItem("CSE")
        self.course2_combo.addItem("IT")
        self.course2_combo.addItem("ECE")
        self.course2_combo.addItem("EEE")
        self.course2_combo.addItem("MECH")

        # Create submit button
        self.submit_button = QPushButton(self)
        self.submit_button.setText("Submit")
        self.submit_button.setStyleSheet("background-color: green; color: white; font-size: 18px;")
        self.submit_button.setGeometry(150, 550, 100, 30)
        self.submit_button.clicked.connect(self.submit_form)

        
        close_button = QPushButton(self)
        close_button.setText("Close")
        close_button.setStyleSheet("background-color: red; color: white; font-size: 18px;")
        close_button.setGeometry(270, 550, 100, 30)
        close_button.clicked.connect(self.close)

    def validate_email(self, email):
        # Very basic email validation
        if "@" in email and "." in email:
            return True
        else:
            return False

    def validate_phone(self, phone):
        # Very basic phone validation
        if phone.isdigit() and len(phone) == 10:
            return True
        else:
            return False

    def submit_form(self):
        name = self.name_edit.text()
        email = self.email_edit.text()
        phone = self.phone_edit.text()
        course1 = self.course1_combo.currentText()
        course2 = self.course2_combo.currentText()

        # Basic validation for phone and email
        if not email:
            QMessageBox.critical(self, "Error", "Please enter your email.")
            return
        if not re.match(r'^\+\d{1,3}\d{10}$', phone):
            QMessageBox.critical(self, "Error", "Please enter a valid mobile number.")
            return

        # Check if course preferences are different
        if course1 == course2:
            QMessageBox.critical(self, "Error", "Please select different courses for course preference 1 and 2.")
            return

        # Write data to CSV file
        with open("course_suggestions.csv", "a", newline="") as file:
            writer = csv.writer(file)
            if file.tell() == 0:  # write header if file is empty
                writer.writerow(["Name", "Email", "Course Preference 1", "Course Preference 2", "Mobile No."])
            writer.writerow([name, email, course1, course2, phone])
            
            
        QMessageBox.information(self, "Success", "Thanks for filling the details. We will reach you soon with application process and guidelines..")
        subprocess.call(['python', 'sms.py'])


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    course_suggestion = CourseSuggestionForm()
    course_suggestion.show()
    app.exec_()
