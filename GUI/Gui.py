from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
from Diseños.interfazPrincipal import Ui_MainWindow




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())