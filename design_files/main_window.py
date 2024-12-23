
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1313, 909)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 911, 421))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../cafe.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(930, 0, 261, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(920, 60, 391, 361))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 389, 359))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.text = QtWidgets.QLabel(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(10, 430, 1291, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.text.setFont(font)
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        self.text.setObjectName("text")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 470, 1311, 401))
        self.tabWidget.setObjectName("tabWidget")
        self.table_1 = QtWidgets.QPushButton(self.centralwidget)
        self.table_1.setGeometry(QtCore.QRect(20, 30, 221, 161))
        self.table_1.setText("")
        self.table_1.setFlat(True)
        self.table_1.setObjectName("table_1")
        self.table_4 = QtWidgets.QPushButton(self.centralwidget)
        self.table_4.setGeometry(QtCore.QRect(20, 210, 221, 161))
        self.table_4.setText("")
        self.table_4.setFlat(True)
        self.table_4.setObjectName("table_4")
        self.table_2 = QtWidgets.QPushButton(self.centralwidget)
        self.table_2.setGeometry(QtCore.QRect(350, 30, 221, 161))
        self.table_2.setText("")
        self.table_2.setFlat(True)
        self.table_2.setObjectName("table_2")
        self.table_5 = QtWidgets.QPushButton(self.centralwidget)
        self.table_5.setGeometry(QtCore.QRect(350, 210, 221, 161))
        self.table_5.setText("")
        self.table_5.setFlat(True)
        self.table_5.setObjectName("table_5")
        self.table_3 = QtWidgets.QPushButton(self.centralwidget)
        self.table_3.setGeometry(QtCore.QRect(690, 30, 221, 161))
        self.table_3.setText("")
        self.table_3.setFlat(True)
        self.table_3.setObjectName("table_3")
        self.table_6 = QtWidgets.QPushButton(self.centralwidget)
        self.table_6.setGeometry(QtCore.QRect(680, 210, 221, 161))
        self.table_6.setText("")
        self.table_6.setFlat(True)
        self.table_6.setObjectName("table_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1313, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Текущие заказы:"))
        self.text.setText(_translate("MainWindow", "Все заказы за последнюю неделю"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
