import sys
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QLabel, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSlot, Qt
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui

FILENAME = ""


class App(QWidget):

	def __init__(self):
		super().__init__()
		self.title = 'Tompgraph Simulator'
		self.left = 10
		self.top = 10
		self.width = 640
		self.height = 480
		self.initUI()

	def initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)

		self.loadButton = QPushButton('Load image', self)
		self.loadButton.setToolTip('Click here to load the image from files')
		# self.loadButton.resize(100, 100)
		self.loadButton.move(10, 10)
		self.loadButton.clicked.connect(self.loadClickAction)

		self.imageLabel = QLabel(self)

		param_tree = (
			{'name': 'img_size', 'type': 'int', 'value': 400},
			{'name': 'n_angles', 'type': 'int', 'value': 50},
			{'name': 'n_detectors', 'type': 'int', 'value': 10},
			{'name': 'width', 'type': 'float', 'value': 0.9},
			{'name': 'mask_size', 'type': 'float', 'value': 5},
			{'name': 'play_rate', 'type': 'int', 'value': 2}
		)
		self.parameters = pg.parametertree.Parameter.create(name='Settings', type='group', children=param_tree)
		self.param_tree = pg.parametertree.ParameterTree()
		self.param_tree.setParameters(self.parameters, showTop=False)
		self.param_tree.setSizePolicy(QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Preferred))

		self.layout = QtGui.QVBoxLayout(self)
		self.inputLayout = QtGui.QHBoxLayout()

		self.layout.addWidget(self.loadButton)
		self.inputLayout.addWidget(self.param_tree)
		self.inputLayout.addWidget(self.imageLabel)

		self.layout.addLayout(self.inputLayout)

		self.show()

	@pyqtSlot()
	def loadClickAction(self):
		global FILENAME
		print('load image')
		FILENAME = QFileDialog.getOpenFileName(filter="Images (*.png *.jpg)")[0]
		if FILENAME == '': return
		print(FILENAME)

		px = QPixmap(FILENAME)
		px = px.scaled(500, 500, Qt.KeepAspectRatio)

		self.imageLabel.setPixmap(px)
		self.imageLabel.setToolTip(FILENAME)
		self.imageLabel.move(10, self.loadButton.height()+20)
		self.imageLabel.resize(500, 500)
		self.imageLabel.show()


def startApp():
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())


if __name__ == '__main__':
	startApp()
