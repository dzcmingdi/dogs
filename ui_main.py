from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from dog_classify import DogClassify
from ui import contents


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1391, 753)
        MainWindow.setStyleSheet(u"font: 14pt '黑体';")
        self.AppTab = QTabWidget(MainWindow)
        self.AppTab.setObjectName(u"AppTab")
        self.AppTab.setDocumentMode(True)
        self.AppTab.setTabsClosable(False)
        self.AppTab.setMovable(False)
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.gridLayout_home = QGridLayout(self.home)
        self.gridLayout_home.setObjectName(u"gridLayout_home")
        self.gridLayout_home.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_dogs = QGridLayout()
        self.gridLayout_dogs.setObjectName(u"gridLayout_dogs")
        self.gridLayout_dogs.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.list_dogs = QListWidget(self.home)
        self.list_dogs.setObjectName(u"list_dogs")
        self.list_dogs.setStyleSheet(u"font: 14pt '黑体';")

        self.gridLayout_dogs.addWidget(self.list_dogs, 0, 0, 1, 1)

        self.gridLayout_home.addLayout(self.gridLayout_dogs, 2, 0, 1, 1)

        self.gridLayout_page_dogs = QGridLayout()
        self.gridLayout_page_dogs.setObjectName(u"gridLayout_page_dogs")
        self.gridLayout_page_dogs.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.scrollArea = QScrollArea(self.home)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.frame_page_dogs = QFrame()
        self.frame_page_dogs.setObjectName(u"frame_page_dogs")
        self.frame_page_dogs.setGeometry(QRect(0, 0, 1023, 687))
        self.frame_page_dogs.setMinimumSize(QSize(1023, 0))
        self.frame_page_dogs.setFrameShape(QFrame.NoFrame)
        self.frame_page_dogs.setFrameShadow(QFrame.Plain)
        self.gridLayout_content = QGridLayout(self.frame_page_dogs)
        self.gridLayout_content.setObjectName(u"gridLayout_content")
        self.gridLayout_content.setVerticalSpacing(6)
        self.gridLayout_header = QGridLayout()
        self.gridLayout_header.setObjectName(u"gridLayout_header")
        self.label_header = QLabel(self.frame_page_dogs)
        self.label_header.setObjectName(u"label_header")
        self.label_header.setStyleSheet(u"font: 48pt '黑体' bold;")
        self.label_header.setAlignment(Qt.AlignCenter)
        self.label_header.setWordWrap(True)

        self.gridLayout_header.addWidget(self.label_header, 0, 0, 1, 1)

        self.gridLayout_content.addLayout(self.gridLayout_header, 0, 0, 1, 1)

        self.gridLayout_body = QGridLayout()
        self.gridLayout_body.setObjectName(u"gridLayout_body")
        self.label_text = QLabel(self.frame_page_dogs)
        self.label_text.setObjectName(u"label_text")
        self.label_text.setStyleSheet(u"font: 20pt '黑体';")
        self.label_text.setWordWrap(True)

        self.gridLayout_body.addWidget(self.label_text, 1, 0, 1, 1)

        self.label_image = QLabel(self.frame_page_dogs)
        self.label_image.setObjectName(u"label_image")
        self.label_image.setWordWrap(False)

        self.gridLayout_body.addWidget(self.label_image, 0, 0, 1, 1)

        self.gridLayout_content.addLayout(self.gridLayout_body, 1, 0, 1, 1)

        self.gridLayout_content.setRowStretch(0, 1)
        self.gridLayout_content.setRowStretch(1, 10)
        self.scrollArea.setWidget(self.frame_page_dogs)

        self.gridLayout_page_dogs.addWidget(self.scrollArea, 1, 0, 1, 1)

        self.gridLayout_home.addLayout(self.gridLayout_page_dogs, 2, 1, 1, 1)

        self.gridLayout_home.setColumnStretch(0, 1)
        self.gridLayout_home.setColumnStretch(1, 3)
        self.AppTab.addTab(self.home, "")

        self.detect = Ui_Detect()
        self.detect.setObjectName("detect")

        self.AppTab.addTab(self.detect, "")
        MainWindow.setCentralWidget(self.AppTab)

        self.retranslateUi(MainWindow)

        self.AppTab.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"狗类识别", None))
        self.label_header.setText("")
        self.label_text.setText("")
        self.label_image.setText("")
        self.AppTab.setTabText(self.AppTab.indexOf(self.home), QCoreApplication.translate("MainWindow", "狗类", None))
        self.AppTab.setTabText(self.AppTab.indexOf(self.detect), QCoreApplication.translate("MainWindow", "识别", None))
    # retranslateUi


