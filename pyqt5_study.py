import sys 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLCDNumber, QApplication, QVBoxLayout, QSlider

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display) # 슬라이더에 값이 변경됐을 경우 연결될 슬롯을 정해준다.(괄호 안)


        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal and slot')
        self.show()
    
if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())