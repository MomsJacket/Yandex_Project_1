from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ListOfFunctions(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(641, 330)
        Dialog.setFixedSize(641, 330)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("")
        self.table = QtWidgets.QTableWidget(Dialog)
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["Функция", "MIN X",
                                              "MAX X", "Цвет",
                                              "Код цвета", "Символ X"])
        self.table.setRowCount(1)
        self.table.setGeometry(QtCore.QRect(10, 10, 621, 281))
        self.table.horizontalHeaderItem(0).setToolTip("Функция")
        self.table.horizontalHeaderItem(1).setToolTip("Минимальное"
                                                      " значение x")
        self.table.horizontalHeaderItem(2).setToolTip("Максимальное"
                                                      " значение x")
        self.table.horizontalHeaderItem(3).setToolTip("Цвет")
        self.table.horizontalHeaderItem(4).setToolTip("Код цвета")
        self.table.horizontalHeaderItem(5).setToolTip("Имеется ли "
                                                      "обозначения "
                                                      "на каждое"
                                                      " целое значение x")
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 295, 101, 31))
        self.pushButton.setObjectName("pushButton")

        self.pushButton2 = QtWidgets.QPushButton(Dialog)
        self.pushButton2.setGeometry(QtCore.QRect(115, 295, 101, 31))
        self.pushButton2.setObjectName("pushButton")

        self.pushButton3 = QtWidgets.QPushButton(Dialog)
        self.pushButton3.setGeometry(QtCore.QRect(480, 295, 151, 31))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Список графиков"))
        self.pushButton.setText(_translate("Dialog", "Обновить"))
        self.pushButton2.setText(_translate("Dialog", "Выйти"))
        self.pushButton3.setText(_translate("Dialog", "Подробнее о "
                                                      "графиках..."))
