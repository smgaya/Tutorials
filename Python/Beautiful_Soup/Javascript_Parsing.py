import sys
from qtpy.QtGui import QGuiApplication
from qtpy.QtCore import QUrl
from qtpy.QtWebEngineWidgets import QWebEnginePage
import bs4 as bs


class Client(QWebEnginePage):
    def __init__(self, url):
        self.app = QGuiApplication(sys.argv)
        QWebEnginePage.__init__(self)
        self.loadFinished.connect(self.on_page_load)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()

    def on_page_load(self):
        self.app.quit()


url = 'https://pythonprogramming.net/parsememcparseface/'
client_response = Client(url)
source = client_response.mainFrame().toHtml()
soup = bs.BeautifulSoup(source, 'lxml')
js_test = soup.find('p', class_='jstest')
print(js_test.text)
