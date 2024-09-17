import math
import datetime

import PyQt6
import matplotlib.pyplot as plt
import numpy as np
from PyQt6.QtCore import Qt, QSize, QVariant
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from styles import *
from target_function import function, FUNC

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from GoldenRatioMethod import *
from FibonacciMethod import *


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self):
        fig = Figure(figsize=(4, 5), dpi=100)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

    def update_plot(self, x, y, opt_x, opt_val):
        self.axes.clear()
        self.axes.plot(x, y)
        self.axes.axvline(opt_x[0], color='r')
        self.axes.axvline(opt_x[1], color='r')

        # self.axes.axhline(opt_val[0], color='r')
        # self.axes.axhline(opt_val[1], color='r')

        self.draw()


class FunctionWidget(QWidget):
    def __init__(self, a, b, method, precision):
        super().__init__()
        self.a = a
        self.b = b
        self.method = method
        self.precision = precision

        self.opt_x = None
        self.opt_val = None
        self.n = None

        if self.is_correct_input(a, b, method, precision):
            self.label = QLabel("ЦЕЛЕВАЯ ФУНКЦИЯ:")
            self.label_func = QLabel(FUNC)
            self.graph = MplCanvas()
            self.graph.axes.plot(np.linspace(self.a, self.b), function(np.linspace(self.a, self.b)))

            self.general_label = QLabel("РЕЗУЛЬТАТЫ:")
            self.opt_x_label = QLabel("Отрезок, где содержится оптимальная точка: ")
            #self.opt_val_label = QLabel("Отрезок, где содержится оптимальное значение: ")
            self.n_label = QLabel("Количество обращений к функции: ")

            self.start_btn = QPushButton("ЗАПУСК")
            self.start_btn.setStyleSheet(STYLE_BTN)

            self.layout = QVBoxLayout()
            self.layout.addWidget(self.label)
            self.layout.addWidget(self.label_func)
            self.layout.addWidget(self.graph)
            self.layout.addWidget(self.general_label)
            self.layout.addWidget(self.opt_x_label)
            #self.layout.addWidget(self.opt_val_label)
            self.layout.addWidget(self.n_label)
            self.layout.addWidget(self.start_btn)

            self.setLayout(self.layout)

            self.start_btn.clicked.connect(self.solve)
        else:
            return

    def is_correct_input(self, a, b, method, precision):
        if a is None or b is None:
            self.a = -5
            self.b = 5
        else:
            self.a = a
            self.b = b

        if self.a >= self.b:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setText("[ОШИБКА ВВОДА]")
            msg.setInformativeText('Неправильно введен отрезок: левая граница должна быть строго меньше правой')
            msg.setWindowTitle("Ошибка")
            msg.exec()
            return False
        return True

    def solve(self):

        def get_count(number):
            s = str(number)
            if '.' in s:
                return abs(s.find('.') - len(s)) - 1
            else:
                return 0

        match self.method:
            case "Метод золотого сечения":
                golden_ratio_method = GoldenRatioMethod(self.a, self.b, self.precision)
                golden_ratio_method.solve()
                self.opt_x = golden_ratio_method.opt_x
                self.opt_val = golden_ratio_method.opt_val
                self.n = golden_ratio_method.n

                # count_digits = golden_ratio_method.get_count(self.precision)

                self.opt_x_label.setText(f"Отрезок, где содержится оптимальная точка: {[np.round(self.opt_x[0], get_count(self.precision) + 2), np.round(self.opt_x[1], get_count(self.precision) + 2)]}")
                #self.opt_val_label.setText(f"Отрезок, где содержится оптимальное значение: {self.opt_val}")
                self.n_label.setText(f"Количество обращений к функции: {self.n}")

                self.graph.update_plot(np.linspace(self.a, self.b), function(np.linspace(self.a, self.b)), self.opt_x,
                                       self.opt_val)

            case "Метод Фибоначчи":
                fibonacci_method = FibonacciMethod(self.a, self.b, self.precision)
                fibonacci_method.solve()
                self.opt_x = fibonacci_method.opt_x
                self.opt_val = fibonacci_method.opt_val
                self.n = fibonacci_method.n

                self.opt_x_label.setText(f"Отрезок, где содержится оптимальная точка: {[np.round(self.opt_x[0], get_count(self.precision) + 2), np.round(self.opt_x[1], get_count(self.precision) + 2)]}")
                #self.opt_val_label.setText(f"Отрезок, где содержится оптимальное значение: {self.opt_val}")
                self.n_label.setText(f"Количество обращений к функции: {self.n}")

                self.graph.update_plot(np.linspace(self.a, self.b), function(np.linspace(self.a, self.b)), self.opt_x,
                                       self.opt_val)

            case _:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Icon.Critical)
                msg.setText("[ОШИБКА ВВОДА]")
                msg.setInformativeText('Не введен метод решения')
                msg.setWindowTitle("Ошибка")
                msg.exec()




