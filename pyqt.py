# PyQt5 introduction

import sys
from PyQt5.QtWidgets import QApplication ,QMainWindow
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("APP") # giving the name
        self.setGeometry(700,300,500,500) # setting geometry
        self.setWindowIcon(QIcon("file path")) # puttinf icons in the widget
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
if __name__=="__main__":
    main()
    
    
# Labels

import sys
from PyQt5.QtWidgets import QApplication ,QMainWindow,QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500) # setting geometry
        label=QLabel("Hello",self)
        label.setFont(QFont("Arial",30)) # setting font of the label
        label.setGeometry(0,0,500,100) # setting the geometry of the label
        label.setStyleSheet("color:black;"
                            "background-color:green") # QSS
        label.setAlignment(Qt.AlignTop) # Vertically top
        label.setAlignment(Qt.AlignBottom) # 
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
if __name__=="__main__":
    main()
    
# images

import sys
from PyQt5.QtWidgets import QApplication ,QMainWindow,QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500) # setting geometry
        label = QLabel(self)
        label.setGeometry(0,0,250,250)
        pixtmap =QPixmap("image")
        label.setPixmap(pixtmap)
        label.setScaledContents(True)
        label.setGeometry(0,0,label.width(),label.height())
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
if __name__=="__main__":
    main()
    
# Layouts

import sys
from PyQt5.QtWidgets import (QApplication ,QMainWindow,
                             QWidget,QLabel,QVBoxLayout,QHBoxLayout,
                             QGridLayout)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500) # setting geometry
        self.initUI()
    def initUI(self):
        central_widget =QWidget()
        self.setCentralWidget(central_widget)
        label1 = QLabel("1#",self)
        label2 = QLabel("2#",self)
        label3 = QLabel("3#",self)
        label4 = QLabel("4#",self)
        label5 = QLabel("5#",self)
    
        hbox = QHBoxLayout() #layouts now
        
        label1.setStyleSheet("background-color: ;")
        label2.setStyleSheet("background-color: yellow;")
        label3.setStyleSheet("background-color: green;")
        label4.setStyleSheet("background-color: blue;")
        label5.setStyleSheet("background-color: purple;")
        hbox.addWidget(label1)
        hbox.addWidget(label2)
        hbox.addWidget(label3)
        hbox.addWidget(label4)
        hbox.addWidget(label5)
        
        grid = QGridLayout() #layouts now
        grid.addWidget(label1,0,0)
        grid.addWidget(label2,0,1)
        grid.addWidget(label3,1,0)
        grid.addWidget(label4,1,1)
        grid.addWidget(label5,1,2)
        central_widget.setLayout(grid)
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
if __name__=="__main__":
    main()

# Buttons

import sys
from PyQt5.QtWidgets import QApplication ,QMainWindow,QPushButton
                             
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500) # setting geometry
        self.button = QPushButton("Click me!", self)
        self.initUI()
    def initUI(self):
        self.button.setGeometry(150,200,200,100)
        self.button.setStyleSheet("font-size:30px")
        self.button.clicked.connect(self.on_click)
    def on_click(self):
            print("Button clicked")
            self.button.setText("clicked")
            self.button.setDisabled(True)  
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
if __name__=="__main__":
    main()
    
# Line edits

import sys
from PyQt5.QtWidgets import QApplication ,QMainWindow,QLineEdit,QPushButton               
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500) # setting geometry
        self.line_edit=QLineEdit(self)
        self.button=QPushButton("Submit",self)
        self.initUI()
        
    def initUI(self):
        self.line_edit.setGeometry(10,10,200,40)
        self.button.setGeometry(210,10,100,10)
        self.line_edit.setStyleSheet("font-size: 25px"
                                     "font-family: Arial")
        self.button.setStyleSheet("font-size: 25px"
                                     "font-family: Arial")
        self.button.clicked.connect(self.submit)
        self.line_edit.setPlaceholderText("Enter your name")
    
    def submit(self):
        text = self.line_edit()
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
if __name__=="__main__":
    main()