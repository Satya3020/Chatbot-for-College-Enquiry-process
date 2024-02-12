import sys
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton


class ImageSwitcher(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("LICET SPORTS")
        self.setFixedSize(500,800)
        self.setStyleSheet("background-color: #D3D3D3;")

        # Create description label
        self.title = QLabel("LICET SPORTS")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet("font-size:28px; color: blue;")

        self.description_label = QLabel("\n“The five S's of sports training are stamina, speed, strength, skill, and spirit; but the greatest of these is spirit” says Ken Doherty. \nIn accordance with this saying LICET trains the students to fight and compete with a spirit of sportsmanship. \nStudents in LICET are given ample opportunity to explore the star within themselves and develop it further to fruition.\nMany of the students have tried their hand at Sports but some were highly successful achieving accolades and honors shining in the firmament of LICET.\n\n")
        self.description_label.setWordWrap(True)
        self.description_label.setStyleSheet("font-size:22px; margin-bottom: 10px;")

        # Create image labels
        self.image_labels = []
        for i in range(4):
            label = QLabel()
            label.setAlignment(Qt.AlignCenter)
            self.image_labels.append(label)

        self.set_images()

        # Create layout
        layout = QVBoxLayout()
        layout.addWidget(self.title)
        layout.addWidget(self.description_label)
        for label in self.image_labels:
            layout.addWidget(label)

        # Create close button
        close_button = QPushButton("Close")
        close_button.setStyleSheet("background-color: red; color: white; font-size: 18px;")
        close_button.clicked.connect(self.close)

        layout.addWidget(close_button)
        self.setLayout(layout)

        # Set up image switching timer
        self.image_index = 0
        self.image_timer = QTimer()
        self.image_timer.timeout.connect(self.switch_image)
        self.image_timer.start(2000)

    def set_images(self):
        # Set up initial images
        for i, label in enumerate(self.image_labels):
            pixmap = QPixmap(f"sports/{i+1}.jpg")
            pixmap = pixmap.scaledToHeight(200, Qt.SmoothTransformation)
            label.setPixmap(pixmap)
            if i != 0:
                label.hide()

    def switch_image(self):
        # Switch to next image label
        self.image_index = (self.image_index + 1) % 4
        for i, label in enumerate(self.image_labels):
            if i == self.image_index:
                label.show()
            else:
                label.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageSwitcher()
    window.show()
    window.set_images()
    QTimer.singleShot(1000, window.image_timer.start)
    sys.exit(app.exec_())
