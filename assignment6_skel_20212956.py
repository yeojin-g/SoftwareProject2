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
        # 문자 생성
        name = QLabel('Name:')
        age = QLabel('Age:')
        score = QLabel('Score:')
        amount = QLabel('Amount:')
        key = QLabel('Key:')
        blank = QLabel('\t')
        result = QLabel('Result:')

        # 입력창 생성
        self.nameEdit = QLineEdit()
        self.ageEdit = QLineEdit()
        self.scoreEdit = QLineEdit()
        self.amountEdit = QLineEdit()
        self.keyEdit = QComboBox()
        self.keyEdit.addItems(['Name', 'Age', 'Score'])
        self.resultEdit = QTextEdit()

        # 버튼 생성
        self.addButton = QPushButton('Add')
        self.delButton = QPushButton('Del')
        self.findButton = QPushButton('Find')
        self.incButton = QPushButton('Inc')
        self.showButton = QPushButton('Show')

        # 1열 가로 배치 (이름, 나이, 점수 입력창)
        hbox = QHBoxLayout()
        hbox.addWidget(name)
        hbox.addWidget(self.nameEdit)
        hbox.addWidget(age)
        hbox.addWidget(self.ageEdit)
        hbox.addWidget(score)
        hbox.addWidget(self.scoreEdit)

        # 2열 가로배치(amount, 정렬키)
        h0box = QHBoxLayout()
        h0box.addWidget(blank)
        h0box.addWidget(blank)
        h0box.addWidget(blank)
        h0box.addWidget(amount)
        h0box.addWidget(self.amountEdit)
        h0box.addWidget(key)
        h0box.addWidget(self.keyEdit)

        # 3열 가로배치(기능 버튼)
        h1box = QHBoxLayout()
        h1box.addWidget(blank)
        h1box.addWidget(self.addButton)
        h1box.addWidget(self.delButton)
        h1box.addWidget(self.findButton)
        h1box.addWidget(self.incButton)
        h1box.addWidget(self.showButton)

        # 결과 문자배치
        h2box = QHBoxLayout()
        h2box.addWidget(result)

        # 결과값 창 배치
        h3box = QHBoxLayout()
        h3box.addWidget(self.resultEdit)

        # 가로열들 세로 배치
        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addLayout(h0box)
        vbox.addLayout(h1box)
        vbox.addLayout(h2box)
        vbox.addLayout(h3box)

        # 버튼과 함수 연결
        self.addButton.clicked.connect(self.addButtonClicked)
        self.delButton.clicked.connect(self.delButtonClicked)
        self.findButton.clicked.connect(self.findButtonClicked)
        self.incButton.clicked.connect(self.incButtonClicked)
        self.showButton.clicked.connect(self.showButtonClicked)

        self.setLayout(vbox)
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.show()

    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return
        scdb = []
        try:
            scdb = pickle.load(fH)
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

    def showScoreDB(self): # 내용 출력
        self.resultEdit.clear()
        keyname = self.keyEdit.currentText()
        for p in sorted(self.scoredb, key=lambda person: person[keyname]):
            for attr in sorted(p):
                self.resultEdit.insertPlainText(attr + "=" + str(p[attr]) + " ")
            self.resultEdit.insertPlainText('\n')

    def addButtonClicked(self): # add버튼 눌렸을 때
        nameT = self.nameEdit.text()
        ageT = self.ageEdit.text()
        scoreT = self.scoreEdit.text()
        record = {"Name": nameT, "Age": int(ageT), "Score": int(scoreT)}
        self.scoredb += [record]
        self.showScoreDB()

    def delButtonClicked(self): # del버튼 눌렸을 때
        self.resultEdit.clear()
        nameT = self.nameEdit.text()
        for p in self.scoredb[:]:
            if p['Name'] == nameT:
                self.scoredb.remove(p)
        self.showScoreDB()

    def findButtonClicked(self): # find버튼 눌렸을 때
        self.resultEdit.clear()
        nameT = self.nameEdit.text()
        for p in sorted(self.scoredb, key=lambda person: person['Name']):
            if p['Name'] == nameT:
                for attr in sorted(p):
                    self.resultEdit.insertPlainText(attr + "=" + str(p[attr]) + " ")
                self.resultEdit.insertPlainText('\n')

    def incButtonClicked(self): # inc버튼 눌렸을 때
        self.resultEdit.clear()
        nameT = self.nameEdit.text()
        amountT = self.amountEdit.text()
        for p in sorted(self.scoredb, key=lambda person: person['Name']):
            if p['Name'] == nameT:
                p['Score'] = int(p['Score']) + int(amountT)
        self.showScoreDB()

    def showButtonClicked(self): # show버튼 눌렸을 때
        self.showScoreDB()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())
