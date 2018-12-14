import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QColorDialog
from PyQt5.QtWidgets import QMainWindow, QDialog, QMessageBox
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtGui import QColor, QIcon
from main_window import Ui_MainWindow
from new_function import Ui_NewFunction
from list_of_functions import Ui_ListOfFunctions
from dots import Ui_Dots
from math import *


class NewFunction(QDialog, Ui_NewFunction):
    def __init__(self, root):
        super().__init__(root)
        self.main = root
        self.setupUi(self)
        self.color_of_graph = '#ff0000'
        self.pushButton.clicked.connect(self.change_color)
        self.pushButton2.clicked.connect(self.create_graph)
        self.pushButton3.clicked.connect(self.cancel)
        self.pushButton.setStyleSheet(
            "background-color: {}".format("#ff0000")
        )

    def cancel(self):
        self.pushButton.setStyleSheet(
            "background-color: {}".format('#ff0000')
        )
        self.textEdit.clear()
        self.textEdit_2.clear()
        self.checkBox.setChecked(False)
        self.checkBox_2.setChecked(False)
        self.close()

    def change_color(self):
        color = QColorDialog.getColor()
        self.color_of_graph = color.name()
        if self.color_of_graph == '#000000':
            msg_box = QMessageBox()
            msg_box.setWindowTitle('')
            msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg_box.setText("Вы уверены что хотите"
                            " использовать черный цвет?")
            result = msg_box.exec_()
            if QMessageBox.Yes == result:
                self.pushButton.setStyleSheet(
                    "background-color: {}".format(color.name())
                )
            elif QMessageBox.No == result:
                self.pushButton.setStyleSheet(
                    "background-color: {}".format("#ff0000")
                )
        else:
            self.pushButton.setStyleSheet(
                "background-color: {}".format(color.name())
            )

    def create_graph(self):
        dots = None
        if self.checkBox.isChecked():
            dots = 'x'
        if self.checkBox_2.isChecked():
            self.main.Plot.clear()
            self.main.full_list = []
        try:
            x_min, x_max = \
                [int(i) for i in self.textEdit_2.toPlainText().split()]
        except Exception:
            x_min = -100
            x_max = 100
        text = self.textEdit.toPlainText().replace('^', '**')
        text = text.replace('math.', '')
        text = text.replace(' ', '')
        if not text:
            QMessageBox.about(self, "Ошибка", "Введите значение функции F(x)")
        else:
            x_dots = []
            y_dots = []
            values = {}
            for i in range(x_min, x_max + 1):
                try:
                    y = eval(text.replace('x', str(i)))
                    values[i] = y
                    y_dots.append(y)
                    x_dots.append(i)
                except Exception:
                    pass
            self.main.Plot.plot(x_dots, y_dots,
                                pen=QColor(self.color_of_graph), symbol=dots)
            if x_dots:
                self.main.full_list.append(Functions(text, x_min, x_max,
                                                     self.color_of_graph,
                                                     dots, values))
            self.pushButton.setStyleSheet(
                "background-color: {}".format('#ff0000')
            )
            self.textEdit.clear()
            self.textEdit_2.clear()
            self.checkBox.setChecked(False)
            self.checkBox_2.setChecked(False)
            self.close()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('icon.png'))
        self.full_list = []
        self.new_function = NewFunction(self)
        self.list_of_function = ListOfFunctions(self)
        self.pushButton.clicked.connect(self.new_function.exec)
        self.pushButton_2.clicked.connect(self.list_of_function.exec)
        self.pushButton_3.clicked.connect(self.clear_plot)

    def clear_plot(self):
        self.Plot.clear()
        self.full_list = []


# Класс, в котором хванится вся необходимая информация о графике
class Functions:
    def __init__(self, equation, low, high, color, symbol, values):
        self.equation = equation
        self.x_min = str(low)
        self.x_max = str(high)
        self.color = color
        self.values = values
        if symbol is None:
            self.symbol = 'Нету'
        else:
            self.symbol = 'Есть'


