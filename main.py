# encoding=utf-8

import sys
from PyQt5.QtWidgets import QApplication
from IME_UI import MyMainWindow
if __name__ == '__main__':

    app = QApplication(sys.argv)
    demo = MyMainWindow()
    demo.show()
    sys.exit(app.exec())
