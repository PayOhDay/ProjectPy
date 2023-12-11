from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1091, 738)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 110, 821, 351))
        self.tabWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tabWidget.setIconSize(QtCore.QSize(40, 40))
        self.tabWidget.setObjectName("tabWidget")

        self.tab_content_doc = QtWidgets.QWidget()
        self.tab_content_doc.setObjectName("tab_content_doc")
        self.tabWidget.addTab(self.tab_content_doc, "")

        self.tab_employ = QtWidgets.QWidget()
        self.tab_employ.setObjectName("tab_employ")
        self.tabWidget.addTab(self.tab_employ, "")

        self.tab_type_doc = QtWidgets.QWidget()
        self.tab_type_doc.setObjectName("tab_type_doc")
        self.tabWidget.addTab(self.tab_type_doc, "")

        self.tab_depart = QtWidgets.QWidget()
        self.tab_depart.setObjectName("tab_depart")
        self.tabWidget.addTab(self.tab_depart, "")

        self.btm_Exel = QtWidgets.QPushButton(self.centralwidget)
        self.btm_Exel.setGeometry(QtCore.QRect(740, 10, 100, 50))
        self.btm_Exel.setObjectName("btm_Exel")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 471, 81))
        self.groupBox.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.groupBox.setObjectName("groupBox")

        self.btm_author = QtWidgets.QPushButton(self.groupBox)
        self.btm_author.setGeometry(QtCore.QRect(10, 20, 100, 50))
        self.btm_author.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btm_author.setObjectName("btm_author")

        self.btm_address = QtWidgets.QPushButton(self.groupBox)
        self.btm_address.setGeometry(QtCore.QRect(120, 20, 100, 50))
        self.btm_address.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btm_address.setObjectName("btm_address")

        self.btm_time = QtWidgets.QPushButton(self.groupBox)
        self.btm_time.setGeometry(QtCore.QRect(230, 20, 120, 50))
        self.btm_time.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btm_time.setObjectName("btm_time")

        self.btm_type = QtWidgets.QPushButton(self.groupBox)
        self.btm_type.setGeometry(QtCore.QRect(360, 20, 100, 50))
        self.btm_type.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btm_type.setObjectName("btm_type")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Введение документооборота колледжа"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_content_doc), _translate("MainWindow", "Содержание документов"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_employ), _translate("MainWindow", "Сотрудники"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_type_doc), _translate("MainWindow", "Тип документов"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_depart), _translate("MainWindow", "Отделения"))
        self.btm_Exel.setText(_translate("MainWindow", "Отчет в Excel"))
        self.groupBox.setTitle(_translate("MainWindow", "Выборки по следующим параметрам:"))
        self.btm_author.setText(_translate("MainWindow", "По автору"))
        self.btm_address.setText(_translate("MainWindow", "По адресату"))
        self.btm_time.setText(_translate("MainWindow", "По периоду\nсоздания документа"))
        self.btm_type.setText(_translate("MainWindow", "По типу\nдокумента"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
