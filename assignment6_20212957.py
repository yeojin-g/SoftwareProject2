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
        # 첫 번째 줄
        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)

        name = QLabel('Name:')
        hbox1.addWidget(name)
        self.nameEdit = QLineEdit()
        hbox1.addWidget(self.nameEdit)
        age = QLabel('Age:')
        hbox1.addWidget(age)
        self.ageEdit = QLineEdit()
        hbox1.addWidget(self.ageEdit)
        score = QLabel('Score:')
        hbox1.addWidget(score)
        self.scoreEdit = QLineEdit()
        hbox1.addWidget(self.scoreEdit)

        # 두 번째 줄
        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)

        amount = QLabel('Amount:')
        hbox2.addWidget(amount)
        self.amountEdit = QLineEdit()
        hbox2.addWidget(self.amountEdit)
        key = QLabel('Key:')
        hbox2.addWidget(key)
        self.keyCombo = QComboBox()
        self.keyCombo.addItem('Name')  # Combo Item 추가
        self.keyCombo.addItem('Age')
        self.keyCombo.addItem('Score')
        hbox2.addWidget(self.keyCombo)

        # 세 번째 줄
        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)

        addButton = QPushButton("Add")
        hbox3.addWidget(addButton)
        addButton.clicked.connect(self.button_add_clicked)

        delButton = QPushButton("Del")
        hbox3.addWidget(delButton)
        delButton.clicked.connect(self.button_del_clicked)

        findButton = QPushButton("Find")
        hbox3.addWidget(findButton)
        findButton.clicked.connect(self.button_find_clicked)

        incButton = QPushButton("Inc")
        hbox3.addWidget(incButton)
        incButton.clicked.connect(self.button_inc_clicked)

        showButton = QPushButton("show")
        hbox3.addWidget(showButton)
        showButton.clicked.connect(self.button_show_clicked)

        # 네 번째 줄
        hbox4 = QHBoxLayout()
        result = QLabel("Result:")
        hbox4.addWidget(result)

        # 다섯 번째 줄
        hbox5 = QHBoxLayout()
        self.resultEdit = QTextEdit()
        hbox5.addWidget(self.resultEdit)

        # 수직 정렬
        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox5)

        self.setLayout(vbox)
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.show()

    def button_add_clicked(self):
        nameText = self.nameEdit.text()
        ageText = self.ageEdit.text()
        scoreText = self.scoreEdit.text()
        record = {'Name': nameText, 'Age': int(ageText), 'Score': int(scoreText)}
        self.scoredb += [record]
        self.showScoreDB()

    def button_del_clicked(self):
        nameText = self.nameEdit.text()
        for p in self.scoredb[:]:
            if p['Name'] == nameText:
                self.scoredb.remove(p)
        self.showScoreDB()

    def button_find_clicked(self):
        nameText = self.nameEdit.text()
        found = list(filter(lambda x: x["Name"] == nameText, self.scoredb))
        self.resultEdit.clear()
        for p in found:
            for attr in sorted(p):
                self.resultEdit.insertPlainText(attr + "=" + str(p[attr]) + "\t")
            self.resultEdit.insertPlainText("\n")

    def button_inc_clicked(self):
        nameText = self.nameEdit.text()
        amountText = self.amountEdit.text()
        for p in self.scoredb:
            if p['Name'] == nameText:
                p['Score'] = int(p['Score']) + int(amountText)
        self.showScoreDB()

    def button_show_clicked(self):
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
            print("Empty DB: ", self.dbfilename)
        else:
            print("Open DB: ", self.dbfilename)
        fH.close()

    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self):
        self.resultEdit.clear()
        keyName = self.keyCombo.currentText()
        for p in sorted(self.scoredb, key=lambda person: person[keyName]):
            for attr in sorted(p):
                self.resultEdit.insertPlainText(attr + "=" + str(p[attr]) + "\t")
            self.resultEdit.insertPlainText("\n")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())
