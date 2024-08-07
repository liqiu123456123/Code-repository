from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TransformWindow(object):
    def setupUi(self, TransformWindow):
        TransformWindow.setObjectName("TransformWindow")
        TransformWindow.resize(801, 648)
        TransformWindow.setStyleSheet("background-color: lightblue;")

        self.centralwidget = QtWidgets.QWidget(TransformWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Source Group Box
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 761, 150))
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

        self.sourcebrowseButton = QtWidgets.QToolButton(self.horizontalLayoutWidget)
        self.sourcebrowseButton.setObjectName("sourcebrowseButton")
        self.horizontalLayout.addWidget(self.sourcebrowseButton)

        self.listword = QtWidgets.QListWidget(self.groupBox)
        self.listword.setGeometry(QtCore.QRect(20, 60, 721, 71))
        self.listword.setObjectName("listword")

        # Result Group Box
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 170, 761, 150))
        self.groupBox_2.setObjectName("groupBox_2")

        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(20, 20, 721, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)

        self.targetpath = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.targetpath.setObjectName("targetpath")
        self.horizontalLayout_4.addWidget(self.targetpath)

        self.targetbrowseButton = QtWidgets.QToolButton(self.horizontalLayoutWidget_4)
        self.targetbrowseButton.setObjectName("targetbrowseButton")
        self.horizontalLayout_4.addWidget(self.targetbrowseButton)

        self.listpdf = QtWidgets.QListWidget(self.groupBox_2)
        self.listpdf.setGeometry(QtCore.QRect(20, 60, 721, 71))
        self.listpdf.setObjectName("listpdf")

        # Execute Buttons and Loading
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 330, 761, 50))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)

        self.showLoding = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.showLoding.setEnabled(True)
        self.showLoding.setObjectName("showLoding")
        self.horizontalLayout_3.addWidget(self.showLoding)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)

        self.multipleExecute = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.multipleExecute.setObjectName("multipleExecute")
        self.horizontalLayout_3.addWidget(self.multipleExecute)

        self.singleExecute = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.singleExecute.setObjectName("singleExecute")
        self.horizontalLayout_3.addWidget(self.singleExecute)

        TransformWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(TransformWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 23))
        self.menubar.setObjectName("menubar")
        TransformWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(TransformWindow)
        self.statusbar.setObjectName("statusbar")
        TransformWindow.setStatusBar(self.statusbar)

        self.retranslateUi(TransformWindow)
        QtCore.QMetaObject.connectSlotsByName(TransformWindow)

    def retranslateUi(self, TransformWindow):
        _translate = QtCore.QCoreApplication.translate
        TransformWindow.setWindowTitle(_translate("TransformWindow", "Word转PDF"))
        self.showLoding.setText(_translate("TransformWindow", "转换进度"))
        self.multipleExecute.setText(_translate("TransformWindow", "批量转换"))
        self.singleExecute.setText(_translate("TransformWindow", "合为一个PDF"))
        self.groupBox.setTitle(_translate("TransformWindow", "源"))
        self.label.setText(_translate("TransformWindow", "请选择Word文档所在目录："))
        self.sourcebrowseButton.setText(_translate("TransformWindow", "..."))
        self.groupBox_2.setTitle(_translate("TransformWindow", "结果"))
        self.label_3.setText(_translate("TransformWindow", "转换后PDF文件保存目录："))
        self.targetbrowseButton.setText(_translate("TransformWindow", "..."))
