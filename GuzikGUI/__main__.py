from PyQt5.QtWidgets import QApplication,
from GuzikGUI.GuzikGUI import GuzikOScopeWindow

app = QApplication(sys.argv)
win = GuzikOScopeWindow()
win.show()
sys.exit(app.exec())
