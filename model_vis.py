import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QPalette,QBrush,QPixmap
from PIL import Image, ImageDraw

import matplotlib.pyplot as plt # plt 用于显示图片
import matplotlib.image as mpimg # mpimg 用于读取图片
import numpy as np
import cv2 as cv


class RoundShadow(QWidget):
    def __init__(self, parent=None):
        super(RoundShadow, self).__init__(parent)
        self.border_width = 8
        # 设置 窗口无边框和背景透明 *必须
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Window)

        self.width = self.size().width()
        self.height = self.size().height()
        self.resize(1000, 800)

                #设置样式
        self.left_close = QPushButton(self) # 关闭按钮 
        self.left_visit = QPushButton(self) # 空白按钮 
        self.left_mini = QPushButton(self)  # 最小化按钮

        self.left_close.move(0.97 * self.width, 0.03 * self.height)
        self.left_visit.move(0.95 * self.width, 0.03 * self.height)
        self.left_mini.move(0.93* self.width, 0.03 * self.height)

        self.left_close.setFixedSize(15,15) # 设置关闭按钮的大小 
        self.left_visit.setFixedSize(15, 15)  # 设置按钮大小 
        self.left_mini.setFixedSize(15, 15) # 设置最小化按钮大小

    def paintEvent(self, event):
        # 圆角
        pat2 = QPainter(self)
        pat2.setRenderHint(pat2.Antialiasing)  # 抗锯齿
        pat2.setBrush(Qt.white)
        pat2.setPen(Qt.transparent)

        rect = self.rect()
        rect.setLeft(9)
        rect.setTop(9)
        rect.setWidth(rect.width()-9)
        rect.setHeight(rect.height()-9)
        pat2.drawRoundedRect(rect, 4, 4)
class TestWindow(RoundShadow, QWidget):
    def __init__(self, parent=None):
        super(TestWindow, self).__init__(parent)

        self.resize(300, 300)

def circle_corner(imgName, radii):
    img = Image.open(imgName)
    # 画圆（用于分离4个角）
    circle = Image.new('L', (radii * 2, radii * 2), 0)  # 创建黑色方形
    # circle.save('1.jpg','JPEG',qulity=100)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, radii * 2, radii * 2), fill=255)  # 黑色方形内切白色圆形
    # circle.save('2.jpg','JPEG',qulity=100)
 
    img = img.convert("RGBA")
    w, h = img.size
 
    alpha = Image.new('L', img.size, 255)
    alpha.paste(circle.crop((0, 0, radii, radii)), (0, 0))  # 左上角
    alpha.paste(circle.crop((radii, 0, radii * 2, radii)),
                (w - radii, 0))  # 右上角
    alpha.paste(circle.crop((radii, radii, radii * 2, radii * 2)),
                (w - radii, h - radii))  # 右下角
    alpha.paste(circle.crop((0, radii, radii, radii * 2)),
                (0, h - radii))  # 左下角
 
    img.putalpha(alpha)		# 白色区域透明可见，黑色区域不可见
    return img

if __name__ == '__main__':
    app = QApplication(sys.argv)
    t = TestWindow()
    # t = RoundImage('./Asset/new_icons/close.png')
    t.show()
    app.exec_()

#批量创建文件夹

def paint_object(imgName, boxes):
    img_src = cv.imread(imgName)
    #✍boxeskuang
    



    temp_imgSrc = QImage(img_src[:], img_src.shape[1], img_src.shape[0], img_src.shape[1] * 3, QImage.Format_BGR888)
    pixmap_imgSrc = QPixmap.fromImage(temp_imgSrc)
    return pixmap_imgSrc

