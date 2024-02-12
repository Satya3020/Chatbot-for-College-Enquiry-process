import sys
import webbrowser
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QToolButton
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
from PyQt5.QtGui import QFont, QPalette, QColor, QIcon
from PyQt5.QtGui import QLinearGradient
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QGridLayout
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
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QUrl, QTimer
from PyQt5.QtWebEngineWidgets import QWebEngineView


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create a QWebEngineView widget
        self.web_view = QWebEngineView(self)


        # Add a label at the bottom of the window
        self.label = QLabel(self)
        self.label.setGeometry(0, self.height() -480, self.width(), 63)
        self.label.setFont(QFont("Arial", 10))
        self.label.setStyleSheet("background-color: #f47f20; color: white; font-weight:bold;")
        self.label.setText("\t\t\tLICET - About Us")

        # Set the Voki animation URL
        url = QUrl("https://tinyurl.com/2gf9h8ju")
        self.web_view.setUrl(url)

        # Hide the Voki logo and start playing the animation using JavaScript
        self.web_view.page().runJavaScript("document.getElementsByClassName('voki-logo')[0].style.display='none'; document.getElementsByClassName('vplayer')[0].click();")

        # Add the QWebEngineView widget to a layout
        layout = QVBoxLayout()
        layout.addWidget(self.web_view)
        self.setLayout(layout)

        # Reload the webpage every 5 minutes
        timer = QTimer(self)
        timer.timeout.connect(self.web_view.reload)
        timer.start(5 * 60 * 1000)  # 5 minutes in milliseconds

        # Add a label at the bottom of the window
        self.label = QLabel(self)
        self.label.setGeometry(0, self.height() +100, self.width(), 200)
        self.label.setFont(QFont("Arial", 14))
        self.label.setStyleSheet("background-color: #f47f20; color: white;")
        self.label.setWordWrap(True)
        self.label.setText('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For more info visit : <a href="https://licet.ac.in/about/"> https://licet.ac.in/about/</a>')
        self.label.setOpenExternalLinks(True)
              
        self.close_button = QPushButton("EXIT", self)
        self.close_button.clicked.connect(self.close)
        self.close_button.setStyleSheet("""
            QPushButton {
                color: white;
                padding: 8px;
                border: none;
                font-size: 14px;
            }
            
            QPushButton:hover {
                background-color: #d32f2f;
            }
        """)
        
if __name__ == '__main__':
    # Create a PyQt application
    app = QApplication(sys.argv)

    # Create the main window and set a fixed size
    main_window = MainWindow()
    main_window.setFixedSize(500, 800)

    # Show the main window
    main_window.show()

    # Run the event loop
    sys.exit(app.exec_())