class Ui_Detect(QWidget):
    def __init__(self):
        super().__init__()
        self.gridLayout_detect = QGridLayout(self)
        self.gridLayout_detect.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_detect.setRowStretch(0, 3)
        self.gridLayout_detect.setRowStretch(1, 1)

        self.gridLayout_0 = QGridLayout()
        self.gridLayout_0.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_0.setObjectName("gridLayout_detect_0")
        self.gridLayout_1 = QGridLayout()
        self.gridLayout_1.setSizeConstraint(QLayout.SetDefaultConstraint)

        self.gridLayout_1.setObjectName("gridLayout_detect_1")
        self.frame_0 = QWidget(self)
        self.gridLayout_0.addWidget(self.frame_0, 0, 0)

        self.previous_button = QPushButton("上一张")
        self.previous_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.file_dialog_button = QPushButton("选择图片")
        self.next_button = QPushButton("下一张")
        self.next_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.file_dialog_button.clicked.connect(self.file_dialog_show)
        # self.frame_1 = QWidget()
        self.gridLayout_1.addWidget(self.file_dialog_button, 0, 1)
        self.gridLayout_0_ = QGridLayout(self.frame_0)
        self.gridLayout_0_.setSizeConstraint(QLayout.SetDefaultConstraint)

        self.gridLayout_0_.setColumnStretch(0, 5)
        self.gridLayout_0_.setColumnStretch(1, 1)
        self.gridLayout_0_0 = QGridLayout(self.frame_0)
        self.gridLayout_0_0.setSizeConstraint(QLayout.SetDefaultConstraint)

        # image grid layout
        self.gridLayout_0_0_0 = QGridLayout(self.frame_0)
        self.gridLayout_0_0_0.setSizeConstraint(QLayout.SetDefaultConstraint)

        self.image_frame = QFrame(self.frame_0)
        self.gridLayout_image = QGridLayout(self.image_frame)
        self.gridLayout_image.setSizeConstraint(QLayout.SetDefaultConstraint)

        self.button_frame = QWidget(self.frame_0)
        self.gridLayout_0_0_0.addWidget(self.image_frame, 0, 0)

        # button grid layout
        self.gridLayout_0_0_1 = QGridLayout()
        self.gridLayout_0_0_1.addWidget(self.button_frame)
        self.gridLayout_0_0.setRowStretch(0, 3)
        self.gridLayout_0_0.setRowStretch(1, 1)
        self.gridLayout_0_0.addLayout(self.gridLayout_0_0_0, 0, 0)
        self.gridLayout_0_0.addLayout(self.gridLayout_0_0_1, 1, 0)

        self.previous_button.setVisible(False)
        self.previous_button.clicked.connect(self.previous)
        self.next_button.clicked.connect(self.next)
        self.next_button.setVisible(False)
        self.gridLayout_0_0_0_ = QGridLayout(self.button_frame)
        self.gridLayout_0_0_0_.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_0_0_0_.addWidget(self.previous_button, 0, 0)
        self.gridLayout_0_0_0_.addWidget(self.next_button, 0, 1)
        # image
        self.image_label = QLabel(self.image_frame)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.gridLayout_image.addWidget(self.image_label, 0, 0)
        # classify text
        self.gridLayout_0_1 = QGridLayout()
        self.gridLayout_0_1.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.frame_0_widget_1 = QWidget()
        self.text_list = QListView(self.frame_0_widget_1)
        self.text_list.clicked.connect(self.text_selected)
        self.text_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.gridLayout_0_1.addWidget(self.frame_0_widget_1, 0, 0)

        self.gridLayout_0_.addLayout(self.gridLayout_0_0, 0, 0)
        self.gridLayout_0_.addLayout(self.gridLayout_0_1, 0, 1)

        self.gridLayout_detect.addLayout(self.gridLayout_0, 0, 0)
        self.gridLayout_detect.addLayout(self.gridLayout_1, 1, 0)

        self.current = 0
        self.length = 0
        self.results = []

        self.classifier = DogClassify()

        self.text_dialog = TextDialog(self)

    def file_dialog_show(self):
        filenames = QFileDialog.getOpenFileNames(self, ("Open Image"), "/home/", ("Image Files (*.png *.jpg *.bmp)"))
        self.file_dialog_selected(filenames[0])

    def file_dialog_selected(self, files):

        files = files if type(files) == list else list(files)
        if len(files) == 0:
            return

        self.previous_button.setVisible(True)
        self.next_button.setVisible(True)
        self.current = 0
        results = classify(self.classifier, files)
        self.length = len(results)
        self.results = results
        if self.current == self.length - 1:
            self.next_button.setEnabled(False)
        else:
            self.next_button.setEnabled(True)
        self.previous_button.setEnabled(False)

        r = results[self.current]

        image = r['image']
        label = self.results[self.current]['classify']

        self.set_pixmap(image)
        self.set_text(label)

    def next(self):
        self.previous_button.setEnabled(True)
        if self.current == self.length - 1:
            self.next_button.setEnabled(False)
            return
        self.current += 1
        if self.current == self.length - 1:
            self.next_button.setEnabled(False)

        image = self.results[self.current]['image']
        label = self.results[self.current]['classify']
        self.set_pixmap(image)
        self.set_text(label)

    def previous(self):
        self.next_button.setEnabled(True)
        if self.current == 0:
            self.previous_button.setEnabled(False)
            return
        self.current -= 1

        if self.current == 0:
            self.previous_button.setEnabled(False)

        image = self.results[self.current]['image']
        label = self.results[self.current]['classify']

        self.set_pixmap(image)
        self.set_text(label)

    def set_pixmap(self, image):
        q_image = QImage(image, image.shape[1], image.shape[0], image.shape[1] * 3, QImage.Format_BGR888)
        p_size = self.image_label.parent().size()
        p_w, p_h = p_size.width(), p_size.height()
        q_image = q_image.scaled(int(p_w * 0.8), int(p_h * 0.8), Qt.KeepAspectRatio, Qt.SmoothTransformation)

        self.image_label.setPixmap(QPixmap.fromImage(q_image))
        self.update()

    def set_text(self, label):
        m = QStandardItemModel()
        for i, l in enumerate(label):
            item = QStandardItem(f"{i}:{contents[int(l) - 1]['name'][:-1]}")
            item.setData(l, 1)
            item.setData(i, 3)
            m.appendRow(item)
        if len(label) == 0:
            item = QStandardItem('无法识别出狗')
            item.setData(0, 1)
            item.setData(0, 3)
            m.appendRow(item)

        self.text_list.setModel(m)

    def text_selected(self, item: QStandardItem):

        dog_id = item.data(1)
        if dog_id == 0:
            return
        item_id = int(item.data(3))
        crop_image = self.results[self.current]['crop_image'][item_id]
        self.text_dialog.update_inf(dog_id, crop_image)
        self.text_dialog.exec()


