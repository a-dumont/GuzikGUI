from .GuzikGUI import launch

app = QApplication(sys.argv)
win = GuzikOScopeWindow()
win.show()
sys.exit(app.exec())
