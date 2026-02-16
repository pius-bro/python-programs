import sys 
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QPushButton
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
        self.button = QPushButton("CLICK HERE",self)
        self.label = QLabel("HEY" , self)
        self.initUI()
        
    def initUI(self):
        self.button.setFont(QFont("Arial" , 20))
        self.button.setGeometry(200,150,300,100)
        self.button.setStyleSheet("font-size:30px")
        self.button.clicked.connect(self.on_click)
        self.label.setGeometry(200,210,300,120)
        self.label.setStyleSheet("font-size:30px")
    def on_click(self):
        print("{CSC 311: COMPUTER ARCHTECTURE,CSC 312: SYSTEM SECURITY,CSC 313:DATABASE SYSTEM,CSC 314:NETWORK PROGRAMMIG}")
        self.button.setText("Done")
        self.label.setText("Wow!")
         
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
        

