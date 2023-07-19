from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # checking the types of input values
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout, QGridLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)


from instr import *
from final_win import *

class TestWin(QWidget):
   def __init__(self):
       ''' the window in which the survey is being conducted '''
       super().__init__()
       # sets what the window will look like (label, size, location)
       self.set_appear()
       # creating and configuring graphic elements:
       self.initUI()
       #establishes connections between elements
       self.connects()
       # start:
       self.show()
