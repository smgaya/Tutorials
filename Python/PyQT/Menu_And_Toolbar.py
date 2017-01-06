import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        text = QTextEdit()
        self.setCentralWidget(text)

        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.setStatusTip("Exit application")
        exit_action.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        file_menu = menubar.addMenu("&File")
        file_menu.addAction(exit_action)

        toolbar = self.addToolBar("Exit")
        toolbar.addAction(exit_action)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle("Menubar and Toolbar Example")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
