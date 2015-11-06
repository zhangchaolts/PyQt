#coding:gbk
import sys
import time,datetime
from PyQt4 import QtCore, QtGui
from p2p_sign_ui import Ui_Form
import gujinsuo
import yourongwang
import huirendai
import minxindai
import jinronggongchang

# 有融网签到线程类
class YourongwangThread(QtCore.QThread):

    signal_yrw = QtCore.pyqtSignal(int, str)
    signal_finished_yrw = QtCore.pyqtSignal()
    
    def __init__(self,parent=None):
        QtCore.QThread.__init__(self, parent)
        self.usernameList = None
        self.passwordList = None
        
    def setAccountList(self, accountList):
        self.accountList = accountList
    
    def run(self):
        line_ptr = 0
        for [username,password] in self.accountList:
            self.signal_yrw.emit(line_ptr, '签到中...'.decode('gbk'))
            status = yourongwang.sign(username, password)
            status = status.decode('gbk')
            self.signal_yrw.emit(line_ptr, status)
            line_ptr += 1
        self.signal_finished_yrw.emit()

# 固金所签到线程类
class GujinsuoThread(QtCore.QThread):

    signal_gjs = QtCore.pyqtSignal(int, str)
    signal_finished_gjs = QtCore.pyqtSignal()
    
    def __init__(self,parent=None):
        QtCore.QThread.__init__(self, parent)
        self.usernameList = None
        self.passwordList = None
        
    def setAccountList(self, accountList):
        self.accountList = accountList
    
    def run(self):
        line_ptr = 0
        for [username,password] in self.accountList:
            self.signal_gjs.emit(line_ptr, '签到中...'.decode('gbk'))
            status = gujinsuo.sign(username, password)
            status = status.decode('gbk')
            self.signal_gjs.emit(line_ptr, status)
            line_ptr += 1
        self.signal_finished_gjs.emit()

# 惠人贷签到线程类
class HuirendaiThread(QtCore.QThread):

    signal_hrd = QtCore.pyqtSignal(int, str)
    signal_finished_hrd = QtCore.pyqtSignal()
    
    def __init__(self,parent=None):
        QtCore.QThread.__init__(self, parent)
        self.usernameList = None
        self.passwordList = None
        
    def setAccountList(self, accountList):
        self.accountList = accountList
    
    def run(self):
        line_ptr = 0
        for [username,password] in self.accountList:
            self.signal_hrd.emit(line_ptr, '签到中...'.decode('gbk'))
            status = huirendai.sign(username, password)
            status = status.decode('gbk')
            self.signal_hrd.emit(line_ptr, status)
            line_ptr += 1
        self.signal_finished_hrd.emit()

# 金融工场签到线程类
class JinronggongchangThread(QtCore.QThread):

    signal_jrgc = QtCore.pyqtSignal(int, str)
    signal_finished_jrgc = QtCore.pyqtSignal()
    
    def __init__(self,parent=None):
        QtCore.QThread.__init__(self, parent)
        self.usernameList = None
        self.passwordList = None
        
    def setAccountList(self, accountList):
        self.accountList = accountList
    
    def run(self):
        line_ptr = 0
        for [username,password] in self.accountList:
            self.signal_jrgc.emit(line_ptr, '签到中...'.decode('gbk'))
            status = jinronggongchang.sign(username, password)
            status = status.decode('gbk')
            self.signal_jrgc.emit(line_ptr, status)
            line_ptr += 1
        self.signal_finished_jrgc.emit()

# 民信贷签到线程类
class MinxindaiThread(QtCore.QThread):

    signal_mxd = QtCore.pyqtSignal(int, str)
    signal_finished_mxd = QtCore.pyqtSignal()
    
    def __init__(self,parent=None):
        QtCore.QThread.__init__(self, parent)
        self.usernameList = None
        self.passwordList = None
        
    def setAccountList(self, accountList):
        self.accountList = accountList
    
    def run(self):
        line_ptr = 0
        for [username,password] in self.accountList:
            self.signal_mxd.emit(line_ptr, '签到中...'.decode('gbk'))
            status = minxindai.sign(username, password)
            status = status.decode('gbk')
            self.signal_mxd.emit(line_ptr, status)
            line_ptr += 1
        self.signal_finished_mxd.emit()

