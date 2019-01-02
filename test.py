from PyQt5 import QtWidgets, uic

def Convert():
    dlg.dollars.setText(str(float(dlg.euros.text())*1.23))


app = QtWidgets.QApplication([])
dlg = uic.loadUi("untitled.ui")

dlg.euros.setFocus()
dlg.euros.setPlaceholderText("e")
dlg.pushButton.clicked.connect(Convert)

dlg.euros.returnPressed.connect(Convert)
dlg.dollars.setReadOnly(True)

dlg.show()
app.exec()
