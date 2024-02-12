import sys, webbrowser
import subprocess
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QToolButton
from PyQt5.QtGui import QFont, QPalette, QColor, QIcon
from PyQt5 import QtCore
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QToolButton
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtWidgets import QApplication, QPushButton
   
class ChatbotUI(QWidget):
    def __init__(self):
        super().__init__()
     
        # Set window title and dimensions
        self.setWindowTitle('LICET Admission Enquiry Bot')
        self.setFixedSize(500,800)
        
        self.image_label = QLabel(self)
        self.image_label.setGeometry(150, 120, 200,200)
        self.image_label.setStyleSheet("background-image: url('logo2.png'); background-repeat: no-repeat; background-position: center;")

        # Display quote below image
        self.quote_label = QLabel(self)
        self.quote_label.setGeometry(0, 350, 500, 75)
        self.quote_label.setText("Let your light shine")
        self.quote_label.setAlignment(Qt.AlignCenter)
        font = QFont('Arial', 14)
        font.setBold(True)
        self.quote_label.setFont(font)
        self.quote_label.setStyleSheet("color: white; background-color: #293241;")

        # Create functionality buttons
        self.button1 = QPushButton('VIRTUAL CAMPUS TOUR')
        self.button1.clicked.connect(self.open_tour)
        self.button2 = QPushButton('COURSE PREFERENCE FORM')
        self.button2.clicked.connect(self.open_course_page)
        self.button3 = QPushButton('DOWNLOAD PROSPECTUS')
        self.button3.clicked.connect(self.execute_other_script)
        self.button4 = QPushButton('CUTOFF INSIGHTS')
        self.button4.clicked.connect(self.cutoff)
        self.button5 = QPushButton('COURSE SUGGESTION')
        self.button5.clicked.connect(self.sugg)
        self.button6 = QPushButton('REVIEWS')
        self.button6.clicked.connect(self.reviews)
        self.button7 = QPushButton('ADMISSION PORTAL')
        self.button7.clicked.connect(self.open_adm_page)
        self.button8 = QPushButton('PLACEMENT INSIGHTS')
        self.button8.clicked.connect(self.open_html_file)
        self.button9 = QPushButton('ABOUT LICET')
        self.button9.clicked.connect(self.open_about_page)
        self.button14 = QPushButton('SPORTS')
        self.button14.clicked.connect(self.open_sports_page)
        self.button15 = QPushButton('COURSES OFFERED')
        self.button15.clicked.connect(self.open_courses_page)
        self.button16 = QPushButton('GALLERY')
        self.button16.clicked.connect(self.open_gallery)

        self.button10 = QToolButton()
        icon = QIcon()
        icon.addPixmap(QPixmap("send_icon.png"), QIcon.Normal, QIcon.Off)
        self.button10.setIcon(icon)
        self.button10.setText('')
        self.button10.clicked.connect(self.chat)
        icon_size = QSize(60, 60)
        self.button10.setIconSize(icon_size)
        self.button10.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        
        self.button11= QToolButton()
        icon = QIcon()
        icon.addPixmap(QPixmap("voice_icon.png"), QIcon.Normal, QIcon.Off)
        self.button11.setIcon(icon)
        self.button11.setText('')
        self.button11.clicked.connect(self.voice)
        icon_size = QSize(60, 60)
        self.button11.setIconSize(icon_size)
        self.button11.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        
        self.button12= QToolButton()
        icon = QIcon()
        icon.addPixmap(QPixmap("call.png"), QIcon.Normal, QIcon.Off)
        self.button12.setIcon(icon)
        self.button12.setText('')
        self.button12.clicked.connect(self.call)
        icon_size = QSize(60,60)
        self.button12.setIconSize(icon_size)
        self.button12.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        
        self.button13 = QPushButton('ABOUT LICET')
        self.button13.clicked.connect(self.open_about_page)

        
        button_style = """
    QPushButton {
        border: 2px solid #555555;
        border-radius: 10px;
        padding: 10px;
        font-size: 16px;
    }
    
    QPushButton#special_button3:hover {
        border: 3.5px solid #3B3A39;
    }
    
    QPushButton#special_button1:hover {
        border: 3.5px solid #3B3A39;
    }


    QPushButton#special_button3 {
        background-color: #ffc315;
        color: black;
    }
        
    QPushButton#special_button1 {
        background-color: #137ec2;
        color: white;
        
    }"""
        self.button1.setStyleSheet(button_style)
        self.button2.setStyleSheet(button_style)
        self.button3.setStyleSheet(button_style)
        self.button4.setStyleSheet(button_style)
        self.button5.setStyleSheet(button_style)
        self.button6.setStyleSheet(button_style)
        self.button7.setStyleSheet(button_style)
        self.button8.setStyleSheet(button_style)
        self.button9.setStyleSheet(button_style)
        self.button10.setStyleSheet(button_style)
        self.button11.setStyleSheet(button_style)
        self.button12.setStyleSheet(button_style)
        self.button14.setStyleSheet(button_style)
        self.button15.setStyleSheet(button_style)
        self.button16.setStyleSheet(button_style)
        self.button1.setObjectName('special_button3')
        self.button2.setObjectName('special_button3')
        self.button3.setObjectName('special_button3')
        self.button4.setObjectName('special_button3')
        self.button5.setObjectName('special_button1')
        self.button6.setObjectName('special_button1')
        self.button7.setObjectName('special_button1')
        self.button8.setObjectName('special_button3')
        self.button9.setObjectName('special_button3')
        self.button14.setObjectName('special_button1')
        self.button15.setObjectName('special_button1')
        self.button16.setObjectName('special_button1')
        self.button1.setStyleSheet(button_style)
        self.button2.setStyleSheet(button_style)

        # Create layouts and add UI elements
        messages_layout = QVBoxLayout()
        input_layout = QHBoxLayout()
        button_layout = QVBoxLayout()
        row1_layout = QHBoxLayout()
        row1_layout.addWidget(self.button1)
        row1_layout.addWidget(self.button2)
        row3_layout = QHBoxLayout()
        row3_layout.addWidget(self.button3)
        row3_layout.addWidget(self.button4)
        row2_layout = QHBoxLayout()
        row2_layout.addWidget(self.button5)
        row2_layout.addWidget(self.button6)
        row2_layout.addWidget(self.button7)
        row6_layout=QHBoxLayout()
        row6_layout.addWidget(self.button8)
        row6_layout.addWidget(self.button9)
        row4_layout = QHBoxLayout()
        row4_layout.addWidget(self.button14)
        row4_layout.addWidget(self.button15)
        row4_layout.addWidget(self.button16)
        row5_layout = QHBoxLayout()

        row5_layout.addWidget(self.button10)
        row5_layout.addWidget(self.button11)
        row5_layout.addWidget(self.button12)
        button_layout.addLayout(row1_layout)
        button_layout.addLayout(row2_layout)
        button_layout.addLayout(row3_layout)
        button_layout.addLayout(row4_layout)
        button_layout.addLayout(row6_layout)
        button_layout.addLayout(row5_layout)
        
        main_layout = QVBoxLayout()
        welcome_label = QLabel('\nWELCOME TO LICET \n ADMISSION ENQUIRY CHATBOT\n')
        welcome_label.setAlignment(QtCore.Qt.AlignHCenter)
        font2 = QFont('Arial', 8)
        welcome_label.setFont(font2)  
        main_layout.addWidget(welcome_label)
        main_layout.addWidget(QLabel(''))
        main_layout.addLayout(button_layout)
        main_layout.addLayout(messages_layout)
        main_layout.addLayout(input_layout)
        self.setLayout(main_layout)

        
        
        # Set background color and font for welcome message
        palette = QPalette()
        palette.setColor(QPalette.WindowText, QColor('blue'))
        self.layout().itemAt(0).widget().setPalette(palette)

        font = QFont()
        font.setBold(True)
        font.setPointSize(16)
        self.layout().itemAt(0).widget().setFont(font)        
    
    def open_adm_page(self):
        webbrowser.open('https://admission.licet.ac.in/login/index.php?_gl=1*w18m7r*_ga*NDA4NjI2NjU2LjE2ODA5MjcxMTE.*_ga_762BPEDVM4*MTY4MjE1MDY2OC4yLjEuMTY4MjE1NjQzNS4wLjAuMA..&_ga=2.268898545.1072618897.1682143494-408626656.1680927111')
        
    def open_tour(self):
        file_path = 'index.html'
        url = QUrl.fromLocalFile(file_path)
        QDesktopServices.openUrl(url)
           
    def cutoff(self):
        subprocess.run(['python', 'cutoff.py'])
        
    def open_about_page(self):
        subprocess.run(['python', 'avatar.py'])

        
    def reviews(self):
        webbrowser.open('https://kanishkumar-k.github.io/Licet_reviews/')
        
    def execute_other_script(self):
        subprocess.run(['python', 'prospectus.py'])
        
    def open_html_file(self):
        file_path = 'https://kanishkumar-k.github.io/Placement-Details/Placement.html'
        url = QUrl.fromLocalFile(file_path)
        QDesktopServices.openUrl(url)
        
    def chat(self):
        subprocess.run(['python', 'gichat.py'])
        
    def voice(self):
        subprocess.run(['python', 'gispeech.py'])
        
    def call(self):
        subprocess.run(['python', 'call.py'])
        
    def sugg(self):
        subprocess.run(['python', 'suggestion.py'])
        
    def open_sports_page(self):
        subprocess.run(['python', 'sports.py'])
        
    def open_course_page(self):
        subprocess.run(['python', 'course.py'])    
        
    def open_courses_page(self):
        subprocess.run(['python', 'courses.py'])  
            
    def open_gallery(self):
        subprocess.run(['python', 'testgallery.py'])

def run_ui():
    # Create application and UI
    app = QApplication(sys.argv)
    ui = ChatbotUI()
    ui.show()
    
    
    # Run application
    sys.exit(app.exec_())

if __name__ == '__main__':
    run_ui()