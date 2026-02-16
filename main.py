import sys 
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout,QHBoxLayout,QPushButton
from PyQt5.QtCore import Qt,QTime,QTimer 

class StopWatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0,0,0,0)
        self.time_label = QLabel("00:00:00.00",self)
        self.setStyleSheet("""QPushButton,QLabel{padding:10px;font-weight:bold;}QPushButton{font-size: 30px;padding:10px;}
                           QLabel{font-size:120px;background-color:blue;border-radius:20px;}""")
        self.start_button = QPushButton("start",self)
        self.stop_button = QPushButton("stop",self)
        self.reset_button = QPushButton("reset",self)
        self.timer = QTimer()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("Stopwatch")
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        
        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)
        vbox.addLayout(hbox)
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update)
    def start(self):
        self.timer.start(10)
    def stop(self):
        self.timer.stop() 
    def reset(self):
        self.timer.stop()
        self.time = QTime(0,0,0,0)
        self.time_label.setText(self.formart_time(self.time))
    def formart_time(self,time):
        hour = time.hour()
        minute = time.minute()
        second = time.second()
        millisecond = time.msec()//10
        return f"{hour:02}:{minute:02}:{second:02}.{millisecond:02}"
    def update(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.formart_time(self.time))
if __name__ =='__main__':
    app = QApplication(sys.argv)
    stopwatch = StopWatch()
    stopwatch.show()
    sys.exit(app.exec_())