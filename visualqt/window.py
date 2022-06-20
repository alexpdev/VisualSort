from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
try:
    from visualqt.algorithms import bubblesort
    from visualqt.gui import View, Scene
    from visualqt.structures import Rect
except ImportError:
    from algorithms import bubblesort
    from gui import View, Scene
    from structures import Rect

class Window(QMainWindow):

    def __init__(self, app) -> None:
        super().__init__()
        self.app = app
        self.layout = QVBoxLayout()
        self.central = QWidget()
        self.central.setLayout(self.layout)

        self.button1 = QPushButton("shuffle", parent=self)
        self.button2 = QPushButton("bubblesort", parent=self)
        self.button3 = QPushButton("clear", parent=self)
        self.button4 = QPushButton("populate", parent=self)

        self.hlayout  = QHBoxLayout()
        self.xlayout = QHBoxLayout()
        self.ylayout = QHBoxLayout()
        self.group1 = QGroupBox()
        self.group2 = QGroupBox()
        self.group1.setLayout(self.xlayout)
        self.group2.setLayout(self.ylayout)

        self.xlayout.addWidget(self.button1)
        self.xlayout.addWidget(self.button2)
        self.ylayout.addWidget(self.button3)
        self.ylayout.addWidget(self.button4)

        self.hlayout.addWidget(self.group1)
        self.hlayout.addWidget(self.group2)

        self.layout.addLayout(self.hlayout)
        self.view = View(parent=self)
        self.layout.addWidget(self.view)
        self.setCentralWidget(self.central)
        self.button1.clicked.connect(self.shuffle)
        self.button2.clicked.connect(self.bubblesort)
        self.button3.clicked.connect(self.clear)
        self.button4.clicked.connect(self.populate)
        self.view.timerStop.connect(self.stopTimer)

    def stopTimer(self):
        self.timer.stop()

    def shuffle(self):
        self.view.shuffle()

    def clear(self):
        self.view.clear()

    def bubblesort(self):
        bubblesort(self.view)

    def populate(self):
        if self.view.fillfunc is None:
            self.timer = QTimer()
            self.timer.setInterval(70)
            self.timer.timeout.connect(self.view.fill)
            self.timer.start()
        else:
            print("Board has not been cleared.")
