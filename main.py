#import GUI


import sys
    
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore
from PyQt5.QtGui import QCursor


from GUI import *  # 加载我们的布局




#线程相关开始

from threading import Thread
from time import sleep

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QProgressBar

class _Signals(QtCore.QObject):

    updateProgress = QtCore.pyqtSignal(int)


Signals = _Signals()


class UpdateThread(Thread):

    def run(self):
        self.i = 0
        for i in range(101):
            self.i += 1
            Signals.updateProgress.emit(i)
            sleep(1)
        self.i = 0
        Signals.updateProgress.emit(i)




#线程相关结束



#style 

#import qdarkstyle
from darktheme.widget_template import DarkPalette
#style end











class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MyApp, self).__init__(*args, **kwargs)
        self.setupUi(self)  # 初始化ui
        # 在这里，可以做一些UI的操作了，或者是点击事件或者是别的
        # 也可以另外写方法，可以改变lable的内容
        #self.change()
        #QMainWindow.__init__(self, parent)
        #self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)#去除标题栏
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(0.8)


        #设置窗口
        self.window2 = Ui_Setting_Dialog()
        self.Window2_O = QtWidgets.QDialog()
        self.window2.setupUi(self.Window2_O)
        self.Window2_O.setWindowFlags(QtCore.Qt.FramelessWindowHint)



        #self.window3 = Ui_Assist01()
        #self.window3.setupUi()
        #self.window4 = Ui_KEY_Dialog()
        #self.window4.setupUi()
        self.action11.triggered.connect(self.Window2_O.show)#
        #线程相关


        #layout = QVBoxLayout(self)
        #self.progressBar = QProgressBar(self)
        #layout.addWidget(self.progressBar)
        #Signals.updateProgress.connect(
        #    self.progressBar.setValue, type=QtCore.Qt.QueuedConnection)

        QtCore.QTimer.singleShot(2000, self.doStart)
        
    def doStart(self):
        self.updateThread = UpdateThread(daemon=True)
        self.updateThread.start()


        #线程相关结束















    #def change(self):
    #    self.label.setText("试试，改变内容")

    def mousePressEvent(self, event):
        if event.button()==QtCore.Qt.LeftButton:
            self.m_flag=True
            self.m_Position=event.globalPos()-self.pos() #获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(QtCore.Qt.OpenHandCursor))  #更改鼠标图标
            #print('fffmmouse')
    def mouseMoveEvent(self, QMouseEvent):
        if QtCore.Qt.LeftButton and self.m_flag:  
            self.move(QMouseEvent.globalPos()-self.m_Position)#更改窗口位置
            QMouseEvent.accept()
            
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag=False
        self.setCursor(QCursor(QtCore.Qt.ArrowCursor))
















if __name__ == '__main__':  # 程序的入口
    Main_app = QApplication(sys.argv)



    #Main_app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    Main_app.setStyle("Fusion")
    Main_app.setPalette(DarkPalette())
    Main_app.setStyleSheet("QToolTip { color: #ffffff; background-color: grey; border: 1px solid white; }")
    
    #Main_app.setStyle(style)
    _win = MyApp()
    _win.show()
    sys.exit(Main_app.exec_())