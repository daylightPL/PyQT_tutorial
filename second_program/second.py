from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
import json

app = QtWidgets.QApplication([])
dlg = uic.loadUi("second.ui")


def addItem():

    if not (dlg.lineEdit.text() == ""):
        dlg.listWidget.addItem(dlg.lineEdit.text())


    else:
        show_message('Warning', "You have to type at least one character")
    dlg.lineEdit.setFocus()

    with open('data.json', 'r') as file:
        data = json.load(file)
    data["items"].append(dlg.lineEdit.text())
    with open('data.json', 'w') as file:
        json.dump(data, file)

    dlg.lineEdit.setText("")


def show_message(title='Test', message='Test'):
    QMessageBox.information(None, title, message)

def main():
    with open('data.json', 'r') as file:
        data = json.load(file)


    for item in data['items']:
        dlg.listWidget.addItem(item)

if __name__ == "__main__":
    main()

dlg.lineEdit.setFocus()
dlg.lineEdit.returnPressed.connect(addItem)
dlg.pushButton.clicked.connect(addItem)

dlg.show()
app.exec()