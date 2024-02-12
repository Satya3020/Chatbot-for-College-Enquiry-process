import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QTabWidget, QPushButton
import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QToolButton
from PyQt5.QtGui import QFont, QPalette, QColor, QIcon
from PyQt5 import QtCore
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QPushButton
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtWidgets import QApplication, QPushButton


class CoursePage(QWidget):
    def __init__(self, course_name):
        super().__init__()

        
        if course_name == 'CSE':
            self.course_name = 'Computer Science Engineering'
            self.description = 'Computer Science Engineering (CSE) is a field of engineering that focuses on computer software and hardware. \n\nCSE is a rapidly growing field with diverse career paths such as software development, cybersecurity, data science, artificial intelligence/machine learning, web development, and cloud computing. With the increasing digitization of almost every industry, CSE graduates are in high demand and can find employment in a variety of fields.'
        elif course_name == 'Mechanical':
            self.course_name = 'Mechanical Engineering'
            self.description = 'Mechanical Engineering is a field of engineering that deals with the design, construction, and maintenance of machines and mechanical systems. \n\nMechanical engineers are in high demand in industries such as robotics, manufacturing, automotive, aerospace, and power generation. In addition to traditional fields, mechanical engineers are also involved in emerging areas such as renewable energy, nanotechnology, and biomechanics.'
        elif course_name == 'ECE':
            self.course_name = 'Electronics and Communication Engineering'
            self.description = 'Electronics and Communication Engineering (ECE) is a field of engineering that deals with the design and development of electronic devices, circuits, communication equipment, and systems. \n\nECE has a wide range of career options such as telecommunications, embedded systems, signal processing, control systems, and VLSI design. With the increasing demand for communication technology, ECE graduates are in high demand and can find employment in industries such as telecommunications, consumer electronics, automotive, and aerospace.'
        elif course_name == 'IT':
            self.course_name = 'Information Technology'
            self.description = 'Information Technology (IT) is a field of engineering that deals with the use of computers, software, and networks to manage, process, and store information. \n\nIT has a diverse range of career opportunities such as software development, network administration, cybersecurity, web development, and database management. With the increasing digitization of almost every industry, IT graduates are in high demand and can find employment in a variety of fields such as healthcare, finance, retail, and government.'
        elif course_name == 'EEE':
            self.course_name = 'Electrical and Electronics Engineering'
            self.description = 'Electrical and Electronics Engineering (EEE) is a field of engineering that deals with the study and application of electricity, electronics, and electromagnetism. \n\nEEE has a wide range of career opportunities such as power generation, renewable energy, automation and control, signal processing, and communication systems. With the increasing demand for sustainable energy and smart technology, EEE graduates are in high demand and can find employment in industries such as power generation, renewable energy, automation and control, and telecommunications.'
        elif course_name == 'ME CSE':
            self.course_name = 'Computer Science Engineering'
            self.description = 'Computer Science Engineering (CSE) is a field of engineering that focuses on computer software and hardware. \n\nCSE is a rapidly growing field with diverse career paths such as software development, cybersecurity, data science, artificial intelligence/machine learning, web development, and cloud computing. With the increasing digitization of almost every industry, CSE graduates are in high demand and can find employment in a variety of fields.'
        self.course_label = QLabel(self.course_name)
        self.course_label.setStyleSheet('font-size: 20px; font-weight: bold; margin-top: 50px; margin-bottom: 20px;')
        self.description_label = QLabel(self.description)
        self.description_label.setWordWrap(True)
        self.description_label.setAlignment(QtCore.Qt.AlignJustify)
        self.description_label.setStyleSheet('font-size: 18px; margin-bottom: 20px; padding: 3px')

        layout = QVBoxLayout()
        layout.addWidget(self.course_label)
        layout.addWidget(self.description_label)
        self.setLayout(layout)


class LICETWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('LICET Courses')
        self.setFixedSize(500, 800)
        self.setStyleSheet('background-color:lightcyan')
        cse_page = CoursePage('CSE')
        mechanical_page = CoursePage('Mechanical')
        it_page = CoursePage('IT')
        ece_page = CoursePage('ECE')
        eee_page = CoursePage('EEE')
        cse2_page = CoursePage('ME CSE')

        tab_widget = QTabWidget()
        tab_widget.addTab(cse_page, 'BE CSE')
        tab_widget.addTab(mechanical_page, 'BE Mechanical')
        tab_widget.addTab(it_page,'BTech IT')
        tab_widget.addTab(ece_page, 'BE ECE')
        tab_widget.addTab(eee_page, 'BE EEE')
        tab_widget.addTab(cse2_page, 'ME CSE')
        tab_widget.setStyleSheet('font-size: 16px;')

        self.close_button = QPushButton('Close')
        self.close_button.setStyleSheet("background-color: red; color: white; font-size: 18px;")
        self.close_button.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(tab_widget)
        layout.addWidget(self.close_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LICETWindow()
    window.show()
    sys.exit(app.exec_())
