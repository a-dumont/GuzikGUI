import sys

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox

from matplotlib.backends.qt_compat import QtWidgets
try:
    from matplotlib.backends.backend_qtagg import (FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
except:
    from matplotlib.backends.backend_qt5agg import (FigureCanvas, NavigationToolbar2QT as NavigationToolbar)

import matplotlib.pyplot as plt

from .GuzikLayout import Ui_MainWindow

class Window(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.fig, ax = plt.subplots()
        self.axes = [ax]
        canvas = FigureCanvas(self.fig)
        self.mpl_layout.addWidget(NavigationToolbar(canvas, self))
        self.mpl_layout.addWidget(canvas)

        return None

