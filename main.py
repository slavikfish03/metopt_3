from main_window import *


if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()

    window.show()
    window.update()

    app.exec()
