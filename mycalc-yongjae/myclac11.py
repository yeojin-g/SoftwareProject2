from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout

from keypad2 import numPadList, operatorList, constantList, functionList, constantDic, functionMap


class Button(QToolButton):

    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size


class Calculator(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Display Window
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(35)

        # Button Creation and Placement
        numLayout = QGridLayout()
        opLayout = QGridLayout()
        constLayout = QGridLayout()
        funcLayout = QGridLayout()

        buttonGroups = {
            'num': {'buttons': numPadList, 'layout': numLayout, 'columns': 3},
            'op': {'buttons': operatorList, 'layout': opLayout, 'columns': 2},
            'constants': {'buttons': constantList, 'layout': constLayout, 'columns': 1},
            'functions': {'buttons': functionList, 'layout': funcLayout, 'columns': 1},
        }

        for label in buttonGroups.keys():
            r = 0; c = 0
            buttonPad = buttonGroups[label]
            for btnText in buttonPad['buttons']:
                button = Button(btnText, self.buttonClicked)
                buttonPad['layout'].addWidget(button, r, c)
                c += 1
                if c >= buttonPad['columns']:
                    c = 0; r += 1

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 2)
        mainLayout.addLayout(numLayout, 1, 0)
        mainLayout.addLayout(opLayout, 1, 1)
        mainLayout.addLayout(constLayout, 2, 0)
        mainLayout.addLayout(funcLayout, 2, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle("My Calculator")


    def buttonClicked(self):

        if self.display.text() == "0으로 나눌 수 없습니다":
            self.display.setText('')

        if self.display.text() == 'Error!':
            self.display.setText('')

        button = self.sender()
        key = button.text()
        num = "0 1 2 3 4 5 6 7 8 9"
        numlist = num.split()
        oper = "+ - * /"
        operlist = oper.split()

        if key == "=":
            if self.display.text()[-1] in ["*", "+", "-", "("]:
                self.display.setText(self.display.text() + "0")

            if self.display.text().count("(") > self.display.text().count(")"):
                a = self.display.text().count("(")
                b = self.display.text().count(")")
                self.display.setText(self.display.text() + (")" * (a-b)))

            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except ZeroDivisionError:
                self.display.setText("0으로 나눌 수 없습니다")
            except:
                self.display.setText('Error!')

        elif key == "C":
            self.display.setText("")

        elif key == "c":
            try:
                result = self.display.text()
                if len(result) >= 1:
                    result = result[0:len(result) - 1]
                    self.display.setText(result)
            except:
                pass

        elif key == "(":
            try:
                result = self.display.text()
                if result[-1] == "(" or (result[-1] in operlist):
                    self.display.setText(self.display.text() + key)
            except:
                self.display.setText(self.display.text() + key)

        elif key == ")":
            try:
                result = self.display.text()
                if result.count("(") > result.count(")") and (result[-1] not in operlist) and result[-1] != "(":
                    self.display.setText(self.display.text() + key)
            except:
                pass

        elif key in numlist:
            try:
               result = self.display.text()
               if result[-1] != ")":
                   self.display.setText(self.display.text() + key)
            except:
                self.display.setText(self.display.text() + key)

        elif key == ".":
            try:
                result = self.display.text()
                if result[-1] in numlist:
                    self.display.setText(self.display.text() + key)
            except:
                pass

        elif key in operlist:
            try:
               result = self.display.text()
               if result[-1] in numlist or result[-1] == ")":
                   self.display.setText(self.display.text() + key)
            except:
                pass

        elif key in constantList:
            self.display.setText(self.display.text() + constantDic[key])

        elif key in functionList:
            n = self.display.text()
            value = functionMap[functionList.index(key)][1](n)
            self.display.setText(str(value))

        else:
            self.display.setText(self.display.text() + key)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())