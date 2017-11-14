import math
import random
import string
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import numberformatdlg1
import numberformatdlg2
import numberformatdlg3


class Form(QDialog):

    X_MAX = 26
    Y_MAX = 60

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.numberFormatDlg = None
        self.format = dict(thousandsseparator=",",
                           decimalmarker=".", decimalplaces=2,
                           rednegatives=False)
        self.numbers = {}
        for x in range(self.X_MAX):
            for y in range(self.Y_MAX):
                self.numbers[(x, y)] = (10000 * random.random()) - 5000

        self.table = QTableWidget()
        format_button1 = QPushButton("Set Number Format... "
                                     "(&Modal)")
        format_button2 = QPushButton("Set Number Format... "
                                     "(Modele&ss)")
        format_button3 = QPushButton("Set Number Format... "
                                     "(`&Live')")

        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(format_button1)
        button_layout.addWidget(format_button2)
        button_layout.addWidget(format_button3)
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addLayout(button_layout)
        self.setLayout(layout)

        format_button1.clicked.connect(self.setNumberFormat1)
        format_button2.clicked.connect(self.setNumberFormat2)
        format_button3.clicked.connect(self.setNumberFormat3)

        self.setWindowTitle("Numbers")
        self.refreshTable()

    def refreshTable(self):
        self.table.clear()
        self.table.setColumnCount(self.X_MAX)
        self.table.setRowCount(self.Y_MAX)
        self.table.setHorizontalHeaderLabels(
                list(string.ascii_uppercase))
        for x in range(self.X_MAX):
            for y in range(self.Y_MAX):
                fraction, whole = math.modf(self.numbers[(x, y)])
                sign = "-" if whole < 0 else ""
                whole = "%d" % math.floor(abs(whole))
                digits = []
                for i, digit in enumerate(reversed(whole)):
                    if i and i % 3 == 0:
                        digits.insert(0, self.format["thousandsseparator"])
                    digits.insert(0, digit)
                if self.format["decimalplaces"]:
                    fraction = "%0.7f" % abs(fraction)
                    fraction = (self.format["decimalmarker"] +
                                fraction[2:self.format["decimalplaces"]
                                + 2])
                else:
                    fraction = ""
                text = "%s%s%s" % (sign, "".join(digits), fraction)
                item = QTableWidgetItem(text)
                item.setTextAlignment(Qt.AlignRight|Qt.AlignVCenter)
                if sign and self.format["rednegatives"]:
                    item.setBackground(Qt.red)
                self.table.setItem(y, x, item)

    def setNumberFormat1(self):
        dialog = numberformatdlg1.NumberFormatDlg(self.format, self)
        if dialog.exec_():
            self.format = dialog.numberFormat()
            self.refreshTable()

    def setNumberFormat2(self):
        try:
            dialog = numberformatdlg2.NumberFormatDlg(self.format, self)
            dialog.changed.connect(self.refreshTable)
            dialog.show()
        except Exception as e:
            print(e)

    def setNumberFormat3(self):
        try:
            if self.numberFormatDlg is None:
                self.numberFormatDlg = numberformatdlg3.NumberFormatDlg(
                        self.format, self.refreshTable, self)
            self.numberFormatDlg.show()
            self.numberFormatDlg.raise_()
            self.numberFormatDlg.activateWindow()
        except Exception as e:
            print(e)


app = QApplication(sys.argv)
form = Form()
form.show()
sys.exit(app.exec_())

