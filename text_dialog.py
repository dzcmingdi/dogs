# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1036, 723)
        self.gridLayout_3 = QGridLayout(Dialog)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")

        self.gridLayout_4.addLayout(self.gridLayout_6, 1, 1, 1, 1)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")

        self.gridLayout_4.addLayout(self.gridLayout_7, 1, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_4, 1, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setWordWrap(True)

        self.gridLayout_8.addWidget(self.label_2, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_8, 0, 0, 1, 1)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_9.addWidget(self.pushButton, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_9, 0, 1, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 10)
        self.gridLayout_2.setColumnStretch(1, 1)

        self.gridLayout_3.addLayout(self.gridLayout_2, 2, 0, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(26)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_5, 0, 0, 1, 1)

        self.gridLayout_3.setRowStretch(0, 1)
        self.gridLayout_3.setRowStretch(1, 4)
        self.gridLayout_3.setRowStretch(2, 2)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u64ad\u653e", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
    # retranslateUi

