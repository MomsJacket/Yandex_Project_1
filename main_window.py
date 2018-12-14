from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(637, 729)
        MainWindow.setFixedSize(637, 729)
        MainWindow.setToolTip("")
        self.setWindowIcon(QtGui.QIcon('icon.png'))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.Plot = PlotWidget(self.centralwidget)
        self.Plot.setGeometry(QtCore.QRect(10, 10, 621, 601))
        self.Plot.setObjectName("graphicsView")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 620, 301, 41))
        self.pushButton.setDefault(True)
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 620, 301, 41))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 670, 621, 31))
        self.pushButton_3.setObjectName("pushButton_3")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 637, 21))
        self.menubar.setObjectName("menubar")

        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu2 = QtWidgets.QMenu(self.menubar)
        self.menu2.setObjectName("menu2")
        MainWindow.setMenuBar(self.menubar)

        self.action = QtWidgets.QAction(MainWindow)
        self.action.triggered.connect(self.help)
        self.action.setObjectName("action")
        self.exitAction = QtWidgets.QAction()
        self.exitAction.triggered.connect(QtWidgets.qApp.quit)

        self.menu.addAction(self.action)
        self.menu2.addAction(self.exitAction)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow",
                                             "Graphic Creator V.1.0"))
        self.pushButton.setText(_translate("MainWindow",
                                           "Добавить новый график"))
        self.pushButton_2.setText(_translate("MainWindow",
                                             "Посмотреть список графиков"))
        self.pushButton_3.setText(_translate("MainWindow",
                                             "Отчистить поле"))
        self.menu.setTitle(_translate("MainWindow", "Справка"))
        self.menu2.setTitle(_translate("MainWindow", "Выход"))
        self.action.setText(_translate("MainWindow", "Помощь"))
        self.exitAction.setText(_translate("MainWindow", "Выйти   Alt+F4"))

    def help(self):
        QtWidgets.QMessageBox.about(self, "Справка", 'Программа строит график'
                                    ' функции f(x), которая в'
                                    'водится в окне, которое'
                                    ' можно вызвать нажав на'
                                    ' кнопку "Добавить новый'
                                    ' график" \n \n Также мо'
                                    'жно задавать цвет г'
                                    'рафику и отслеживать '
                                    'имеющиеся графики.')
