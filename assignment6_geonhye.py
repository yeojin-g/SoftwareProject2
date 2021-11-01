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

        # Add QLabel
        name = QLabel('Name:')
        age = QLabel('Age:')
        score = QLabel('Score:')
        amount = QLabel('Amount:')
        key = QLabel('Key:')
        result = QLabel('Result:')

        # Add Edit
        self.nameEdit = QLineEdit()
        self.ageEdit = QLineEdit()
        self.scoreEdit = QLineEdit()
        self.amountEdit = QLineEdit()
        self.keyEdit = QComboBox()
        self.keyEdit.addItems(['Name','Age','Score'])
        self.resultEdit = QTextEdit()

        # Horizontal_Layout1 : name, age, score
        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(name)
        hbox1.addWidget(self.nameEdit)
        hbox1.addWidget(age)
        hbox1.addWidget(self.ageEdit)
        hbox1.addWidget(score)
        hbox1.addWidget(self.scoreEdit)

        # Horizontal_Layout2 : amount, key
        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(amount)
        hbox2.addWidget(self.amountEdit)
        hbox2.addWidget(key)
        hbox2.addWidget(self.keyEdit)

        # Horizontal_Layout3 : Button
        self.addButton = QPushButton("Add")
        self.delButton = QPushButton("Del")
        self.findButton = QPushButton("Find")
        self.incButton = QPushButton("Inc")
        self.showButton = QPushButton("Show")
        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(self.addButton)
        hbox3.addWidget(self.delButton)
        hbox3.addWidget(self.findButton)
        hbox3.addWidget(self.incButton)
        hbox3.addWidget(self.showButton)

        # Vertical_Layout : all
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addWidget(result)
        vbox.addWidget(self.resultEdit)

        self.setLayout(vbox)

        # 창 편집
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.show()

        # ButtonClicked method
        self.addButton.clicked.connect(self.addButtonClicked)
        self.delButton.clicked.connect(self.delButtonClicked)
        self.findButton.clicked.connect(self.findButtonClicked)
        self.incButton.clicked.connect(self.incButtonClicked)
        self.showButton.clicked.connect(self.showButtonClicked)


    def addButtonClicked(self):
        nameinput = self.nameEdit.text()
        ageinput = self.ageEdit.text()
        scoreinput = self.scoreEdit.text()
        record = {"Name": nameinput, "Age": ageinput, "Score": scoreinput}
        self.scoredb += [record]
        self.showScoreDB()

    def delButtonClicked(self):
        nameinput = self.nameEdit.text()
        for p in range(len(self.scoredb)-1):
            if self.scoredb[p]['Name'] == nameinput:
                del self.scoredb[p]
        self.showScoreDB()

    def findButtonClicked(self):
        nameinput = self.nameEdit.text()
        self.resultEdit.clear()
        for p in self.scoredb:
            resultline = ''
            if p['Name'] == nameinput:
                for attr in p:
                    resultline += attr + "=" + str(p[attr]) + '         '
                self.resultEdit.append(resultline)

    def incButtonClicked(self):
        nameinput = self.nameEdit.text()
        amountinput = self.amountEdit.text()
        for p in self.scoredb:
            if p['Name'] == nameinput:
                p['Score'] = int(p['Score']) + int(amountinput)
        self.showScoreDB()


    def showButtonClicked(self):
        self.showScoreDB()

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
        keyname = self.keyEdit.currentText()
        for p in sorted(self.scoredb, key=lambda person: person[keyname]):
            resultline = ''
            for attr in sorted(p):
                resultline += attr + "=" + str(p[attr]) + '         '
            self.resultEdit.append(resultline)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())