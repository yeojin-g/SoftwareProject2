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

    # Set Layouts and organize
    def initUI(self):
        # define Widgets and add them to Layouts.

        #line1

        lblName = QLabel('Name:', self)
        self.liEditName = QLineEdit()

        lblAge = QLabel('Age:', self)
        self.liEditAge = QLineEdit()

        lblScore = QLabel('Score:', self)
        self.liEditScore = QLineEdit()

        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(lblName)
        hbox1.addWidget(self.liEditName)
        hbox1.addWidget(lblAge)
        hbox1.addWidget(self.liEditAge)
        hbox1.addWidget(lblScore)
        hbox1.addWidget(self.liEditScore)

        #line2

        lblAmount = QLabel('Amount:', self)
        self.liEditAmount = QLineEdit()

        lblKey = QLabel('Key:', self)
        self.coboxKey = QComboBox()
        self.coboxKey.addItem('Name')
        self.coboxKey.addItem('Age')
        self.coboxKey.addItem('Score')

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(lblAmount)
        hbox2.addWidget(self.liEditAmount)
        hbox2.addWidget(lblKey)
        hbox2.addWidget(self.coboxKey)

        #line3 - Buttons

        btnAdd = QPushButton('Add')
        btnDel = QPushButton('Del')
        btnFind = QPushButton('Find')
        btnInc = QPushButton('Inc')
        btnShow = QPushButton('Show')

        #Set Buttons events
        btnAdd.clicked.connect(self.btnAddClicked)
        btnDel.clicked.connect(self.btnDelClicked)
        btnFind.clicked.connect(self.btnFindClicked)
        btnInc.clicked.connect(self.btnIncClicked)
        btnShow.clicked.connect(self.btnShowClicked)

        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(btnAdd)
        hbox3.addWidget(btnDel)
        hbox3.addWidget(btnFind)
        hbox3.addWidget(btnInc)
        hbox3.addWidget(btnShow)

        #line4 and 5 - Result
        lblResult = QLabel('Result:')
        self.textEditResult = QTextEdit()


        #Allign vertical
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addWidget(lblResult)
        vbox.addWidget(self.textEditResult)
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
        try:
            self.scoredb =  pickle.load(fH)
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
        keyname = self.coboxKey.currentText()
        for p in sorted(self.scoredb, key=lambda person: person[keyname]):
            line = ''
            for attr in sorted(p):
                line += attr + "=" + str(p[attr]) + '\t\t'
            self.textEditResult.append(line)

    #Add button event
    def btnAddClicked(self):
        name, age, score = self.liEditName.text(), self.liEditAge.text(), self.liEditScore.text()
        #Exception
        if not age.isdigit() or not score.isdigit() or not name.strip() or not age.strip() or not score.strip():
            return

        record = {'Name': self.liEditName.text(), 'Age': int(self.liEditAge.text()), 'Score': int(self.liEditScore.text())}
        self.scoredb += [record]

        self.textEditResult.clear()
        self.showScoreDB()

    #Del button event
    def btnDelClicked(self):
        remove_list = []
        for i in range(len(self.scoredb)):
            if self.scoredb[i]['Name'] == self.liEditName.text():
                remove_list.append(i)
        remove_cnt = 0
        for i in remove_list:
            del self.scoredb[i - remove_cnt]
            remove_cnt += 1

        self.textEditResult.clear()
        self.showScoreDB()

    #Find button event
    def btnFindClicked(self):
        #Exception
        if not self.liEditName.text().strip():
            return

        self.textEditResult.clear()
        for p in self.scoredb:
            line = ''
            if p['Name'] == self.liEditName.text():
                for attr in sorted(p):
                    line += attr + "=" + str(p[attr]) + '\t\t'
                self.textEditResult.append(line)

        self.textEditResult.append('\n')
        self.showScoreDB()

    #Inc button event
    def btnIncClicked(self):
        if not self.liEditAmount.text().isdigit():
            return
        for p in self.scoredb:
            if p['Name'] == self.liEditName.text():
                p['Score'] += int(self.liEditAmount.text())

        self.textEditResult.clear()
        self.showScoreDB()

    #Show button event
    def btnShowClicked(self):
        self.showScoreDB()

if __name__ == '__main__':    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())

