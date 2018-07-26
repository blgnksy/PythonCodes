from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
		QWidget.__init__(self)
		layout = QGridLayout()
		self.setLayout(layout)
		label = QLabel("The Story of Dale")
		layout.addWidget(label, 0, 0)
		label = QLabel("Few people could understand Dale's motivation. It wasn't something that was easy.")
		label.setWordWrap(True)
		label.setAlignment(Qt.AlignRight | Qt.AlignBottom)
		layout.addWidget(label, 0, 1)
				   
app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())
