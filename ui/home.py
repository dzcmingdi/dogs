from PySide6 import QtCore
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import *
import ui


class HomeInit:
    def __init__(self, window: QMainWindow):
        self.list_dogs = window.findChild(QListWidget, "list_dogs")  # type: QListWidget
        self.gl_page_dogs = window.findChild(QGridLayout, "gridLayout_page_dogs")  # type: QGridLayout
        self.frame_content_dogs = window.findChild(QFrame, "frame_page_dogs")  # type: QFrame

        self.contents = ui.contents


    def init_view(self):

        self.list_dogs.currentItemChanged.connect(self.list_dogs_item_changed)

        for i, c in enumerate(self.contents):
            item = QListWidgetItem(c['name'][:-1], self.list_dogs)
            item.setData(1, i)
            self.list_dogs.insertItem(i, item)

    def list_dogs_item_changed(self, item: QListWidgetItem):
        id = item.data(1)
        self.dog_page_update(id)

    def dog_page_update(self, dog_id):
        c = self.contents[dog_id]
        pic = QPixmap(c['image'])


        label_header = self.frame_content_dogs.findChild(QLabel, 'label_header',
                                                         QtCore.Qt.FindChildrenRecursively)  # type: QLabel
        label_text = self.frame_content_dogs.findChild(QLabel, 'label_text')  # type:QLabel
        label_image = self.frame_content_dogs.findChild(QLabel, 'label_image')  # type: QLabel
        label_header.setText(c['name'])
        label_text.setText(c['text'])
        label_image.setPixmap(pic)
