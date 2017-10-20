import sys
from math import *
from PyQt5.QtWidgets import *


class Form(QDialog):
    def __init__(self):
        super().__init__()

        self.browser = QTextBrowser()
        self.line_edit = QLineEdit("Type an expression and press Enter")
        self.line_edit.selectAll()
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.line_edit)
        self.setLayout(layout)
        self.line_edit.setFocus()
        self.line_edit.returnPressed.connect(self.updateUi)
        self.setWindowTitle("Calculator")

    def updateUi(self):
        try:
            text = self.line_edit.text()
            self.browser.append("%s = <b>%s</b>" %(text, eval(text)))
            self.line_edit.clear()
        except Exception:
            self.browser.append("<b>%s is invalid</b>")


app = QApplication(sys.argv)
form = Form()
form.show()
sys.exit(app.exec_())
