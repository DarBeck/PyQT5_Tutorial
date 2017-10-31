import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class PenPropertiesDlg(QDialog):

    def __init__(self, parent=None):
        super(PenPropertiesDlg, self).__init__(parent)

        width_label = QLabel("&Width:")
        self.widthSpinBox = QSpinBox()
        width_label.setBuddy(self.widthSpinBox)
        self.widthSpinBox.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.widthSpinBox.setRange(0, 24)
        self.beveledCheckBox = QCheckBox("&Beveled edges")
        style_label = QLabel("&Style:")
        self.styleComboBox = QComboBox()
        style_label.setBuddy(self.styleComboBox)
        self.styleComboBox.addItems(["Solid", "Dashed", "Dotted",
                                     "DashDotted", "DashDotDotted"])
        ok_button = QPushButton("&OK")
        cancel_button = QPushButton("Cancel")

        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(ok_button)
        button_layout.addWidget(cancel_button)
        layout = QGridLayout()
        layout.addWidget(width_label, 0, 0)
        layout.addWidget(self.widthSpinBox, 0, 1)
        layout.addWidget(self.beveledCheckBox, 0, 2)
        layout.addWidget(style_label, 1, 0)
        layout.addWidget(self.styleComboBox, 1, 1, 1, 2)
        layout.addLayout(button_layout, 2, 0, 1, 3)
        self.setLayout(layout)

        self.setWindowTitle("Pen Properties")

        # Connect buttons to actions
        ok_button.clicked.connect(self.accept)
        cancel_button.clicked.connect(self.reject)


class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.width = 1
        self.beveled = False
        self.style = "Solid"

        pen_button_inline = QPushButton("Set Pen... (Dumb &inline)")
        pen_button = QPushButton("Set Pen... (Dumb &class)")
        self.label = QLabel("The Pen has not been set")
        self.label.setTextFormat(Qt.RichText)

        layout = QVBoxLayout()
        layout.addWidget(pen_button_inline)
        layout.addWidget(pen_button)
        layout.addWidget(self.label)
        self.setLayout(layout)

        pen_button_inline.clicked.connect(self.setPenInline)
        pen_button.clicked.connect(self.setPenProperties)
        self.setWindowTitle("Pen")
        self.updateData()


    def updateData(self):
        bevel = ""
        if self.beveled:
            bevel = "<br>Beveled"
        self.label.setText("Width = %d<br>Style = %s%s" % (
                           self.width, self.style, bevel))

    def setPenInline(self):
        try:
            width_label = QLabel("&Width:")
            width_spin_box = QSpinBox()
            width_label.setBuddy(width_spin_box)
            width_spin_box.setAlignment(Qt.AlignRight)
            width_spin_box.setRange(0, 24)
            width_spin_box.setValue(self.width)
            beveled_check_box = QCheckBox("&Beveled edges")
            beveled_check_box.setChecked(self.beveled)
            style_label = QLabel("&Style:")
            style_combo_box = QComboBox()
            style_label.setBuddy(style_combo_box)
            style_combo_box.addItems(["Solid", "Dashed", "Dotted",
                                     "DashDotted", "DashDotDotted"])
            style_combo_box.setCurrentIndex(style_combo_box.findText(
                                            self.style))
            ok_button = QPushButton("&OK")
            cancel_button = QPushButton("Cancel")

            button_layout = QHBoxLayout()
            button_layout.addStretch()
            button_layout.addWidget(ok_button)
            button_layout.addWidget(cancel_button)
            layout = QGridLayout()
            layout.addWidget(width_label, 0, 0)
            layout.addWidget(width_spin_box, 0, 1)
            layout.addWidget(beveled_check_box, 0, 2)
            layout.addWidget(style_label, 1, 0)
            layout.addWidget(style_combo_box, 1, 1, 1, 2)
            layout.addLayout(button_layout, 2, 0, 1, 3)

            form = QDialog()
            form.setLayout(layout)
            ok_button.clicked.connect(form.accept)
            cancel_button.clicked.connect(form.reject)
            form.setWindowTitle("Pen Properties")

            if form.exec_():
                self.width = width_spin_box.value()
                self.beveled = beveled_check_box.isChecked()
                self.style = style_combo_box.currentText()
                self.updateData()
        except Exception as e:
            print(e)

    def setPenProperties(self):
        try:
            dialog = PenPropertiesDlg(self)
            dialog.widthSpinBox.setValue(self.width)
            dialog.beveledCheckBox.setChecked(self.beveled)
            dialog.styleComboBox.setCurrentIndex(
                    dialog.styleComboBox.findText(self.style))
            if dialog.exec_():
                self.width = dialog.widthSpinBox.value()
                self.beveled = dialog.beveledCheckBox.isChecked()
                self.style = dialog.styleComboBox.currentText()
                self.updateData()
        except Exception as e:
            print(e)


app = QApplication(sys.argv)
form = Form()
form.show()
sys.exit(app.exec_())

