import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from cutoff_calculator import cutoff_calculator

class CollegeAdmissionChatbot(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Create the UI elements
        self.setWindowTitle('LICET Admission Chatbot')
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setStyleSheet('background-color: #f5f5f5;')
        self.setFixedSize(500, 800)
        self.heading_label = QtWidgets.QLabel('LICET Admission Chatbot - CUTOFF Insights')
        self.heading_label.setStyleSheet('font-size: 24px; font-family: Arial; font-weight: bold; color: #333333;')
        self.heading_label.setWordWrap(True)
        self.marks_label = QtWidgets.QLabel('Please enter your marks in Maths, Physics, and Chemistry (Seperated by comma\'s)')
        self.marks_label.setStyleSheet('font-size: 20px; font-family: Arial; color: #333333;')
        self.marks_label.setWordWrap(True)
        self.cast_label = QtWidgets.QLabel('Please select your category:')
        self.cast_label.setStyleSheet('font-size: 20px; font-family: Arial; color: #333333;')
        self.cast_label.setWordWrap(True)

        self.marks_input = QtWidgets.QLineEdit()
        self.marks_input.setStyleSheet('font-size: 16px; font-family: Arial; color: #333333; margin-top: 0px;')

        self.cast_combo = QtWidgets.QComboBox()
        self.cast_combo.setStyleSheet('font-size: 16px; font-family: Arial; color: #333333; margin-top: 0px;')
        self.cast_combo.addItem("OC")
        self.cast_combo.addItem("BCM")
        self.cast_combo.addItem("BC")
        self.cast_combo.addItem("MBC")
        self.cast_combo.addItem("SC")
        self.cast_combo.addItem("SCA")
        self.cast_combo.addItem("ST")

        self.cutoff_label = QtWidgets.QLabel('Your cutoff mark is: ')
        self.cutoff_label.setWordWrap(True)
        self.cutoff_label.setStyleSheet('font-size: 16px; font-family: Arial; color: #333333; margin-top: 0px;')
        self.cutoff_output = QtWidgets.QLabel()
        self.cutoff_output.setStyleSheet('font-size: 46px; font-family: Arial; color: #008080;')
        self.result_label = QtWidgets.QLabel()
        self.result_label.setWordWrap(True)
        self.result_label.setStyleSheet('font-size: 16px; font-family: Arial; color: #333333;')      
        self.submit_button = QtWidgets.QPushButton('GET CUTOFF INSIGHTS')
        self.submit_button.setStyleSheet('font-size: 16px; font-family: Arial; color: #ffffff; background-color: #008080; padding:20px')
        self.submit_button.clicked.connect(self.calculate_cutoff)
        self.result_label.setWordWrap(True)

        # Create a layout and add the UI elements to it
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.heading_label)
        layout.setContentsMargins(50, 50, 50, 50)
        layout.addWidget(self.marks_label)
        layout.addWidget(self.marks_input)
        layout.addWidget(self.cast_label)
        layout.addWidget(self.cast_combo)
        layout.addWidget(self.cutoff_label)
        layout.addWidget(self.cutoff_output)
        layout.addWidget(self.result_label)
        layout.addWidget(self.submit_button)

        # Set the layout for the widget
        self.setLayout(layout)

    def calculate_cutoff(self):
        # Get the user input
        user_input = self.marks_input.text()

        # Get the selected caste
        selected_caste = self.cast_combo.currentText()

        # Calculate the cutoff mark
        try:
            maths_marks, physics_marks, chemistry_marks = map(int, user_input.split(","))
        except ValueError:
            self.result_label.setText('Invalid input! Please enter your marks in the format "maths,physics,chemistry".')
            return
        cutoff_marks = cutoff_calculator(maths_marks, physics_marks, chemistry_marks)

        # Display the result
        self.cutoff_output.setText(str(cutoff_marks))
        if selected_caste == 'OC':
            if cutoff_marks >= 185:
                self.result_label.setText('Congratulations! You have a great chance of getting admission through AU counselling for CSE, IT, ECE, EE, Mech departments.')
            elif cutoff_marks >= 180:
                self.result_label.setText('Congratulations! You have a great chance of getting admission through AU counselling for IT, ECE, EEE, Mech departments.')
            elif cutoff_marks >= 178:
                self.result_label.setText('Congratulations! You have a great chance of getting admission through AU counselling for ECE, EEE, Mech departments.')
            elif cutoff_marks >= 171:
                self.result_label.setText('Congratulations! You have a great chance of getting admission through AU counselling for EEE, Mech departments.')
            elif cutoff_marks >= 161:
                self.result_label.setText('Congratulations! You have a great chance of getting admission through AU counselling for Mech department.')
            else:
                self.result_label.setText('Sorry, your marks do not meet the cutoff criteria for any department. .')
            if cutoff_marks >= 140 and cutoff_marks < 190:
                self.result_label.setText('\nHowever, you may be eligible for admission for other departments through management quota.')

        elif selected_caste == 'BC':
            if cutoff_marks >= 178:
                self.result_label.setText('Congratulations! You have a great chance of getting admission through AU counselling for CSE, IT, ECE, EE, Mech departments.')
            elif cutoff_marks >= 175:
                self.result_label.setText('Congratulations! You have a great chance of getting admission through AU counselling for ECE, IT, EEE, Mech departments.')
            elif cutoff_marks >= 169:
                self.result_label.setText('Congratulations! You have a great chance of getting admission through AU counselling for IT, EEE, Mech departments.')
            elif cutoff_marks >= 166:
                self.result_label.setText('Congratulations! You have a great chance of getting admission through AU counselling for EEE, Mech departments.')
            elif cutoff_marks >= 150:
                self.result_label.setText('Congratulations! You have a great chance of getting admission through AU counselling for Mech department.')
            elif cutoff_marks >= 140:
                self.result_label.setText('Congratulations! You have a great chance of getting admission through AU counselling for Civil, Chemical department but unfortunately we dont provide those departments.')
            else:
                self.result_label.setText('Sorry, your marks do not meet the cutoff criteria for any department. .')
            if cutoff_marks >= 130 and cutoff_marks < 180:
                self.result_label.setText('\nHowever, you may be eligible for admission for other departments through management quota.')

        elif selected_caste == 'BCM':
            if cutoff_marks >= 174:
                self.result_label.setText('Congratulations! You have a great chance of getting admission through AU counselling for CSE, IT, ECE, EE, Mech departments.')
            elif cutoff_marks >= 170:
                self.result_label.setText('Congratulations! You have a great chance of getting admission through AU counselling for ECE, IT, EEE, Mech departments.')
            elif cutoff_marks >= 165:
                self.result_label.setText('Congratulations! You have a great chance of getting admission through AU counselling for IT, EEE, Mech departments.')
            elif cutoff_marks >= 160:
                self.result_label.setText('Congratulations! You have a great chance of getting admission through AU counselling for EEE, Mech departments.')
            elif cutoff_marks >= 150:
                self.result_label.setText('Congratulations! You have a great chance of getting admission through AU counselling for Mech department.')
            elif cutoff_marks >= 140:
                self.result_label.setText('Congratulations! You have a great chance of getting admission through AU counselling for Civil, Chemical department but unfortunately we dont provide those departments.')
            else:
                self.result_label.setText('Sorry, your marks do not meet the cutoff criteria for any department. .')
            if cutoff_marks >= 130 and cutoff_marks < 180:
                self.result_label.setText('\nHowever, you may be eligible for admission for other departments through management quota.')

        elif selected_caste == 'MBC':
            if cutoff_marks >= 175:
                self.result_label.setText('Congratulations! You have a great chance of getting admission through AU counselling for CSE, IT, ECE, EE, Mech departments.')
            elif cutoff_marks >= 170:
                self.result_label.setText('Congratulations! You have a great chance of getting admission through AU counselling for ECE, IT, EEE, Mech departments.')
            elif cutoff_marks >= 167:
                self.result_label.setText('Congratulations! You have a great chance of getting admission through AU counselling for IT, EEE, Mech departments.')
            elif cutoff_marks >= 163:
                self.result_label.setText('Congratulations! You have a great chance of getting admission through AU counselling for EEE, Mech departments.')
            elif cutoff_marks >= 154:
                self.result_label.setText('Congratulations! You have a great chance of getting admission through AU counselling for Mech department.')
            elif cutoff_marks >= 140:
                self.result_label.setText('Congratulations! You have a great chance of getting admission through AU counselling for Civil, Chemical department but unfortunately we dont provide those departments.')
            else:
                self.result_label.setText('Sorry, your marks do not meet the cutoff criteria for any department. .')
            if cutoff_marks >= 130 and cutoff_marks < 180:
                self.result_label.setText('\nHowever, you may be eligible for admission for other departments through management quota.')

        elif selected_caste == 'SC':
            if cutoff_marks >= 148:
                self.result_label.setText('Congratulations! You have a great chance of getting admission through AU counselling for CSE, IT, ECE, EE, Mech departments.')
            elif cutoff_marks >= 146:
                self.result_label.setText('Congratulations! You have a great chance of getting admission through AU counselling for ECE, IT, EEE, Mech departments.')
            elif cutoff_marks >= 144:
                self.result_label.setText('Congratulations! You have a great chance of getting admission through AU counselling for IT, EEE, Mech departments.')
            elif cutoff_marks >= 127:
                self.result_label.setText('Congratulations! You have a great chance of getting admission through AU counselling for EEE, Mech departments.')
            elif cutoff_marks >= 116:
                self.result_label.setText('Congratulations! You have a great chance of getting admission through AU counselling for Mech department.')
            elif cutoff_marks >= 140:
                self.result_label.setText('Congratulations! You have a great chance of getting admission through AU counselling for Civil, Chemical department but unfortunately we dont provide those departments.')
            else:
                self.result_label.setText('Sorry, your marks do not meet the cutoff criteria for any department. .')
            if cutoff_marks >= 130 and cutoff_marks < 180:
                self.result_label.setText('\nHowever, you may be eligible for admission for other departments through management quota.')

        elif selected_caste == 'SCA':
            if cutoff_marks >= 174:
                self.result_label.setText('Congratulations! You have a great chance of getting admission through AU counselling for CSE, IT, ECE, EE, Mech departments.')
            elif cutoff_marks >= 167:
                self.result_label.setText('Congratulations! You have a great chance of getting admission through AU counselling for IT, ECE, EEE, Mech departments.')
            elif cutoff_marks >= 0:
                self.result_label.setText('Congratulations! You have a great chance of getting admission through AU counselling for ECE, EEE, Mech departments.')
            elif cutoff_marks >= 0:
                self.result_label.setText('Congratulations! You have a great chance of getting admission through AU counselling for EEE, Mech departments.')
            elif cutoff_marks >= 150:
                self.result_label.setText('Congratulations! You have a great chance of getting admission through AU counselling for Mech department.')
            elif cutoff_marks >= 140:
                self.result_label.setText('Congratulations! You have a great chance of getting admission through AU counselling for Civil, Chemical department but unfortunately we dont provide those departments.')
            else:
                self.result_label.setText('Sorry, your marks do not meet the cutoff criteria for any department. .')
            if cutoff_marks >= 130 and cutoff_marks < 180:
                self.result_label.setText('\nHowever, you may be eligible for admission for other departments through management quota.')

        elif selected_caste == 'ST':
            if cutoff_marks >= 0:
                self.result_label.setText('Congratulations! You have a great chance of getting admission through AU counselling for CSE, IT, ECE, EE, Mech departments.')
            else:
                self.result_label.setText('\nHowever, you may be eligible for admission for other departments through management quota.')


        else:
            result_text = 'Invalid caste selection. Please select from the available options: OC, BCM, BC, MBC, SC, SCA, ST'

    def run(self):
        self.show()

app = QtWidgets.QApplication([])
widget = CollegeAdmissionChatbot()
widget.run()
app.exec_()        