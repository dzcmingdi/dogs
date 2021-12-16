import sys
from time import sleep
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QPalette,QBrush,QPixmap
from cv2 import sepFilter2D
from torch._C import set_flush_denormal
from model_vis import RoundShadow
from model_vis import circle_corner, paint_object
from dog_classify_main import DogClassify
import os
import win32com.client
from PyQt5.Qt import QThread
import sys
import winsound

#主界面类
class menu_page(QtWidgets.QMainWindow, RoundShadow):
    def __init__(self, flag):
        super(menu_page, self).__init__()
          #窗口尺寸
        self.resize(1000, 800)
        self.setWindowTitle("dog_classify")
        self.flag = flag

        self.width = self.size().width()
        self.height = self.size().height()

        self.labelText = QLabel(self)
        self.labelText.setFixedSize(400, 400)

        self.labelText.move(0.35*self.width, 0.04*self.height)
        self.labelText.setText('狗狗识别系统')
        self.labelText.setAlignment(Qt.AlignLeft)
        self.labelText.setScaledContents(True)

        self.btnopen_alldog = QPushButton(self)
        self.btnopen_alldog.move(0.05 * self.width, 0.85 * self.height)
        self.btnopen_alldog.clicked.connect(self.jump_to_alldog)
        self.btnopen_alldog.setFixedSize(100, 100)
        self.btnopen_alldog.setStyleSheet("QPushButton{border-image:url(./data/images/icon2.png)}")

        

        self.btnopen_predictdog = QPushButton(self)
        self.btnopen_predictdog.move(0.85 * self.width, 0.85 * self.height)
        self.btnopen_predictdog.clicked.connect(self.jump_to_dog_classify)
        self.btnopen_predictdog.setFixedSize(100, 100)
        self.btnopen_predictdog.setStyleSheet("QPushButton{border-image:url(./data/images/icon1.png)}")

        #设置样式
        self.left_close = QPushButton(self) # 关闭按钮 
        self.left_visit = QPushButton(self) # 空白按钮 
        self.left_mini = QPushButton(self)  # 最小化按钮

        self.left_close.move(0.97 * self.width, 0.03 * self.height)
        self.left_visit.move(0.95 * self.width, 0.03 * self.height)
        self.left_mini.move(0.93* self.width, 0.03 * self.height)

        self.left_close.clicked.connect(self.close)
        self.left_visit.clicked.connect(self.initUI)
        self.left_mini.clicked.connect(self.showMinimized)

        self.left_close.setFixedSize(15,15) # 设置关闭按钮的大小 
        self.left_visit.setFixedSize(15, 15)  # 设置按钮大小 
        self.left_mini.setFixedSize(15, 15) # 设置最小化按钮大小

        # spin_icon = QIcon('/data/images/paw1.png')
        # self.btnopen_predictdog.setIcon(spin_icon)#设置图标
        # self.btnopen_predictdog.setIconSize(QtCore.QSize(50,50))
        # self.btnopen_predictdog.setStyleSheet('''QPushButton{border:none;}
        # QPushButton:hover{color:white;
        #             border:2px solid #F3F3F5;
        #             border-radius:35px;
        #             background:darkGray;}''')

        self.left_close.setStyleSheet('''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''') 
        self.left_visit.setStyleSheet('''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''') 
        self.left_mini.setStyleSheet('''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
        self.labelText.setStyleSheet('background-color: rgb(20, 20, 0)')    #设置背景色
        self.labelText.setStyleSheet('font-size:40px;color:balck;font-family:黑体 ') #设置字体大小，字体颜色,字体
#显示图片的label，目测6张
        self.label_dogtitle1 = QLabel(self)
        self.label_dogtitle2 = QLabel(self)
        self.create_titledog()
        img_dir = './data/images/'
        imgName = []
        for i in range(6):
            imgName.append(img_dir + 'dog' + str(i) + '.jpg')
        self.showdog1 = QLabel(self)
        self.showdog2 = QLabel(self)
        self.showdog3 = QLabel(self)
        self.showdog4 = QLabel(self)
        self.showdog5 = QLabel(self)
        self.showdog6 = QLabel(self)
        self.show_label_dog(imgName[0], 50, 120, self.showdog1)
        self.show_label_dog(imgName[1], 350, 120, self.showdog2)
        self.show_label_dog(imgName[2], 650, 120, self.showdog3)
        self.show_label_dog(imgName[3], 50, 420, self.showdog4)
        self.show_label_dog(imgName[4], 350, 420, self.showdog5)
        self.show_label_dog(imgName[5], 650, 420, self.showdog6)

        if self.flag == 1:
            self.initUI()

    def create_titledog(self):
        self.label_dogtitle1.setFixedSize(0.05 * self.width, 0.0625 * self.height)
        self.label_dogtitle1.move(0.3*self.width, 0.04*self.height)
 
        self.label_dogtitle1.setStyleSheet("QLabel{background:white;}"
                 "QLabel{color:rgb(300,300,300,120);font-size:10px;font-weight:bold;font-family:宋体;}"
                 "QLabel:{border:2px groove gray;border-radius:25px;padding:2px 4px;}"
                 )
        imgName = 'data/images/dog1.jpg'
        jpg = QtGui.QPixmap(imgName).scaled(self.label_dogtitle1.width(), self.label_dogtitle1.height())
        self.label_dogtitle1.setPixmap(jpg)

        self.label_dogtitle2.setFixedSize(0.05 * self.width, 0.0625 * self.height)
        self.label_dogtitle2.move(0.59*self.width, 0.04*self.height)
 
        self.label_dogtitle2.setStyleSheet("QLabel{background:white;}"
                 "QLabel{color:rgb(300,300,300,120);font-size:10px;font-weight:bold;font-family:宋体;}"
                 "QLabel:{border:2px groove gray;border-radius:25px;padding:2px 4px;}"
                 )
        imgName = 'data/images/dog1.jpg'
        jpg = QtGui.QPixmap(imgName).scaled(self.label_dogtitle2.width(), self.label_dogtitle2.height())
        self.label_dogtitle2.setPixmap(jpg)

    def show_label_dog(self, imgName, x, y, label):
        label.setFixedSize(0.2 * self.width, 0.315 * self.height)
        label.move(x, y)
    
        label.setStyleSheet("QLabel{background:white;}"
                "QLabel{color:rgb(300,300,300,120);font-size:10px;font-weight:bold;font-family:宋体;}"
                "QLabel:{border:2px groove gray;border-radius:25px;padding:2px 4px;}"
                )
        jpg = QtGui.QPixmap(imgName).scaled(label.width(), label.height())
        label.setPixmap(jpg)

    def initUI(self):
        self.showMaximized()

        
        self.width = self.size().width()
        self.height = self.size().height()

        self.labelText.setFixedSize(0.4 * self.width, 0.5 * self.height)

        self.labelText.move(0.4*self.width, 0.04*self.height)
        self.labelText.setText('狗狗识别系统')
        self.labelText.setAlignment(Qt.AlignLeft)
        self.labelText.setScaledContents(True)

        self.btnopen_alldog.move(0.05 * self.width, 0.85 * self.height)
        self.btnopen_alldog.clicked.connect(self.jump_to_alldog)

        self.btnopen_predictdog.move(0.85 * self.width, 0.85 * self.height)
        self.btnopen_predictdog.clicked.connect(self.jump_to_dog_classify)

        self.left_close.move(0.97 * self.width, 0.03 * self.height)
        self.left_visit.move(0.95 * self.width, 0.03 * self.height)
        self.left_mini.move(0.93* self.width, 0.03 * self.height)

        self.create_titledog()

        img_dir = './data/images/'
        imgName = []
        for i in range(6):
            imgName.append(img_dir + 'dog' + str(i) + '.jpg')
        self.show_label_dog(imgName[0], 100, 120, self.showdog1)
        self.show_label_dog(imgName[1], 700, 120, self.showdog2)
        self.show_label_dog(imgName[2], 1300, 120, self.showdog3)
        self.show_label_dog(imgName[3], 100, 500, self.showdog4)
        self.show_label_dog(imgName[4], 700, 500, self.showdog5)
        self.show_label_dog(imgName[5], 1300, 500, self.showdog6)

        self.flag = 1

#跳转到预测界面
    def jump_to_dog_classify(self):
        self.hide()
        self.dog_classify_page = dog_classify(self.flag)
        self.dog_classify_page.show()
#跳转到所有狗类界面
    def jump_to_alldog(self):
        self.hide()
        self.alldog_menu = menu_all_dog(flag = self.flag)
        self.alldog_menu.show()


#上传图片界面类
class dog_classify(QtWidgets.QMainWindow,RoundShadow):
    def __init__(self, flag):
        super(dog_classify, self).__init__()
        self.dog_classify = DogClassify()
        self.is_openimage = 0


      
    #窗口尺寸
        
        self.resize(1000, 800)
        self.setWindowTitle("狗类识别系统")
         #窗口尺寸
        self.width = self.size().width()
        self.height = self.size().height()

        self.halfwidth = self.width // 2
        self.halfheight = self.height // 2

        QToolTip.setFont(QFont('SansSerif', 10))

 
 #显示图片label
        self.label = QLabel(self)
        self.label.setFixedSize(0.7 * self.width, 0.5 * self.height)
        self.label.move(0.25* self.width, 0.25 * self.height)
 
        self.label.setStyleSheet("QLabel{background:white;}"
                 "QLabel{color:rgb(300,300,300,120);font-size:10px;font-weight:bold;font-family:宋体;}"
                 )
         #打开图片按钮
        self.btn_open = QPushButton(self)
        self.btn_open.move(0.01 * self.width, 0.8 * self.height)
        self.btn_open.setFixedSize(100, 100)
        self.btn_open.setStyleSheet("QPushButton{border-image:url(./data/images/icon2.png)}")
        self.btn_open.clicked.connect(self.openimage)
        self.btn_open.setToolTip("打开图片")

        #预测按钮
        self.btn_predict = QPushButton(self)
        self.btn_predict.move(0.85 * self.width, 0.8 * self.height)
        self.btn_predict.clicked.connect(self.predict_dog)
        self.btn_predict.setFixedSize(100, 100)
        self.btn_predict.setStyleSheet("QPushButton{border-image:url(./data/images/icon2.png)}")
        self.btn_predict.setToolTip("开始预测")



        self.btn_return  = QPushButton(self)
        self.btn_return.move(0.01 * self.width, 0.03 * self.height)
        self.btn_return.clicked.connect(self.returnback)
        self.btn_return.setToolTip("返回")



        self.btn_return.setStyleSheet("QPushButton{border-image:url(./data/images/return.png)}")
        #设置样式
        self.left_close = QPushButton(self) # 关闭按钮 
        self.left_visit = QPushButton(self) # 空白按钮 
        self.left_mini = QPushButton(self)  # 最小化按钮

        self.left_close.move(0.97 * self.width, 0.03 * self.height)
        self.left_visit.move(0.95 * self.width, 0.03 * self.height)
        self.left_mini.move(0.93* self.width, 0.03 * self.height)

        self.left_close.clicked.connect(self.close)
        self.left_visit.clicked.connect(self.initUI)
        self.left_mini.clicked.connect(self.showMinimized)

 

        # self.setWindowOpacity(0.9) # 设置窗口透明度 
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground) # 设置窗口背景透明
        self.left_close.setFixedSize(15,15) # 设置关闭按钮的大小 
        self.left_visit.setFixedSize(15, 15)  # 设置按钮大小 
        self.left_mini.setFixedSize(15, 15) # 设置最小化按钮大小

        self.left_close.setStyleSheet('''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''') 
        self.left_visit.setStyleSheet('''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''') 
        self.left_mini.setStyleSheet('''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
    #打开文件资源管理器
        self.flag = flag
        self.imgName = '1'

        if self.flag == 1:
            self.initUI()
        self.drawn()
    def openimage(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
        jpg = QtGui.QPixmap(imgName)
        if jpg.width() == 0:
            pass
        else:
            self.jpg = jpg
            if self.jpg.width() <= self.jpg.height() * 1.25:
                self.jpg = self.jpg.scaled(self.jpg.width() // (self.jpg.height() / self.halfheight), self.jpg.height() // (self.jpg.height() / self.halfheight))
            else:
                self.jpg = self.jpg.scaled(self.jpg.width() // (self.jpg.width() / self.halfwidth), self.jpg.height() // (self.jpg.width() / self.halfwidth))
            self.imgName = imgName
            self.label.move(self.halfwidth - self.jpg.width() // 2, self.halfheight - self.jpg.height() // 2)
            self.label.setFixedSize(self.jpg.width(), self.jpg.height())
            self.label.setPixmap(self.jpg)
            self.is_openimage = 1

    def drawn(self):
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap("./data/images/dog1.jpg")))
        self.setPalette(self.palette)
#返回到开始界面
    def returnback(self):
        self.close()
        self.back = menu_page(self.flag)
        self.back.show()
#跳转预测界面
    def predict_dog(self):
        if self.imgName == '1':
            self.remain = QMessageBox.about(self, '提示', '请选择图片')
        else:
            self.hide()
            dog_what, boxes =  self.dog_classify.classify(self.imgName)#输入图片给模型
            self.predict_picture = predict_result(imgName = self.imgName, jpg = self.jpg, dog_what = dog_what, flag = self.flag, boxes = boxes)
            self.predict_picture.show()

    def initUI(self):
        self.showMaximized()
        self.width = self.size().width()
        self.height = self.size().height()

        self.halfheight = self.height // 2
        self.halfwidth = self.width // 2

        self.btn_open.move(0.01 * self.width, 0.8 * self.height)
        self.btn_open.setFixedSize(100, 100)

        self.btn_predict.move(0.9 * self.width, 0.8 * self.height)
        self.btn_predict.setFixedSize(100, 100)

        self.left_close.move(0.97 * self.width, 0.03 * self.height)
        self.left_visit.move(0.95 * self.width, 0.03 * self.height)
        self.left_mini.move(0.93* self.width, 0.03 * self.height)

        #有jpg才运行
        if self.is_openimage == 1:
            if self.jpg.width() <= self.jpg.height() * 1.25:
                self.jpg = self.jpg.scaled(self.jpg.width() // (self.jpg.height() / self.halfheight), self.jpg.height() // (self.jpg.height() / self.halfheight))
            else:
                self.jpg = self.jpg.scaled(self.jpg.width() // (self.jpg.width() / self.halfwidth), self.jpg.height() // (self.jpg.width() / self.halfwidth))
            self.label.move(self.halfwidth - self.jpg.width() // 2, self.halfheight - self.jpg.height() // 2)
            self.label.setFixedSize(self.jpg.width(), self.jpg.height())
            self.label.setPixmap(self.jpg)

        self.flag = 1



#预测结果界面类
class predict_result(QtWidgets.QMainWindow, RoundShadow):
    def __init__(self, imgName, jpg, dog_what, flag, boxes):
        super(predict_result, self).__init__()
        self.resize(1000, 800)
        self.setWindowTitle("狗类")
        self.dog_what = dog_what
        self.flag = flag
        self.jpg = jpg
        self.imgName = imgName
        self.label = QLabel(self)
        self.labelTrue = QLabel(self)
        self.te = QTextEdit(self)  #本办法也适用于QTextBrowser,QPlainTextEdit
        self.sortdog = 0
        self.boxes = boxes
        self.speak_btn = QPushButton(self)
        self.btn_return = QPushButton(self)
        self.pause_speak = QPushButton(self)


        self.width = self.size().width()
        self.height = self.size().height()

        self.halfwidth = self.width // 2
        self.halfheight = self.height // 2

#返回按钮
        self.btn_return.move(0.01 * self.width, 0.03 * self.height)
        self.btn_return.clicked.connect(self.returnback)
        self.btn_return.setStyleSheet("QPushButton{border-image:url(./data/images/return.png)}")
#播放语音按钮
        self.speak_btn.move(0.01 * self.width, 0.9 * self.height)
        self.speak_btn.clicked.connect(self.speak_txt)
        self.speak_btn.setFixedSize(50, 50)
        self.speak_btn.setStyleSheet("QPushButton{border-image:url(./data/images/play.png)}")
#pause 按钮
        self.pause_speak.move(0.2 * self.width, 0.9 * self.height)
        self.pause_speak.clicked.connect(self.pause_txt)
        self.pause_speak.setFixedSize(50, 50)
        self.pause_speak.setStyleSheet("QPushButton{border-image:url(./data/images/pause.png)}")

        self.left_close = QPushButton(self) # 关闭按钮 
        self.left_visit = QPushButton(self) # 空白按钮 
        self.left_mini = QPushButton(self)  # 最小化按钮

        self.left_close.move(0.97 * self.width, 0.03 * self.height)
        self.left_visit.move(0.95 * self.width, 0.03 * self.height)
        self.left_mini.move(0.93* self.width, 0.03 * self.height)

        self.left_close.clicked.connect(self.close)
        self.left_visit.clicked.connect(self.initUI)
        self.left_mini.clicked.connect(self.showMinimized)

#如果多dog，需要按鈕实现切换（上一张下一张）
        self.nextdog = QPushButton(self)
        self.nextdog.setStyleSheet("QPushButton{border-image:url(./data/images/next.png)}")
        self.nextdog.move(0.7 * self.width, 0.03 * self.height)
        self.nextdog.clicked.connect(self.next_dog)

        self.forwarddog = QPushButton(self)
        self.forwarddog.move(0.5 * self.width, 0.03 * self.height)
        self.forwarddog.clicked.connect(self.forwrad_dog)
        self.forwarddog.setStyleSheet("QPushButton{border-image:url(./data/images/return.png)}")


        # self.setWindowOpacity(0.9) # 设置窗口透明度 
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground) # 设置窗口背景透明
        self.left_close.setFixedSize(15,15) # 设置关闭按钮的大小 
        self.left_visit.setFixedSize(15, 15)  # 设置按钮大小 
        self.left_mini.setFixedSize(15, 15) # 设置最小化按钮大小

        self.left_close.setStyleSheet('''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''') 
        self.left_visit.setStyleSheet('''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''') 
        self.left_mini.setStyleSheet('''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
        self.labelTrue.setStyleSheet("QLabel{color:rgb(300,300,300,120);font-size:10px;font-weight:bold;font-family:宋体;}"
                 )
        self.label.setStyleSheet("QLabel{background:white;}"
                 "QLabel{color:rgb(300,300,300,120);font-size:10px;font-weight:bold;font-family:宋体;}"
                 )
        self.label.setStyleSheet("QLabel{background:white;}"
                 "QLabel{color:rgb(300,300,300,120);font-size:10px;font-weight:bold;font-family:宋体;}"
                 )
        self.te.setStyleSheet("font:63 11pt 微软雅黑;color:rgb(0,0,0); margin:10px 0px 5px;")



        if self.flag == 1:
            self.initUI()
        self.get_result()

        #假设文本内容，实际可以用任何你需要的文本，暂时当作提示说明。

        #self.te.setReadOnly(True)   #把光标隐去，不加就显示光标移动

    def get_result(self): 

        self.jpgkuang = paint_object(self.imgName, self.boxes[self.sortdog])
        self.jpgkuang = self.property_size(self.jpgkuang)
        self.label.setFixedSize(self.jpgkuang.width(), self.jpgkuang.height())

        self.label.setPixmap(self.jpgkuang)
        self.label.move(50, self.halfheight - self.jpgkuang.height() // 2)


        self.dog_jpg = img_dir + path_all[self.dog_what[self.sortdog]] + '/' + path_all[self.dog_what[self.sortdog]] + '.jpg'
        self.dog_txt = img_dir + path_all[self.dog_what[self.sortdog]] + '/' + path_all[self.dog_what[self.sortdog]] + '.txt'
        self.dog_wav = img_dir + path_all[self.dog_what[self.sortdog]] + '/' + path_all[self.dog_what[self.sortdog]] + '.wav'

        self.jpgTrue = QtGui.QPixmap(self.dog_jpg)
        self.jpgTrue = self.property_size(self.jpgTrue)
        self.jpgTrue = self.jpgTrue.scaled(self.jpgTrue.width() // 1.5, self.jpgTrue.height() // 1.5)
        self.labelTrue.move(self.width // 4 - self.jpgTrue.width() // 3 + self.width // 2, self.height // 4 - self.jpgTrue.height() // 3)
        self.labelTrue.setFixedSize(self.jpgTrue.width(), self.jpgTrue.height())
        self.labelTrue.setPixmap(self.jpgTrue)

        with open(self.dog_txt, encoding='utf-8',mode="r") as f:  # 打开文件
            self.data = f.read()  # 读取文件
        self.te.setText(self.data)
        
        self.te.move(self.width // 4 - self.jpgTrue.width() // 3 + self.width // 2, self.height // 4 - self.jpgTrue.height() // 3 + 1.2* self.jpgTrue.height())
        self.te.resize(self.jpgTrue.width(),self.jpgTrue.height())


    def next_dog(self):
        self.sortdog += 1
        if len(self.dog_what) == self.sortdog:
            self.dog_picture = QMessageBox.about(self, '提示', '已经是最后一张狗了')
            self.sortdog -= 1
        else:
            winsound.PlaySound(playsound, winsound.SND_PURGE)
            self.get_result()

    def forwrad_dog(self):
        if self.sortdog == 0 :
            self.dog_picture = QMessageBox.about(self, '提示', '这是第一张狗了')
        else:
            #传入boxes
            winsound.PlaySound(playsound, winsound.SND_PURGE)
            self.sortdog -= 1
            self.get_result()


    def returnback(self):
        self.close()
        self.back = dog_classify(flag = self.flag)
        self.back.show()

    def initUI(self):

        self.showMaximized()

        self.width = self.size().width()
        self.height = self.size().height()

        self.halfwidth = self.width // 2
        self.halfheight = self.height // 2

        self.btn_return.move(0.01 * self.width, 0.03 * self.height)
        self.left_close.move(0.97 * self.width, 0.03 * self.height)
        self.left_visit.move(0.95 * self.width, 0.03 * self.height)
        self.left_mini.move(0.93* self.width, 0.03 * self.height)

        self.label.move(self.halfwidth - self.jpg.width() // 2, self.halfheight - self.jpg.height() // 2)
        self.label.setFixedSize(self.jpg.width(), self.jpg.height())
        self.label.setPixmap(self.jpg)
        self.flag = 1

        self.nextdog.move(0.7 * self.width, 0.03 * self.height)
        self.forwarddog.move(0.5 * self.width, 0.03 * self.height)
        self.pause_speak.move(0.2 * self.width, 0.9 * self.height)
        self.speak_btn.move(0.01 * self.width, 0.9 * self.height)

        self.get_result()




    def property_size(self, jpg):
        if jpg.width() <= jpg.height() * 1.25:
            jpg = jpg.scaled(jpg.width() // (jpg.height() / self.halfheight), jpg.height() // (jpg.height() / self.halfheight))
        else:
            jpg = jpg.scaled(jpg.width() // (jpg.width() / self.halfwidth), jpg.height() // (jpg.width() / self.halfwidth))
        return jpg

    def speak_txt(self):
        global playsound
        playsound = winsound.PlaySound(self.dog_wav, winsound.SND_ASYNC)
    def pause_txt(self):
        winsound.PlaySound(playsound, winsound.SND_PURGE)




        

#狗全部类别界面类
class menu_all_dog(QtWidgets.QMainWindow, RoundShadow):
    def __init__(self, flag):
        super(menu_all_dog, self).__init__()

        self.resize(1000, 800)
        self.setWindowTitle("狗类")
        self.flag = flag
                
        self.width = self.size().width()
        self.height = self.size().height()

        self.btn_return = QPushButton(self)
        self.btn_return.move(0.01 * self.width, 0.03 * self.height)
        self.btn_return.clicked.connect(self.returnback)

        self.btn_return.setStyleSheet("QPushButton{border-image:url(./data/images/return.png)}")

                #设置样式
        self.left_close = QPushButton(self) # 关闭按钮 
        self.left_visit = QPushButton(self) # 空白按钮 
        self.left_mini = QPushButton(self)  # 最小化按钮

        self.left_close.move(0.97 * self.width, 0.03 * self.height)
        self.left_visit.move(0.95 * self.width, 0.03 * self.height)
        self.left_mini.move(0.93* self.width, 0.03 * self.height)



        self.left_close.clicked.connect(self.close)
        self.left_visit.clicked.connect(self.initUI)
        self.left_mini.clicked.connect(self.showMinimized)

 

        # self.setWindowOpacity(0.9) # 设置窗口透明度 
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground) # 设置窗口背景透明
        self.left_close.setFixedSize(15,15) # 设置关闭按钮的大小 
        self.left_visit.setFixedSize(15, 15)  # 设置按钮大小 
        self.left_mini.setFixedSize(15, 15) # 设置最小化按钮大小

        self.left_close.setStyleSheet('''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''') 
        self.left_visit.setStyleSheet('''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''') 
        self.left_mini.setStyleSheet('''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')

        if self.flag == 1:
            self.initUI()
            
    def returnback(self):
        self.close()
        self.back = menu_page(flag = self.flag)
        self.back.show()

    def initUI(self):
        self.showMaximized()
        self.width = self.size().width()
        self.height = self.size().height()
        self.btn_return.move(0.01 * self.width, 0.03 * self.height)

        self.left_close.move(0.97 * self.width, 0.03 * self.height)
        self.left_visit.move(0.95 * self.width, 0.03 * self.height)
        self.left_mini.move(0.93* self.width, 0.03 * self.height)

        self.flag = 1
        
# class Thread_1(QThread):
#     def __init__(self, wav):
#         super().__init__()
#         self.wav = wav

#     def run(self):
#         playsound(self.wav)
    
if __name__ == "__main__":
    playsound = winsound.PlaySound(None, winsound.SND_NODEFAULT)
    app = QtWidgets.QApplication(sys.argv)
    img_dir = 'data/dog_data/'
    path_all = []
    for path in os.listdir(img_dir):
        path_all.append(path)
    # apply_stylesheet(app, theme = 'light_blue.xml')
    main_Widnow = dog_classify(flag = 0)
    main_Widnow.show()
    sys.exit(app.exec_())
