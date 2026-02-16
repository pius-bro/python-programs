import sys 
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QPushButton,QWidget,QHBoxLayout,QVBoxLayout,QGridLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My fist window")
        self.setGeometry(400,100,700,420)
        
        
        label = QLabel("COMPUTER UNITS" , self)
        label.setFont(QFont("Arial" , 20))
        label.setGeometry(100,20,500,100)
        label.setStyleSheet("color : black;"
                            "background-color: green;"
                            "font-style : italic;"
                            "font-weight : bold;"
                            "text-decoration : underline" )
        label.setAlignment(Qt.AlignCenter)
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
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
        

