import sys 
from PyQt5.QtWidgets import QMainWindow,QApplication,QRadioButton,QButtonGroup  

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Radio Buttons")
        self.setGeometry(300,200,400,300)
        self.radio_button1 = QRadioButton("Visa",self)
        self.radio_button2 =QRadioButton("Mastercard",self)
        self.radio_button3 = QRadioButton("Giftcard",self)
        self.group_button1 =QButtonGroup(self)
        self.group_button2 =QButtonGroup(self)
        self.group_button3 =QButtonGroup(self)
        
        self.initUI()
        
    def initUI(self):
        self.radio_button1.setGeometry(0,0,300,50)
        self.radio_button2.setGeometry(0,50,300,50)
        self.radio_button3.setGeometry(0,100,300,50)
        self.setStyleSheet("QRadioButton{""font-size:40px;""font-family:Arial;""padding:10px""}")
        self.group_button1.addButton(self.radio_button1)
        self.group_button2.addButton(self.radio_button2)
        self.group_button3.addButton(self.radio_button3)
        
        self.radio_button1.toggled.connect(self.checked)
        self.radio_button2.toggled.connect(self.checked)
        self.radio_button3.toggled.connect(self.checked)
                                     
    def checked(self):
        radio_button = self.sender()
        if radio_button . isChecked():
            print(f"{radio_button.text()} is selected")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    


        