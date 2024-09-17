import math


import PyQt6
import matplotlib.pyplot as plt
from PyQt6.QtCore import Qt, QSize, QVariant
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from styles import *


class InputWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.selected_method = None
        self.selected_precision = None
        self.a = None
        self.b = None

        # self.setFixedSize(QSize(1250, 650))

        self.warning_func_label = self.init_warning_func()

        self.method_label = QLabel("МЕТОД: ")
        self.method_combobox = self.init_method_combobox()

        self.precision_label = QLabel("ТОЧНОСТЬ: ")
        self.precision_combobox = self.init_precision_combobox()

        self.point_a_label = QLabel("ЛЕВАЯ ГРАНИЦА ОТРЕЗКА: ")
        self.point_a_doublespinbox = self.init_point_a_doublespinbox()

        self.point_b_label = QLabel("ПРАВАЯ ГРАНИЦА ОТРЕЗКА: ")
        self.point_b_doublespinbox = self.init_point_b_doublespinbox()

        self.separate_label = QLabel("")

        self.next_btn = self.init_next_btn()

        layout = QVBoxLayout()

        layout.addWidget(self.warning_func_label)

        layout.addWidget(self.method_label)
        layout.addWidget(self.method_combobox)
        layout.addWidget(self.precision_label)
        layout.addWidget(self.precision_combobox)
        layout.addWidget(self.point_a_label)
        layout.addWidget(self.point_a_doublespinbox)
        layout.addWidget(self.point_b_label)
        layout.addWidget(self.point_b_doublespinbox)
        layout.addWidget(self.separate_label)
        layout.addWidget(self.next_btn)

        self.setLayout(layout)

    # Initialize method's
    def init_warning_func(self):
        warning_func_label = QLabel("[ВНИМАНИЕ]: Целевая функция устанавливается в коде\n (файл target_function)")
        warning_func_label.setStyleSheet("color: rgb(232, 0, 0);")
        return warning_func_label

    def init_method_combobox(self):
        method_combobox = QComboBox()
        method_combobox.addItems(["Метод золотого сечения", "Метод Фибоначчи"])
        method_combobox.setPlaceholderText("Выберите метод...")
        method_combobox.setCurrentIndex(-1)
        method_combobox.setStyleSheet(STYLE_COMBOBOX)
        method_combobox.currentIndexChanged.connect(self.on_method_change)
        method_combobox.view().window().setWindowFlags(
            Qt.WindowType.Popup | Qt.WindowType.NoDropShadowWindowHint | Qt.WindowType.FramelessWindowHint
        )
        return method_combobox

    def init_precision_combobox(self):
        precision_combobox = QComboBox()

        precision_combobox.addItem("0.1", QVariant(0.1))
        precision_combobox.addItem("0.01", QVariant(0.01))
        precision_combobox.addItem("0.001", QVariant(0.001))
        precision_combobox.addItem("0.0001", QVariant(0.0001))
        precision_combobox.addItem("0.00001", QVariant(0.00001))
        precision_combobox.addItem("0.000001", QVariant(0.000001))
        precision_combobox.addItem("0.0000001", QVariant(0.0000001))
        precision_combobox.addItem("0.00000001", QVariant(0.00000001))
        precision_combobox.addItem("0.000000001", QVariant(0.000000001))
        precision_combobox.addItem("0.0000000001", QVariant(0.0000000001))

        precision_combobox.setPlaceholderText("Выберите точность...")
        precision_combobox.setCurrentIndex(-1)
        precision_combobox.setStyleSheet(STYLE_COMBOBOX)
        precision_combobox.currentIndexChanged.connect(self.on_precision_change)
        precision_combobox.view().window().setWindowFlags(
            Qt.WindowType.Popup | Qt.WindowType.NoDropShadowWindowHint | Qt.WindowType.FramelessWindowHint
        )
        return precision_combobox

    def init_point_a_doublespinbox(self):
        point_a_doublespinbox = QDoubleSpinBox()
        point_a_doublespinbox.setStyleSheet(STYLE_DOUBLESPINBOX)

        point_a_doublespinbox.setDecimals(3)
        point_a_doublespinbox.setRange(-math.inf, math.inf)
        step_type = QAbstractSpinBox.StepType.AdaptiveDecimalStepType
        point_a_doublespinbox.setStepType(step_type)
        point_a_doublespinbox.valueChanged.connect(self.on_point_a_change)

        return point_a_doublespinbox

    def init_point_b_doublespinbox(self):
        point_b_doublespinbox = QDoubleSpinBox()
        point_b_doublespinbox.setStyleSheet(STYLE_DOUBLESPINBOX)

        point_b_doublespinbox.setDecimals(3)
        point_b_doublespinbox.setRange(-math.inf, math.inf)
        step_type = QAbstractSpinBox.StepType.AdaptiveDecimalStepType
        point_b_doublespinbox.setStepType(step_type)
        point_b_doublespinbox.valueChanged.connect(self.on_point_b_change)

        return point_b_doublespinbox

    def init_next_btn(self):
        next_btn = QPushButton("OK")
        next_btn.setStyleSheet(STYLE_BTN)
        return next_btn

    # Slot's
    def on_method_change(self, index):
        self.method_combobox.setStyleSheet(STYLE_COMBOBOX + STYLE_COMBOBOX_AFTER)
        self.selected_method = self.method_combobox.itemText(index)

    def on_precision_change(self, index):
        self.precision_combobox.setStyleSheet(STYLE_COMBOBOX + STYLE_COMBOBOX_AFTER)
        self.selected_precision = self.precision_combobox.itemData(index)
        print(type(self.selected_precision))

    def on_point_a_change(self):
        self.point_a_doublespinbox.setStyleSheet(STYLE_DOUBLESPINBOX + STYLE_DOUBLESPINBOX_AFTER)
        self.a = self.point_a_doublespinbox.value()

    def on_point_b_change(self):
        self.point_b_doublespinbox.setStyleSheet(STYLE_DOUBLESPINBOX + STYLE_DOUBLESPINBOX_AFTER)
        self.b = self.point_b_doublespinbox.value()