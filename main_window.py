import math


import PyQt6
import matplotlib.pyplot as plt
from PyQt6.QtCore import Qt, QSize, QVariant
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from styles import *
from input_widget import InputWidget
from function_widget import FunctionWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ЛАБОРАТОРНАЯ РАБОТА №3: МЕТОДЫ ОДНОМЕРНОЙ ОПТИМИЗАЦИИ")
        self.setStyleSheet(STYLE_MAINWINDOW)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QHBoxLayout()

        self.layout_right = QHBoxLayout()

        self.input_widget = InputWidget()
        self.function_widget = QWidget()

        self.layout.addWidget(self.input_widget)
        self.layout_right.addWidget(self.function_widget)
        self.layout.addLayout(self.layout_right)

        self.central_widget.setLayout(self.layout)

        self.input_widget.next_btn.clicked.connect(self.init_function_widget)

    def update(self):
        super(MainWindow, self).update()
        self.function_widget.show()

    # Initialize method's
    def init_function_widget(self):
        function_widget = FunctionWidget(
            self.input_widget.a,
            self.input_widget.b,
            self.input_widget.selected_method,
            self.input_widget.selected_precision)

        for i in reversed(range(self.layout_right.count())):
            self.layout_right.itemAt(i).widget().deleteLater()

        self.function_widget = function_widget
        self.layout_right.addWidget(function_widget)

    # Overload method's
    def mousePressEvent(self, event):
        focused_widget = QApplication.focusWidget()
        if focused_widget:
            focused_widget.clearFocus()

        QMainWindow.mousePressEvent(self, event)


