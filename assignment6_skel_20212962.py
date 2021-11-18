import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()

    def initUI(self):
        self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle('Assignment6')

        self.name = QLabel("Name:",self)
        self.name.move(10,10)
        self.nameEdit = QLineEdit(self)
        self.nameEdit.move(70, 7)
        self.nameEdit.resize(105, 25)
        self.nameText = self.nameEdit.text()


        self.age = QLabel("Age:",self)
        self.age.move(180,10)
        self.ageEdit = QLineEdit(self)
        self.ageEdit.move(225, 7)
        self.ageEdit.resize(100, 25)
        self.ageText = self.ageEdit.text()

        self.score = QLabel("Score:",self)
        self.score.move(330,10)
        self.scoreEdit = QLineEdit(self)
        self.scoreEdit.move(390, 7)
        self.scoreEdit.resize(100, 25)
        self.scoreText = self.scoreEdit.text()

        self.amount = QLabel("Amount:",self)
        self.amount.move(180,38)
        self.amountEdit = QLineEdit(self)
        self.amountEdit.move(255,35)
        self.amountEdit.resize(100,25)
        self.amountText = self.amountEdit.text()

        self.key = QLabel("Key:",self)
        self.key.move(360,38)
        self.keyBox = QComboBox(self)
        self.keys = ["Name", "Age", "Score"]
        self.keyBox.addItems(self.keys)
        self.keyBox.move(405,35)
        self.keyBox.resize(85,25)
        self.keyText = self.keyBox.currentText()

        self.addButton = QPushButton("Add",self)
        self.addButton.move(83,62)
        self.addButton.resize(80,28)
        self.addButton.clicked.connect(self.addScoreDB)

        self.delButton = QPushButton("Del", self)
        self.delButton.move(165, 62)
        self.delButton.resize(80, 28)
        self.delButton.clicked.connect(self.delScoreDB)

        self.findButton = QPushButton("Find", self)
        self.findButton.move(247, 62)
        self.findButton.resize(80, 28)
        self.findButton.clicked.connect(self.findScoreDB)

        self.incButton = QPushButton("Inc", self)
        self.incButton.move(329, 62)
        self.incButton.resize(80, 28)
        self.incButton.clicked.connect(self.incScoreDB)

        self.showButton = QPushButton("Show", self)
        self.showButton.move(411, 62)
        self.showButton.resize(80, 28)
        self.showButton.clicked.connect(self.showScoreDB)

        self.result = QLabel("Result:",self)
        self.result.move(10,90)
        self.resultText = QTextEdit(self)
        self.resultText.move(10,110)
        self.resultText.resize(480,280)

        self.show()

    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb = pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self):
        try:
            self.keyText = self.keyBox.currentText()
            tempText = ""
            for p in sorted(self.scoredb, key=lambda person: person[self.keyText]):
                for attr in sorted(p):
                    tempText = tempText + attr + "=" + str(p[attr]) + " "
                tempText += "\n"
            self.resultText.setText(tempText)
        except:
            self.resultText.setText("show error")


    def addScoreDB(self):
        try:
            tempdic = {}
            self.nameText = self.nameEdit.text()
            self.ageText = self.ageEdit.text()
            self.scoreText = self.scoreEdit.text()
            if self.nameText == "" or self.ageText == "" or self.scoreText == "":
                pass
            if (self.ageText.isdigit() and self.scoreText.isdigit()):
                tempdic["Name"] = self.nameText
                tempdic["Age"] = self.ageText
                tempdic["Score"] = self.scoreText
                self.scoredb.append(tempdic)
                self.showScoreDB()
        except:
            self.resultText.setText("add error")


    def delScoreDB(self):
        try:
            self.nameText = self.nameEdit.text()
            for i in self.scoredb[::-1]:
                if i["Name"] == self.nameText:
                    self.scoredb.remove(i)
            self.showScoreDB()
        except:
            self.resultText.setText("del error")

    def findScoreDB(self):
        try:
            self.nameText = self.nameEdit.text()
            tempText = ""
            for i in self.scoredb:
                if i["Name"] == self.nameText:
                    for j in i:
                        tempText = tempText + j + "=" + str(i[j]) + " "
                    tempText += "\n"
            self.resultText.setText(tempText)
        except:
            self.resultText.setText("find error")

    def incScoreDB(self):
        try:
            self.nameText = self.nameEdit.text()
            self.amountText = self.amountEdit.text()
            for i in self.scoredb:
                if i["Name"] == self.nameText:
                    i["Score"] = str(int(i["Score"])+int(self.amountText))
            self.showScoreDB()
        except:
            self.resultText.setText("inc error")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())
