# Browser
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import *
from PyQt5.QtWidgets import*
from PyQt5.QtWebEngineWidgets import*
import sys

class MainWindow(QMainWindow):
      def __init__(self):
            super(MainWindow, self).__init__()
            self.browser=QWebEngineView()
            self.browser.setUrl(QUrl("https://www.google.com")) 
            self.setCentralWidget(self.browser)
            self.showMaximized()
            
            
            #navigators
            navbar = QToolBar()
            self.addToolBar(navbar)
            
            back_btn = QAction(' ⮜ ',self)
            back_btn.triggered.connect(self.browser.back)
            navbar.addAction(back_btn)
            
                        
            frw_btn = QAction(' ⮞ ',self)
            frw_btn.triggered.connect(self.browser.forward)
            navbar.addAction(frw_btn)
            
                        
            relod_btn = QAction(' ⭮ ',self)
            relod_btn.triggered.connect(self.browser.reload)
            navbar.addAction(relod_btn)
            
            home_btn = QAction(' ♚ ',self)
            home_btn.triggered.connect(self.navigate_home)
            navbar.addAction(home_btn)
            
            self.url_bar = QLineEdit()
            self.url_bar.returnPressed.connect(self.navigate_Url)
            navbar.addWidget(self.url_bar)
            
            self.browser.urlChanged.connect(self.update_Url)
            
            
            
      def update_Url(self, q):
            self.url_bar.setText(q.toString())
                  
            
      def navigate_Url(self):
            url = self.url_bar.text()
            self.browser.setUrl(QUrl(url))
            
      def navigate_home(self):
            self.browser.setUrl(QUrl("https://www.google.com"))
      
      
      
      
                  
            
            
app = QApplication(sys.argv)
QApplication.setApplicationName("Edith")
window =MainWindow()
app.exec_()

