from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ListWindow(object):
    def setupUi(self, ListWindow):
        ListWindow.setObjectName("ListWindow")
        ListWindow.resize(800, 588)
        self.centralwidget = QtWidgets.QWidget(ListWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 443, 761, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.checkBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget_3)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_3.addWidget(self.checkBox)
        self.executeButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.executeButton.setObjectName("executeButton")
        self.horizontalLayout_3.addWidget(self.executeButton)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 761, 431))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 721, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.sourcepath = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.sourcepath.setObjectName("sourcepath")
        self.horizontalLayout.addWidget(self.sourcepath)
        self.browseButton = QtWidgets.QToolButton(self.horizontalLayoutWidget)
        self.browseButton.setObjectName("browseButton")
        self.horizontalLayout.addWidget(self.browseButton)
        self.listword = QtWidgets.QListWidget(self.groupBox)
        self.listword.setGeometry(QtCore.QRect(20, 70, 721, 341))
        self.listword.setObjectName("listword")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 470, 761, 81))
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 30, 721, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.listfile = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.listfile.setObjectName("listfile")
        self.horizontalLayout_2.addWidget(self.listfile)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.openButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.openButton.setObjectName("openButton")
        self.horizontalLayout_2.addWidget(self.openButton)
        ListWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ListWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        ListWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ListWindow)
        self.statusbar.setObjectName("statusbar")
        ListWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ListWindow)
        QtCore.QMetaObject.connectSlotsByName(ListWindow)

    def retranslateUi(self, ListWindow):
        _translate = QtCore.QCoreApplication.translate
        ListWindow.setWindowTitle(_translate("ListWindow", "提取总目录"))
        self.checkBox.setText(_translate("ListWindow", "包含页码      "))
        self.executeButton.setText(_translate("ListWindow", "开始提取"))
        self.groupBox.setTitle(_translate("ListWindow", "源"))
        self.label.setText(_translate("ListWindow", "请选择Word文档所在目录："))
        self.browseButton.setText(_translate("ListWindow", "..."))
        self.groupBox_2.setTitle(_translate("ListWindow", "结果"))
        self.label_2.setText(_translate("ListWindow", "目录文件保存位置："))
        self.listfile.setText(_translate("ListWindow", "还未提取..."))
        self.openButton.setText(_translate("ListWindow", "打开文件"))

