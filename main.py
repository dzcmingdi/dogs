import sys
from PySide6.QtWidgets import *
from qt_material import apply_stylesheet
import ui
from ui.creator import Creator
from ui_main import Ui_MainWindow



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    creator = Creator(window)
    creator.create()
    apply_stylesheet(app, 'light_blue.xml')

    window.show()
    sys.exit(app.exec())
