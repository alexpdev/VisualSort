import sys
from PySide6.QtWidgets import QApplication

try:
    from visualqt.window import Window
except ImportError:
    from window import Window


def execute():
    app = QApplication(sys.argv)
    win = Window(app)
    win.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    execute()
