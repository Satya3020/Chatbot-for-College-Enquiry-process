import sys
import urllib.request
import os
import webbrowser
import os.path
from pathlib import Path
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QLinearGradient, QColor, QPalette, QBrush

from PyQt5.QtGui import QLinearGradient, QColor, QBrush
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap


class BrochureViewer(QMainWindow):
    def __init__(self, pdf_url, college_name, description):
        super().__init__()
        self.pdf_url = pdf_url
        self.college_name = college_name
        self.description = description
        
        self.setWindowTitle(college_name + " Brochure Viewer")
        self.setFixedSize(500, 800)
        self.setStyleSheet("background-color: #F9F9F9;")

        # Add image above the buttons
        image_label = QLabel(self)
        pixmap = QPixmap("logo.jpg")
        pixmap = pixmap.scaledToWidth(200)
        image_label.setPixmap(pixmap)
        image_label.setGeometry(150, 20, 250, 250)
        
        self.college_label = QLabel(self)
        self.college_label.setText(college_name)
        self.college_label.setGeometry(20, 290, 460, 40)
        self.college_label.setStyleSheet("font: bold 24px Arial; color: #007FFF;")

        self.desc_label = QLabel(self)
        self.desc_label.setText(description)
        self.desc_label.setWordWrap(True)
        self.desc_label.setGeometry(20, 340, 460, 100)
        self.desc_label.setStyleSheet("font: bold 16px Arial;")

        
        self.view_button = QPushButton(self)
        self.view_button.setText("VIEW PROSPECTUS")
        self.view_button.setGeometry(20, 470, 460, 60)
        self.view_button.clicked.connect(self.view_brochure)
        self.view_button.setStyleSheet("font: bold 17px Arial; background-color: #007FFF; color: #FFFFFF;")

        
        self.download_button = QPushButton(self)
        self.download_button.setText("DOWNLOAD PROSPECTUS")
        self.download_button.setGeometry(20, 550, 460, 60)
        self.download_button.clicked.connect(self.download_brochure)
        self.download_button.setStyleSheet("font: bold 17px Arial; background-color: #ffc315; color: #000000;")

        
        self.close_button = QPushButton(self)
        self.close_button.setText("EXIT")
        self.close_button.setGeometry(20, 630, 460, 60)
        self.close_button.clicked.connect(self.close)
        self.close_button.setStyleSheet("font: bold 17px Arial; background-color: red; color: #FFFFFF;")
        
    
    def view_brochure(self):
        webbrowser.open_new(self.pdf_url)
    
    def download_brochure(self):
        pdf_filename = self.college_name.replace(" ", "_").lower() + "_brochure.pdf"
        
        home = str(Path.home())
        downloads_path = os.path.join(home, "Downloads")
        pdf_file_path = os.path.join(downloads_path, pdf_filename)

        if os.path.exists(pdf_file_path):
            print("File already exists in Downloads folder.")
        else:
            urllib.request.urlretrieve(self.pdf_url, pdf_file_path)
            print("Brochure downloaded successfully in Downloads folder.")
        
        os.startfile(downloads_path)


if __name__ == '__main__':
    # Set the URL of the PDF file to open
    pdf_url = "https://licet.ac.in/wp-content/uploads/2021/05/Prospectus-2023-1.pdf"

    # Set the name of the college and a brief description of the brochure
    college_name = "\t LICET PROSPECTUS"

    description = "Learn more about the application process, campus life, and more at LICET by downloading Prospectus '23!"

    app = QApplication(sys.argv)
    brochure_viewer = BrochureViewer(pdf_url, college_name, description)
    brochure_viewer.show()
    sys.exit(app.exec_())