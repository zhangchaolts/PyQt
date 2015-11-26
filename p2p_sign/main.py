#coding:gbk
import sys
import time,datetime
from PyQt4 import QtCore, QtGui
from p2p_sign_ui import Ui_Form
import gujinsuo
import yourongwang
import dangtianjinrong
import huirendai
import minxindai
import jinronggongchang
import wangxinlicai_bid
import multiprocessing

# 当天金融签到线程类
class DangtianjinrongThread(QtCore.QThread):

    signal_dtjr = QtCore.pyqtSignal(int, str)
    signal_finished_dtjr = QtCore.pyqtSignal()
    
    def __init__(self,parent=None):
        QtCore.QThread.__init__(self, parent)
        
    def setAccountList(self, accountList):
        self.accountList = accountList
    
    def run(self):
        for i in xrange(len(self.accountList)):
            self.signal_dtjr.emit(i, '签到中...'.decode('gbk'))
        status_list = dangtianjinrong.sign_all(self.accountList)
        for i in xrange(len(status_list)):
            self.signal_dtjr.emit(i, status_list[i].decode('gbk'))
        self.signal_finished_dtjr.emit()

# 固金所签到线程类
class GujinsuoThread(QtCore.QThread):

    signal_gjs = QtCore.pyqtSignal(int, str)
    signal_finished_gjs = QtCore.pyqtSignal()
    
    def __init__(self,parent=None):
        QtCore.QThread.__init__(self, parent)
        
    def setAccountList(self, accountList):
        self.accountList = accountList
    
    def run(self):
        for i in xrange(len(self.accountList)):
            self.signal_gjs.emit(i, '签到中...'.decode('gbk'))
        status_list = gujinsuo.sign_all(self.accountList)
        for i in xrange(len(status_list)):
            self.signal_gjs.emit(i, status_list[i].decode('gbk'))
        self.signal_finished_gjs.emit()

# 有融网签到线程类
class YourongwangThread(QtCore.QThread):

    signal_yrw = QtCore.pyqtSignal(int, str)
    signal_finished_yrw = QtCore.pyqtSignal()
    
    def __init__(self,parent=None):
        QtCore.QThread.__init__(self, parent)
        
    def setAccountList(self, accountList):
        self.accountList = accountList
    
    def run(self):
        for i in xrange(len(self.accountList)):
            self.signal_yrw.emit(i, '签到中...'.decode('gbk'))
        status_list = yourongwang.sign_all(self.accountList)
        for i in xrange(len(status_list)):
            self.signal_yrw.emit(i, status_list[i].decode('gbk'))
        self.signal_finished_yrw.emit()

# 金融工场签到线程类
class JinronggongchangThread(QtCore.QThread):

    signal_jrgc = QtCore.pyqtSignal(int, str)
    signal_finished_jrgc = QtCore.pyqtSignal()
    
    def __init__(self,parent=None):
        QtCore.QThread.__init__(self, parent)
        
    def setAccountList(self, accountList):
        self.accountList = accountList
    
    def run(self):
        for i in xrange(len(self.accountList)):
            self.signal_jrgc.emit(i, '签到中...'.decode('gbk'))
        status_list = jinronggongchang.sign_all(self.accountList)
        for i in xrange(len(status_list)):
            self.signal_jrgc.emit(i, status_list[i].decode('gbk'))
        self.signal_finished_jrgc.emit()

# 民信贷签到线程类
class MinxindaiThread(QtCore.QThread):

    signal_mxd = QtCore.pyqtSignal(int, str)
    signal_finished_mxd = QtCore.pyqtSignal()
    
    def __init__(self,parent=None):
        QtCore.QThread.__init__(self, parent)
        
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

# 网信理财签到线程类
class WangxinlicaiThread(QtCore.QThread):

    signal_wxlc = QtCore.pyqtSignal(int, str)
    signal_finished_wxlc = QtCore.pyqtSignal()
    
    def __init__(self,parent=None):
        QtCore.QThread.__init__(self, parent)
        
    def setAccountList(self, accountList):
        self.accountList = accountList

    def setInvestDaysIsShuhui(self, investDays, isShuhui):
        self.investDays = investDays
        self.isShuhui = isShuhui
    
    def run(self):
        line_ptr = 0
        for [username,password] in self.accountList:
            self.signal_wxlc.emit(line_ptr, '进行中...'.decode('gbk'))
            status = wangxinlicai_bid.bid(username, password, self.investDays, self.isShuhui)
            status = status.decode('gbk')
            self.signal_wxlc.emit(line_ptr, status)
            line_ptr += 1
        self.signal_finished_wxlc.emit()