# 主框架
class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
 
        # 有融网账号密码加载
        self.ui.treeWidget_yrw.setColumnWidth(0,150)
        self.ui.treeWidget_yrw.setColumnWidth(1,120)
        self.ui.treeWidget_yrw.setColumnWidth(2,350)

        for line in file("有融网账号密码.txt"):
            line = line.strip()
            parts = line.split(" ")
            if len(parts) == 2:
                a = QtGui.QTreeWidgetItem(self.ui.treeWidget_yrw)
                a.setText(0, parts[0])
                a.setText(1, parts[1])

        # 固金所账号密码加载
        self.ui.treeWidget_gjs.setColumnWidth(0,150)
        self.ui.treeWidget_gjs.setColumnWidth(1,120)
        self.ui.treeWidget_gjs.setColumnWidth(2,350)
        
        for line in file("固金所账号密码.txt"):
            line = line.strip()
            parts = line.split(" ")
            if len(parts) == 2:
                a = QtGui.QTreeWidgetItem(self.ui.treeWidget_gjs)
                a.setText(0, parts[0])
                a.setText(1, parts[1])

        # 惠人贷账号密码加载
        self.ui.treeWidget_hrd.setColumnWidth(0,150)
        self.ui.treeWidget_hrd.setColumnWidth(1,120)
        self.ui.treeWidget_hrd.setColumnWidth(2,350)

        for line in file("惠人贷账号密码.txt"):
            line = line.strip()
            parts = line.split(" ")
            if len(parts) == 2:
                a = QtGui.QTreeWidgetItem(self.ui.treeWidget_hrd)
                a.setText(0, parts[0])
                a.setText(1, parts[1])

        # 金融工场账号密码加载
        self.ui.treeWidget_jrgc.setColumnWidth(0,150)
        self.ui.treeWidget_jrgc.setColumnWidth(1,120)
        self.ui.treeWidget_jrgc.setColumnWidth(2,350)

        for line in file("金融工场账号密码.txt"):
            line = line.strip()
            parts = line.split(" ")
            if len(parts) == 2:
                a = QtGui.QTreeWidgetItem(self.ui.treeWidget_jrgc)
                a.setText(0, parts[0])
                a.setText(1, parts[1])

        # 民信贷账号密码加载
        self.ui.treeWidget_mxd.setColumnWidth(0,150)
        self.ui.treeWidget_mxd.setColumnWidth(1,120)
        self.ui.treeWidget_mxd.setColumnWidth(2,350)

        for line in file("民信贷账号密码.txt"):
            line = line.strip()
            parts = line.split(" ")
            if len(parts) == 2:
                a = QtGui.QTreeWidgetItem(self.ui.treeWidget_mxd)
                a.setText(0, parts[0])
                a.setText(1, parts[1])

        # 连接
        QtCore.QObject.connect(self.ui.pushButton_gjs, QtCore.SIGNAL("clicked()"), self.exec_sign_gjs) 
        QtCore.QObject.connect(self.ui.pushButton_yrw, QtCore.SIGNAL("clicked()"), self.exec_sign_yrw)
        QtCore.QObject.connect(self.ui.pushButton_hrd, QtCore.SIGNAL("clicked()"), self.exec_sign_hrd)
        QtCore.QObject.connect(self.ui.pushButton_jrgc, QtCore.SIGNAL("clicked()"), self.exec_sign_jrgc)
        QtCore.QObject.connect(self.ui.pushButton_mxd, QtCore.SIGNAL("clicked()"), self.exec_sign_mxd)

        # 判断程序是否过期
        timestamp_now_date = time.mktime(datetime.datetime.now().timetuple())
        timestamp_expired_date = time.mktime(datetime.datetime.strptime("2015-12-01 00:00:00", '%Y-%m-%d %H:%M:%S').timetuple())
        if timestamp_now_date >= timestamp_expired_date:
            self.ui.pushButton_yrw.setEnabled(False)
            self.ui.pushButton_gjs.setEnabled(False)
            self.ui.pushButton_hrd.setEnabled(False)
            self.ui.pushButton_jrgc.setEnabled(False)
            self.ui.pushButton_mxd.setEnabled(False)
            self.ui.label_yrw.setText("程序已经过期，请到群共享中下载！".decode('gbk'))
            self.ui.label_gjs.setText("程序已经过期，请到群共享中下载！".decode('gbk'))
            self.ui.label_hrd.setText("程序已经过期，请到群共享中下载！".decode('gbk'))
            self.ui.label_jrgc.setText("程序已经过期，请到群共享中下载！".decode('gbk'))
            self.ui.label_mxd.setText("程序已经过期，请到群共享中下载！".decode('gbk'))

    # 有融网签到    
    def exec_sign_yrw(self):
        self.ui.pushButton_yrw.setText("签到中...".decode('gbk'))
        self.ui.pushButton_yrw.setEnabled(False)
        self.ui.treeWidget_yrw.repaint()
        accountList = []
        it = QtGui.QTreeWidgetItemIterator(self.ui.treeWidget_yrw)
        while it.value():
            accountList.append([it.value().text(0), it.value().text(1)])
            it += 1
        self.thread_yrw = YourongwangThread()
        self.thread_yrw.setAccountList(accountList)
        self.thread_yrw.signal_yrw.connect(self.add_status_for_yrw)
        self.thread_yrw.signal_finished_yrw.connect(self.change_button_yrw)
        self.thread_yrw.start()

    def add_status_for_yrw(self, line_ptr, status):
        ptr = 0
        it = QtGui.QTreeWidgetItemIterator(self.ui.treeWidget_yrw)
        while it.value():
            if ptr == line_ptr:
                it.value().setText(2, status)
            ptr += 1
            it += 1

    def change_button_yrw(self):
        self.ui.pushButton_yrw.setText("签到完毕".decode('gbk'))
        
    # 固金所签到
    def exec_sign_gjs(self):
        self.ui.pushButton_gjs.setText("签到中...".decode('gbk'))
        self.ui.pushButton_gjs.setEnabled(False)
        self.ui.treeWidget_gjs.repaint()
        accountList = []
        it = QtGui.QTreeWidgetItemIterator(self.ui.treeWidget_gjs)
        while it.value():
            accountList.append([it.value().text(0), it.value().text(1)])
            it += 1
        self.thread_gjs = GujinsuoThread()
        self.thread_gjs.setAccountList(accountList)
        self.thread_gjs.signal_gjs.connect(self.add_status_for_gjs)
        self.thread_gjs.signal_finished_gjs.connect(self.change_button_gjs)
        self.thread_gjs.start()

    def add_status_for_gjs(self, line_ptr, status):
        ptr = 0
        it = QtGui.QTreeWidgetItemIterator(self.ui.treeWidget_gjs)
        while it.value():
            if ptr == line_ptr:
                it.value().setText(2, status)
            ptr += 1
            it += 1

    def change_button_gjs(self):
        self.ui.pushButton_gjs.setText("签到完毕".decode('gbk'))
            
    # 惠人贷签到      
    def exec_sign_hrd(self):
        self.ui.pushButton_hrd.setText("签到中...".decode('gbk'))
        self.ui.pushButton_hrd.setEnabled(False)
        self.ui.treeWidget_hrd.repaint()
        accountList = []
        it = QtGui.QTreeWidgetItemIterator(self.ui.treeWidget_hrd)
        while it.value():
            accountList.append([it.value().text(0), it.value().text(1)])
            it += 1
        self.thread_hrd = HuirendaiThread()
        self.thread_hrd.setAccountList(accountList)
        self.thread_hrd.signal_hrd.connect(self.add_status_for_hrd)
        self.thread_hrd.signal_finished_hrd.connect(self.change_button_hrd)
        self.thread_hrd.start()

    def add_status_for_hrd(self, line_ptr, status):
        ptr = 0
        it = QtGui.QTreeWidgetItemIterator(self.ui.treeWidget_hrd)
        while it.value():
            if ptr == line_ptr:
                it.value().setText(2, status)
            ptr += 1
            it += 1

    def change_button_hrd(self):
        self.ui.pushButton_hrd.setText("签到完毕".decode('gbk'))

    # 金融工场签到     
    def exec_sign_jrgc(self):
        self.ui.pushButton_jrgc.setText("签到中...".decode('gbk'))
        self.ui.pushButton_jrgc.setEnabled(False)
        self.ui.treeWidget_jrgc.repaint()
        accountList = []
        it = QtGui.QTreeWidgetItemIterator(self.ui.treeWidget_jrgc)
        while it.value():
            accountList.append([it.value().text(0), it.value().text(1)])
            it += 1
        self.thread_jrgc = JinronggongchangThread()
        self.thread_jrgc.setAccountList(accountList)
        self.thread_jrgc.signal_jrgc.connect(self.add_status_for_jrgc)
        self.thread_jrgc.signal_finished_jrgc.connect(self.change_button_jrgc)
        self.thread_jrgc.start()

    def add_status_for_jrgc(self, line_ptr, status):
        ptr = 0
        it = QtGui.QTreeWidgetItemIterator(self.ui.treeWidget_jrgc)
        while it.value():
            if ptr == line_ptr:
                it.value().setText(2, status)
            ptr += 1
            it += 1

    def change_button_jrgc(self):
        self.ui.pushButton_jrgc.setText("签到完毕".decode('gbk'))

    # 民信贷签到
    def exec_sign_mxd(self):
        self.ui.pushButton_mxd.setText("签到中...".decode('gbk'))
        self.ui.pushButton_mxd.setEnabled(False)
        self.ui.treeWidget_mxd.repaint()
        accountList = []
        it = QtGui.QTreeWidgetItemIterator(self.ui.treeWidget_mxd)
        while it.value():
            accountList.append([it.value().text(0), it.value().text(1)])
            it += 1
        self.thread_mxd = MinxindaiThread()
        self.thread_mxd.setAccountList(accountList)
        self.thread_mxd.signal_mxd.connect(self.add_status_for_mxd)
        self.thread_mxd.signal_finished_mxd.connect(self.change_button_mxd)
        self.thread_mxd.start()

    def add_status_for_mxd(self, line_ptr, status):
        ptr = 0
        it = QtGui.QTreeWidgetItemIterator(self.ui.treeWidget_mxd)
        while it.value():
            if ptr == line_ptr:
                it.value().setText(2, status)
            ptr += 1
            it += 1
        
    def change_button_mxd(self):
        self.ui.pushButton_mxd.setText("签到完毕".decode('gbk'))

# 主函数    
if __name__ == "__main__":

    reload(sys)
    sys.setdefaultencoding("gbk")
    
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())