class ListOfFunctions(QDialog, Ui_ListOfFunctions):
    def __init__(self, root):
        super().__init__(root)
        self.main = root
        self.dots = Dots(root)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.refresh)
        self.pushButton2.clicked.connect(self.exit)
        self.pushButton3.clicked.connect(self.dots.exec)

    def refresh(self):
        self.reconstruct_table()
        for i in range(len(self.main.full_list)):
            if i + 1 > self.table.rowCount():
                self.table.insertRow(self.table.rowCount())
            self.table.setItem(i, 0, QTableWidgetItem(self.main.
                                                      full_list[i].equation))
            self.table.setItem(i, 1, QTableWidgetItem(self.main.
                                                      full_list[i].x_min))
            self.table.setItem(i, 2, QTableWidgetItem(self.main.
                                                      full_list[i].x_max))
            self.table.setItem(i, 3, QTableWidgetItem(''))
            self.table.item(i, 3).setBackground(QColor(self.main.
                                                       full_list[i].color))
            self.table.setItem(i, 4, QTableWidgetItem(self.main.
                                                      full_list[i].color))
            self.table.setItem(i, 5, QTableWidgetItem(self.main.
                                                      full_list[i].symbol))

    def exit(self):
        self.close()

    def reconstruct_table(self):
        self.table.clear()
        self.table.setRowCount(1)
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
        self.table.horizontalHeaderItem(5).setToolTip("Имеется ли обозначения "
                                                      "на каждое"
                                                      " целое значение x")


class Dots(QDialog, Ui_Dots):
    def __init__(self, root):
        super().__init__(root)
        self.main = root
        self.setupUi(self)
        self.pushButton.clicked.connect(self.exit)
        self.pushButton_2.clicked.connect(self.dots)
        self.pushButton_3.clicked.connect(self.compare)

    def exit(self):
        self.textEdit.clear()
        self.textEdit_2.clear()
        self.textEdit_3.clear()
        self.plainTextEdit.clear()
        self.close()

    def compare(self):
        number = self.textEdit_2.toPlainText()
        number2 = self.textEdit_3.toPlainText()
        flag = True
        try:
            number = int(number)
            number2 = int(number2)
        except Exception:
            flag = False

        if not number or not number2 or not flag:
            QMessageBox.about(self, "Ошибка", "Не введен номер графика")
        elif int(number) > len(self.main.full_list) or int(number) < 1:
            QMessageBox.about(self, "Ошибка", "Неверно введен номер")
        elif int(number2) > len(self.main.full_list) or int(number2) < 1:
            QMessageBox.about(self, "Ошибка", "Неверно введен номер")
        else:
            self.plainTextEdit.clear()
            x_min1 = int(self.main.full_list[int(number) - 1].x_min)
            x_min2 = int(self.main.full_list[int(number2) - 1].x_min)
            x_max1 = int(self.main.full_list[int(number) - 1].x_max)
            x_max2 = int(self.main.full_list[int(number2) - 1].x_max)
            start = max(x_min1, x_min2)
            end = min(x_max1, x_max2)
            for i in range(start, end):
                dot_1 = self.main.full_list[int(number) - 1].values[i]
                dot_2 = self.main.full_list[int(number2) - 1].values[i]
                if dot_1 == dot_2:
                    self.plainTextEdit.insertPlainText(
                        'X: ' + str(i) + ' ' +
                        'Y: ' + str(dot_1) + '\n')

    def dots(self):
        number = self.textEdit.toPlainText()
        flag = True
        try:
            number = int(number)
        except Exception:
            flag = False
        if not number or not flag:
            QMessageBox.about(self, "Ошибка", "Не введен номер графика")
        elif int(number) > len(self.main.full_list) or int(number) < 1:
            QMessageBox.about(self, "Ошибка", "Неверно введен номер")
        else:
            self.plainTextEdit.clear()
            for i in self.main.full_list[int(number) - 1].values:
                self.plainTextEdit.insertPlainText(
                    'X: ' + str(i) + '  ' + 'Y: ' +
                    str(self.main.full_list[int(number) - 1].values[i]) + '\n')


app = QApplication(sys.argv)
ex = MainWindow()
ex.show()
sys.exit(app.exec_())
