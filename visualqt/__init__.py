import sys
from PySide6.QtWidgets import QApplication
from visualqt.gui import Rect, View, Window, Scene


def execute():
    app = QApplication(sys.argv)
    win = Window(app)
    win.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    execute()
