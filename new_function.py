from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewFunction(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(410, 320)
        Dialog.setFixedSize(410, 320)
        self.setWindowIcon(QtGui.QIcon('icon.png'))

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 161, 31))

        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 391, 41))
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")

        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(170, 10, 231, 31))
        self.textEdit.setObjectName("textEdit")

        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(240, 60, 161, 31))
        self.textEdit_2.setObjectName("textEdit_2")

        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 140, 391, 16))
        self.label_4.setObjectName("label_4")

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 160, 391, 41))
        self.pushButton.setObjectName("pushButton")

        self.pushButton2 = QtWidgets.QPushButton(Dialog)
        self.pushButton2.setGeometry(QtCore.QRect(10, 250, 391, 31))
        self.pushButton2.setObjectName("pushButton2")

        self.pushButton3 = QtWidgets.QPushButton(Dialog)
        self.pushButton3.setGeometry(QtCore.QRect(10, 285, 391, 31))
        self.pushButton3.setObjectName("pushButton3")

        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(10, 210, 381, 17))
        self.checkBox.setObjectName("checkBox")

        self.checkBox_2 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 230, 381, 17))
        self.checkBox_2.setObjectName("checkBox_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Новая функция"))
        self.label.setText(_translate("Dialog", "Введите F(x):"))
        self.label_2.setText(_translate("Dialog", "Введите "
                                                  "диапазон значений X:"))
        self.label_3.setText(_translate("Dialog",
                                        "Введите два целых числа "
                                        "Xmin и Xmax через"
                                        " пробел. Если значения введены"
                                        " неверно, то будет использоваться"
                                        " стандартный диапазон Xmin = -100;"
                                        " Xmax = 100;"))
        self.label_4.setText(_translate("Dialog", "Рекомендуется вводить"
                                                  " диапазон не больше 10^5"))
        self.pushButton.setText(_translate("Dialog", "Выбрать цвет графика"))
        self.pushButton2.setText(_translate("Dialog", "Создать график"))
        self.pushButton3.setText(_translate("Dialog", "Отмена"))
        self.checkBox.setText(_translate("Dialog", "Ставить точки на"
                                                   " месте значении "
                                                   "функции при целом X"))
        self.checkBox_2.setText(_translate("Dialog", "Отчистить поле перед "
                                                     "построением графика"))
