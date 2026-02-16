import sys 
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QPushButton,QWidget,QHBoxLayout,QVBoxLayout,QGridLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My fist window")
        self.setGeometry(400,100,700,500)
        
        self.initUI()
        
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        label1 = QLabel("1",self)
        label2 = QLabel("2",self)
        label3 = QLabel("3",self)
        label4 = QLabel("4",self)
        label5 = QLabel("5",self)
        label6 = QLabel("6",self)
        label7 = QLabel("7",self)
        
        label1.setGeometry(100,150,500,20)
        label2.setGeometry(100,170,500,20)
        label3.setGeometry(100,190,500,20)
        label4.setGeometry(100,210,500,20)
        label5.setGeometry(100,230,500,20)
        label6.setGeometry(100,250,500,20)
        label7.setGeometry(100,270,500,20)
        
        label1.setStyleSheet("background-color:red")
        label2.setStyleSheet("background-color:blue")
        label3.setStyleSheet("background-color:black")
        label4.setStyleSheet("background-color:green")
        label5.setStyleSheet("background-color:white")
        label6.setStyleSheet("background-color:blue")
        label7.setStyleSheet("background-color:red")
    
        hbox = QHBoxLayout()
        hbox.addWidget(label1)
        hbox.addWidget(label2)
        hbox.addWidget(label3)
        hbox.addWidget(label4)
        hbox.addWidget(label5)
        hbox.addWidget(label6)
        hbox.addWidget(label6)
        hbox.addWidget(label7) 
       
        central_widget.setLayout(hbox)
        grid = QGridLayout()
        grid.addWidget(label1, 20,30)
        grid.addWidget(label2 ,30,20)
        grid.addWidget(label3, 20,30)
        grid.addWidget(label4 ,30,20)
        grid.addWidget(label5 ,20,30)
        grid.addWidget(label6 ,30,20)
        grid.addWidget(label7 ,20,30)
        
        central_widget.setLayout(grid)   
        
        
        
        
        
        
        
        
        
        
        

        
        
        
        
        
        
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
        

