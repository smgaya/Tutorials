import sys
from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
                             QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)
        self.statusBar()

        open_file = QAction("Open", self)
        open_file.setShortcut("Ctrl+O")
        open_file.setStatusTip("Open New File")
        open_file.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        file_menu = menubar.addMenu("&File")
        file_menu.addAction(open_file)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle("File Dialog Example")
        self.show()

    def showDialog(self):
        filename = QFileDialog.getOpenFileName(self, "Open file", "/home")

        if filename[0]:
            f = open(filename[0], 'r')

            with f:
                data = f.read()
                print(data)
                self.textEdit.setText(data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
