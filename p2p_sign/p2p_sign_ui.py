# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'p2p_sign.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(721, 351)
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 701, 341))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_dtjr = QtGui.QWidget()
        self.tab_dtjr.setObjectName(_fromUtf8("tab_dtjr"))
        self.pushButton_dtjr = QtGui.QPushButton(self.tab_dtjr)
        self.pushButton_dtjr.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.pushButton_dtjr.setObjectName(_fromUtf8("pushButton_dtjr"))
        self.treeWidget_dtjr = QtGui.QTreeWidget(self.tab_dtjr)
        self.treeWidget_dtjr.setGeometry(QtCore.QRect(10, 40, 681, 271))
        self.treeWidget_dtjr.setObjectName(_fromUtf8("treeWidget_dtjr"))
        self.label_dtjr = QtGui.QLabel(self.tab_dtjr)
        self.label_dtjr.setGeometry(QtCore.QRect(140, 10, 431, 20))
        self.label_dtjr.setText(_fromUtf8(""))
        self.label_dtjr.setObjectName(_fromUtf8("label_dtjr"))
        self.tabWidget.addTab(self.tab_dtjr, _fromUtf8(""))
        self.tab_gjs = QtGui.QWidget()
        self.tab_gjs.setObjectName(_fromUtf8("tab_gjs"))
        self.pushButton_gjs = QtGui.QPushButton(self.tab_gjs)
        self.pushButton_gjs.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.pushButton_gjs.setObjectName(_fromUtf8("pushButton_gjs"))
        self.treeWidget_gjs = QtGui.QTreeWidget(self.tab_gjs)
        self.treeWidget_gjs.setGeometry(QtCore.QRect(10, 40, 681, 271))
        self.treeWidget_gjs.setObjectName(_fromUtf8("treeWidget_gjs"))
        self.label_gjs = QtGui.QLabel(self.tab_gjs)
        self.label_gjs.setGeometry(QtCore.QRect(140, 10, 431, 20))
        self.label_gjs.setText(_fromUtf8(""))
        self.label_gjs.setObjectName(_fromUtf8("label_gjs"))
        self.tabWidget.addTab(self.tab_gjs, _fromUtf8(""))
        self.tab_yrw = QtGui.QWidget()
        self.tab_yrw.setObjectName(_fromUtf8("tab_yrw"))
        self.treeWidget_yrw = QtGui.QTreeWidget(self.tab_yrw)
        self.treeWidget_yrw.setGeometry(QtCore.QRect(10, 40, 681, 271))
        self.treeWidget_yrw.setObjectName(_fromUtf8("treeWidget_yrw"))
        self.pushButton_yrw = QtGui.QPushButton(self.tab_yrw)
        self.pushButton_yrw.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.pushButton_yrw.setObjectName(_fromUtf8("pushButton_yrw"))
        self.label_yrw = QtGui.QLabel(self.tab_yrw)
        self.label_yrw.setGeometry(QtCore.QRect(140, 10, 431, 20))
        self.label_yrw.setText(_fromUtf8(""))
        self.label_yrw.setObjectName(_fromUtf8("label_yrw"))
        self.tabWidget.addTab(self.tab_yrw, _fromUtf8(""))
        self.tab_jrgc = QtGui.QWidget()
        self.tab_jrgc.setObjectName(_fromUtf8("tab_jrgc"))
        self.treeWidget_jrgc = QtGui.QTreeWidget(self.tab_jrgc)
        self.treeWidget_jrgc.setGeometry(QtCore.QRect(10, 40, 681, 271))
        self.treeWidget_jrgc.setObjectName(_fromUtf8("treeWidget_jrgc"))
        self.pushButton_jrgc = QtGui.QPushButton(self.tab_jrgc)
        self.pushButton_jrgc.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.pushButton_jrgc.setObjectName(_fromUtf8("pushButton_jrgc"))
        self.label_jrgc = QtGui.QLabel(self.tab_jrgc)
        self.label_jrgc.setGeometry(QtCore.QRect(140, 10, 431, 20))
        self.label_jrgc.setText(_fromUtf8(""))
        self.label_jrgc.setObjectName(_fromUtf8("label_jrgc"))
        self.tabWidget.addTab(self.tab_jrgc, _fromUtf8(""))
        self.tab_hrd = QtGui.QWidget()
        self.tab_hrd.setObjectName(_fromUtf8("tab_hrd"))
        self.pushButton_hrd = QtGui.QPushButton(self.tab_hrd)
        self.pushButton_hrd.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.pushButton_hrd.setObjectName(_fromUtf8("pushButton_hrd"))
        self.treeWidget_hrd = QtGui.QTreeWidget(self.tab_hrd)
        self.treeWidget_hrd.setGeometry(QtCore.QRect(10, 40, 681, 271))
        self.treeWidget_hrd.setObjectName(_fromUtf8("treeWidget_hrd"))
        self.label_hrd = QtGui.QLabel(self.tab_hrd)
        self.label_hrd.setGeometry(QtCore.QRect(140, 10, 431, 20))
        self.label_hrd.setText(_fromUtf8(""))
        self.label_hrd.setObjectName(_fromUtf8("label_hrd"))
        self.tabWidget.addTab(self.tab_hrd, _fromUtf8(""))

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "P2P签到软件 - Kevin", None))
        self.pushButton_dtjr.setText(_translate("Form", "签到", None))
        self.treeWidget_dtjr.headerItem().setText(0, _translate("Form", "账号", None))
        self.treeWidget_dtjr.headerItem().setText(1, _translate("Form", "密码", None))
        self.treeWidget_dtjr.headerItem().setText(2, _translate("Form", "状态", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_dtjr), _translate("Form", "当天金融", None))
        self.pushButton_gjs.setText(_translate("Form", "签到", None))
        self.treeWidget_gjs.headerItem().setText(0, _translate("Form", "账号", None))
        self.treeWidget_gjs.headerItem().setText(1, _translate("Form", "密码", None))
        self.treeWidget_gjs.headerItem().setText(2, _translate("Form", "状态", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_gjs), _translate("Form", "固金所", None))
        self.treeWidget_yrw.headerItem().setText(0, _translate("Form", "账号", None))
        self.treeWidget_yrw.headerItem().setText(1, _translate("Form", "密码", None))
        self.treeWidget_yrw.headerItem().setText(2, _translate("Form", "状态", None))
        self.pushButton_yrw.setText(_translate("Form", "签到", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_yrw), _translate("Form", "有融网", None))
        self.treeWidget_jrgc.headerItem().setText(0, _translate("Form", "账号", None))
        self.treeWidget_jrgc.headerItem().setText(1, _translate("Form", "密码", None))
        self.treeWidget_jrgc.headerItem().setText(2, _translate("Form", "状态", None))
        self.pushButton_jrgc.setText(_translate("Form", "签到", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_jrgc), _translate("Form", "金融工场", None))
        self.pushButton_hrd.setText(_translate("Form", "签到", None))
        self.treeWidget_hrd.headerItem().setText(0, _translate("Form", "账号", None))
        self.treeWidget_hrd.headerItem().setText(1, _translate("Form", "密码", None))
        self.treeWidget_hrd.headerItem().setText(2, _translate("Form", "状态", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_hrd), _translate("Form", "惠人贷", None))

