import sys 
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QPushButton,QWidget,QHBoxLayout,QVBoxLayout,QGridLayout,QCheckBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My fist window")
        self.setGeometry(400,100,700,500) 
        label = QLabel("Marital status" , self)
        label.setGeometry(150,20,300,30)
        label.setStyleSheet("background-color:blue;"
                            "font-family : Arial;")
        label.setStyleSheet("font-size:40px")  
        self.initUI()
        
    def initUI(self):
        
     checkbox =QCheckBox("Open relationship!",self)
     checkbox.setGeometry(150,50,300,100)
     checkbox =QCheckBox("Complicated!",self)
     checkbox.setGeometry(150,50,300,140)
     checkbox =QCheckBox("Marriend!",self)
     checkbox.setGeometry(150,50,300,180)
     checkbox =QCheckBox("Single!",self)
     checkbox.setGeometry(150,50,300,220)
     
     checkbox.setStyleSheet("font-size:20px;"
                            "font-family:Arial;")
     checkbox.setStyleSheet("font-size:20px;"
                            "font-family:Arial;")
     checkbox.setStyleSheet("font-size:20px;"
                            "font-family:Arial;")
     checkbox.setStyleSheet("font-size:20px;"
                            "font-family:Arial;")
     
    
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
        

