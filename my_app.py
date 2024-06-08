from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QVBoxLayout,
    QGroupBox, QRadioButton, QPushButton, QLabel,
    QListWidget, QLineEdit
)
from instr import *
from second_win import *

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.hello_text = QLabel(txt_hello)
        self.hello_text.setStyleSheet("font-size: 24px; font-weight: bold; color: #444;")

        self.instruction = QLabel(txt_instruction)
        self.instruction.setStyleSheet("font-size: 18px; color: #666;")

        self.button = QPushButton(txt_next)
        '''
        self.button.setStyleSheet("""background-color: #3498db; 
                                    color: white; 
                                    font-size: 30px;
                                    border-radius:20px; 
                                    padding: 15px 50px;""")
        '''
        self.button.setStyleSheet("""
                    QPushButton {   background-color: #3498db; 
                                    color: white; 
                                    font-size: 30px;
                                    border-radius:20px; 
                                    padding: 15px 50px;
                                }
                    QPushButton:hover { color: blue;
                                        background-color: gray;}
                                        
                    QPushButton:pressed {  
                                    color: black;
                                    background-color : red;  
                                            }
                    """)                             
         
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.instruction, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.button, alignment=Qt.AlignCenter)
        self.setLayout(self.layout)

    def next_click(self):
        self.tw = TestWin()
        self.hide()

    def connects(self):
        self.button.clicked.connect(self.next_click)


app = QApplication([])
mw = MainWin()
app.exec_()