def classify(classier: DogClassify, files):
    labels, images, crop_images = classier.classify(files)
    results = []
    for label, image, crop_image in zip(labels, images, crop_images):
        results.append({'image': image, 'classify': label, 'crop_image': crop_image})
    return results


class TextDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowTitle("狗类信息")
        self.resize(1391, 753)
        self.gridLayout_3 = QGridLayout(self)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_image_0 = QLabel(self)
        self.label_image_1 = QLabel(self)
        self.label_image_0.setAlignment(Qt.AlignCenter)
        self.label_image_1.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addLayout(self.gridLayout_6, 1, 1, 1, 1)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")

        self.gridLayout_6.addWidget(self.label_image_0, 0, 0)
        self.gridLayout_7.addWidget(self.label_image_1, 0, 0)

        self.gridLayout_4.addLayout(self.gridLayout_7, 1, 0, 1, 1)

        self.gridLayout_3.addLayout(self.gridLayout_4, 1, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_content = QLabel(self)
        self.label_content.setObjectName(u"label_2")

        self.label_content.setStyleSheet(u"font: 20pt '黑体'; ")
        self.label_content.setWordWrap(True)

        self.gridLayout_8.addWidget(self.label_content, 0, 0, 1, 1)

        self.gridLayout_2.addLayout(self.gridLayout_8, 0, 0, 1, 1)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.pushButton = QPushButton("播放", self)
        self.pushButton.clicked.connect(self.play_audio)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_9.addWidget(self.pushButton, 0, 0, 1, 1)

        self.gridLayout_2.addLayout(self.gridLayout_9, 0, 1, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 10)
        self.gridLayout_2.setColumnStretch(1, 1)

        self.gridLayout_3.addLayout(self.gridLayout_2, 2, 0, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_head = QLabel(self)
        self.label_head.setObjectName(u"label")

        self.label_head.setStyleSheet(u"font: 40pt '黑体' bold;")
        self.label_head.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_head, 0, 0, 1, 1)

        self.gridLayout_3.addLayout(self.gridLayout_5, 0, 0, 1, 1)

        self.gridLayout_3.setRowStretch(0, 1)
        self.gridLayout_3.setRowStretch(1, 4)
        self.gridLayout_3.setRowStretch(2, 2)

        from PySide6.QtMultimedia import QSoundEffect

        self.player = QSoundEffect()

        self.local_dog_id = 0
        self.play_button_status = 1

    def update_inf(self, dog_id, crop_image):

        if dog_id == 0:
            return

        local_dog_id = dog_id - 1
        self.label_head.setText(contents[local_dog_id]['name'])
        self.label_content.setText(contents[local_dog_id]['text'])
        self.label_image_0.setPixmap(
            QPixmap(contents[local_dog_id]['image']).scaled(400, 400, Qt.KeepAspectRatio, Qt.SmoothTransformation))

        self.label_image_1.setPixmap(QPixmap.fromImage(
            QImage(crop_image, crop_image.shape[1], crop_image.shape[0], crop_image.shape[1] * 3,
                   QImage.Format_BGR888).scaled(400, 400, Qt.KeepAspectRatio, Qt.SmoothTransformation)))

        self.local_dog_id = local_dog_id

        self.player.setSource(QUrl.fromLocalFile(contents[self.local_dog_id]['audio']))

    def play_audio(self):

        if self.play_button_status == 1:
            self.player.play()
            self.play_button_status = 0
            self.pushButton.setText("停止")
        else:
            self.player.stop()
            self.play_button_status = 1
            self.pushButton.setText("播放")

    def closeEvent(self, event):
        self.play_button_status = 1
        self.pushButton.setText("播放")
        self.player.stop()
