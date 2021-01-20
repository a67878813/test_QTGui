# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testQT.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
#from win32.lib import win32con
#from win32.win32gui import ReleaseCapture
#from win32.win32api import SendMessage
#from PyQt5.QtGui import QCursor

class MYQDialog(QtWidgets.QDialog):
    #鼠标自由拖动 QDialog子类
    def mousePressEvent(self, event):
        if event.button()==QtCore.Qt.LeftButton:
            self.m_flag=True
            self.m_Position=event.globalPos()-self.pos() #获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  #更改鼠标图标
            #print('fffmmouse')
    def mouseMoveEvent(self, QMouseEvent):
        if QtCore.Qt.LeftButton and self.m_flag:  
            self.move(QMouseEvent.globalPos()-self.m_Position)#更改窗口位置
            QMouseEvent.accept()
            
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag=False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))








class Ui_MainWindow(object):    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(219, 138)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider.setGeometry(QtCore.QRect(190, 0, 22, 71))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(116, 0, 31, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(2, 0, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(7)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(118, 50, 61, 51))
        self.label_2.setObjectName("label_2")
        self.progressing = QtWidgets.QProgressBar(self.centralwidget)
        self.progressing.setGeometry(QtCore.QRect(190, 80, 21, 21))
        self.progressing.setMouseTracking(False)
        self.progressing.setProperty("value", 24)
        self.progressing.setAlignment(QtCore.Qt.AlignCenter)
        self.progressing.setFormat("")
        self.progressing.setObjectName("progressing")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(146, 0, 31, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(1, 20, 111, 91))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.treeWidget.setFont(font)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(116, 20, 31, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(146, 20, 31, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalSlider.raise_()
        self.lineEdit.raise_()
        self.label_2.raise_()
        self.progressing.raise_()
        self.pushButton_2.raise_()
        self.treeWidget.raise_()
        self.pushButton_4.raise_()
        self.pushButton_6.raise_()
        self.pushButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 219, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuAbout_2 = QtWidgets.QMenu(self.menubar)
        self.menuAbout_2.setObjectName("menuAbout_2")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.actionsave = QtWidgets.QAction(MainWindow)
        self.actionsave.setObjectName("actionsave")
        self.actionexit = QtWidgets.QAction(MainWindow)
        self.actionexit.setObjectName("actionexit")
        self.action11 = QtWidgets.QAction(MainWindow)
        self.action11.setObjectName("action11")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionRegist_Key = QtWidgets.QAction(MainWindow)
        self.actionRegist_Key.setObjectName("actionRegist_Key")
        self.menuFile.addAction(self.actionsave)
        self.menuFile.addAction(self.actionexit)
        self.menuAbout.addAction(self.action11)
        self.menuAbout_2.addAction(self.actionAbout)
        self.menu.addAction(self.actionRegist_Key)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menuAbout_2.menuAction())




        #定义
        #self.action11.triggered.connect(self.openSetting)#
        self.actionRegist_Key.triggered.connect(self.openKey)#
        self.actionsave.triggered.connect(self.openAssist)#
        self.actionexit.triggered.connect(QtCore.QCoreApplication.quit)#
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "^En"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_2.setText(_translate("MainWindow", "%T"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "name"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "阿松大"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "阿斯顿撒旦"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_4.setText(_translate("MainWindow", "^En"))
        self.pushButton_6.setText(_translate("MainWindow", "%S"))
        self.menuFile.setTitle(_translate("MainWindow", "Func"))
        self.menuAbout.setTitle(_translate("MainWindow", "Setting"))
        self.menuAbout_2.setTitle(_translate("MainWindow", "About"))
        self.menu.setTitle(_translate("MainWindow", "TralV"))
        self.actionsave.setText(_translate("MainWindow", "Assist"))
        self.actionexit.setText(_translate("MainWindow", "退出"))
        self.action11.setText(_translate("MainWindow", "设置"))
        self.actionAbout.setText(_translate("MainWindow", "关于"))
        self.actionRegist_Key.setText(_translate("MainWindow", "Regist Key"))
    
    def openSetting(self):
        Setting_Dialog = QtWidgets.QDialog()
        
        #super(Setting_Dialog, self).__init__(*args, **kwargs)
        ui = Ui_Setting_Dialog()
        ui.setupUi(Setting_Dialog)
        
        #super(ui, self).__init__(*args, **kwargs)
        Setting_Dialog.show()
        Setting_Dialog.exec_()
    def openKey(self):
        KEY_Dialog = QtWidgets.QDialog()
        ui = Ui_KEY_Dialog()
        ui.setupUi(KEY_Dialog)
        KEY_Dialog.show()
        KEY_Dialog.exec_()
    def openAssist(self):
        
        
        Assist01 = MYQDialog()
        ui = Ui_Assist01()
        ui.setupUi(Assist01)
        Assist01.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Assist01.setWindowOpacity(0.7)
        
        Assist01.show()
        Assist01.exec_()


class Ui_Setting_Dialog(object):
    def setupUi(self, Setting_Dialog):
        Setting_Dialog.setObjectName("Setting_Dialog")
        Setting_Dialog.resize(398, 380)
        self.buttonBox = QtWidgets.QDialogButtonBox(Setting_Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 340, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.checkBox_2 = QtWidgets.QCheckBox(Setting_Dialog)
        self.checkBox_2.setGeometry(QtCore.QRect(30, 30, 81, 21))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox = QtWidgets.QCheckBox(Setting_Dialog)
        self.checkBox.setGeometry(QtCore.QRect(220, 10, 91, 21))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_3 = QtWidgets.QCheckBox(Setting_Dialog)
        self.checkBox_3.setGeometry(QtCore.QRect(220, 70, 81, 21))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(Setting_Dialog)
        self.checkBox_4.setGeometry(QtCore.QRect(30, 10, 121, 21))
        self.checkBox_4.setObjectName("checkBox_4")
        self.keySequenceEdit = QtWidgets.QKeySequenceEdit(Setting_Dialog)
        self.keySequenceEdit.setGeometry(QtCore.QRect(220, 40, 113, 20))
        self.keySequenceEdit.setObjectName("keySequenceEdit")
        self.keySequenceEdit_2 = QtWidgets.QKeySequenceEdit(Setting_Dialog)
        self.keySequenceEdit_2.setGeometry(QtCore.QRect(220, 100, 113, 20))
        self.keySequenceEdit_2.setObjectName("keySequenceEdit_2")
        self.checkBox_5 = QtWidgets.QCheckBox(Setting_Dialog)
        self.checkBox_5.setGeometry(QtCore.QRect(30, 100, 81, 21))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_7 = QtWidgets.QCheckBox(Setting_Dialog)
        self.checkBox_7.setGeometry(QtCore.QRect(30, 120, 121, 21))
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(Setting_Dialog)
        self.checkBox_8.setGeometry(QtCore.QRect(30, 220, 81, 21))
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QtWidgets.QCheckBox(Setting_Dialog)
        self.checkBox_9.setGeometry(QtCore.QRect(30, 240, 121, 21))
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_10 = QtWidgets.QCheckBox(Setting_Dialog)
        self.checkBox_10.setGeometry(QtCore.QRect(30, 141, 101, 21))
        self.checkBox_10.setObjectName("checkBox_10")
        self.keySequenceEdit_3 = QtWidgets.QKeySequenceEdit(Setting_Dialog)
        self.keySequenceEdit_3.setGeometry(QtCore.QRect(150, 141, 61, 21))
        self.keySequenceEdit_3.setObjectName("keySequenceEdit_3")
        self.checkBox_11 = QtWidgets.QCheckBox(Setting_Dialog)
        self.checkBox_11.setGeometry(QtCore.QRect(30, 80, 131, 21))
        self.checkBox_11.setObjectName("checkBox_11")
        self.checkBox_13 = QtWidgets.QCheckBox(Setting_Dialog)
        self.checkBox_13.setGeometry(QtCore.QRect(30, 166, 111, 21))
        self.checkBox_13.setObjectName("checkBox_13")
        self.lineEdit = QtWidgets.QLineEdit(Setting_Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(150, 166, 61, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.keySequenceEdit_4 = QtWidgets.QKeySequenceEdit(Setting_Dialog)
        self.keySequenceEdit_4.setGeometry(QtCore.QRect(150, 261, 61, 21))
        self.keySequenceEdit_4.setObjectName("keySequenceEdit_4")
        self.checkBox_14 = QtWidgets.QCheckBox(Setting_Dialog)
        self.checkBox_14.setGeometry(QtCore.QRect(30, 286, 111, 21))
        self.checkBox_14.setObjectName("checkBox_14")
        self.checkBox_12 = QtWidgets.QCheckBox(Setting_Dialog)
        self.checkBox_12.setGeometry(QtCore.QRect(30, 261, 101, 21))
        self.checkBox_12.setObjectName("checkBox_12")
        self.lineEdit_2 = QtWidgets.QLineEdit(Setting_Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 286, 61, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.checkBox_6 = QtWidgets.QCheckBox(Setting_Dialog)
        self.checkBox_6.setGeometry(QtCore.QRect(220, 130, 121, 21))
        self.checkBox_6.setObjectName("checkBox_6")

        self.retranslateUi(Setting_Dialog)
        self.buttonBox.accepted.connect(Setting_Dialog.accept)
        self.buttonBox.rejected.connect(Setting_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Setting_Dialog)

    def retranslateUi(self, Setting_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Setting_Dialog.setWindowTitle(_translate("Setting_Dialog", "Setting"))
        self.checkBox_2.setText(_translate("Setting_Dialog", "开机自启"))
        self.checkBox.setText(_translate("Setting_Dialog", "呼出快捷键"))
        self.checkBox_3.setText(_translate("Setting_Dialog", "中止快捷键"))
        self.checkBox_4.setText(_translate("Setting_Dialog", "主窗口保持最前"))
        self.checkBox_5.setText(_translate("Setting_Dialog", "辅助窗口2"))
        self.checkBox_7.setText(_translate("Setting_Dialog", "辅助窗口2保持最前"))
        self.checkBox_8.setText(_translate("Setting_Dialog", "辅助窗口3"))
        self.checkBox_9.setText(_translate("Setting_Dialog", "辅助窗口3保持最前"))
        self.checkBox_10.setText(_translate("Setting_Dialog", "辅助窗口2呼出"))
        self.checkBox_11.setText(_translate("Setting_Dialog", "辅助窗口2 assist"))
        self.checkBox_13.setText(_translate("Setting_Dialog", "辅助窗口2透明度"))
        self.checkBox_14.setText(_translate("Setting_Dialog", "辅助窗口3透明度"))
        self.checkBox_12.setText(_translate("Setting_Dialog", "辅助窗口3呼出"))
        self.checkBox_6.setText(_translate("Setting_Dialog", "记忆关闭位置"))







class Ui_Assist01(object):
    
    def setupUi(self, Assist01):
        #super().__init__(Assist01)
        Assist01.setObjectName("Assist01")
        Assist01.resize(504, 303)
        #Assist01.mouseMoveEvent = self.MY_mouseMoveEvent
        #Assist01.mousePressEvent = self.MY_mousePressEvent
        #Assist01.mouseReleaseEvent = self.MY_mouseReleaseEvent

        self.buttonBox = QtWidgets.QDialogButtonBox(Assist01)
        self.buttonBox.setGeometry(QtCore.QRect(460, 10, 31, 61))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.frame = QtWidgets.QFrame(Assist01)
        self.frame.setGeometry(QtCore.QRect(10, 10, 431, 281))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(110, 0, 61, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(110, 130, 61, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(10, 150, 61, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(10, 110, 61, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(10, 130, 61, 16))
        self.label_7.setObjectName("label_7")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(258, 0, 20, 261))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 0, 61, 16))
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(92, 0, 20, 261))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(280, 0, 71, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(280, 130, 71, 16))
        self.label_9.setObjectName("label_9")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser.setGeometry(QtCore.QRect(270, 20, 161, 111))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser_2.setGeometry(QtCore.QRect(270, 150, 161, 111))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser_3.setGeometry(QtCore.QRect(104, 150, 161, 111))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser_4.setGeometry(QtCore.QRect(104, 20, 161, 111))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(10, 260, 61, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(10, 240, 61, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(10, 170, 61, 16))
        self.label_12.setObjectName("label_12")
        self.frame.raise_()
        self.buttonBox.raise_()

        self.retranslateUi(Assist01)
        self.buttonBox.accepted.connect(Assist01.accept)
        self.buttonBox.rejected.connect(Assist01.reject)




        QtCore.QMetaObject.connectSlotsByName(Assist01)
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    def retranslateUi(self, Assist01):
        _translate = QtCore.QCoreApplication.translate
        Assist01.setWindowTitle(_translate("Assist01", "Assist"))
        self.label_3.setText(_translate("Assist01", "异常检验"))
        self.label_4.setText(_translate("Assist01", "建议处置"))
        self.label_5.setText(_translate("Assist01", "病人："))
        self.label_6.setText(_translate("Assist01", "已入院"))
        self.label_7.setText(_translate("Assist01", "已术后"))
        self.label_2.setText(_translate("Assist01", "术式"))
        self.label.setText(_translate("Assist01", "确定诊断"))
        self.label_8.setText(_translate("Assist01", "分级、分度"))
        self.label_9.setText(_translate("Assist01", "临床路径"))
        self.label_10.setText(_translate("Assist01", "执行状态"))
        self.label_11.setText(_translate("Assist01", "轮询行"))
        self.label_12.setText(_translate("Assist01", "病程状态"))

    
    




class Ui_KEY_Dialog(object):
    def setupUi(self, KEY_Dialog):
        KEY_Dialog.setObjectName("KEY_Dialog")
        KEY_Dialog.resize(400, 155)
        self.buttonBox = QtWidgets.QDialogButtonBox(KEY_Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 110, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(KEY_Dialog)
        self.label.setGeometry(QtCore.QRect(60, 20, 54, 12))
        self.label.setObjectName("label")
        self.end_date = QtWidgets.QLabel(KEY_Dialog)
        self.end_date.setGeometry(QtCore.QRect(130, 20, 54, 12))
        self.end_date.setObjectName("end_date")

        self.retranslateUi(KEY_Dialog)
        self.buttonBox.accepted.connect(KEY_Dialog.accept)
        self.buttonBox.rejected.connect(KEY_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(KEY_Dialog)

    def retranslateUi(self, KEY_Dialog):
        _translate = QtCore.QCoreApplication.translate
        KEY_Dialog.setWindowTitle(_translate("KEY_Dialog", "KEY"))
        self.label.setText(_translate("KEY_Dialog", "到期日："))
        self.end_date.setText(_translate("KEY_Dialog", "TextLabel"))