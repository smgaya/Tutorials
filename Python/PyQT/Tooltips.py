import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.setToolTip("This is a <b>QWidget</b>")
        button = QPushButton("Quit", self)
        button.clicked.connect(QCoreApplication.instance().quit)
        button.setToolTip("This is a <b>QPushButton</b>")
        button.resize(button.sizeHint())
        button.move(0, 0)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("Tooltips Example")
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