# 主框架
class MyForm(QtGui.QMainWindow):

    account_list_yrw = []
    account_list_gjs = []
    account_list_dtjr = []
    account_list_hrd = []
    account_list_jrgc = []
    account_list_mxd = []
    
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.account_list_dtjr = self.read_account("当天金融账号密码.txt")
        self.account_list_gjs = self.read_account("固金所账号密码.txt")
        self.account_list_yrw = self.read_account("有融网账号密码.txt")      
        self.account_list_jrgc = self.read_account("金融工场账号密码.txt")
        self.account_list_mxd = self.read_account("民信贷账号密码.txt")
        self.account_list_wxlc = self.read_account("网信理财账号密码.txt")

        # 当天金融账号密码加载
        self.ui.treeWidget_dtjr.setColumnWidth(0,150)
        self.ui.treeWidget_dtjr.setColumnWidth(1,120)
        self.ui.treeWidget_dtjr.setColumnWidth(2,350)
        for account in self.account_list_dtjr:
            a = QtGui.QTreeWidgetItem(self.ui.treeWidget_dtjr)
            a.setText(0, account[0])
            a.setText(1, account[1][0]+"*******")
            
        # 固金所账号密码加载
        self.ui.treeWidget_gjs.setColumnWidth(0,150)
        self.ui.treeWidget_gjs.setColumnWidth(1,120)
        self.ui.treeWidget_gjs.setColumnWidth(2,350)
        for account in self.account_list_gjs:
            a = QtGui.QTreeWidgetItem(self.ui.treeWidget_gjs)
            a.setText(0, account[0])
            a.setText(1, account[1][0]+"*******")
            
        # 有融网账号密码加载
        self.ui.treeWidget_yrw.setColumnWidth(0,150)
        self.ui.treeWidget_yrw.setColumnWidth(1,120)
        self.ui.treeWidget_yrw.setColumnWidth(2,350)
        for account in self.account_list_yrw:
            a = QtGui.QTreeWidgetItem(self.ui.treeWidget_yrw)
            a.setText(0, account[0])
            a.setText(1, account[1][0]+"*******")

        # 金融工场账号密码加载
        self.ui.treeWidget_jrgc.setColumnWidth(0,150)
        self.ui.treeWidget_jrgc.setColumnWidth(1,120)
        self.ui.treeWidget_jrgc.setColumnWidth(2,350)
        for account in self.account_list_jrgc:
            a = QtGui.QTreeWidgetItem(self.ui.treeWidget_jrgc)
            a.setText(0, account[0])
            a.setText(1, account[1][0]+"*******")

        # 民信贷账号密码加载
        self.ui.treeWidget_mxd.setColumnWidth(0,150)
        self.ui.treeWidget_mxd.setColumnWidth(1,120)
        self.ui.treeWidget_mxd.setColumnWidth(2,350)
        for account in self.account_list_mxd:
            a = QtGui.QTreeWidgetItem(self.ui.treeWidget_mxd)
            a.setText(0, account[0])
            a.setText(1, account[1][0]+"*******")

        # 网信理财账号密码加载
        self.ui.treeWidget_wxlc.setColumnWidth(0,150)
        self.ui.treeWidget_wxlc.setColumnWidth(1,120)
        self.ui.treeWidget_wxlc.setColumnWidth(2,350)
        for account in self.account_list_wxlc:
            a = QtGui.QTreeWidgetItem(self.ui.treeWidget_wxlc)
            a.setText(0, account[0])
            a.setText(1, account[1][0]+"*******")

        # 连接
        QtCore.QObject.connect(self.ui.pushButton_dtjr, QtCore.SIGNAL("clicked()"), self.exec_sign_dtjr)
        QtCore.QObject.connect(self.ui.pushButton_gjs, QtCore.SIGNAL("clicked()"), self.exec_sign_gjs)
        QtCore.QObject.connect(self.ui.pushButton_yrw, QtCore.SIGNAL("clicked()"), self.exec_sign_yrw)
        QtCore.QObject.connect(self.ui.pushButton_jrgc, QtCore.SIGNAL("clicked()"), self.exec_sign_jrgc)
        QtCore.QObject.connect(self.ui.pushButton_mxd, QtCore.SIGNAL("clicked()"), self.exec_sign_mxd)
        QtCore.QObject.connect(self.ui.pushButton_wxlc_7, QtCore.SIGNAL("clicked()"), self.exec_sign_wxlc_7)
        QtCore.QObject.connect(self.ui.pushButton_wxlc_10, QtCore.SIGNAL("clicked()"), self.exec_sign_wxlc_10)
        QtCore.QObject.connect(self.ui.pushButton_wxlc_15, QtCore.SIGNAL("clicked()"), self.exec_sign_wxlc_15)
        QtCore.QObject.connect(self.ui.pushButton_wxlc_30, QtCore.SIGNAL("clicked()"), self.exec_sign_wxlc_30)
        QtCore.QObject.connect(self.ui.pushButton_wxlc_shuhui, QtCore.SIGNAL("clicked()"), self.exec_sign_wxlc_shuhui)

        # 判断程序是否过期
        timestamp_now_date = time.mktime(datetime.datetime.now().timetuple())
        timestamp_expired_date = time.mktime(datetime.datetime.strptime("2015-12-01 00:00:00", '%Y-%m-%d %H:%M:%S').timetuple())
        if timestamp_now_date >= timestamp_expired_date:
            self.ui.pushButton_dtjr.setEnabled(False)
            self.ui.pushButton_gjs.setEnabled(False)
            self.ui.pushButton_yrw.setEnabled(False)
            self.ui.pushButton_jrgc.setEnabled(False)
            self.ui.pushButton_mxd.setEnabled(False)
            self.ui.pushButton_wxlc_7.setEnabled(False)
            self.ui.pushButton_wxlc_10.setEnabled(False)
            self.ui.pushButton_wxlc_15.setEnabled(False)
            self.ui.pushButton_wxlc_30.setEnabled(False)
            self.ui.pushButton_wxlc_shuhui.setEnabled(False)
            self.ui.label_dtjr.setText("程序已经过期，请到群共享中下载！".decode('gbk'))
            self.ui.label_gjs.setText("程序已经过期，请到群共享中下载！".decode('gbk'))
            self.ui.label_yrw.setText("程序已经过期，请到群共享中下载！".decode('gbk'))   
            self.ui.label_jrgc.setText("程序已经过期，请到群共享中下载！".decode('gbk'))
            self.ui.label_mxd.setText("程序已经过期，请到群共享中下载！".decode('gbk'))

    # 读取账号密码函数
    def read_account(self, filename):
        list = []
        for line in file(filename):
            line = line.strip()
            parts = line.split(" ")
            if len(parts) == 2:
                list.append([parts[0], parts[1]])
        return list

    # 当天金融签到
    def exec_sign_dtjr(self):
        self.ui.pushButton_dtjr.setText("签到中...".decode('gbk'))
        self.ui.pushButton_dtjr.setEnabled(False)
        self.ui.treeWidget_dtjr.repaint()
        self.thread_dtjr = DangtianjinrongThread()
        self.thread_dtjr.setAccountList(self.account_list_dtjr)
        self.thread_dtjr.signal_dtjr.connect(self.add_status_for_dtjr)
        self.thread_dtjr.signal_finished_dtjr.connect(self.change_button_dtjr)
        self.thread_dtjr.start()

    def add_status_for_dtjr(self, line_ptr, status):
        ptr = 0
        it = QtGui.QTreeWidgetItemIterator(self.ui.treeWidget_dtjr)
        while it.value():
            if ptr == line_ptr:
                it.value().setText(2, status)
            ptr += 1
            it += 1

    def change_button_dtjr(self):
        self.ui.pushButton_dtjr.setText("签到完毕".decode('gbk'))
        
    # 固金所签到
    def exec_sign_gjs(self):
        self.ui.pushButton_gjs.setText("签到中...".decode('gbk'))
        self.ui.pushButton_gjs.setEnabled(False)
        self.ui.treeWidget_gjs.repaint()
        self.thread_gjs = GujinsuoThread()
        self.thread_gjs.setAccountList(self.account_list_gjs)
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
        
    # 有融网签到    
    def exec_sign_yrw(self):
        self.ui.pushButton_yrw.setText("签到中...".decode('gbk'))
        self.ui.pushButton_yrw.setEnabled(False)
        self.ui.treeWidget_yrw.repaint()
        self.thread_yrw = YourongwangThread()
        self.thread_yrw.setAccountList(self.account_list_yrw)
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
        
    # 金融工场签到     
    def exec_sign_jrgc(self):
        self.ui.pushButton_jrgc.setText("签到中...".decode('gbk'))
        self.ui.pushButton_jrgc.setEnabled(False)
        self.ui.treeWidget_jrgc.repaint()
        self.thread_jrgc = JinronggongchangThread()
        self.thread_jrgc.setAccountList(self.account_list_jrgc)
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
        self.thread_mxd = MinxindaiThread()
        self.thread_mxd.setAccountList(self.account_list_mxd)
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

    # 网信理财投标
    def exec_sign_wxlc_7(self):
        self.change_all_button_status_wxlc(False)
        self.ui.treeWidget_wxlc.repaint()
        investDays = 7
        isShuhui = 'no'
        self.exec_sign_wxlc(investDays, isShuhui)

    def exec_sign_wxlc_10(self):
        self.change_all_button_status_wxlc(False)
        self.ui.treeWidget_wxlc.repaint()
        investDays = 10
        isShuhui = 'no'
        self.exec_sign_wxlc(investDays, isShuhui)

    def exec_sign_wxlc_15(self):
        self.change_all_button_status_wxlc(False)
        self.ui.treeWidget_wxlc.repaint()
        investDays = 15
        isShuhui = 'no'
        self.exec_sign_wxlc(investDays, isShuhui)

    def exec_sign_wxlc_30(self):
        self.change_all_button_status_wxlc(False)
        self.ui.treeWidget_wxlc.repaint()
        investDays = 30
        isShuhui = 'no'
        self.exec_sign_wxlc(investDays, isShuhui)

    def exec_sign_wxlc_shuhui(self):
        self.change_all_button_status_wxlc(False)
        self.ui.treeWidget_wxlc.repaint()
        investDays = 0
        isShuhui = 'yes'
        self.exec_sign_wxlc(investDays, isShuhui)

    def change_all_button_status_wxlc(self, status):
        self.ui.pushButton_wxlc_7.setEnabled(status)
        self.ui.pushButton_wxlc_10.setEnabled(status)
        self.ui.pushButton_wxlc_15.setEnabled(status)
        self.ui.pushButton_wxlc_30.setEnabled(status)
        self.ui.pushButton_wxlc_shuhui.setEnabled(status)
        if status == False:
            self.clear_status_for_wxlc()

    def exec_sign_wxlc(self, investDays, isShuhui):
        self.thread_wxlc = WangxinlicaiThread()
        self.thread_wxlc.setAccountList(self.account_list_wxlc)
        self.thread_wxlc.setInvestDaysIsShuhui(investDays, isShuhui)
        self.thread_wxlc.signal_wxlc.connect(self.add_status_for_wxlc)
        self.thread_wxlc.signal_finished_wxlc.connect(self.change_button_wxlc)
        self.thread_wxlc.start()

    def add_status_for_wxlc(self, line_ptr, status):
        ptr = 0
        it = QtGui.QTreeWidgetItemIterator(self.ui.treeWidget_wxlc)
        while it.value():
            if ptr == line_ptr:
                it.value().setText(2, status)
            ptr += 1
            it += 1
            
    def clear_status_for_wxlc(self):
        it = QtGui.QTreeWidgetItemIterator(self.ui.treeWidget_wxlc)
        while it.value():
            it.value().setText(2, '')
            it += 1
  
    def change_button_wxlc(self):
        self.change_all_button_status_wxlc(True)
      

# 主函数    
if __name__ == "__main__":

    reload(sys)
    sys.setdefaultencoding("gbk")

    multiprocessing.freeze_support()

    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())


