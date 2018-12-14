from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dots(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(499, 299)
        Dialog.setFixedSize(499, 299)

        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(150, 10, 341, 281))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.setReadOnly(True)

        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 30, 131, 31))
        self.textEdit.setObjectName("textEdit")

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 260, 131, 31))
        self.pushButton.setObjectName("pushButton")

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 131, 16))
        self.label.setObjectName("label")

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 70, 131, 31))
        self.pushButton_2.setObjectName("pushButton_2")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 131, 61))
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")

        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 170, 61, 31))
        self.textEdit_2.setObjectName("textEdit_2")

        self.textEdit_3 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_3.setGeometry(QtCore.QRect(80, 170, 61, 31))
        self.textEdit_3.setObjectName("textEdit_3")

        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 210, 131, 31))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Побробнее о графиках"))
        self.pushButton.setText(_translate("Dialog", "Выйти"))
        self.label.setText(_translate("Dialog", "Введите номер графика"))
        self.pushButton_2.setText(_translate("Dialog", "Найти все "
                                                       "значения Y"))
        self.label_2.setText(
            _translate("Dialog", "Введите номера графиков\n(Поиск "
                                 "производится среди целых значений X)"))
        self.pushButton_3.setText(_translate("Dialog", "Найти общие точки"))
